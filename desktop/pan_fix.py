"""Fast, reliable navigation for large graph views."""
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsView


ZOOM_STEP = 1.35
MIN_ZOOM_FROM_FIT = 0.20
MAX_ZOOM_FROM_FIT = 250.0


def install_bidirectional_pan(view_class: type[QGraphicsView]) -> None:
    """Add fast wheel zoom, middle-button pan and keyboard navigation."""
    original_press = view_class.mousePressEvent
    original_move = view_class.mouseMoveEvent
    original_release = view_class.mouseReleaseEvent
    original_wheel = view_class.wheelEvent
    original_key = view_class.keyPressEvent
    original_set_graph = getattr(view_class, "set_graph", None)

    def fit_graph_view(self) -> None:
        bounds = getattr(self, "_graph_content_bounds", None)
        if bounds is None or bounds.isNull() or bounds.isEmpty():
            scene = self.scene()
            if scene is None or not scene.items():
                return
            bounds = scene.itemsBoundingRect()
        margin_x = max(20.0, bounds.width() * 0.02)
        margin_y = max(20.0, bounds.height() * 0.02)
        target = bounds.adjusted(-margin_x, -margin_y, margin_x, margin_y)
        self.resetTransform()
        self.fitInView(target, Qt.AspectRatioMode.KeepAspectRatio)
        self._graph_fit_scale = max(abs(self.transform().m11()), 1e-9)

    def zoom_graph(self, factor: float) -> None:
        current = max(abs(self.transform().m11()), 1e-9)
        fit_scale = max(float(getattr(self, "_graph_fit_scale", current)), 1e-9)
        minimum = fit_scale * MIN_ZOOM_FROM_FIT
        maximum = fit_scale * MAX_ZOOM_FROM_FIT
        target = max(minimum, min(maximum, current * factor))
        actual_factor = target / current
        if abs(actual_factor - 1.0) > 1e-9:
            self.scale(actual_factor, actual_factor)

    def mouse_press(self, event):  # type: ignore[no-untyped-def]
        if event.button() == Qt.MouseButton.MiddleButton:
            self._middle_button_panning = True
            self._middle_pan_position = event.position().toPoint()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
            return
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

    def _pan_by_delta(self, delta) -> None:  # type: ignore[no-untyped-def]
        horizontal = self.horizontalScrollBar()
        vertical = self.verticalScrollBar()
        horizontal.setValue(horizontal.value() - delta.x())
        vertical.setValue(vertical.value() - delta.y())

    def mouse_move(self, event):  # type: ignore[no-untyped-def]
        if getattr(self, "_middle_button_panning", False):
            current = event.position().toPoint()
            delta = current - self._middle_pan_position
            self._middle_pan_position = current
            _pan_by_delta(self, delta)
            event.accept()
            return
        if getattr(self, "_bidirectional_panning", False):
            current = event.position().toPoint()
            delta = current - self._bidirectional_pan_position
            self._bidirectional_pan_position = current
            _pan_by_delta(self, delta)
            event.accept()
            return
        original_move(self, event)

    def mouse_release(self, event):  # type: ignore[no-untyped-def]
        if event.button() == Qt.MouseButton.MiddleButton and getattr(self, "_middle_button_panning", False):
            self._middle_button_panning = False
            self.unsetCursor()
            event.accept()
            return
        if event.button() == Qt.MouseButton.LeftButton and getattr(self, "_bidirectional_panning", False):
            self._bidirectional_panning = False
            self.unsetCursor()
            event.accept()
            return
        original_release(self, event)

    def wheel_event(self, event):  # type: ignore[no-untyped-def]
        delta = event.angleDelta().y()
        if delta == 0:
            original_wheel(self, event)
            return
        # 120 is one conventional wheel notch. Fractional values also work for touchpads.
        steps = delta / 120.0
        zoom_graph(self, ZOOM_STEP**steps)
        event.accept()

    def key_press(self, event):  # type: ignore[no-untyped-def]
        key = event.key()
        if key in (Qt.Key.Key_Home, Qt.Key.Key_0):
            fit_graph_view(self)
            event.accept()
            return

        horizontal = self.horizontalScrollBar()
        vertical = self.verticalScrollBar()
        step_x = max(60, int(self.viewport().width() * 0.25))
        step_y = max(60, int(self.viewport().height() * 0.25))
        if key == Qt.Key.Key_Left:
            horizontal.setValue(horizontal.value() - step_x)
        elif key == Qt.Key.Key_Right:
            horizontal.setValue(horizontal.value() + step_x)
        elif key == Qt.Key.Key_Up:
            vertical.setValue(vertical.value() - step_y)
        elif key == Qt.Key.Key_Down:
            vertical.setValue(vertical.value() + step_y)
        else:
            original_key(self, event)
            return
        event.accept()

    def set_graph(self, graph):  # type: ignore[no-untyped-def]
        if original_set_graph is not None:
            original_set_graph(self, graph)
        scene = self.scene()
        if scene is None or not scene.items():
            return

        # Keep the real content bounds separately from the padded navigation area.
        # The extra area guarantees that both axes remain pannable even after fitInView.
        content = scene.itemsBoundingRect()
        self._graph_content_bounds = content
        self._graph_fit_scale = max(abs(self.transform().m11()), 1e-9)
        pad_x = max(content.width(), 400.0)
        pad_y = max(content.height(), 400.0)
        scene.setSceneRect(content.adjusted(-pad_x, -pad_y, pad_x, pad_y))

    view_class.fit_graph_view = fit_graph_view
    view_class.zoom_graph = zoom_graph
    view_class.mousePressEvent = mouse_press
    view_class.mouseMoveEvent = mouse_move
    view_class.mouseReleaseEvent = mouse_release
    view_class.wheelEvent = wheel_event
    view_class.keyPressEvent = key_press
    if original_set_graph is not None:
        view_class.set_graph = set_graph
