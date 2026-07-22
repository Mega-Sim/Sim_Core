"""Graph UI behavior and DXF graph post-processing for Sim_Core."""
from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Dict, Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsPathItem, QGraphicsSimpleTextItem, QGraphicsView


def install_shift_left_pan(view_class: type[QGraphicsView]) -> None:
    """Enable Shift+Left drag panning even when fitInView leaves no scroll range."""
    original_press = view_class.mousePressEvent
    original_move = view_class.mouseMoveEvent
    original_release = view_class.mouseReleaseEvent

    def mouse_press(self, event):  # type: ignore[no-untyped-def]
        if event.button() == Qt.MouseButton.LeftButton and bool(event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            self._shift_left_panning = True
            self._shift_left_pan_position = event.position().toPoint()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
            return
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

    view_class.mousePressEvent = mouse_press
    view_class.mouseMoveEvent = mouse_move
    view_class.mouseReleaseEvent = mouse_release


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

    # Compact topology nodes while preserving intermediate curve coordinates only in geometry.
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
    """Install the Workbench dark-theme directed graph renderer."""
    def set_graph(self, graph: Optional[Dict[str, Any]]) -> None:
        self._white_canvas = False
        scene = self.scene()
        scene.clear()
        if not graph:
            label = scene.addText("DXF 파일을 선택하면 변환된 방향성 Graph가 표시됩니다.")
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

        for edge_id, edge in enumerate(graph.get("edges", [])):
            start_node, end_node = int(edge.get("start", -1)), int(edge.get("end", -1))
            if not (0 <= start_node < len(raw_nodes) and 0 <= end_node < len(raw_nodes)):
                continue
            direction = edge.get("dir")
            directed = isinstance(direction, list) and len(direction) == 2
            source_id, target_id = (direction if directed else [start_node, end_node])

            path = QPainterPath()
            geometry = edge.get("geometry")
            if isinstance(geometry, list) and len(geometry) >= 2:
                path.moveTo(*raw_point(geometry[0]))
                for raw in geometry[1:]:
                    path.lineTo(*raw_point(raw))
            else:
                path.moveTo(*point(start_node)); path.lineTo(*point(end_node))
            rail = QGraphicsPathItem(path)
            rail.setPen(QPen(QColor("#315568"), 2.6, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            rail.setZValue(1)
            scene.addItem(rail)

            if directed:
                source_x, source_y = point(int(source_id)); target_x, target_y = point(int(target_id))
                dx, dy = target_x - source_x, target_y - source_y
                magnitude = math.hypot(dx, dy)
                if magnitude > 0.1:
                    ux, uy = dx / magnitude, dy / magnitude
                    marker_x, marker_y = source_x + dx * 0.62, source_y + dy * 0.62
                    arrow_size = min(10.0, max(5.5, magnitude * 0.30)); wing = arrow_size * 0.62
                    base_x, base_y = marker_x - ux * arrow_size, marker_y - uy * arrow_size
                    arrow = QPainterPath(); arrow.moveTo(marker_x, marker_y)
                    arrow.lineTo(base_x - uy * wing, base_y + ux * wing); arrow.moveTo(marker_x, marker_y)
                    arrow.lineTo(base_x + uy * wing, base_y - ux * wing)
                    arrow_item = QGraphicsPathItem(arrow)
                    arrow_item.setPen(QPen(QColor("#43e4d3"), 2.0, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
                    arrow_item.setZValue(3); scene.addItem(arrow_item)

            rail.setToolTip(f"Edge {edge_id}\n{start_node} - {end_node}\n{source_id} -> {target_id}" if directed else f"Edge {edge_id}\n방향 미결정")

        for label in graph.get("metadata", {}).get("labels", []):
            try:
                x = (float(label["x"]) - min_x) * scale; y = (float(label["y"]) - min_y) * scale
            except (KeyError, TypeError, ValueError):
                continue
            text = QGraphicsSimpleTextItem(str(label.get("text", "")))
            text.setBrush(QColor("#a9c0cb")); text.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold)); text.setPos(x - 35, y - 18); text.setZValue(4)
            scene.addItem(text)

        node_radius = 3.5 if len(raw_nodes) < 2000 else 2.1
        for node_id in range(len(raw_nodes)):
            x, y = point(node_id)
            dot = QGraphicsEllipseItem(x - node_radius, y - node_radius, node_radius * 2, node_radius * 2)
            dot.setBrush(QColor("#0b1b27")); dot.setPen(QPen(QColor("#719bad"), 1)); dot.setZValue(2)
            dot.setToolTip(f"Node {node_id}\n({raw_nodes[node_id][0]}, {raw_nodes[node_id][1]})")
            scene.addItem(dot)

        bounds = scene.itemsBoundingRect().adjusted(-35, -35, 35, 35)
        scene.setSceneRect(bounds); self.resetTransform(); self.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)

    view_class.set_graph = set_graph
