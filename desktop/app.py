"""Sim_Core desktop entry point with graph interaction enhancements."""

from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Dict, Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsPathItem, QGraphicsSimpleTextItem, QGraphicsView

import app_base as base


def _mouse_press_event(self, event) -> None:  # type: ignore[no-untyped-def]
    if event.button() == Qt.MouseButton.MiddleButton:
        self._middle_panning = True
        self._middle_pan_position = event.position().toPoint()
        self.setCursor(Qt.CursorShape.ClosedHandCursor)
        event.accept()
        return
    QGraphicsView.mousePressEvent(self, event)


def _mouse_move_event(self, event) -> None:  # type: ignore[no-untyped-def]
    if getattr(self, "_middle_panning", False):
        current = event.position().toPoint()
        delta = current - self._middle_pan_position
        self._middle_pan_position = current
        horizontal = self.horizontalScrollBar()
        vertical = self.verticalScrollBar()
        horizontal.setValue(horizontal.value() - delta.x())
        vertical.setValue(vertical.value() - delta.y())
        event.accept()
        return
    QGraphicsView.mouseMoveEvent(self, event)


def _mouse_release_event(self, event) -> None:  # type: ignore[no-untyped-def]
    if event.button() == Qt.MouseButton.MiddleButton and getattr(self, "_middle_panning", False):
        self._middle_panning = False
        self.unsetCursor()
        event.accept()
        return
    QGraphicsView.mouseReleaseEvent(self, event)


def _curved_chain_arrow_edges(graph: Dict[str, Any], raw_nodes: list[Any]) -> set[int]:
    """Keep one representative arrow for each curved degree-2 rail chain.

    DXF ARC entities are converted into several short edges.  The preview used
    to draw an arrow on every segment, which made curves visually noisy.  This
    pass detects maximal degree-2 chains.  Chains whose segment heading changes
    are treated as curved areas and keep only the middle edge's arrow.  Straight
    chains keep their normal per-edge arrows.
    """

    edges = graph.get("edges", [])
    arrow_edges = set(range(len(edges)))
    incident: defaultdict[int, list[int]] = defaultdict(list)
    for edge_id, edge in enumerate(edges):
        try:
            start = int(edge.get("start", -1))
            end = int(edge.get("end", -1))
        except (TypeError, ValueError):
            continue
        if 0 <= start < len(raw_nodes) and 0 <= end < len(raw_nodes) and start != end:
            incident[start].append(edge_id)
            incident[end].append(edge_id)

    visited: set[int] = set()

    def other(edge_id: int, node_id: int) -> int:
        edge = edges[edge_id]
        start = int(edge["start"])
        end = int(edge["end"])
        return end if start == node_id else start

    def curved(edge_ids: list[int], node_path: list[int]) -> bool:
        if len(edge_ids) < 2 or len(node_path) != len(edge_ids) + 1:
            return False
        headings: list[tuple[float, float]] = []
        for first_id, second_id in zip(node_path, node_path[1:]):
            first = raw_nodes[first_id]
            second = raw_nodes[second_id]
            dx = float(second[0]) - float(first[0])
            dy = float(second[1]) - float(first[1])
            length = math.hypot(dx, dy)
            if length <= 1e-9:
                continue
            headings.append((dx / length, dy / length))
        for first, second in zip(headings, headings[1:]):
            dot = max(-1.0, min(1.0, first[0] * second[0] + first[1] * second[1]))
            if math.acos(dot) > math.radians(2.0):
                return True
        return False

    def reduce_chain(edge_ids: list[int], node_path: list[int]) -> None:
        if not curved(edge_ids, node_path):
            return
        arrow_edges.difference_update(edge_ids)
        arrow_edges.add(edge_ids[len(edge_ids) // 2])

    anchors = [node_id for node_id, linked in incident.items() if len(linked) != 2]
    for anchor in anchors:
        for first_edge in incident[anchor]:
            if first_edge in visited:
                continue
            edge_ids = [first_edge]
            node_path = [anchor, other(first_edge, anchor)]
            visited.add(first_edge)
            previous = anchor
            current = node_path[-1]
            while len(incident[current]) == 2:
                candidates = [edge_id for edge_id in incident[current] if edge_id not in visited]
                if not candidates:
                    break
                next_edge = candidates[0]
                next_node = other(next_edge, current)
                visited.add(next_edge)
                edge_ids.append(next_edge)
                node_path.append(next_node)
                previous, current = current, next_node
                if current == previous:
                    break
            reduce_chain(edge_ids, node_path)

    for first_edge in range(len(edges)):
        if first_edge in visited:
            continue
        start = int(edges[first_edge].get("start", -1))
        if start < 0 or start >= len(raw_nodes):
            continue
        edge_ids = [first_edge]
        node_path = [start, other(first_edge, start)]
        visited.add(first_edge)
        previous = start
        current = node_path[-1]
        while current != start and len(incident[current]) == 2:
            candidates = [
                edge_id
                for edge_id in incident[current]
                if edge_id not in visited and other(edge_id, current) != previous
            ]
            if not candidates:
                candidates = [edge_id for edge_id in incident[current] if edge_id not in visited]
            if not candidates:
                break
            next_edge = candidates[0]
            next_node = other(next_edge, current)
            visited.add(next_edge)
            edge_ids.append(next_edge)
            node_path.append(next_node)
            previous, current = current, next_node
        reduce_chain(edge_ids, node_path)

    return arrow_edges


def _set_graph(self, graph: Optional[Dict[str, Any]]) -> None:
    """Render the DXF graph using the native dark Workbench theme."""

    self._white_canvas = False
    scene = self.scene()
    scene.clear()
    if not graph:
        label = scene.addText("DXF 파일을 선택하면 변환된 방향성 Graph가 표시됩니다.")
        label.setDefaultTextColor(QColor("#78909d"))
        return

    raw_nodes = graph.get("nodes", [])
    if not raw_nodes:
        label = scene.addText("표시할 Node가 없습니다.")
        label.setDefaultTextColor(QColor("#ffb86b"))
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
    arrow_edge_ids = _curved_chain_arrow_edges(graph, raw_nodes)

    for edge_id, edge in enumerate(edges):
        start_node = int(edge.get("start", -1))
        end_node = int(edge.get("end", -1))
        if start_node < 0 or end_node < 0 or start_node >= len(raw_nodes) or end_node >= len(raw_nodes):
            continue

        direction = edge.get("dir")
        directed = (
            isinstance(direction, list)
            and len(direction) == 2
            and all(isinstance(value, int) for value in direction)
        )
        source_id, target_id = (direction if directed else [start_node, end_node])

        path = QPainterPath()
        geometry = edge.get("geometry")
        if isinstance(geometry, list) and len(geometry) >= 2:
            path.moveTo(*raw_point(geometry[0]))
            for raw in geometry[1:]:
                path.lineTo(*raw_point(raw))
        else:
            path.moveTo(*point(start_node))
            path.lineTo(*point(end_node))

        rail_item = QGraphicsPathItem(path)
        rail_item.setPen(
            QPen(
                QColor("#315568"),
                2.6,
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin,
            )
        )
        rail_item.setZValue(1)
        scene.addItem(rail_item)

        if directed and edge_id in arrow_edge_ids:
            source_x, source_y = point(int(source_id))
            target_x, target_y = point(int(target_id))
            delta_x, delta_y = target_x - source_x, target_y - source_y
            magnitude = math.hypot(delta_x, delta_y)
            if magnitude > 0.1:
                unit_x, unit_y = delta_x / magnitude, delta_y / magnitude
                marker_x = source_x + delta_x * 0.62
                marker_y = source_y + delta_y * 0.62
                arrow_size = min(10.0, max(5.5, magnitude * 0.30))
                wing = arrow_size * 0.62
                base_x = marker_x - unit_x * arrow_size
                base_y = marker_y - unit_y * arrow_size
                arrow = QPainterPath()
                arrow.moveTo(marker_x, marker_y)
                arrow.lineTo(base_x - unit_y * wing, base_y + unit_x * wing)
                arrow.moveTo(marker_x, marker_y)
                arrow.lineTo(base_x + unit_y * wing, base_y - unit_x * wing)
                arrow_item = QGraphicsPathItem(arrow)
                arrow_item.setPen(
                    QPen(
                        QColor("#43e4d3"),
                        2.0,
                        Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap,
                        Qt.PenJoinStyle.RoundJoin,
                    )
                )
                arrow_item.setZValue(3)
                scene.addItem(arrow_item)

        direction_text = f"{source_id} -> {target_id}" if directed else "방향 미결정"
        rail_item.setToolTip(f"Edge {edge_id}\n{start_node} - {end_node}\n{direction_text}")

    metadata = graph.get("metadata", {})
    for label in metadata.get("labels", []):
        try:
            x = (float(label["x"]) - min_x) * scale
            y = (float(label["y"]) - min_y) * scale
        except (KeyError, TypeError, ValueError):
            continue
        text = QGraphicsSimpleTextItem(str(label.get("text", "")))
        text.setBrush(QColor("#a9c0cb"))
        text.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))
        text.setPos(x - 35, y - 18)
        text.setZValue(4)
        scene.addItem(text)

    node_radius = 3.5 if len(raw_nodes) < 2000 else 2.1
    for node_id in range(len(raw_nodes)):
        x, y = point(node_id)
        dot = QGraphicsEllipseItem(
            x - node_radius,
            y - node_radius,
            node_radius * 2,
            node_radius * 2,
        )
        dot.setBrush(QColor("#0b1b27"))
        dot.setPen(QPen(QColor("#719bad"), 1))
        dot.setZValue(2)
        dot.setToolTip(f"Node {node_id}\n({raw_nodes[node_id][0]}, {raw_nodes[node_id][1]})")
        scene.addItem(dot)

    bounds = scene.itemsBoundingRect().adjusted(-35, -35, 35, 35)
    scene.setSceneRect(bounds)
    self.resetTransform()
    self.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)


base.NetworkView.mousePressEvent = _mouse_press_event
base.NetworkView.mouseMoveEvent = _mouse_move_event
base.NetworkView.mouseReleaseEvent = _mouse_release_event
base.NetworkView.set_graph = _set_graph

MainWindow = base.MainWindow
NetworkView = base.NetworkView


def main() -> int:
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
