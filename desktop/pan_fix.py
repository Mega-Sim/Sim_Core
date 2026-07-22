"""Reliable bidirectional Shift+Left panning for graph views."""
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsView


def install_bidirectional_pan(view_class: type[QGraphicsView]) -> None:
    """Allow Shift+Left panning on both axes even when the graph initially fits."""
    original_press = view_class.mousePressEvent
    original_move = view_class.mouseMoveEvent
    original_release = view_class.mouseReleaseEvent
    original_set_graph = getattr(view_class, "set_graph", None)

    def mouse_press(self, event):  # type: ignore[no-untyped-def]
        if (
            event.button() == Qt.MouseButton.LeftButton
            and bool(event.modifiers() & Qt.KeyboardModifier.ShiftModifier)
        ):
            self._bidirectional_panning = True
            self._bidirectional_pan_position = event.position().toPoint()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
            return
        original_press(self, event)

    def mouse_move(self, event):  # type: ignore[no-untyped-def]
        if getattr(self, "_bidirectional_panning", False):
            current = event.position().toPoint()
            delta = current - self._bidirectional_pan_position
            self._bidirectional_pan_position = current

            horizontal = self.horizontalScrollBar()
            vertical = self.verticalScrollBar()
            horizontal.setValue(horizontal.value() - delta.x())
            vertical.setValue(vertical.value() - delta.y())
            event.accept()
            return
        original_move(self, event)

    def mouse_release(self, event):  # type: ignore[no-untyped-def]
        if (
            event.button() == Qt.MouseButton.LeftButton
            and getattr(self, "_bidirectional_panning", False)
        ):
            self._bidirectional_panning = False
            self.unsetCursor()
            event.accept()
            return
        original_release(self, event)

    def set_graph(self, graph):  # type: ignore[no-untyped-def]
        if original_set_graph is not None:
            original_set_graph(self, graph)
        scene = self.scene()
        if scene is None or not scene.items():
            return

        # fitInView normally leaves one axis with no scroll range when the graph
        # aspect ratio is wider/taller than the viewport.  Expand the navigable
        # scene after fitting so Shift+Left drag always has horizontal and
        # vertical room without changing the initial zoom level.
        content = scene.itemsBoundingRect()
        pad_x = max(content.width(), 400.0)
        pad_y = max(content.height(), 400.0)
        scene.setSceneRect(content.adjusted(-pad_x, -pad_y, pad_x, pad_y))

    view_class.mousePressEvent = mouse_press
    view_class.mouseMoveEvent = mouse_move
    view_class.mouseReleaseEvent = mouse_release
    if original_set_graph is not None:
        view_class.set_graph = set_graph
