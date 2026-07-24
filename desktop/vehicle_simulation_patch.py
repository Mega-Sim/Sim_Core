"""Install the centreline 2D vehicle simulation workflow in the desktop UI."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QBrush, QColor, QFont, QPen
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QGraphicsItem,
    QGraphicsRectItem,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QSpinBox,
    QVBoxLayout,
)

from random_flow_analysis import RandomFlowError
from vehicle_simulation_engine import (
    DEFAULT_TRANSFER_DURATION_US,
    VisualVehicleSimulation,
    format_simulation_time,
)


_UNIT_TO_UM = {
    "micrometer": 1.0,
    "millimeter": 1_000.0,
    "meter": 1_000_000.0,
    "inch": 25_400.0,
}


class _SceneCoordinateTransform:
    """Mirror NetworkView's CAD/facility coordinate transform exactly."""

    def __init__(
        self,
        facility: Mapping[str, Any],
        graph: Mapping[str, Any] | None,
    ) -> None:
        self._graph_mode = graph is not None
        if graph is not None:
            nodes = graph.get("nodes", [])
            if not isinstance(nodes, list) or not nodes:
                raise RandomFlowError("2D Simulation에 표시할 CAD Graph Node가 없습니다.")
            xs = [float(item[0]) for item in nodes]
            ys = [float(item[1]) for item in nodes]
            self._min_x = min(xs)
            self._min_y = min(ys)
            self._scale = 1100.0 / max(
                max(xs) - self._min_x,
                max(ys) - self._min_y,
                1.0,
            )
            metadata = graph.get("metadata", {})
            unit = (
                str(metadata.get("coordinate_unit", "millimeter")).casefold()
                if isinstance(metadata, Mapping)
                else "millimeter"
            )
            self._factor = _UNIT_TO_UM.get(unit)
            if self._factor is None:
                raise RandomFlowError(f"지원하지 않는 CAD 좌표 단위입니다: {unit}")
            self._y_direction = 1.0
            return

        positions = [
            item.get("position_um", {})
            for item in facility.get("nodes", [])
            if isinstance(item, Mapping) and item.get("position_um")
        ]
        if not positions:
            raise RandomFlowError("2D Simulation Facility에 Node 좌표가 없습니다.")
        xs = [float(item.get("x", 0.0)) for item in positions]
        ys = [float(item.get("y", 0.0)) for item in positions]
        self._min_x = min(xs)
        self._min_y = min(ys)
        self._scale = 900.0 / max(
            max(xs) - self._min_x,
            max(ys) - self._min_y,
            1.0,
        )
        self._factor = 1.0
        self._y_direction = (
            1.0
            if any(
                isinstance(item, Mapping)
                and str(item.get("kind", "")).casefold() == "dxf"
                for item in facility.get("source_artifacts", [])
            )
            else -1.0
        )

    def point(self, x_um: float, y_um: float) -> tuple[float, float]:
        source_x = float(x_um) / self._factor
        source_y = float(y_um) / self._factor
        return (
            (source_x - self._min_x) * self._scale,
            self._y_direction * (source_y - self._min_y) * self._scale,
        )

    def heading(self, heading_deg: float) -> float:
        return float(heading_deg) * self._y_direction


class VehicleSimulationDialog(QDialog):
    """AutoMod-like lightweight 2D debug animation over the current layout."""

    _STATE_COLORS = {
        "IDLE": QColor("#78909c"),
        "TO_PICKUP": QColor("#29b6f6"),
        "LOADING": QColor("#ffd54f"),
        "TO_SETDOWN": QColor("#66df8b"),
        "UNLOADING": QColor("#ba68c8"),
    }

    def __init__(
        self,
        parent: Any,
        base_module: Any,
        facility: Mapping[str, Any],
        scenario: Mapping[str, Any],
        graph: Mapping[str, Any] | None,
        vehicle_count: int,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle("Sim_Core · 2D Vehicle Simulation")
        self.resize(1480, 900)
        self.setMinimumSize(980, 650)
        self.setModal(False)

        self._base_module = base_module
        self._facility = dict(facility)
        self._scenario = dict(scenario)
        self._graph = dict(graph) if graph is not None else None
        self._vehicle_count = int(vehicle_count)
        self._engine = VisualVehicleSimulation(
            self._facility,
            self._scenario,
            vehicle_count=self._vehicle_count,
            pickup_duration_us=DEFAULT_TRANSFER_DURATION_US,
            setdown_duration_us=DEFAULT_TRANSFER_DURATION_US,
        )
        self._transform = _SceneCoordinateTransform(self._facility, self._graph)
        self._vehicle_items: dict[str, QGraphicsRectItem] = {}
        self._paused = False

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 16)
        layout.setSpacing(10)

        header = QHBoxLayout()
        time_copy = QVBoxLayout()
        time_title = QLabel("SIMULATION TIME")
        time_title.setObjectName("Kicker")
        self.time_label = QLabel("00:00:00.000")
        self.time_label.setFont(QFont("Consolas", 27, QFont.Weight.Bold))
        self.time_label.setMinimumWidth(260)
        self.time_label.setStyleSheet(
            "color:#eafffb; background:#06131c; border:1px solid #24505c; "
            "border-radius:9px; padding:7px 13px;"
        )
        time_copy.addWidget(time_title)
        time_copy.addWidget(self.time_label)
        header.addLayout(time_copy)

        header.addSpacing(18)
        status_copy = QVBoxLayout()
        status_title = QLabel("RUN STATUS")
        status_title.setObjectName("Kicker")
        self.status_label = QLabel()
        self.status_label.setStyleSheet("font-weight:700; color:#9ec4d3;")
        status_copy.addWidget(status_title)
        status_copy.addWidget(self.status_label)
        header.addLayout(status_copy, 1)

        speed_label = QLabel("배속")
        self.speed_combo = QComboBox()
        for value in (1, 5, 10, 20, 50, 100):
            self.speed_combo.addItem(f"{value}×", value)
        self.speed_combo.setCurrentText("10×")
        self.pause_button = base_module.button("일시정지", "secondary")
        self.pause_button.clicked.connect(self._toggle_pause)
        self.reset_button = base_module.button("처음부터", "secondary")
        self.reset_button.clicked.connect(self._reset)
        close_button = base_module.button("닫기", "secondary")
        close_button.clicked.connect(self.close)
        header.addWidget(speed_label)
        header.addWidget(self.speed_combo)
        header.addWidget(self.pause_button)
        header.addWidget(self.reset_button)
        header.addWidget(close_button)
        layout.addLayout(header)

        self.view = base_module.NetworkView()
        self.view.setMinimumHeight(500)
        if self._graph is not None:
            self.view.set_graph(self._graph)
        else:
            self.view.set_model(self._facility)
        layout.addWidget(self.view, 1)

        footer = QHBoxLayout()
        self.metrics_label = QLabel()
        self.metrics_label.setStyleSheet("color:#9cb4c0;")
        legend = QLabel(
            "■ 공차→Pickup   ■ Pickup 10초   ■ 적재→Setdown   "
            "■ Setdown 10초   ■ Edge 대기"
        )
        legend.setStyleSheet("color:#79939f;")
        footer.addWidget(self.metrics_label, 1)
        footer.addWidget(legend)
        layout.addLayout(footer)

        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.TimerType.PreciseTimer)
        self.timer.setInterval(33)
        self.timer.timeout.connect(self._advance)
        self._create_vehicle_items()
        self._render()
        QTimer.singleShot(0, self.timer.start)

    def _create_vehicle_items(self) -> None:
        scene = self.view.scene()
        self._vehicle_items.clear()
        for snapshot in self._engine.vehicle_snapshots():
            item = QGraphicsRectItem(-7.5, -4.2, 15.0, 8.4)
            item.setFlag(
                QGraphicsItem.GraphicsItemFlag.ItemIgnoresTransformations,
                True,
            )
            item.setPen(QPen(QColor("#08131a"), 1.0))
            item.setZValue(100)
            scene.addItem(item)
            self._vehicle_items[str(snapshot["vehicle_id"])] = item

    def _advance(self) -> None:
        if self._paused:
            return
        speed = int(self.speed_combo.currentData() or 1)
        self._engine.tick(self.timer.interval() * 1_000 * speed)
        self._render()
        if self._engine.is_finished:
            self.timer.stop()
            self.pause_button.setEnabled(False)
            self.status_label.setText("COMPLETED · 모든 Job의 Setdown 완료")

    def _render(self) -> None:
        active = 0
        blocked = 0
        for snapshot in self._engine.vehicle_snapshots():
            vehicle_id = str(snapshot["vehicle_id"])
            item = self._vehicle_items[vehicle_id]
            x, y = self._transform.point(
                float(snapshot["x_um"]),
                float(snapshot["y_um"]),
            )
            item.setPos(x, y)
            item.setRotation(self._transform.heading(float(snapshot["heading_deg"])))
            is_blocked = bool(snapshot["blocked"])
            color = QColor("#ef5350") if is_blocked else self._STATE_COLORS.get(
                str(snapshot["state"]), QColor("#90a4ae")
            )
            item.setBrush(QBrush(color))
            item.setPen(QPen(QColor("#ffffff") if is_blocked else QColor("#071019"), 1.0))
            state = str(snapshot["state"])
            if state != "IDLE":
                active += 1
            if is_blocked:
                blocked += 1
            service = int(snapshot["service_remaining_us"])
            service_text = (
                f"\n이적재 남은 시간 {service / 1_000_000:.3f}s" if service > 0 else ""
            )
            item.setToolTip(
                f"{vehicle_id}\nState: {state}\nJob: {snapshot['job_id'] or '—'}"
                f"\nEdge: {snapshot['edge_id'] or '—'}{service_text}"
            )

        self.time_label.setText(format_simulation_time(self._engine.time_us))
        self.metrics_label.setText(
            f"Vehicle {len(self._engine.vehicles)}대 · Active {active} · "
            f"Blocked {blocked} · Job {self._engine.completed_job_count}/"
            f"{len(self._engine.jobs)} 완료 · Released "
            f"{self._engine.released_job_count} · Waiting {self._engine.pending_job_count}"
        )
        if not self._engine.is_finished:
            self.status_label.setText("RUNNING" if not self._paused else "PAUSED")

    def _toggle_pause(self) -> None:
        self._paused = not self._paused
        self.pause_button.setText("계속 실행" if self._paused else "일시정지")
        self._render()

    def _reset(self) -> None:
        self.timer.stop()
        self._engine = VisualVehicleSimulation(
            self._facility,
            self._scenario,
            vehicle_count=self._vehicle_count,
            pickup_duration_us=DEFAULT_TRANSFER_DURATION_US,
            setdown_duration_us=DEFAULT_TRANSFER_DURATION_US,
        )
        for item in self._vehicle_items.values():
            self.view.scene().removeItem(item)
        self._create_vehicle_items()
        self._paused = False
        self.pause_button.setText("일시정지")
        self.pause_button.setEnabled(True)
        self._render()
        self.timer.start()

    def closeEvent(self, event: Any) -> None:  # noqa: N802
        self.timer.stop()
        super().closeEvent(event)


def install_vehicle_simulation(base_module: Any) -> None:
    """Add Random FromTo -> centreline vehicle simulation to MainWindow."""

    cls = base_module.MainWindow
    if getattr(cls, "_vehicle_simulation_installed", False):
        return
    cls._vehicle_simulation_installed = True

    original_build_inputs = cls.build_inputs
    original_refresh = cls.refresh
    original_random_ready = cls._random_flow_ready
    original_clear_outputs = cls._clear_random_flow_outputs

    def build_inputs(self: Any) -> Any:
        page = original_build_inputs(self)
        self._vehicle_simulation_workload = None
        self._vehicle_simulation_dialog = None

        panel = self.random_flow_generate_button.parentWidget()
        form = panel.layout()
        if not isinstance(form, QGridLayout):
            return page

        self.vehicle_simulation_count = QSpinBox()
        self.vehicle_simulation_count.setRange(1, 100)
        self.vehicle_simulation_count.setValue(10)
        self.vehicle_simulation_count.setSuffix(" 대")
        self.vehicle_simulation_button = base_module.button(
            "2D Vehicle Simulation 시작",
            "primary",
        )
        self.vehicle_simulation_button.setEnabled(False)
        self.vehicle_simulation_button.clicked.connect(self.start_vehicle_simulation)
        self.vehicle_simulation_status = QLabel(
            "랜덤 FromTo 생성 후 실행할 수 있습니다. Pickup/Setdown 이적재 시간은 각각 10초입니다."
        )
        self.vehicle_simulation_status.setObjectName("GraphStatus")
        self.vehicle_simulation_status.setWordWrap(True)

        row = form.rowCount()
        form.addWidget(
            base_module.styled_label("애니메이션 Vehicle 수", "FieldLabel"),
            row,
            0,
        )
        form.addWidget(self.vehicle_simulation_count, row + 1, 0)
        form.addWidget(self.vehicle_simulation_status, row, 1, 2, 2)
        form.addWidget(self.vehicle_simulation_button, row, 3, 2, 1)
        return page

    def refresh(self: Any) -> None:
        original_refresh(self)
        if not hasattr(self, "vehicle_simulation_button"):
            return
        ready = bool(
            getattr(self, "_layout_analysis_mode", "random") == "random"
            and getattr(self, "_vehicle_simulation_workload", None) is not None
            and (
                self.cad_facility
                if getattr(self, "_active_layout_kind", "") == "cad"
                else self.facility
            )
        )
        self.vehicle_simulation_button.setEnabled(ready)
        if ready:
            workload = self._vehicle_simulation_workload
            self.vehicle_simulation_status.setText(
                f"실행 준비 완료 · Job {len(workload.scenario.get('jobs', [])):,}건 · "
                "센터라인 주행 · Pickup 10초 · Setdown 10초"
            )

    def random_ready(self: Any, payload: object) -> None:
        workload, _saved = payload  # type: ignore[misc]
        self._vehicle_simulation_workload = workload
        original_random_ready(self, payload)
        self.refresh()

    def clear_outputs(self: Any) -> None:
        self._vehicle_simulation_workload = None
        dialog = getattr(self, "_vehicle_simulation_dialog", None)
        if dialog is not None:
            dialog.close()
        original_clear_outputs(self)
        if hasattr(self, "vehicle_simulation_button"):
            self.vehicle_simulation_button.setEnabled(False)

    def start(self: Any) -> None:
        workload = getattr(self, "_vehicle_simulation_workload", None)
        if workload is None:
            QMessageBox.warning(
                self,
                "랜덤 FromTo 필요",
                "현재 Layout에서 랜덤 FromTo 정적분석을 먼저 실행해 주세요.",
            )
            return
        if getattr(self, "_layout_analysis_mode", "random") != "random":
            QMessageBox.warning(
                self,
                "랜덤 FromTo 모드 필요",
                "2D Vehicle Simulation은 먼저 랜덤 FromTo 모드에서 생성한 Job으로 실행합니다.",
            )
            return
        using_cad = getattr(self, "_active_layout_kind", "") == "cad"
        facility = self.cad_facility if using_cad else self.facility
        graph = self.cad_graph if using_cad else None
        if not isinstance(facility, Mapping):
            QMessageBox.warning(self, "Layout 필요", "시뮬레이션할 Layout이 없습니다.")
            return
        try:
            dialog = VehicleSimulationDialog(
                self,
                base_module,
                facility,
                workload.scenario,
                graph if isinstance(graph, Mapping) else None,
                self.vehicle_simulation_count.value(),
            )
        except Exception as error:
            QMessageBox.critical(self, "2D Vehicle Simulation 시작 실패", str(error))
            return
        self._vehicle_simulation_dialog = dialog
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()
        self.statusBar().showMessage(
            "2D Vehicle Simulation 실행 · 센터라인 주행 및 10초 Pickup/Setdown",
            8_000,
        )

    cls.build_inputs = build_inputs
    cls.refresh = refresh
    cls._random_flow_ready = random_ready
    cls._clear_random_flow_outputs = clear_outputs
    cls.start_vehicle_simulation = start
