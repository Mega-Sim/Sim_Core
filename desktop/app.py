"""Sim_Core desktop entry point with graph interaction enhancements."""
from __future__ import annotations

import sys

import app_base as base
from graph_enhancer_compat import install_compatible_enhancements
from graph_render_optimization import install_fast_graph_renderer
from graph_ui_patch import install_dark_graph_renderer, install_graph_interaction
from pan_fix import install_bidirectional_pan


# Shared graph behavior for preview and graph-only enlarged view.
install_graph_interaction(base.NetworkView)
install_dark_graph_renderer(base.NetworkView)
install_fast_graph_renderer(base.NetworkView)
install_bidirectional_pan(base.NetworkView)

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
