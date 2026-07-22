"""Sim_Core desktop entry point with graph interaction enhancements."""
from __future__ import annotations

import app_base as base
from graph_ui_patch import (
    consolidate_curve_edges,
    install_dark_graph_renderer,
    install_graph_interaction,
)


_original_convert_dxf_to_graph = base.convert_dxf_to_graph


def _convert_dxf_to_graph_with_curve_merge(*args, **kwargs):  # type: ignore[no-untyped-def]
    graph = _original_convert_dxf_to_graph(*args, **kwargs)
    return consolidate_curve_edges(graph)


# Apply all graph behaviors to the shared NetworkView class.  Any normal preview
# or enlarged graph view created from this class inherits the same interaction.
install_graph_interaction(base.NetworkView)
install_dark_graph_renderer(base.NetworkView)
base.convert_dxf_to_graph = _convert_dxf_to_graph_with_curve_merge

MainWindow = base.MainWindow
NetworkView = base.NetworkView


def main() -> int:
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
