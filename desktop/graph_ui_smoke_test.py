"""Smoke test for Graph generation UI enhancements."""
from __future__ import annotations

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from app_wrapper import MainWindow


def main() -> int:
    application = QApplication.instance() or QApplication([])
    window = MainWindow()
    window.show()
    application.processEvents()

    if not getattr(window, "_graph_ui_enhanced", False):
        raise RuntimeError("graph UI enhancements were not installed")
    controller = getattr(window, "_graph_selection_controller", None)
    if controller is None:
        raise RuntimeError("graph selection controller was not created")
    if window.cad_graph_view.minimumHeight() < 470:
        raise RuntimeError("CAD graph canvas was not enlarged")

    for card in window.file_cards.values():
        visible_icons = [
            label
            for label in card.findChildren(type(window.cad_graph_status))
            if label.objectName() in {"FileIcon", "AvailableBadge", "PrototypeBadge"}
            and label.isVisible()
        ]
        if visible_icons:
            raise RuntimeError("wasted file-card icon/badge space is still visible")

    window.close()
    print("graph UI enhancement smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
