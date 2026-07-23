"""Qt worker and popup for random From-To LA-style static flow analysis."""

from __future__ import annotations

import copy
import math
from pathlib import Path
from typing import Any, Mapping

from PySide6.QtCore import QThread, Qt, QUrl, Signal
from PySide6.QtGui import (
    QColor,
    QDesktopServices,
    QFont,
    QPainter,
    QPainterPath,
    QPen,
)
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsPathItem,
    QGraphicsScene,
    QGraphicsSimpleTextItem,
    QGraphicsView,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from random_flow_analysis import (
    GeneratedRandomWorkload,
    SavedRandomWorkload,
    generate_random_workload,
    save_random_workload,
)


def _uses_dxf_screen_coordinates(facility: Mapping[str, Any]) -> bool:
    return any(
        isinstance(artifact, Mapping)
        and str(artifact.get("kind", "")).casefold() == "dxf"
        for artifact in facility.get("source_artifacts", [])
    )


class RandomWorkloadWorker(QThread):
    """Generate and save a workload without blocking the Qt UI thread."""

    completed = Signal(object)
    failed = Signal(str)

    def __init__(
        self,
        facility: Mapping[str, Any],
        moves_per_hour: int,
        seed: int,
        output_root: str | Path,
        model_name: str,
        parent: Any = None,
    ) -> None:
        super().__init__(parent)
        self._facility = copy.deepcopy(dict(facility))
        self._moves_per_hour = moves_per_hour
        self._seed = seed
        self._output_root = Path(output_root)
        self._model_name = model_name

    def run(self) -> None:
        try:
            workload = generate_random_workload(
                self._facility,
                self._moves_per_hour,
                self._seed,
            )
            saved = save_random_workload(
                workload,
                self._facility,
                self._output_root,
                model_name=self._model_name,
            )
        except Exception as error:  # Qt worker must return errors to the UI thread.
            self.failed.emit(str(error))
            return
        self.completed.emit((workload, saved))


def heatmap_color(relative_load: float) -> QColor:
    """Map 0..1 traffic from green through yellow to red."""

    share = max(0.0, min(1.0, float(relative_load)))
    hue = (120.0 * (1.0 - share)) / 360.0
    return QColor.fromHsvF(hue, 0.82, 0.92)


class FlowHeatmapView(QGraphicsView):
    """Canonical facility renderer dedicated to static route heatmaps."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._fit_bounds = None
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.setBackgroundBrush(QColor("#071019"))

    def wheelEvent(self, event: Any) -> None:  # noqa: N802
        factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(factor, factor)

    def resizeEvent(self, event: Any) -> None:  # noqa: N802
        super().resizeEvent(event)
        if self._fit_bounds is not None and not self._fit_bounds.isEmpty():
            self.fitInView(self._fit_bounds, Qt.AspectRatioMode.KeepAspectRatio)

    def set_heatmap(
        self,
        facility: Mapping[str, Any],
        analysis: Mapping[str, Any],
    ) -> None:
        scene = self.scene()
        scene.clear()
        nodes = facility.get("nodes", [])
        positions = {
            str(item.get("id")): item.get("position_um")
            for item in nodes
            if isinstance(item, Mapping)
            and item.get("id")
            and isinstance(item.get("position_um"), Mapping)
        }
        if not positions:
            label = scene.addText("표시할 Node 좌표가 없습니다.")
            label.setDefaultTextColor(QColor("#ffb86b"))
            return

        xs = [float(raw.get("x", 0.0)) for raw in positions.values()]
        ys = [float(raw.get("y", 0.0)) for raw in positions.values()]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        scale = 1150.0 / max(max_x - min_x, max_y - min_y, 1.0)
        y_direction = 1.0 if _uses_dxf_screen_coordinates(facility) else -1.0

        def point(raw: Mapping[str, Any]) -> tuple[float, float]:
            return (
                (float(raw.get("x", 0.0)) - min_x) * scale,
                y_direction * (float(raw.get("y", 0.0)) - min_y) * scale,
            )

        flows = {
            str(item.get("edge_id")): item
            for item in analysis.get("edge_flows", [])
            if isinstance(item, Mapping) and item.get("edge_id")
        }
        summary = analysis.get("flow_summary", {})
        max_moves = float(summary.get("max_edge_moves_per_hour", 0.0) or 0.0)
        if max_moves <= 0:
            max_moves = max(
                (
                    float(item.get("expected_moves_per_hour", 0.0) or 0.0)
                    for item in flows.values()
                ),
                default=0.0,
            )

        for edge in facility.get("edges", []):
            if not isinstance(edge, Mapping):
                continue
            edge_id = str(edge.get("id", ""))
            polyline = edge.get("polyline_um")
            if not isinstance(polyline, list) or len(polyline) < 2:
                start = positions.get(str(edge.get("from_node_id", "")))
                end = positions.get(str(edge.get("to_node_id", "")))
                if start is None or end is None:
                    continue
                polyline = [start, end]
            try:
                path = QPainterPath()
                path.moveTo(*point(polyline[0]))
                for raw in polyline[1:]:
                    path.lineTo(*point(raw))
            except (AttributeError, TypeError, ValueError):
                continue
            observation = flows.get(edge_id, {})
            moves = float(observation.get("expected_moves_per_hour", 0.0) or 0.0)
            relative = moves / max_moves if max_moves > 0 else 0.0
            rail = QGraphicsPathItem(path)
            rail.setPen(
                QPen(
                    heatmap_color(relative),
                    2.4 + 5.0 * math.sqrt(relative),
                    Qt.PenStyle.SolidLine,
                    Qt.PenCapStyle.RoundCap,
                    Qt.PenJoinStyle.RoundJoin,
                )
            )
            rail.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
            rail.setData(0, "random-flow-edge")
            rail.setData(1, edge_id)
            rail.setData(2, moves)
            rail.setData(3, relative)
            rail.setZValue(1)
            rail.setToolTip(
                f"{edge_id}\n"
                f"{edge.get('from_node_id', '')} → {edge.get('to_node_id', '')}\n"
                f"통행량 {moves:.1f} moves/h · 최대 Edge 대비 {relative * 100:.1f}%"
            )
            scene.addItem(rail)

        node_radius = 1.8 if len(positions) < 2_000 else 1.0
        for node_id, raw in positions.items():
            x, y = point(raw)
            dot = QGraphicsEllipseItem(
                x - node_radius,
                y - node_radius,
                node_radius * 2,
                node_radius * 2,
            )
            dot.setBrush(QColor("#0c1d29"))
            dot.setPen(QPen(QColor("#416273"), 0.8))
            dot.setZValue(2)
            dot.setToolTip(node_id)
            scene.addItem(dot)

        stations = [
            item for item in facility.get("stations", []) if isinstance(item, Mapping)
        ]
        show_station_names = len(stations) <= 200
        for station in stations:
            raw = station.get("position_um")
            if not isinstance(raw, Mapping):
                raw = positions.get(str(station.get("attachment_node_id", "")))
            if not isinstance(raw, Mapping):
                continue
            x, y = point(raw)
            marker = QGraphicsEllipseItem(x - 5.5, y - 5.5, 11.0, 11.0)
            marker.setBrush(QColor("#071019"))
            marker.setPen(QPen(QColor("#66f2df"), 2.0))
            marker.setData(0, "random-flow-station")
            marker.setData(1, str(station.get("id", "")))
            marker.setZValue(4)
            marker.setToolTip(
                f"Station {station.get('id', '')}\n{station.get('operation_type', '')}"
            )
            scene.addItem(marker)
            if show_station_names:
                text = QGraphicsSimpleTextItem(str(station.get("id", "")))
                text.setBrush(QColor("#c2d5dc"))
                text.setFont(QFont("Segoe UI", 7, QFont.Weight.DemiBold))
                text.setPos(x + 7, y - 16)
                text.setZValue(5)
                scene.addItem(text)

        bounds = scene.itemsBoundingRect().adjusted(-35, -35, 35, 35)
        scene.setSceneRect(bounds)
        self._fit_bounds = bounds
        self.resetTransform()
        self.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)


def _metric(title: str, value: str) -> QFrame:
    frame = QFrame()
    frame.setObjectName("MetricCard")
    layout = QVBoxLayout(frame)
    layout.setContentsMargins(14, 10, 14, 10)
    layout.setSpacing(2)
    heading = QLabel(title)
    heading.setObjectName("MetricLabel")
    content = QLabel(value)
    content.setObjectName("MetricValue")
    content.setStyleSheet("font-size: 19px; font-weight: 700;")
    content.setToolTip(value)
    layout.addWidget(heading)
    layout.addWidget(content)
    return frame


def _button(text: str, *, primary: bool = False) -> QPushButton:
    widget = QPushButton(text)
    widget.setCursor(Qt.CursorShape.PointingHandCursor)
    widget.setMinimumHeight(36)
    if primary:
        widget.setProperty("kind", "primary")
    return widget


def show_random_flow_dialog(
    parent: QWidget,
    facility: Mapping[str, Any],
    workload: GeneratedRandomWorkload,
    saved: SavedRandomWorkload,
) -> QDialog:
    """Show the requested green-to-red static analysis popup."""

    dialog = QDialog(parent)
    dialog.setObjectName("RandomFlowDialog")
    dialog.setWindowTitle("Sim_Core · Random From-To LA 정적분석")
    dialog.resize(1480, 900)
    dialog.setStyleSheet("QDialog#RandomFlowDialog { background: #071019; }")
    dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
    layout = QVBoxLayout(dialog)
    layout.setContentsMargins(16, 14, 16, 14)
    layout.setSpacing(10)

    header = QHBoxLayout()
    texts = QVBoxLayout()
    title = QLabel("Random From-To · Edge 통행량 Heatmap")
    title.setObjectName("SectionTitle")
    description = QLabel(
        "입력한 시간당 반송을 방향성 최단경로에 누적했습니다. "
        "초록색은 저사용, 빨간색은 고사용 Edge입니다."
    )
    description.setObjectName("Muted")
    texts.addWidget(title)
    texts.addWidget(description)
    header.addLayout(texts)
    header.addStretch(1)
    open_folder = _button("생성 파일 폴더 열기")
    close = _button("닫기", primary=True)
    open_folder.clicked.connect(
        lambda: QDesktopServices.openUrl(QUrl.fromLocalFile(str(saved.directory)))
    )
    close.clicked.connect(dialog.close)
    header.addWidget(open_folder)
    header.addWidget(close)
    layout.addLayout(header)

    summary = workload.analysis.get("flow_summary", {})
    generation = workload.analysis.get("generation", {})
    metrics = QHBoxLayout()
    values = (
        ("총 반송량", f"{workload.moves_per_hour:,} moves/h"),
        ("생성 OD", f"{len(workload.demands):,} pairs"),
        ("도달 가능 OD", f"{workload.reachable_pair_count:,} pairs"),
        (
            "사용 Edge",
            f"{int(summary.get('used_edge_count', 0)):,} / {int(summary.get('total_edge_count', 0)):,}",
        ),
        (
            "최대 Edge",
            f"{float(summary.get('max_edge_moves_per_hour', 0.0)):.1f} moves/h",
        ),
        ("생성 Vehicle", f"{int(generation.get('generated_vehicle_count', 0)):,} 대"),
    )
    for title_text, value in values:
        metrics.addWidget(_metric(title_text, value))
    layout.addLayout(metrics)

    legend = QHBoxLayout()
    low = QLabel("저사용 · 0")
    low.setObjectName("Muted")
    gradient = QFrame()
    gradient.setFixedHeight(14)
    gradient.setMinimumWidth(420)
    gradient.setStyleSheet(
        "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, "
        "stop:0 #2ee66b, stop:0.5 #f0e83b, stop:1 #eb2f2f); "
        "border: 1px solid #294452; border-radius: 6px;"
    )
    high = QLabel("최대 사용 · 100%")
    high.setObjectName("Muted")
    legend.addStretch(1)
    legend.addWidget(low)
    legend.addWidget(gradient)
    legend.addWidget(high)
    legend.addStretch(1)
    layout.addLayout(legend)

    view = FlowHeatmapView(dialog)
    view.setObjectName("RandomFlowHeatmap")
    view.set_heatmap(facility, workload.analysis)
    layout.addWidget(view, 1)

    footer = QLabel(
        f"Seed {workload.seed} · Facility {saved.facility_json_path.name} · "
        f"CSV {saved.demand_csv_path.name} · "
        f"Scenario {saved.scenario_json_path.name} · 분석 {saved.analysis_json_path.name}"
    )
    footer.setObjectName("TinyMuted")
    footer.setToolTip(str(saved.directory))
    layout.addWidget(footer)
    dialog.show()
    return dialog
