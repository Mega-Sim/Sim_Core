"""Viewport-culling renderer for large CAD graph previews.

The graph data stays unchanged. This module only changes how Guide Paths, arrows,
labels and nodes are drawn on the Qt canvas so very large FAB layouts remain
responsive while panning and zooming.
"""
from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Dict, Optional

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsItem, QGraphicsPathItem, QGraphicsScene, QGraphicsView


EDGE_COLOR = QColor("#315568")
EDGE_SELECTED_COLOR = QColor("#ffd54f")
ARROW_COLOR = QColor("#43e4d3")
STATION_LABEL_SCALE = 0.1
ARROW_SCALE = 0.2
RENDER_TILE_SIZE = 120.0
ARROW_MIN_VIEW_SCALE = 1.15


def _cosmetic_pen(color: QColor, width: float) -> QPen:
    """Return a CAD-like screen-space pen that never becomes thick when zooming."""
    pen = QPen(color)
    pen.setWidthF(width)
    pen.setCosmetic(True)
    pen.setStyle(Qt.PenStyle.SolidLine)
    pen.setCapStyle(Qt.PenCapStyle.FlatCap)
    pen.setJoinStyle(Qt.PenJoinStyle.MiterJoin)
    return pen


def _tile_key(x: float, y: float) -> tuple[int, int]:
    return int(math.floor(x / RENDER_TILE_SIZE)), int(math.floor(y / RENDER_TILE_SIZE))


def _bucket_path(
    buckets: dict[tuple[int, int], QPainterPath],
    key: tuple[int, int],
) -> QPainterPath:
    path = buckets.get(key)
    if path is None:
        path = QPainterPath()
        buckets[key] = path
    return path


class _ZoomPathItem(QGraphicsPathItem):
    """Skip detail paths until the user zooms in enough to benefit from them."""

    def __init__(self, path: QPainterPath, minimum_scale: float) -> None:
        super().__init__(path)
        self._minimum_scale = minimum_scale

    def paint(self, painter: QPainter, option: Any, widget: Any = None) -> None:
        transform = painter.worldTransform()
        level = max(abs(transform.m11()), abs(transform.m22()))
        if level < self._minimum_scale:
            return
        super().paint(painter, option, widget)


class _SpatialLabelsItem(QGraphicsItem):
    """Paint only labels that fall inside the currently exposed viewport tiles."""

    def __init__(self, labels: list[tuple[float, float, str]], bounds: QRectF) -> None:
        super().__init__()
        self._bounds = bounds.adjusted(-80.0, -40.0, 80.0, 40.0)
        self._label_count = len(labels)
        self._tiles: defaultdict[tuple[int, int], list[tuple[float, float, str]]] = defaultdict(list)
        for x, y, text in labels:
            self._tiles[_tile_key(x, y)].append((x, y, text))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemUsesExtendedStyleOption, True)
        self.setZValue(4)

    def boundingRect(self) -> QRectF:  # noqa: N802
        return self._bounds

    def paint(self, painter: QPainter, option: Any, _widget: Any = None) -> None:
        transform = painter.worldTransform()
        level = max(abs(transform.m11()), abs(transform.m22()))
        if self._label_count > 500 and level < 0.72:
            return

        exposed = option.exposedRect.adjusted(-80.0, -30.0, 80.0, 30.0)
        min_tx = int(math.floor(exposed.left() / RENDER_TILE_SIZE))
        max_tx = int(math.floor(exposed.right() / RENDER_TILE_SIZE))
        min_ty = int(math.floor(exposed.top() / RENDER_TILE_SIZE))
        max_ty = int(math.floor(exposed.bottom() / RENDER_TILE_SIZE))

        painter.save()
        painter.setPen(QColor("#a9c0cb"))
        painter.setFont(QFont("Segoe UI", max(1, round(10 * STATION_LABEL_SCALE)), QFont.Weight.DemiBold))
        for tx in range(min_tx, max_tx + 1):
            for ty in range(min_ty, max_ty + 1):
                for x, y, label in self._tiles.get((tx, ty), ()):
                    if exposed.contains(QPointF(x, y)):
                        painter.drawText(
                            QPointF(x - 35.0 * STATION_LABEL_SCALE, y - 4.0 * STATION_LABEL_SCALE),
                            label,
                        )
        painter.restore()


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


def install_fast_graph_renderer(view_class: type[QGraphicsView]) -> None:
    """Replace the graph preview with a tiled, viewport-culling renderer.

    Important: nodes remain in the graph model and are still used for routing and
    edge geometry. Only the circular node markers are omitted from canvas paint.
    """

    original_init = view_class.__init__

    def init(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        original_init(self, *args, **kwargs)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.MinimalViewportUpdate)
        self.setOptimizationFlag(QGraphicsView.OptimizationFlag.DontAdjustForAntialiasing, True)
        self.setCacheMode(QGraphicsView.CacheModeFlag.CacheBackground)

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
        self.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        scene = self.scene()
        scene.clear()
        scene.setItemIndexMethod(QGraphicsScene.ItemIndexMethod.BspTreeIndex)
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

        rail_tiles: dict[tuple[int, int], QPainterPath] = {}
        arrow_tiles: dict[tuple[int, int], QPainterPath] = {}
        content_bounds = QRectF(
            0.0,
            0.0,
            max((max_x - min_x) * scale, 1.0),
            max((max_y - min_y) * scale, 1.0),
        )

        for edge in graph.get("edges", []):
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

            edge_path = QPainterPath()
            edge_path.moveTo(*polyline[0])
            for first, second in zip(polyline, polyline[1:]):
                edge_path.lineTo(*second)
                mid_x = (first[0] + second[0]) * 0.5
                mid_y = (first[1] + second[1]) * 0.5
                tile_path = _bucket_path(rail_tiles, _tile_key(mid_x, mid_y))
                tile_path.moveTo(*first)
                tile_path.lineTo(*second)

            self._graph_edge_polylines.append(polyline)
            self._graph_edge_bounds.append(edge_path.boundingRect())

            if not directed:
                continue

            oriented = (
                list(reversed(polyline))
                if [int(source_id), int(target_id)] == [end_node, start_node]
                else polyline
            )
            segment_lengths = [math.dist(first, second) for first, second in zip(oriented, oriented[1:])]
            total_length = sum(segment_lengths)
            if total_length <= 1.0:
                continue

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
            arrow_path = _bucket_path(arrow_tiles, _tile_key(marker_x, marker_y))
            arrow_path.moveTo(marker_x, marker_y)
            arrow_path.lineTo(base_x - uy * wing, base_y + ux * wing)
            arrow_path.moveTo(marker_x, marker_y)
            arrow_path.lineTo(base_x + uy * wing, base_y - ux * wing)

        # AutoMod-like light Guide Path display: split the layout into small scene
        # tiles so Qt can cull off-screen geometry instead of repainting one giant path.
        guide_pen = _cosmetic_pen(EDGE_COLOR, 1.0)
        for tile_path in rail_tiles.values():
            rail_item = QGraphicsPathItem(tile_path)
            rail_item.setPen(guide_pen)
            rail_item.setData(0, "graph-edge-tile")
            rail_item.setZValue(1)
            scene.addItem(rail_item)

        # Direction arrows are detail information. Hide them in the full-layout
        # overview and paint only zoomed-in, visible tiles.
        arrow_pen = _cosmetic_pen(ARROW_COLOR, 1.0)
        for tile_path in arrow_tiles.values():
            arrow_item = _ZoomPathItem(tile_path, ARROW_MIN_VIEW_SCALE)
            arrow_item.setPen(arrow_pen)
            arrow_item.setZValue(3)
            scene.addItem(arrow_item)

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
            scene.addItem(_SpatialLabelsItem(label_records, content_bounds))

        # Intentionally do not create QGraphicsEllipseItem node markers here.
        # The raw node list remains untouched in graph and continues to drive
        # routing, edge direction, selection lookup and JSON export.

        selection_item = QGraphicsPathItem()
        selection_item.setPen(_cosmetic_pen(EDGE_SELECTED_COLOR, 2.0))
        selection_item.setZValue(5)
        scene.addItem(selection_item)
        self._graph_selection_item = selection_item

        bounds = content_bounds.adjusted(-35.0, -35.0, 35.0, 35.0)
        scene.setSceneRect(bounds)
        self.resetTransform()
        self.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)

    view_class.__init__ = init
    view_class.graph_edge_at = graph_edge_at
    view_class.graph_edges_in_rect = graph_edges_in_rect
    view_class.set_graph_selection = set_graph_selection
    view_class.set_graph = set_graph
