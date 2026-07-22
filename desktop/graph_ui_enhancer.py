"""Graph generation UI enhancements for Sim_Core desktop workbench.

Adds a larger CAD graph workspace, graph-only popup, rubber-band block selection,
and direction reversal for selected directed edges without changing the canonical
DXF conversion algorithm.
"""
from __future__ import annotations

import re
from typing import Any

from PySide6.QtCore import QEvent, QObject, QPoint, QRect, Qt
from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QRubberBand,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

_EDGE_RE = re.compile(r"^Edge\s+(\d+)")


def _button(text: str) -> QPushButton:
    widget = QPushButton(text)
    widget.setCursor(Qt.PointingHandCursor)
    widget.setMinimumHeight(36)
    return widget


def _edge_id_from_item(item: Any) -> int | None:
    tooltip = item.toolTip() if hasattr(item, "toolTip") else ""
    match = _EDGE_RE.match(str(tooltip))
    return int(match.group(1)) if match else None


class GraphSelectionController(QObject):
    """Adds click and rubber-band selection to an existing NetworkView."""

    def __init__(self, owner: Any, view: Any, *, popup: bool = False) -> None:
        super().__init__(view)
        self.owner = owner
        self.view = view
        self.popup = popup
        self.selected_edges: set[int] = set()
        self.origin = QPoint()
        self.rubber_band = QRubberBand(QRubberBand.Rectangle, view.viewport())
        self.dragging = False
        view.viewport().installEventFilter(self)
        view.setCursor(Qt.CrossCursor)

    def eventFilter(self, watched: Any, event: Any) -> bool:  # noqa: N802
        if watched is not self.view.viewport():
            return super().eventFilter(watched, event)
        if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
            self.origin = event.position().toPoint()
            self.dragging = True
            self.rubber_band.setGeometry(QRect(self.origin, self.origin))
            self.rubber_band.show()
            return True
        if event.type() == QEvent.Type.MouseMove and self.dragging:
            current = event.position().toPoint()
            self.rubber_band.setGeometry(QRect(self.origin, current).normalized())
            return True
        if (
            event.type() == QEvent.Type.MouseButtonRelease
            and event.button() == Qt.MouseButton.LeftButton
            and self.dragging
        ):
            self.dragging = False
            rect = self.rubber_band.geometry().normalized()
            self.rubber_band.hide()
            if rect.width() < 5 and rect.height() < 5:
                self._select_single(event.position().toPoint())
            else:
                self._select_rect(rect)
            return True
        return super().eventFilter(watched, event)

    def _select_single(self, pos: QPoint) -> None:
        item = self.view.itemAt(pos)
        edge_id = _edge_id_from_item(item) if item else None
        self.selected_edges = {edge_id} if edge_id is not None else set()
        self.highlight()

    def _select_rect(self, viewport_rect: QRect) -> None:
        scene_rect = self.view.mapToScene(viewport_rect).boundingRect()
        selected: set[int] = set()
        for item in self.view.scene().items(scene_rect):
            edge_id = _edge_id_from_item(item)
            if edge_id is not None:
                selected.add(edge_id)
        self.selected_edges = selected
        self.highlight()

    def highlight(self) -> None:
        for item in self.view.scene().items():
            edge_id = _edge_id_from_item(item)
            if edge_id is None or not hasattr(item, "pen") or not hasattr(item, "setPen"):
                continue
            pen = item.pen()
            if edge_id in self.selected_edges:
                item.setPen(
                    QPen(
                        QColor("#ffd54f"),
                        max(4.5, pen.widthF() + 1.5),
                        pen.style(),
                        pen.capStyle(),
                        pen.joinStyle(),
                    )
                )

    def reverse_selected(self) -> None:
        graph = getattr(self.owner, "cad_graph", None)
        if not graph or not self.selected_edges:
            QMessageBox.information(
                self.view,
                "방향 반전",
                "먼저 Edge를 클릭하거나 마우스로 영역을 드래그해 선택해 주세요.",
            )
            return
        changed = 0
        edges = graph.get("edges", [])
        for edge_id in sorted(self.selected_edges):
            if edge_id < 0 or edge_id >= len(edges):
                continue
            direction = edges[edge_id].get("dir")
            if isinstance(direction, list) and len(direction) == 2:
                edges[edge_id]["dir"] = [direction[1], direction[0]]
                changed += 1
        if not changed:
            QMessageBox.information(
                self.view,
                "방향 반전",
                "선택 영역에 반전 가능한 방향성 Edge가 없습니다.",
            )
            return
        self.refresh_views()
        status = getattr(self.owner, "cad_graph_status", None)
        if status is not None:
            status.setText(
                f"선택한 Edge {changed}개의 방향을 반전했습니다. "
                "Graph JSON 저장 시 변경 내용이 반영됩니다."
            )

    def refresh_views(self) -> None:
        graph = getattr(self.owner, "cad_graph", None)
        main_view = getattr(self.owner, "cad_graph_view", None)
        if main_view is not None:
            main_view.set_graph(graph)
        popup_view = getattr(self.owner, "_graph_popup_view", None)
        if popup_view is not None:
            popup_view.set_graph(graph)
        self.highlight()
        popup_controller = getattr(self.owner, "_graph_popup_controller", None)
        if popup_controller is not None and popup_controller is not self:
            popup_controller.selected_edges = set(self.selected_edges)
            popup_controller.highlight()


def _remove_wasted_file_card_space(window: Any) -> None:
    for card in getattr(window, "file_cards", {}).values():
        for label in card.findChildren(QLabel):
            if label.objectName() in {"FileIcon", "AvailableBadge", "PrototypeBadge"}:
                label.hide()
        layout = card.layout()
        if layout is None:
            continue
        layout.setContentsMargins(16, 10, 16, 10)
        layout.setSpacing(5)
        for index in reversed(range(layout.count())):
            item = layout.itemAt(index)
            if item.spacerItem() is not None:
                layout.removeItem(item)
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)


def _add_graph_toolbar(window: Any, module: Any) -> None:
    view = getattr(window, "cad_graph_view", None)
    if view is None:
        return
    view.setMinimumHeight(470)
    controller = GraphSelectionController(window, view)
    window._graph_selection_controller = controller

    parent = view.parentWidget()
    if parent is None or parent.layout() is None:
        return
    toolbar_widget = QWidget(parent)
    toolbar = QHBoxLayout(toolbar_widget)
    toolbar.setContentsMargins(0, 0, 0, 4)
    help_label = QLabel("Edge 클릭 또는 빈 영역에서 드래그: 블록 선택")
    help_label.setObjectName("Muted")
    popup_button = _button("▣  그래프만 크게 보기")
    reverse_button = _button("⇄  선택 방향 반전")
    popup_button.clicked.connect(lambda: _open_graph_popup(window, module))
    reverse_button.clicked.connect(controller.reverse_selected)
    toolbar.addWidget(help_label)
    toolbar.addStretch(1)
    toolbar.addWidget(reverse_button)
    toolbar.addWidget(popup_button)
    parent.layout().insertWidget(1, toolbar_widget)


def _open_graph_popup(window: Any, module: Any) -> None:
    dialog = getattr(window, "_graph_popup", None)
    if dialog is not None:
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()
        return

    dialog = QDialog(window)
    dialog.setWindowTitle("Sim_Core · CAD Graph 전체 화면")
    dialog.resize(1450, 900)
    layout = QVBoxLayout(dialog)
    layout.setContentsMargins(12, 12, 12, 12)
    layout.setSpacing(8)

    top = QHBoxLayout()
    guide = QLabel(
        "마우스 드래그로 Edge 블록 선택 · 클릭으로 단일 Edge 선택 · 선택 후 방향 반전"
    )
    guide.setObjectName("Muted")
    reverse = _button("⇄  선택 방향 반전")
    close = _button("닫기")
    top.addWidget(guide)
    top.addStretch(1)
    top.addWidget(reverse)
    top.addWidget(close)
    layout.addLayout(top)

    popup_view = module.NetworkView()
    popup_view.set_graph(getattr(window, "cad_graph", None))
    popup_view.setMinimumSize(900, 600)
    layout.addWidget(popup_view, 1)

    controller = GraphSelectionController(window, popup_view, popup=True)
    window._graph_popup = dialog
    window._graph_popup_view = popup_view
    window._graph_popup_controller = controller
    reverse.clicked.connect(controller.reverse_selected)
    close.clicked.connect(dialog.close)
    dialog.finished.connect(lambda _result: _clear_popup(window))
    dialog.show()


def _clear_popup(window: Any) -> None:
    window._graph_popup = None
    window._graph_popup_view = None
    window._graph_popup_controller = None


def _enhance_window(window: Any, module: Any) -> None:
    if getattr(window, "_graph_ui_enhanced", False):
        return
    window._graph_ui_enhanced = True
    _remove_wasted_file_card_space(window)
    _add_graph_toolbar(window, module)


def install_enhancements(module: Any) -> None:
    """Patch MainWindow.show so enhancements are applied after legacy UI creation."""
    original_show = module.MainWindow.show

    def enhanced_show(window: Any) -> None:
        _enhance_window(window, module)
        original_show(window)

    module.MainWindow.show = enhanced_show
