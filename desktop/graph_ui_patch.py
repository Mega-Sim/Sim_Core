"""Graph UI behavior and DXF graph post-processing for Sim_Core."""
from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Dict, Optional

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import (
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsPathItem,
    QGraphicsView,
)

EDGE_COLOR = QColor("#315568")
EDGE_SELECTED_COLOR = QColor("#ffd54f")
INTERACTIVE_EDGE_LIMIT = 2_500
INTERACTIVE_NODE_LIMIT = 4_000
STATION_LABEL_SCALE = 0.1
ARROW_SCALE = 0.2


class _GraphLabelsItem(QGraphicsItem):
    """Paint all graph labels through one scene item instead of thousands."""

    def __init__(self, labels: list[tuple[float, float, str]], bounds: QRectF) -> None:
        super().__init__()
        self._labels = labels
        self._bounds = bounds.adjusted(-80.0, -40.0, 80.0, 40.0)
        self.setZValue(4)

    def boundingRect(self) -> QRectF:  # noqa: N802
        return self._bounds

    def paint(self, painter: QPainter, option: Any, _widget: Any = None) -> None:
        # A full FAB has thousands of equipment labels.  Keep the overview
        # clean and draw them only after the user zooms in far enough to read.
        transform = painter.worldTransform()
        level = max(abs(transform.m11()), abs(transform.m22()))
        if len(self._labels) > 500 and level < 0.72:
            return
        exposed = option.exposedRect.adjusted(-80.0, -30.0, 80.0, 30.0)
        painter.setPen(QColor("#a9c0cb"))
        painter.setFont(QFont("Segoe UI", max(1, round(10 * STATION_LABEL_SCALE)), QFont.Weight.DemiBold))
        for x, y, label in self._labels:
            if exposed.contains(QPointF(x, y)):
                painter.drawText(
                    QPointF(x - 35.0 * STATION_LABEL_SCALE, y - 4.0 * STATION_LABEL_SCALE),
                    label,
                )


def _distance_to_segment(
    point_x: float,
    point_y: float,
    first: tuple[float, float],
    second: tuple[float, float],
) -> float:
    dx, dy = second[0] - first[0], second[1] - first[1]
    length_squared = dx * dx + dy * dy
    if length_squared <= 1e-12:
        return math.hypot(point_x - first[0], point_y - first[1])
    ratio = ((point_x - first[0]) * dx + (point_y - first[1]) * dy) / length_squared
    ratio = max(0.0, min(1.0, ratio))
    projection_x = first[0] + dx * ratio
    projection_y = first[1] + dy * ratio
    return math.hypot(point_x - projection_x, point_y - projection_y)


def install_graph_interaction(view_class: type[QGraphicsView]) -> None:
    """Enable Shift+Left panning, rubber-band edge selection and clear-on-Esc/background click."""
    original_init = view_class.__init__
    original_press = view_class.mousePressEvent
    original_move = view_class.mouseMoveEvent
    original_release = view_class.mouseReleaseEvent
    original_key = view_class.keyPressEvent

    def update_edge_colors(self) -> None:
        for item in self.scene().items():
            if isinstance(item, QGraphicsPathItem) and item.data(0) == "graph-edge":
                pen = item.pen()
                pen.setColor(EDGE_SELECTED_COLOR if item.isSelected() else EDGE_COLOR)
                item.setPen(pen)

    def clear_edge_selection(self) -> None:
        self.scene().clearSelection()
        update_edge_colors(self)

    def init(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        original_init(self, *args, **kwargs)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
        self.scene().selectionChanged.connect(lambda: update_edge_colors(self))

    def mouse_press(self, event):  # type: ignore[no-untyped-def]
        if event.button() == Qt.MouseButton.LeftButton and bool(event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            self._shift_left_panning = True
            self._shift_left_pan_position = event.position().toPoint()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
            return
        if event.button() == Qt.MouseButton.LeftButton and not self.itemAt(event.position().toPoint()):
            clear_edge_selection(self)
        original_press(self, event)

    def mouse_move(self, event):  # type: ignore[no-untyped-def]
        if getattr(self, "_shift_left_panning", False):
            current = event.position().toPoint()
            delta = current - self._shift_left_pan_position
            self._shift_left_pan_position = current
            sx = abs(self.transform().m11()) or 1.0
            sy = abs(self.transform().m22()) or 1.0
            self.translate(delta.x() / sx, delta.y() / sy)
            event.accept()
            return
        original_move(self, event)

    def mouse_release(self, event):  # type: ignore[no-untyped-def]
        if event.button() == Qt.MouseButton.LeftButton and getattr(self, "_shift_left_panning", False):
            self._shift_left_panning = False
            self.unsetCursor()
            event.accept()
            return
        original_release(self, event)

    def key_press(self, event):  # type: ignore[no-untyped-def]
        if event.key() == Qt.Key.Key_Escape:
            clear_edge_selection(self)
            event.accept()
            return
        original_key(self, event)

    view_class.__init__ = init
    view_class.mousePressEvent = mouse_press
    view_class.mouseMoveEvent = mouse_move
    view_class.mouseReleaseEvent = mouse_release
    view_class.keyPressEvent = key_press


def _is_curved_chain(node_path: list[int], nodes: list[list[float]], threshold_degrees: float = 2.0) -> bool:
    headings: list[tuple[float, float]] = []
    for first_id, second_id in zip(node_path, node_path[1:]):
        first, second = nodes[first_id], nodes[second_id]
        dx, dy = float(second[0]) - float(first[0]), float(second[1]) - float(first[1])
        length = math.hypot(dx, dy)
        if length > 1e-9:
            headings.append((dx / length, dy / length))
    for left, right in zip(headings, headings[1:]):
        dot = max(-1.0, min(1.0, left[0] * right[0] + left[1] * right[1]))
        if math.degrees(math.acos(dot)) > threshold_degrees:
            return True
    return False


def consolidate_curve_edges(graph: Dict[str, Any]) -> Dict[str, Any]:
    """Collapse each curved degree-2 chain between junction anchors into one logical edge."""
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    if not isinstance(nodes, list) or not isinstance(edges, list) or not edges:
        return graph

    incident: defaultdict[int, list[int]] = defaultdict(list)
    for edge_id, edge in enumerate(edges):
        start, end = int(edge["start"]), int(edge["end"])
        incident[start].append(edge_id)
        incident[end].append(edge_id)

    def other(edge_id: int, node_id: int) -> int:
        edge = edges[edge_id]
        return int(edge["end"]) if int(edge["start"]) == node_id else int(edge["start"])

    visited: set[int] = set()
    replacement: dict[int, dict[str, Any]] = {}
    removed: set[int] = set()
    merged_segments = 0

    anchors = [node_id for node_id, linked in incident.items() if len(linked) != 2]
    for anchor in anchors:
        for first_edge in incident[anchor]:
            if first_edge in visited:
                continue
            chain = [first_edge]
            node_path = [anchor, other(first_edge, anchor)]
            visited.add(first_edge)
            current = node_path[-1]
            while len(incident[current]) == 2:
                candidates = [edge_id for edge_id in incident[current] if edge_id not in visited]
                if not candidates:
                    break
                next_edge = candidates[0]
                visited.add(next_edge)
                chain.append(next_edge)
                current = other(next_edge, current)
                node_path.append(current)

            if len(chain) < 2 or not _is_curved_chain(node_path, nodes):
                continue

            forward = reverse = 0
            for index, edge_id in enumerate(chain):
                direction = edges[edge_id].get("dir")
                if direction == [node_path[index], node_path[index + 1]]:
                    forward += 1
                elif direction == [node_path[index + 1], node_path[index]]:
                    reverse += 1
            oriented = list(reversed(node_path)) if reverse > forward else node_path
            first = chain[0]
            replacement[first] = {
                "start": oriented[0],
                "end": oriented[-1],
                "dir": [oriented[0], oriented[-1]],
                "geometry": [nodes[node_id] for node_id in oriented],
                "geometry_type": "CURVE_CHAIN",
                "source_edge_count": len(chain),
            }
            removed.update(chain[1:])
            merged_segments += len(chain) - 1

    if not merged_segments:
        return graph

    merged_edges = [replacement.get(edge_id, edge) for edge_id, edge in enumerate(edges) if edge_id not in removed]
    used_nodes: set[int] = set()
    for edge in merged_edges:
        used_nodes.update((int(edge["start"]), int(edge["end"])))
    ordered = sorted(used_nodes)
    remap = {old: new for new, old in enumerate(ordered)}
    compact_nodes = [nodes[old] for old in ordered]
    for edge in merged_edges:
        old_start, old_end = int(edge["start"]), int(edge["end"])
        direction = edge.get("dir")
        edge["start"], edge["end"] = remap[old_start], remap[old_end]
        if isinstance(direction, list) and len(direction) == 2:
            edge["dir"] = [remap[int(direction[0])], remap[int(direction[1])]]

    graph["nodes"] = compact_nodes
    graph["edges"] = merged_edges
    statistics = graph.setdefault("metadata", {}).setdefault("statistics", {})
    statistics["node_count"] = len(compact_nodes)
    statistics["edge_count"] = len(merged_edges)
    statistics["merged_curve_segment_count"] = merged_segments
    statistics["curve_chain_count"] = len(replacement)
    statistics["unresolved_direction_count"] = sum(1 for edge in merged_edges if edge.get("dir") is None)
    return graph


def install_dark_graph_renderer(view_class: type[QGraphicsView]) -> None:
    """Install a batched Workbench renderer for large directed Rail graphs."""

    def graph_edge_at(self, viewport_position: Any) -> int | None:
        polylines = getattr(self, "_graph_edge_polylines", [])
        bounds = getattr(self, "_graph_edge_bounds", [])
        if not polylines:
            return None
        scene_point = self.mapToScene(viewport_position)
        view_scale = max(abs(self.transform().m11()), abs(self.transform().m22()), 1e-6)
        tolerance = 7.0 / view_scale
        best_id: int | None = None
        best_distance = tolerance
        for edge_id, (polyline, edge_bounds) in enumerate(zip(polylines, bounds)):
            if len(polyline) < 2:
                continue
            if not edge_bounds.adjusted(-tolerance, -tolerance, tolerance, tolerance).contains(scene_point):
                continue
            distance = min(
                _distance_to_segment(scene_point.x(), scene_point.y(), first, second)
                for first, second in zip(polyline, polyline[1:])
            )
            if distance <= best_distance:
                best_id = edge_id
                best_distance = distance
        return best_id

    def graph_edges_in_rect(self, scene_rect: QRectF) -> set[int]:
        return {
            edge_id
            for edge_id, edge_bounds in enumerate(getattr(self, "_graph_edge_bounds", []))
            if edge_bounds.intersects(scene_rect) or scene_rect.contains(edge_bounds)
        }

    def set_graph_selection(self, edge_ids: set[int]) -> None:
        selection_item = getattr(self, "_graph_selection_item", None)
        if selection_item is None:
            return
        highlight = QPainterPath()
        polylines = getattr(self, "_graph_edge_polylines", [])
        for edge_id in sorted(edge_ids):
            if edge_id < 0 or edge_id >= len(polylines):
                continue
            points = polylines[edge_id]
            if len(points) < 2:
                continue
            highlight.moveTo(*points[0])
            for point_value in points[1:]:
                highlight.lineTo(*point_value)
        selection_item.setPath(highlight)

    def set_graph(self, graph: Optional[Dict[str, Any]]) -> None:
        self._white_canvas = False
        scene = self.scene()
        scene.clear()
        self._graph_edge_polylines = []
        self._graph_edge_bounds = []
        self._graph_selection_item = None
        if not graph:
            label = scene.addText("DXF 또는 Rail 파일을 선택하면 방향성 Graph가 표시됩니다.")
            label.setDefaultTextColor(QColor("#78909d"))
            return

        raw_nodes = graph.get("nodes", [])
        if not raw_nodes:
            return
        xs = [float(node[0]) for node in raw_nodes]
        ys = [float(node[1]) for node in raw_nodes]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        scale = 1100.0 / max(max_x - min_x, max_y - min_y, 1.0)

        def point(node_id: int) -> tuple[float, float]:
            raw = raw_nodes[node_id]
            return (float(raw[0]) - min_x) * scale, (float(raw[1]) - min_y) * scale

        def raw_point(raw: Any) -> tuple[float, float]:
            return (float(raw[0]) - min_x) * scale, (float(raw[1]) - min_y) * scale

        edges = graph.get("edges", [])
        batch_edges = len(edges) > INTERACTIVE_EDGE_LIMIT
        all_rails = QPainterPath()
        all_arrows = QPainterPath()

        for edge_id, edge in enumerate(edges):
            start_node, end_node = int(edge.get("start", -1)), int(edge.get("end", -1))
            if not (0 <= start_node < len(raw_nodes) and 0 <= end_node < len(raw_nodes)):
                self._graph_edge_polylines.append([])
                self._graph_edge_bounds.append(QRectF())
                continue
            direction = edge.get("dir")
            directed = (
                isinstance(direction, list)
                and len(direction) == 2
                and all(isinstance(value, int) for value in direction)
            )
            source_id, target_id = (direction if directed else [start_node, end_node])

            geometry = edge.get("geometry")
            if isinstance(geometry, list) and len(geometry) >= 2:
                polyline = [raw_point(raw) for raw in geometry]
            else:
                polyline = [point(start_node), point(end_node)]
            path = QPainterPath()
            path.moveTo(*polyline[0])
            for point_value in polyline[1:]:
                path.lineTo(*point_value)
            all_rails.addPath(path)
            self._graph_edge_polylines.append(polyline)
            self._graph_edge_bounds.append(path.boundingRect())

            if not batch_edges:
                rail = QGraphicsPathItem(path)
                rail.setPen(
                    QPen(
                        EDGE_COLOR,
                        2.6,
                        Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap,
                        Qt.PenJoinStyle.RoundJoin,
                    )
                )
                rail.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
                rail.setData(0, "graph-edge")
                rail.setData(1, edge_id)
                rail.setZValue(1)
                rail.setToolTip(
                    f"Edge {edge_id}\n{start_node} - {end_node}\n{source_id} -> {target_id}"
                    if directed
                    else f"Edge {edge_id}\n방향 미결정"
                )
                scene.addItem(rail)

            if directed:
                oriented = (
                    list(reversed(polyline))
                    if [int(source_id), int(target_id)] == [end_node, start_node]
                    else polyline
                )
                segment_lengths = [
                    math.dist(first, second)
                    for first, second in zip(oriented, oriented[1:])
                ]
                total_length = sum(segment_lengths)
                if total_length > 1.0:
                    target_length = total_length * 0.62
                    travelled = 0.0
                    marker_x, marker_y = oriented[-1]
                    ux, uy = 1.0, 0.0
                    for (first, second), segment_length in zip(zip(oriented, oriented[1:]), segment_lengths):
                        if segment_length <= 1e-9:
                            continue
                        if travelled + segment_length >= target_length:
                            ratio = (target_length - travelled) / segment_length
                            marker_x = first[0] + (second[0] - first[0]) * ratio
                            marker_y = first[1] + (second[1] - first[1]) * ratio
                            ux = (second[0] - first[0]) / segment_length
                            uy = (second[1] - first[1]) / segment_length
                            break
                        travelled += segment_length
                    arrow_size = min(6.0, max(2.5, total_length * 0.22)) * ARROW_SCALE
                    wing = arrow_size * 0.62
                    base_x, base_y = marker_x - ux * arrow_size, marker_y - uy * arrow_size
                    all_arrows.moveTo(marker_x, marker_y)
                    all_arrows.lineTo(base_x - uy * wing, base_y + ux * wing)
                    all_arrows.moveTo(marker_x, marker_y)
                    all_arrows.lineTo(base_x + uy * wing, base_y - ux * wing)

        if batch_edges:
            rail_batch = QGraphicsPathItem(all_rails)
            rail_batch.setPen(
                QPen(
                    EDGE_COLOR,
                    2.6,
                    Qt.PenStyle.SolidLine,
                    Qt.PenCapStyle.RoundCap,
                    Qt.PenJoinStyle.RoundJoin,
                )
            )
            rail_batch.setData(0, "graph-edge-batch")
            rail_batch.setZValue(1)
            scene.addItem(rail_batch)

        if not all_arrows.isEmpty():
            arrow_batch = QGraphicsPathItem(all_arrows)
            arrow_batch.setPen(
                QPen(
                    QColor("#43e4d3"),
                    1.45 * ARROW_SCALE,
                    Qt.PenStyle.SolidLine,
                    Qt.PenCapStyle.RoundCap,
                    Qt.PenJoinStyle.RoundJoin,
                )
            )
            arrow_batch.setZValue(3)
            scene.addItem(arrow_batch)

        label_records: list[tuple[float, float, str]] = []
        for label in graph.get("metadata", {}).get("labels", []):
            try:
                x = (float(label["x"]) - min_x) * scale
                y = (float(label["y"]) - min_y) * scale
            except (KeyError, TypeError, ValueError):
                continue
            label_text = str(label.get("text", ""))
            if label_text:
                label_records.append((x, y, label_text))
        if label_records:
            scene.addItem(_GraphLabelsItem(label_records, all_rails.boundingRect()))

        node_radius = 3.5 if len(raw_nodes) < 2000 else 2.1
        if len(raw_nodes) <= INTERACTIVE_NODE_LIMIT:
            for node_id in range(len(raw_nodes)):
                x, y = point(node_id)
                dot = QGraphicsEllipseItem(x - node_radius, y - node_radius, node_radius * 2, node_radius * 2)
                dot.setBrush(QColor("#0b1b27"))
                dot.setPen(QPen(QColor("#719bad"), 1))
                dot.setZValue(2)
                dot.setToolTip(f"Node {node_id}\n({raw_nodes[node_id][0]}, {raw_nodes[node_id][1]})")
                scene.addItem(dot)
        else:
            node_path = QPainterPath()
            for node_id in range(len(raw_nodes)):
                x, y = point(node_id)
                node_path.addEllipse(x - node_radius, y - node_radius, node_radius * 2, node_radius * 2)
            node_batch = QGraphicsPathItem(node_path)
            node_batch.setBrush(QColor("#0b1b27"))
            node_batch.setPen(QPen(QColor("#719bad"), 0.8))
            node_batch.setZValue(2)
            scene.addItem(node_batch)

        selection_item = QGraphicsPathItem()
        selection_item.setPen(
            QPen(
                EDGE_SELECTED_COLOR,
                4.5,
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin,
            )
        )
        selection_item.setZValue(5)
        scene.addItem(selection_item)
        self._graph_selection_item = selection_item

        bounds = scene.itemsBoundingRect().adjusted(-35, -35, 35, 35)
        scene.setSceneRect(bounds)
        self.resetTransform()
        self.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)

    view_class.graph_edge_at = graph_edge_at
    view_class.graph_edges_in_rect = graph_edges_in_rect
    view_class.set_graph_selection = set_graph_selection
    view_class.set_graph = set_graph
