"""Sim_Core desktop entry point with graph interaction and Layout analysis enhancements."""
from __future__ import annotations

import sys

import app_base as base
from graph_enhancer_compat import install_compatible_enhancements
from graph_render_optimization import install_fast_graph_renderer
from graph_ui_patch import install_dark_graph_renderer, install_graph_interaction
from layout_static_analysis_patch import install_layout_static_analysis
from pan_fix import install_bidirectional_pan
from rail_static_analysis_compat import install_rail_compat


# Preserve the high-speed graph renderer from main.
install_graph_interaction(base.NetworkView)
install_dark_graph_renderer(base.NetworkView)
install_fast_graph_renderer(base.NetworkView)
install_bidirectional_pan(base.NetworkView)

# Restore .rail support on top of the Layout static-analysis app_base, then add
# Random/Actual FromTo mode selection without touching the source CSV.
install_rail_compat(base)
install_layout_static_analysis(base)

MainWindow = base.MainWindow
NetworkView = base.NetworkView

# Graph toolbar, enlarged popup, block selection and direction reversal.
install_compatible_enhancements(sys.modules[__name__])


def main() -> int:
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
