"""Sim_Core desktop entry point with graph interaction enhancements."""
from __future__ import annotations

import sys

import app_base as base
from curve_edge_fix import consolidate_arc_edges
from graph_enhancer_compat import install_compatible_enhancements
from graph_ui_patch import install_dark_graph_renderer, install_graph_interaction
from layout_static_analysis_patch import install_layout_static_analysis
from pan_fix import install_bidirectional_pan


_original_convert_dxf_to_graph = base.convert_dxf_to_graph


def _convert_dxf_to_graph_with_curve_merge(*args, **kwargs):  # type: ignore[no-untyped-def]
    graph = _original_convert_dxf_to_graph(*args, **kwargs)
    filename = args[0] if args else kwargs.get("filename")
    if filename is None:
        return graph
    return consolidate_arc_edges(
        graph,
        filename,
        layers=kwargs.get("layers"),
        arc_segments=int(kwargs.get("arc_segments", 10)),
        coordinate_precision=int(kwargs.get("coordinate_precision", 3)),
    )


# Shared graph behavior for preview and graph-only enlarged view.
install_graph_interaction(base.NetworkView)
install_dark_graph_renderer(base.NetworkView)
install_bidirectional_pan(base.NetworkView)
base.convert_dxf_to_graph = _convert_dxf_to_graph_with_curve_merge

# Keep the existing Random FromTo analysis intact and add a selectable real
# FromTo CSV path for Layout static analysis.  The real CSV is treated as
# read-only and only timestamped analysis snapshots are written.
install_layout_static_analysis(base)

MainWindow = base.MainWindow
NetworkView = base.NetworkView

# Restore the graph toolbar, graph-only popup, edge block selection and
# "selected direction reverse" button. The compatibility controller lets
# Shift+Left mouse events pass through to NetworkView panning.
install_compatible_enhancements(sys.modules[__name__])


def main() -> int:
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
