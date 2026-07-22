"""Compatibility layer between graph selection toolbar and Shift+Left panning."""
from __future__ import annotations

from typing import Any

from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QColor, QPen

import graph_ui_enhancer as enhancer


class CompatibleGraphSelectionController(enhancer.GraphSelectionController):
    """Let Shift+Left events reach NetworkView while preserving edge selection."""

    def eventFilter(self, watched: Any, event: Any) -> bool:  # noqa: N802
        if watched is self.view.viewport():
            event_type = event.type()
            mouse_types = {
                QEvent.Type.MouseButtonPress,
                QEvent.Type.MouseMove,
                QEvent.Type.MouseButtonRelease,
            }
            if event_type in mouse_types and bool(event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
                self.dragging = False
                self.rubber_band.hide()
                return False
            if event_type == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Escape:
                self.selected_edges.clear()
                self.highlight()
                return False
        return super().eventFilter(watched, event)

    def highlight(self) -> None:
        # Always restore the normal rail appearance first, then highlight selection.
        for item in self.view.scene().items():
            edge_id = enhancer._edge_id_from_item(item)
            if edge_id is None or not hasattr(item, "pen") or not hasattr(item, "setPen"):
                continue
            pen = item.pen()
            width = 4.5 if edge_id in self.selected_edges else 2.6
            color = QColor("#ffd54f") if edge_id in self.selected_edges else QColor("#315568")
            item.setPen(QPen(color, width, pen.style(), pen.capStyle(), pen.joinStyle()))


def install_compatible_enhancements(module: Any) -> None:
    """Restore graph toolbar/fullscreen/direction controls without blocking Shift pan."""
    enhancer.GraphSelectionController = CompatibleGraphSelectionController
    enhancer.install_enhancements(module)
