"""Final English-only cleanup for the Applied Materials sharing build."""
from __future__ import annotations

import sys
from typing import Any

from PySide6.QtWidgets import QGraphicsView, QLabel, QPushButton, QWidget

from english_ui_patch import _translate_text


_SUBSTRING_REPLACEMENTS = (
    ("워크스페이스", "Workspace"),
    ("입력 · CAD", "Inputs · CAD"),
    ("Flow 분석", "Flow Analysis"),
    ("시뮬레이션", "Simulation"),
)

_SCENE_TEXT_REPLACEMENTS = {
    "Facility JSON을 연결하면 레이아웃이 표시됩니다.": "Connect a Facility JSON file to display the layout.",
    "DXF 파일을 선택하면 변환된 방향성 Graph가 표시됩니다.": "Select a DXF file to display the converted directed graph.",
    "DXF 또는 Rail 파일을 선택하면 방향성 Graph가 표시됩니다.": "Select a DXF or Rail file to display the directed graph.",
    "표시할 Node가 없습니다.": "No nodes are available to display.",
    "표시할 Node 좌표가 없습니다.": "No node coordinates are available to display.",
}


def _translate_remaining_text(text: str) -> str:
    translated = _translate_text(text)
    for source, target in _SUBSTRING_REPLACEMENTS:
        translated = translated.replace(source, target)
    return translated


def _translate_graphics_view(view: QGraphicsView) -> None:
    scene = view.scene()
    if scene is None:
        return
    for item in scene.items():
        if hasattr(item, "toolTip") and hasattr(item, "setToolTip"):
            tooltip = item.toolTip()
            if tooltip:
                item.setToolTip(_translate_remaining_text(tooltip))
        if hasattr(item, "toPlainText") and hasattr(item, "setPlainText"):
            text = item.toPlainText()
            replacement = _SCENE_TEXT_REPLACEMENTS.get(text)
            if replacement is not None:
                item.setPlainText(replacement)
        elif hasattr(item, "text") and hasattr(item, "setText"):
            text = item.text()
            replacement = _SCENE_TEXT_REPLACEMENTS.get(text)
            if replacement is not None:
                item.setText(replacement)


def _translate_remaining(root: QWidget) -> None:
    for label in root.findChildren(QLabel):
        if label.objectName() == "FileName":
            continue
        label.setText(_translate_remaining_text(label.text()))
    for button in root.findChildren(QPushButton):
        button.setText(_translate_remaining_text(button.text()))
    for view in root.findChildren(QGraphicsView):
        _translate_graphics_view(view)


def _wrap_widget_method(cls: type, name: str) -> None:
    original = getattr(cls, name, None)
    if not callable(original) or getattr(original, "_applied_finalizer_wrapped", False):
        return

    def wrapped(self: Any, *args: Any, **kwargs: Any) -> Any:
        result = original(self, *args, **kwargs)
        _translate_remaining(self)
        return result

    wrapped._applied_finalizer_wrapped = True  # type: ignore[attr-defined]
    setattr(cls, name, wrapped)


def _wrap_view_method(view_class: type, name: str) -> None:
    original = getattr(view_class, name, None)
    if not callable(original) or getattr(original, "_applied_finalizer_wrapped", False):
        return

    def wrapped(self: Any, *args: Any, **kwargs: Any) -> Any:
        result = original(self, *args, **kwargs)
        _translate_graphics_view(self)
        return result

    wrapped._applied_finalizer_wrapped = True  # type: ignore[attr-defined]
    setattr(view_class, name, wrapped)


def install_applied_share_finalizer(base_module: Any) -> None:
    """Translate text surfaces created after the main English presentation pass."""

    cls = base_module.MainWindow
    if getattr(cls, "_applied_share_finalizer_installed", False):
        return
    cls._applied_share_finalizer_installed = True

    _wrap_widget_method(cls, "show")
    _wrap_widget_method(cls, "refresh")
    _wrap_view_method(base_module.NetworkView, "set_graph")
    _wrap_view_method(base_module.NetworkView, "set_model")

    random_flow_module = sys.modules.get("random_flow_ui")
    heatmap_view = getattr(random_flow_module, "FlowHeatmapView", None) if random_flow_module else None
    if heatmap_view is not None:
        _wrap_view_method(heatmap_view, "set_heatmap")

    enhancer = sys.modules.get("graph_ui_enhancer")
    if enhancer is not None:
        controller = getattr(enhancer, "GraphSelectionController", None)
        original_reverse = getattr(controller, "reverse_selected", None) if controller else None
        if callable(original_reverse) and not getattr(original_reverse, "_applied_finalizer_wrapped", False):
            def reverse_selected(self: Any, *args: Any, **kwargs: Any) -> Any:
                result = original_reverse(self, *args, **kwargs)
                owner = getattr(self, "owner", None)
                if isinstance(owner, QWidget):
                    _translate_remaining(owner)
                return result

            reverse_selected._applied_finalizer_wrapped = True  # type: ignore[attr-defined]
            controller.reverse_selected = reverse_selected

        original_popup = getattr(enhancer, "_open_graph_popup", None)
        if callable(original_popup) and not getattr(original_popup, "_applied_finalizer_wrapped", False):
            def open_graph_popup(window: Any, app_module: Any) -> Any:
                result = original_popup(window, app_module)
                dialog = getattr(window, "_graph_popup", None)
                if isinstance(dialog, QWidget):
                    _translate_remaining(dialog)
                return result

            open_graph_popup._applied_finalizer_wrapped = True  # type: ignore[attr-defined]
            enhancer._open_graph_popup = open_graph_popup
