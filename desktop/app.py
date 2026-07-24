"""Sim_Core desktop entry point with graph, Layout and AutoMod enhancements."""
from __future__ import annotations

import sys

import app_base as base
from automod_modeling_patch import install_automod_modeling
from english_ui_patch import install_english_ui
from graph_enhancer_compat import install_compatible_enhancements
from graph_render_optimization import install_fast_graph_renderer
from graph_ui_patch import install_dark_graph_renderer, install_graph_interaction
from input_ui_compact_patch import install_input_ui_compact
from layout_static_analysis_patch import install_layout_static_analysis
from pan_fix import install_bidirectional_pan
from rail_static_analysis_compat import install_rail_compat


# Preserve the high-speed graph renderer from main.
install_graph_interaction(base.NetworkView)
install_dark_graph_renderer(base.NetworkView)
install_fast_graph_renderer(base.NetworkView)
install_bidirectional_pan(base.NetworkView)

# Layer optional feature patches on the current workbench without replacing
# app_base: Rail/DXF support, Layout static analysis, then AutoMod export.
install_rail_compat(base)
install_layout_static_analysis(base)
install_automod_modeling(base)

MainWindow = base.MainWindow
NetworkView = base.NetworkView

# Graph toolbar, enlarged popup, block selection and direction reversal.
install_compatible_enhancements(sys.modules[__name__])

# Apply the final input-page presentation pass after every feature has added
# its controls, so Layout/CAD panels stay compact without changing behavior.
install_input_ui_compact(base)

# English-only branch: translate all user-facing Qt text, including dynamic
# dialogs/status messages, and apply the dedicated Sim_Core application icon.
install_english_ui(base)


def main() -> int:
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
