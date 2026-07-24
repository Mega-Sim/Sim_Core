"""Render CAD Layout static analysis with the same canvas as Conversion Preview.

The existing static-analysis popup owns a separate Facility renderer.  That makes
its background, labels, direction arrows and large-layout performance differ from
the CAD Conversion Preview even when both screens represent the same DXF graph.

This patch keeps the analysis dialog and metrics intact, replaces only its canvas
with the already configured ``NetworkView``, and overlays the green-to-red load
heatmap on the exact graph polylines produced by ``NetworkView.set_graph``.
"""
from __future__ import annotations

import math
import re
from collections import defaultdict
from collections.abc import Mapping
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainterPath, QPen
from PySide6.QtWidgets import QGraphicsPathItem

import layout_static_analysis_patch
import random_flow_ui


_SOURCE_GRAPH_EDGE = re.compile(r"^graph-edge:(\d+)(?::part:\d+)?$")
_FACILITY_EDGE_ID = re.compile(r"^E-(\d+)(?:-\d+)?$")
_TILE_SIZE = 120.0
_HEAT_LEVELS = 24


def _source_graph_edge_index(edge: Mapping[str, Any]) -> int | None:
    """Resolve a canonical Facility edge back to its Conversion Preview edge."""

    identities = edge.get("source_identities", [])
    if isinstance(identities, list):
        for identity in identities:
            if not isinstance(identity, Mapping):
                continue
            match = _SOURCE_GRAPH_EDGE.fullmatch(
                str(identity.get("external_id", "")).strip()
            )
            if match:
                return int(match.group(1))

    # Compatibility fallback for older CAD Facility snapshots whose edge IDs
    # still preserve the original E-00000[-part] numbering convention.
    match = _FACILITY_EDGE_ID.fullmatch(str(edge.get("id", "")).strip())
    return int(match.group(1)) if match else None


def graph_edge_moves(
    facility: Mapping[str, Any], analysis: Mapping[str, Any]
) -> dict[int, float]:
    """Return the maximum routed load represented by each original graph edge.

    Station projection can split one Conversion Preview edge into multiple
    canonical Facility edges.  The preview cannot visually split that source
    edge without changing its geometry, so the highest loaded part determines
    the color of the original edge.  This preserves the exact preview shape
    while avoiding artificial double counting across sequential split parts.
    """

    flow_by_facility_edge = {
        str(item.get("edge_id", "")): float(
            item.get("expected_moves_per_hour", 0.0) or 0.0
        )
        for item in analysis.get("edge_flows", [])
        if isinstance(item, Mapping) and item.get("edge_id")
    }

    loads: dict[int, float] = {}
    for edge in facility.get("edges", []):
        if not isinstance(edge, Mapping):
            continue
        graph_edge_index = _source_graph_edge_index(edge)
        if graph_edge_index is None:
            continue
        moves = max(0.0, flow_by_facility_edge.get(str(edge.get("id", "")), 0.0))
        loads[graph_edge_index] = max(loads.get(graph_edge_index, 0.0), moves)
    return loads


def _tile_key(x: float, y: float) -> tuple[int, int]:
    return int(math.floor(x / _TILE_SIZE)), int(math.floor(y / _TILE_SIZE))


def _overlay_heatmap(
    view: Any,
    facility: Mapping[str, Any],
    analysis: Mapping[str, Any],
) -> None:
    """Replace base guide paths with tiled heatmap paths on the same scene."""

    scene = view.scene()
    polylines = list(getattr(view, "_graph_edge_polylines", []))
    if not polylines:
        return

    # Keep arrows, labels, selection and the CAD background from Conversion
    # Preview, but hide its neutral guide-path tiles before drawing heat colors.
    for item in scene.items():
        if item.data(0) == "graph-edge-tile":
            item.setVisible(False)

    moves_by_graph_edge = graph_edge_moves(facility, analysis)
    max_moves = max(moves_by_graph_edge.values(), default=0.0)
    buckets: dict[tuple[int, int, int], QPainterPath] = defaultdict(QPainterPath)

    for edge_index, polyline in enumerate(polylines):
        if len(polyline) < 2:
            continue
        moves = moves_by_graph_edge.get(edge_index, 0.0)
        relative = moves / max_moves if max_moves > 0 else 0.0
        level = min(_HEAT_LEVELS, max(0, int(round(relative * _HEAT_LEVELS))))
        for first, second in zip(polyline, polyline[1:]):
            mid_x = (float(first[0]) + float(second[0])) * 0.5
            mid_y = (float(first[1]) + float(second[1])) * 0.5
            path = buckets[(*_tile_key(mid_x, mid_y), level)]
            path.moveTo(float(first[0]), float(first[1]))
            path.lineTo(float(second[0]), float(second[1]))

    for (_tile_x, _tile_y, level), path in buckets.items():
        relative = level / _HEAT_LEVELS
        pen = QPen(random_flow_ui.heatmap_color(relative))
        pen.setWidthF(1.15)
        pen.setCosmetic(True)
        pen.setStyle(Qt.PenStyle.SolidLine)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        pen.setJoinStyle(Qt.PenJoinStyle.MiterJoin)
        item = QGraphicsPathItem(path)
        item.setPen(pen)
        item.setData(0, "layout-static-heatmap-tile")
        item.setData(1, level)
        item.setZValue(2)
        scene.addItem(item)

    # Expose the mapping for graph interaction diagnostics and regression tests.
    view._layout_static_graph_edge_moves = moves_by_graph_edge
    view._layout_static_heatmap_max_moves = max_moves


def _replace_heatmap_canvas(
    dialog: Any,
    parent: Any,
    facility: Mapping[str, Any],
    analysis: Mapping[str, Any],
    base_module: Any,
) -> None:
    graph = getattr(parent, "cad_graph", None)
    if getattr(parent, "_active_layout_kind", "") != "cad" or not isinstance(
        graph, Mapping
    ):
        return

    old_view = next(
        (
            child
            for child in dialog.findChildren(random_flow_ui.FlowHeatmapView)
            if child.objectName() == "RandomFlowHeatmap"
        ),
        None,
    )
    if old_view is None:
        return

    container = old_view.parentWidget()
    layout = container.layout() if container is not None else None
    if layout is None:
        return
    index = layout.indexOf(old_view)
    if index < 0:
        return

    preview = base_module.NetworkView()
    preview.setObjectName("RandomFlowHeatmap")
    preview.setMinimumHeight(max(400, old_view.minimumHeight()))
    preview.set_graph(dict(graph))
    _overlay_heatmap(preview, facility, analysis)

    layout.removeWidget(old_view)
    old_view.hide()
    old_view.deleteLater()
    layout.insertWidget(index, preview, 1)
    dialog._layout_static_preview_view = preview


def install_layout_static_preview(base_module: Any) -> None:
    """Install the shared Conversion Preview renderer for Layout analysis."""

    if getattr(base_module.MainWindow, "_layout_static_preview_installed", False):
        return
    base_module.MainWindow._layout_static_preview_installed = True

    original_show_dialog = random_flow_ui.show_random_flow_dialog

    def show_dialog(
        parent: Any,
        facility: Mapping[str, Any],
        workload: Any,
        saved: Any,
    ) -> Any:
        dialog = original_show_dialog(parent, facility, workload, saved)
        try:
            _replace_heatmap_canvas(
                dialog,
                parent,
                facility,
                workload.analysis,
                base_module,
            )
        except Exception as error:
            # Rendering must never discard a completed analysis.  Keep the
            # original Facility heatmap as a safe fallback and retain the reason
            # as a Qt property for diagnostics.
            dialog.setProperty("layoutStaticPreviewFallback", str(error))
        return dialog

    # Both call sites captured the function during module import, so rebind all
    # three references after Layout static-analysis installation.
    random_flow_ui.show_random_flow_dialog = show_dialog
    layout_static_analysis_patch.show_random_flow_dialog = show_dialog
    base_module.show_random_flow_dialog = show_dialog
