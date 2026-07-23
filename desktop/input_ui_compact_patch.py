"""Compact the input-page analysis and CAD settings panels.

The patch is intentionally layered after the existing Rail, Layout analysis,
AutoMod and graph UI patches so it only changes presentation.  Core conversion,
analysis and file-selection behavior remain untouched.
"""
from __future__ import annotations

from typing import Any

from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
)


def _find_label(parent: Any, text: str) -> QLabel | None:
    for label in parent.findChildren(QLabel):
        if label.text() == text:
            return label
    return None


def _find_button(parent: Any, text: str) -> QPushButton | None:
    for button in parent.findChildren(QPushButton):
        if button.text() == text:
            return button
    return None


def _hide_description(parent: Any, prefix: str) -> None:
    for label in parent.findChildren(QLabel):
        if label.objectName() == "Muted" and label.text().startswith(prefix):
            label.hide()


def _set_expanding_button(button: QPushButton) -> None:
    button.setMinimumWidth(0)
    button.setMaximumWidth(16_777_215)
    button.setMinimumHeight(40)
    button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


def install_input_ui_compact(base_module: Any) -> None:
    """Place Layout analysis and CAD conversion panels side by side."""

    cls = base_module.MainWindow
    if getattr(cls, "_input_ui_compact_installed", False):
        return
    cls._input_ui_compact_installed = True

    original_build_inputs = cls.build_inputs

    def build_inputs(self: Any) -> Any:
        scroll = original_build_inputs(self)
        if not isinstance(scroll, QScrollArea):
            return scroll

        page = scroll.widget()
        page_layout = page.layout() if page is not None else None
        if not isinstance(page_layout, QVBoxLayout):
            return scroll

        # Remove the redundant page-level heading requested by the UI review:
        # "실제 데이터 연결" / "HTTP 전송 없이 ...".
        for index in range(page_layout.count() - 1, -1, -1):
            item = page_layout.itemAt(index)
            widget = item.widget() if item is not None else None
            if widget is None:
                continue
            texts = {label.text() for label in widget.findChildren(QLabel)}
            if "실제 데이터 연결" in texts or any(
                text.startswith("HTTP 전송 없이 선택한") for text in texts
            ):
                page_layout.removeWidget(widget)
                widget.deleteLater()
                break

        random_panel = self.random_flow_generate_button.parentWidget()
        cad_panel = self.cad_save_button.parentWidget()
        if random_panel is None or cad_panel is None:
            return scroll

        random_index = page_layout.indexOf(random_panel)
        page_layout.removeWidget(random_panel)
        page_layout.removeWidget(cad_panel)

        compact_row = QHBoxLayout()
        compact_row.setContentsMargins(0, 0, 0, 0)
        compact_row.setSpacing(12)
        compact_row.addWidget(random_panel, 1)
        compact_row.addWidget(cad_panel, 1)
        page_layout.insertLayout(max(0, random_index), compact_row)

        random_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        cad_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        random_form = random_panel.layout()
        if isinstance(random_form, QGridLayout):
            random_form.setContentsMargins(16, 13, 16, 13)
            random_form.setHorizontalSpacing(8)
            random_form.setVerticalSpacing(6)
            _hide_description(random_panel, "랜덤 FromTo 또는 연결한 실제 FromTo CSV를 선택해")

            mode_label = _find_label(random_panel, "FromTo 분석 방식")
            if mode_label is not None:
                random_form.removeWidget(mode_label)
            random_form.removeWidget(self.random_fromto_mode_button)
            random_form.removeWidget(self.actual_fromto_mode_button)

            mode_row = QHBoxLayout()
            mode_row.setContentsMargins(0, 0, 0, 0)
            mode_row.setSpacing(8)
            if mode_label is not None:
                mode_row.addWidget(mode_label)
            _set_expanding_button(self.random_fromto_mode_button)
            _set_expanding_button(self.actual_fromto_mode_button)
            mode_row.addWidget(self.random_fromto_mode_button, 1)
            mode_row.addWidget(self.actual_fromto_mode_button, 1)
            random_form.addLayout(mode_row, 3, 0, 1, 4)

            random_form.removeWidget(self.random_flow_status)
            random_form.removeWidget(self.random_flow_generate_button)
            self.random_flow_status.setMaximumHeight(44)
            _set_expanding_button(self.random_flow_generate_button)
            random_form.addWidget(self.random_flow_status, 4, 0, 1, 3)
            random_form.addWidget(self.random_flow_generate_button, 4, 3)
            random_form.setColumnStretch(0, 1)
            random_form.setColumnStretch(1, 1)
            random_form.setColumnStretch(2, 1)
            random_form.setColumnStretch(3, 1)

        cad_form = cad_panel.layout()
        if isinstance(cad_form, QGridLayout):
            cad_form.setContentsMargins(16, 13, 16, 13)
            cad_form.setHorizontalSpacing(8)
            cad_form.setVerticalSpacing(6)
            _hide_description(cad_panel, "Graph_Maker 참조 로직으로")

            convert_button = _find_button(cad_panel, "↻  DXF 다시 변환")
            action_buttons = [
                button
                for button in (
                    convert_button,
                    self.cad_save_button,
                    getattr(self, "cad_automod_button", None),
                )
                if button is not None
            ]
            if action_buttons:
                action_row = QHBoxLayout()
                action_row.setContentsMargins(0, 0, 0, 0)
                action_row.setSpacing(8)
                for action_button in action_buttons:
                    cad_form.removeWidget(action_button)
                    _set_expanding_button(action_button)
                    action_row.addWidget(action_button, 1)
                cad_form.addLayout(action_row, 3, 0, 1, 4)

            cad_form.setColumnStretch(0, 1)
            cad_form.setColumnStretch(1, 2)
            cad_form.setColumnStretch(2, 1)
            cad_form.setColumnStretch(3, 1)

        return scroll

    cls.build_inputs = build_inputs
