"""Qt worker and popup for random From-To LA-style flow analysis and animation."""

from __future__ import annotations

import copy
import math
from pathlib import Path
from typing import Any, Mapping

from PySide6.QtCore import QThread, QTimer, Qt, QUrl, Signal
from PySide6.QtGui import (
    QColor,
    QDesktopServices,
    QFont,
    QPainter,
    QPainterPath,
    QPen,
)
from PySide6.QtWidgets import (
    QComboBox,
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
from random_flow_animation import locate_route_pose, route_total_time_us


MAX_ANIMATED_VEHICLES = 300
DEFAULT_ANIMATION_SPEED = 300.0
ANIMATION_INTERVAL_MS = 40


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
    """Facility heatmap plus path-bound vehicle preview animation.

    Vehicle rendering follows an AutoMod-style path-bound rule: the logical state
    is the current directed Edge and progress on that Edge. X/Y/heading are derived
    from the Edge centerline polyline every frame, never integrated independently.
    """

    animation_status_changed = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._fit_bounds = None
        self._edge_geometries: dict[str, dict[str, object]] = {}
        self._vehicle_states: list[dict[str, object]] = []
        self._simulation_time_us = 0
        self._animation_duration_us = 0
        self._speed_factor = DEFAULT_ANIMATION_SPEED
        self._total_source_vehicle_count = 0
        self._animation_timer = QTimer(self)
        self._animation_timer.setInterval(ANIMATION_INTERVAL_MS)
        self._animation_timer.timeout.connect(self._advance_animation)
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
        self.pause_animation()
        self._vehicle_states.clear()
        self._edge_geometries.clear()
        self._simulation_time_us = 0
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

        def point(raw: Mapping[str, Any]) -> tuple[float, float]:
            return (
                (float(raw.get("x", 0.0)) - min_x) * scale,
                -(float(raw.get("y", 0.0)) - min_y) * scale,
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
                scene_points = [point(raw) for raw in polyline]
                path = QPainterPath()
                path.moveTo(*scene_points[0])
                for scene_point in scene_points[1:]:
                    path.lineTo(*scene_point)
            except (AttributeError, TypeError, ValueError):
                continue

            try:
                length_um = int(edge.get("length_um", 0))
                speed_limit = int(edge.get("speed_limit_um_per_s", 0))
            except (TypeError, ValueError):
                continue
            if length_um > 0 and speed_limit > 0:
                self._edge_geometries[edge_id] = {
                    "points": scene_points,
                    "length_um": length_um,
                    "speed_limit_um_per_s": speed_limit,
                }

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

    def configure_vehicle_animation(
        self,
        workload: GeneratedRandomWorkload,
        *,
        max_vehicles: int = MAX_ANIMATED_VEHICLES,
    ) -> None:
        """Create a bounded preview fleet from generated jobs and OD routes."""

        self.pause_animation()
        self._remove_vehicle_items()
        self._simulation_time_us = 0

        route_lookup = {
            (
                str(item.get("from_station_id", "")),
                str(item.get("to_station_id", "")),
            ): tuple(str(edge_id) for edge_id in item.get("edge_ids", []))
            for item in workload.analysis.get("demand_routes", [])
            if isinstance(item, Mapping)
        }
        jobs = [
            item
            for item in workload.scenario.get("jobs", [])
            if isinstance(item, Mapping)
        ]
        self._total_source_vehicle_count = len(jobs)
        if not jobs or not route_lookup or not self._edge_geometries:
            self._emit_animation_status(0, 0, 0)
            return

        limit = max(1, min(int(max_vehicles), len(jobs)))
        if limit == len(jobs):
            selected_jobs = jobs
        elif limit == 1:
            selected_jobs = [jobs[0]]
        else:
            indices = [
                round(index * (len(jobs) - 1) / (limit - 1))
                for index in range(limit)
            ]
            selected_jobs = [jobs[index] for index in indices]

        vehicle_shape = QPainterPath()
        vehicle_shape.moveTo(6.5, 0.0)
        vehicle_shape.lineTo(-4.5, -3.6)
        vehicle_shape.lineTo(-2.5, 0.0)
        vehicle_shape.lineTo(-4.5, 3.6)
        vehicle_shape.closeSubpath()

        duration = 0
        for job in selected_jobs:
            pair = (
                str(job.get("pickup_station_id", "")),
                str(job.get("dropoff_station_id", "")),
            )
            edge_ids = route_lookup.get(pair)
            if not edge_ids or any(edge_id not in self._edge_geometries for edge_id in edge_ids):
                continue
            try:
                route_time = route_total_time_us(edge_ids, self._edge_geometries)
                release_time = int(job.get("release_time_us", 0) or 0)
            except (KeyError, TypeError, ValueError):
                continue

            item = QGraphicsPathItem(vehicle_shape)
            item.setBrush(QColor("#f4fbff"))
            item.setPen(QPen(QColor("#102a38"), 1.0))
            item.setFlag(
                QGraphicsItem.GraphicsItemFlag.ItemIgnoresTransformations,
                True,
            )
            item.setZValue(12)
            item.setToolTip(
                f"{job.get('id', '')}\n"
                f"{pair[0]} → {pair[1]}\n"
                "Vehicle 위치는 Edge 중앙선에서 계산됩니다."
            )
            item.hide()
            self.scene().addItem(item)
            self._vehicle_states.append(
                {
                    "item": item,
                    "edge_ids": edge_ids,
                    "release_time_us": release_time,
                    "route_time_us": route_time,
                }
            )
            duration = max(duration, release_time + route_time)

        self._animation_duration_us = max(
            duration,
            int(workload.scenario.get("duration_us", 0) or 0),
        )
        self._update_vehicle_items()

    def _remove_vehicle_items(self) -> None:
        scene = self.scene()
        for state in self._vehicle_states:
            item = state.get("item")
            if isinstance(item, QGraphicsPathItem) and item.scene() is scene:
                scene.removeItem(item)
        self._vehicle_states.clear()

    def set_animation_speed(self, speed_factor: float) -> None:
        self._speed_factor = max(1.0, float(speed_factor))
        self._update_vehicle_items()

    def animation_running(self) -> bool:
        return self._animation_timer.isActive()

    def start_animation(self) -> None:
        if not self._vehicle_states:
            return
        if self._animation_duration_us > 0 and self._simulation_time_us >= self._animation_duration_us:
            self._simulation_time_us = 0
        self._animation_timer.start()
        self._update_vehicle_items()

    def pause_animation(self) -> None:
        self._animation_timer.stop()

    def reset_animation(self) -> None:
        self.pause_animation()
        self._simulation_time_us = 0
        self._update_vehicle_items()

    def _advance_animation(self) -> None:
        delta_us = int(
            self._animation_timer.interval()
            * 1_000
            * self._speed_factor
        )
        self._simulation_time_us += max(1, delta_us)
        if (
            self._animation_duration_us > 0
            and self._simulation_time_us >= self._animation_duration_us
        ):
            self._simulation_time_us = self._animation_duration_us
            self.pause_animation()
        self._update_vehicle_items()

    def _update_vehicle_items(self) -> None:
        active = 0
        completed = 0
        released = 0
        for state in self._vehicle_states:
            item = state.get("item")
            if not isinstance(item, QGraphicsPathItem):
                continue
            release_time = int(state.get("release_time_us", 0) or 0)
            if self._simulation_time_us < release_time:
                item.hide()
                continue
            released += 1
            elapsed = self._simulation_time_us - release_time
            try:
                pose = locate_route_pose(
                    state.get("edge_ids", ()),  # type: ignore[arg-type]
                    self._edge_geometries,
                    elapsed,
                )
            except (KeyError, TypeError, ValueError):
                item.hide()
                continue
            if pose.completed:
                completed += 1
                item.hide()
                continue
            active += 1
            item.setPos(pose.x, pose.y)
            item.setRotation(pose.heading_degrees)
            item.show()
        self._emit_animation_status(active, released, completed)

    def _emit_animation_status(self, active: int, released: int, completed: int) -> None:
        seconds = self._simulation_time_us // 1_000_000
        hours, remainder = divmod(seconds, 3_600)
        minutes, second = divmod(remainder, 60)
        preview = len(self._vehicle_states)
        total = self._total_source_vehicle_count
        state = "주행 중" if self.animation_running() else "일시정지"
        if self._animation_duration_us > 0 and self._simulation_time_us >= self._animation_duration_us:
            state = "완료"
        self.animation_status_changed.emit(
            f"{state} · 시뮬레이션 {hours:02d}:{minutes:02d}:{second:02d} · "
            f"화면 {active}대 주행 · {completed}/{released}대 완료 · "
            f"미리보기 {preview}/{total}대 · {self._speed_factor:g}x"
        )


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
    """Show the static heatmap and a path-bound Random From-To vehicle preview."""

    dialog = QDialog(parent)
    dialog.setObjectName("RandomFlowDialog")
    dialog.setWindowTitle("Sim_Core · Random From-To LA 분석 + Vehicle 경로주행")
    dialog.resize(1480, 900)
    dialog.setStyleSheet("QDialog#RandomFlowDialog { background: #071019; }")
    dialog.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
    layout = QVBoxLayout(dialog)
    layout.setContentsMargins(16, 14, 16, 14)
    layout.setSpacing(10)

    header = QHBoxLayout()
    texts = QVBoxLayout()
    title = QLabel("Random From-To · Edge 통행량 Heatmap + Vehicle 경로주행")
    title.setObjectName("SectionTitle")
    description = QLabel(
        "방향성 Dijkstra 경로의 Edge 통행량을 초록→빨강으로 표시하고, "
        "Vehicle은 현재 Edge와 Edge 진행률만으로 중앙선 위를 주행합니다."
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
    view.configure_vehicle_animation(workload)

    animation_controls = QHBoxLayout()
    play_pause = _button("Vehicle 주행 시작", primary=True)
    reset = _button("처음부터")
    speed = QComboBox()
    for label, factor in (("60x", 60.0), ("300x", 300.0), ("1200x", 1200.0)):
        speed.addItem(label, factor)
    speed.setCurrentIndex(1)
    speed.setMinimumWidth(100)
    status = QLabel("Vehicle 경로주행 준비")
    status.setObjectName("Muted")
    status.setWordWrap(True)

    def toggle_animation() -> None:
        if view.animation_running():
            view.pause_animation()
            play_pause.setText("Vehicle 주행 시작")
            view._update_vehicle_items()
        else:
            view.start_animation()
            play_pause.setText("Vehicle 주행 일시정지")

    def reset_animation() -> None:
        view.reset_animation()
        play_pause.setText("Vehicle 주행 시작")

    def change_speed(_index: int) -> None:
        factor = speed.currentData()
        view.set_animation_speed(float(factor or DEFAULT_ANIMATION_SPEED))

    play_pause.clicked.connect(toggle_animation)
    reset.clicked.connect(reset_animation)
    speed.currentIndexChanged.connect(change_speed)
    view.animation_status_changed.connect(status.setText)
    animation_controls.addWidget(play_pause)
    animation_controls.addWidget(reset)
    animation_controls.addWidget(QLabel("재생 속도"))
    animation_controls.addWidget(speed)
    animation_controls.addSpacing(12)
    animation_controls.addWidget(status, 1)
    layout.addLayout(animation_controls)
    layout.addWidget(view, 1)

    footer = QLabel(
        f"Seed {workload.seed} · CSV {saved.demand_csv_path.name} · "
        f"Scenario {saved.scenario_json_path.name} · 분석 {saved.analysis_json_path.name} · "
        f"화면 성능 보호를 위해 최대 {MAX_ANIMATED_VEHICLES}대만 균등 샘플링하여 애니메이션 표시"
    )
    footer.setObjectName("TinyMuted")
    footer.setToolTip(str(saved.directory))
    layout.addWidget(footer)

    dialog.finished.connect(lambda _result: view.pause_animation())
    dialog.show()
    view.start_animation()
    play_pause.setText("Vehicle 주행 일시정지")
    return dialog
