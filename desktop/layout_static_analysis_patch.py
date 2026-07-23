"""Layout static-analysis mode patch for random or real FromTo CSV demand.

This module keeps the existing random workload path intact and adds a second,
read-only analysis path for a user-selected real FromTo CSV.  The source CSV is
never rewritten.  A timestamped analysis snapshot is stored under the existing
Generated output root together with the exact Facility used for routing.
"""
from __future__ import annotations

import copy
import csv
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QButtonGroup, QLabel, QMessageBox

from random_flow_analysis import (
    GeneratedRandomWorkload,
    RandomFlowError,
    SavedRandomWorkload,
    _FacilityRouter,
    default_generated_output_root,
)
from random_flow_ui import show_random_flow_dialog


_FROM_ALIASES = (
    "from_station_id",
    "from_station",
    "from",
    "origin",
    "source",
    "fromstation",
    "출발",
    "출발지",
)
_TO_ALIASES = (
    "to_station_id",
    "to_station",
    "to",
    "destination",
    "target",
    "tostation",
    "도착",
    "도착지",
)
_RATE_ALIASES = (
    "expected_moves_per_hour",
    "moves_per_hour",
    "move_per_hour",
    "moves",
    "quantity",
    "qty",
    "count",
    "volume",
    "transport_count",
    "반송량",
    "시간당반송량",
)
_ID_ALIASES = ("id", "demand_id", "od_id")


def _normalise_header(value: str) -> str:
    return re.sub(r"[\s\-]+", "_", value.strip().casefold())


def _column_name(fieldnames: list[str], aliases: tuple[str, ...], label: str) -> str:
    indexed = {_normalise_header(name): name for name in fieldnames if name}
    for alias in aliases:
        matched = indexed.get(_normalise_header(alias))
        if matched:
            return matched
    raise RandomFlowError(
        f"실제 FromTo CSV에 {label} 열이 없습니다. "
        f"현재 열: {', '.join(fieldnames)}"
    )


def _read_actual_demands(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise RandomFlowError(f"실제 FromTo CSV를 찾을 수 없습니다: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fieldnames = list(reader.fieldnames or [])
        if not fieldnames:
            raise RandomFlowError("실제 FromTo CSV에 헤더가 없습니다.")
        from_key = _column_name(fieldnames, _FROM_ALIASES, "From Station")
        to_key = _column_name(fieldnames, _TO_ALIASES, "To Station")
        rate_key = _column_name(fieldnames, _RATE_ALIASES, "반송량")
        id_key = None
        indexed = {_normalise_header(name): name for name in fieldnames if name}
        for alias in _ID_ALIASES:
            if _normalise_header(alias) in indexed:
                id_key = indexed[_normalise_header(alias)]
                break

        demands: list[dict[str, Any]] = []
        used_ids: set[str] = set()
        for row_number, row in enumerate(reader, start=2):
            from_id = str(row.get(from_key, "") or "").strip()
            to_id = str(row.get(to_key, "") or "").strip()
            raw_rate = str(row.get(rate_key, "") or "").strip().replace(",", "")
            if not from_id and not to_id and not raw_rate:
                continue
            if not from_id or not to_id:
                raise RandomFlowError(
                    f"실제 FromTo CSV {row_number}행의 From/To Station이 비어 있습니다."
                )
            try:
                rate = float(raw_rate)
            except ValueError as error:
                raise RandomFlowError(
                    f"실제 FromTo CSV {row_number}행 반송량이 숫자가 아닙니다: {raw_rate}"
                ) from error
            if rate < 0:
                raise RandomFlowError(
                    f"실제 FromTo CSV {row_number}행 반송량은 0 이상이어야 합니다."
                )
            demand_id = str(row.get(id_key, "") or "").strip() if id_key else ""
            if not demand_id:
                demand_id = f"ACT-OD-{row_number - 1:05d}"
            base_id = demand_id
            suffix = 2
            while demand_id in used_ids:
                demand_id = f"{base_id}-{suffix}"
                suffix += 1
            used_ids.add(demand_id)
            demands.append(
                {
                    "id": demand_id,
                    "from_station_id": from_id,
                    "to_station_id": to_id,
                    "expected_moves_per_hour": rate,
                }
            )

    if not demands:
        raise RandomFlowError("실제 FromTo CSV에 분석할 데이터가 없습니다.")
    return demands


def _build_actual_analysis(
    facility: Mapping[str, Any], demands: list[dict[str, Any]], source_name: str
) -> tuple[dict[str, Any], int]:
    router = _FacilityRouter(facility)
    edge_moves: Counter[str] = Counter()
    edge_demands: dict[str, list[str]] = defaultdict(list)
    station_inbound: Counter[str] = Counter()
    station_outbound: Counter[str] = Counter()
    demand_routes: list[dict[str, Any]] = []
    valid_pairs: set[tuple[str, str]] = set()

    for demand in demands:
        rate = float(demand["expected_moves_per_hour"])
        from_id = str(demand["from_station_id"])
        to_id = str(demand["to_station_id"])
        if from_id not in router.station_nodes:
            raise RandomFlowError(f"실제 FromTo의 From Station이 Layout에 없습니다: {from_id}")
        if to_id not in router.station_nodes:
            raise RandomFlowError(f"실제 FromTo의 To Station이 Layout에 없습니다: {to_id}")
        if rate <= 0:
            continue
        route = router.route_stations(from_id, to_id)
        if route is None:
            raise RandomFlowError(
                f"방향성 Layout에서 실제 FromTo 경로를 찾을 수 없습니다: {from_id} → {to_id}"
            )
        valid_pairs.add((from_id, to_id))
        demand_routes.append(
            {
                "demand_id": demand["id"],
                "from_station_id": from_id,
                "to_station_id": to_id,
                "expected_moves_per_hour": rate,
                "edge_ids": list(route.edge_ids),
                "distance_um": route.distance_um,
                "travel_time_us": route.travel_time_us,
            }
        )
        station_outbound[from_id] += rate
        station_inbound[to_id] += rate
        for edge_id in route.edge_ids:
            edge_moves[edge_id] += rate
            edge_demands[edge_id].append(str(demand["id"]))

    total_edge_moves = float(sum(edge_moves.values()))
    max_edge_moves = float(max(edge_moves.values(), default=0.0))
    edge_flows: list[dict[str, Any]] = []
    node_inflow: Counter[str] = Counter()
    node_outflow: Counter[str] = Counter()
    node_incoming_edges: Counter[str] = Counter()
    for edge_id in sorted(edge_moves):
        edge = router.edges[edge_id]
        moves = float(edge_moves[edge_id])
        contributing = sorted(edge_demands[edge_id])
        edge_flows.append(
            {
                "edge_id": edge.id,
                "from_node_id": edge.from_node_id,
                "to_node_id": edge.to_node_id,
                "length_um": edge.length_um,
                "expected_moves_per_hour": moves,
                "flow_share": moves / total_edge_moves if total_edge_moves else 0.0,
                "relative_load": moves / max_edge_moves if max_edge_moves else 0.0,
                "demand_count": len(contributing),
                "contributing_demand_ids": contributing,
            }
        )
        node_inflow[edge.to_node_id] += moves
        node_outflow[edge.from_node_id] += moves
        node_incoming_edges[edge.to_node_id] += 1

    node_ids = sorted(set(node_inflow) | set(node_outflow))
    node_flows = [
        {
            "node_id": node_id,
            "inflow_moves_per_hour": float(node_inflow[node_id]),
            "outflow_moves_per_hour": float(node_outflow[node_id]),
            "incoming_edge_count": int(node_incoming_edges[node_id]),
            "merge_pressure": (
                float(node_inflow[node_id]) if node_incoming_edges[node_id] >= 2 else 0.0
            ),
        }
        for node_id in node_ids
    ]

    station_capacity = {
        str(station.get("id")): float(
            station.get("handling_capacity_per_hour", 0.0) or 0.0
        )
        for station in facility.get("stations", [])
        if isinstance(station, Mapping)
    }
    station_ids = sorted(set(station_inbound) | set(station_outbound))
    station_flows = []
    for station_id in station_ids:
        inbound = float(station_inbound[station_id])
        outbound = float(station_outbound[station_id])
        peak = max(inbound, outbound)
        capacity = station_capacity.get(station_id, 0.0)
        station_flows.append(
            {
                "station_id": station_id,
                "inbound_moves_per_hour": inbound,
                "outbound_moves_per_hour": outbound,
                "peak_moves_per_hour": peak,
                "handling_capacity_per_hour": capacity,
                "capacity_margin_per_hour": capacity - peak if capacity > 0 else 0.0,
                "utilization_ratio": peak / capacity if capacity > 0 else 0.0,
                "over_capacity": capacity > 0 and peak > capacity,
            }
        )

    total_moves = float(sum(float(item["expected_moves_per_hour"]) for item in demands))
    analysis = {
        "schema_version": "1.0.0",
        "model_revision_id": str(facility.get("revision_id", "")),
        "scenario_id": "actual-fromto-static-analysis",
        "status": "PASS",
        "error_count": 0,
        "warning_count": 0,
        "diagnostics": [],
        "demand_routes": demand_routes,
        "edge_flows": edge_flows,
        "node_flows": node_flows,
        "station_flows": station_flows,
        "flow_summary": {
            "total_moves_per_hour": total_moves,
            "total_edge_traversals_per_hour": total_edge_moves,
            "max_edge_moves_per_hour": max_edge_moves,
            "used_edge_count": len(edge_flows),
            "total_edge_count": len(router.edges),
        },
        "generation": {
            "method": "actual-fromto-csv",
            "source_csv_name": source_name,
            "source_csv_modified": False,
            "generated_demand_count": len(demands),
            "generated_job_count": 0,
            "generated_vehicle_count": 0,
        },
    }
    return analysis, len(valid_pairs)


def _safe_stem(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9가-힣._-]+", "-", value.strip()).strip("-._") or "facility"


def _save_actual_snapshot(
    facility: Mapping[str, Any],
    source_csv: Path,
    analysis: Mapping[str, Any],
    output_root: Path,
    model_name: str,
) -> SavedRandomWorkload:
    output_root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    base = output_root / f"{_safe_stem(model_name)}-actual-flow-{stamp}"
    directory = base
    suffix = 2
    while directory.exists():
        directory = output_root / f"{base.name}-{suffix}"
        suffix += 1
    directory.mkdir(parents=False, exist_ok=False)

    facility_path = directory / "analysis_facility.json"
    csv_snapshot_path = directory / "actual_from_to_snapshot.csv"
    context_path = directory / "actual_analysis_context.json"
    analysis_path = directory / "actual_la_analysis.json"

    with facility_path.open("w", encoding="utf-8") as stream:
        json.dump(facility, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    shutil.copy2(source_csv, csv_snapshot_path)

    compact_analysis = copy.deepcopy(dict(analysis))
    compact_analysis["demand_routes"] = [
        {key: value for key, value in route.items() if key != "edge_ids"}
        | {"edge_count": len(route.get("edge_ids", [])), "edge_path_saved": False}
        for route in analysis.get("demand_routes", [])
    ]
    compact_analysis["edge_flows"] = [
        {key: value for key, value in flow.items() if key != "contributing_demand_ids"}
        | {"contributing_demand_ids_saved": False}
        for flow in analysis.get("edge_flows", [])
    ]
    with analysis_path.open("w", encoding="utf-8") as stream:
        json.dump(compact_analysis, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    with context_path.open("w", encoding="utf-8") as stream:
        json.dump(
            {
                "analysis_type": "actual-fromto-static-analysis",
                "source_csv_name": source_csv.name,
                "source_csv_modified": False,
                "snapshot_csv_name": csv_snapshot_path.name,
                "facility_snapshot_name": facility_path.name,
                "analysis_report_name": analysis_path.name,
            },
            stream,
            ensure_ascii=False,
            indent=2,
        )
        stream.write("\n")

    return SavedRandomWorkload(
        directory=directory,
        facility_json_path=facility_path,
        demand_csv_path=csv_snapshot_path,
        scenario_json_path=context_path,
        analysis_json_path=analysis_path,
    )


def analyze_actual_fromto(
    facility: Mapping[str, Any], source_csv: Path, output_root: Path, model_name: str
) -> tuple[GeneratedRandomWorkload, SavedRandomWorkload]:
    demands = _read_actual_demands(source_csv)
    analysis, valid_pair_count = _build_actual_analysis(facility, demands, source_csv.name)
    total_moves = float(analysis["flow_summary"]["total_moves_per_hour"])
    workload = GeneratedRandomWorkload(
        scenario={},
        demands=tuple(demands),
        analysis=analysis,
        sampled_pairs=tuple(
            (str(item["from_station_id"]), str(item["to_station_id"]))
            for item in demands
            if float(item["expected_moves_per_hour"]) > 0
        ),
        reachable_pair_count=valid_pair_count,
        excluded_station_ids=(),
        moves_per_hour=total_moves,  # runtime formatting supports integer or decimal rates
        seed=0,
    )
    saved = _save_actual_snapshot(
        facility, source_csv, analysis, output_root, model_name
    )
    return workload, saved


class ActualFromToWorker(QThread):
    completed = Signal(object)
    failed = Signal(str)

    def __init__(
        self,
        facility: Mapping[str, Any],
        source_csv: Path,
        output_root: Path,
        model_name: str,
        parent: Any = None,
    ) -> None:
        super().__init__(parent)
        self._facility = copy.deepcopy(dict(facility))
        self._source_csv = Path(source_csv)
        self._output_root = Path(output_root)
        self._model_name = model_name

    def run(self) -> None:
        try:
            payload = analyze_actual_fromto(
                self._facility,
                self._source_csv,
                self._output_root,
                self._model_name,
            )
        except Exception as error:
            self.failed.emit(str(error))
            return
        self.completed.emit((payload[0], payload[1], self._source_csv))


def _decorate_actual_dialog(dialog: Any, source_csv: Path, saved: SavedRandomWorkload) -> None:
    dialog.setWindowTitle("Sim_Core · Layout 정적 분석 · 실제 FromTo")
    replacements = {
        "Random From-To · Edge 통행량 Heatmap": "Layout 정적 분석 · 실제 FromTo Heatmap",
        "입력한 시간당 반송을 방향성 최단경로에 누적했습니다. 초록색은 저사용, 빨간색은 고사용 Edge입니다.": (
            "선택한 실제 FromTo CSV의 반송량을 그대로 방향성 최단경로에 누적했습니다. "
            "원본 CSV는 수정하지 않고 분석 스냅샷만 별도 저장합니다."
        ),
        "생성 OD": "분석 OD",
        "도달 가능 OD": "유효 OD",
        "생성 Vehicle": "원본 CSV",
    }
    for label in dialog.findChildren(QLabel):
        text = label.text()
        if text in replacements:
            label.setText(replacements[text])
        elif text.startswith("Seed ") and "Facility " in text:
            label.setText(
                f"원본 CSV {source_csv.name} · 원본 유지 · "
                f"스냅샷 {saved.demand_csv_path.name} · 분석 {saved.analysis_json_path.name}"
            )


def install_layout_static_analysis(base_module: Any) -> None:
    """Patch the desktop MainWindow before it is instantiated."""

    cls = base_module.MainWindow
    if getattr(cls, "_layout_static_analysis_installed", False):
        return
    cls._layout_static_analysis_installed = True

    original_build_inputs = cls.build_inputs
    original_refresh = cls.refresh
    original_generate = cls.generate_random_flow

    def build_inputs(self: Any) -> Any:
        page = original_build_inputs(self)
        self._layout_analysis_mode = "random"
        panel = self.random_flow_generate_button.parentWidget()
        form = panel.layout()

        for label in panel.findChildren(QLabel):
            if label.text() == "랜덤 From-To 생성 · LA 정적분석":
                label.setText("Layout 정적 분석")
            elif label.text().startswith("현재 Facility의 Station과 방향성 Edge만으로"):
                label.setText(
                    "랜덤 FromTo 또는 연결한 실제 FromTo CSV를 선택해 방향성 최단경로 "
                    "통행량 Heatmap을 분석합니다."
                )

        self.random_fromto_mode_button = base_module.button("랜덤 FromTo", "secondary")
        self.actual_fromto_mode_button = base_module.button("실제 FromTo", "secondary")
        self.random_fromto_mode_button.setCheckable(True)
        self.actual_fromto_mode_button.setCheckable(True)
        self.random_fromto_mode_button.setChecked(True)
        self.layout_analysis_mode_group = QButtonGroup(self)
        self.layout_analysis_mode_group.setExclusive(True)
        self.layout_analysis_mode_group.addButton(self.random_fromto_mode_button)
        self.layout_analysis_mode_group.addButton(self.actual_fromto_mode_button)
        self.random_fromto_mode_button.clicked.connect(
            lambda checked=False: self._set_layout_analysis_mode("random")
        )
        self.actual_fromto_mode_button.clicked.connect(
            lambda checked=False: self._set_layout_analysis_mode("actual")
        )
        form.addWidget(base_module.styled_label("FromTo 분석 방식", "FieldLabel"), 3, 0)
        form.addWidget(self.random_fromto_mode_button, 3, 1)
        form.addWidget(self.actual_fromto_mode_button, 3, 2)
        self.random_flow_generate_button.setText("랜덤 FromTo 정적분석 실행")
        return page

    def set_mode(self: Any, mode: str) -> None:
        self._layout_analysis_mode = mode
        is_random = mode == "random"
        self.random_moves_per_hour.setEnabled(is_random)
        self.random_seed.setEnabled(is_random)
        self.random_fromto_mode_button.setChecked(is_random)
        self.actual_fromto_mode_button.setChecked(not is_random)
        self.random_flow_generate_button.setText(
            "랜덤 FromTo 정적분석 실행" if is_random else "실제 FromTo 정적분석 실행"
        )
        self.refresh()

    def refresh(self: Any) -> None:
        original_refresh(self)
        if getattr(self, "_layout_analysis_mode", "random") != "actual":
            return
        using_cad = self._active_layout_kind == "cad"
        facility = (self.cad_facility if using_cad else self.facility) or {}
        source = self.demand_path
        ready = bool(
            facility
            and len(facility.get("stations", [])) >= 2
            and source
            and Path(source).is_file()
        )
        if self._random_flow_worker is None:
            if source and Path(source).is_file():
                self.random_flow_status.setText(
                    f"실제 FromTo 분석 대상 · {Path(source).name} · 원본 CSV 유지 · "
                    f"Station {len(facility.get('stations', [])):,}개"
                )
            else:
                self.random_flow_status.setText(
                    "실제 FromTo 모드 · 위 From-To CSV 카드에서 실제 반송 CSV를 연결해 주세요."
                )
            self.random_flow_generate_button.setEnabled(ready)

    def generate(self: Any) -> None:
        if getattr(self, "_layout_analysis_mode", "random") != "actual":
            original_generate(self)
            return
        if self._random_flow_worker is not None and self._random_flow_worker.isRunning():
            QMessageBox.information(self, "분석 중", "현재 Layout 정적 분석이 끝날 때까지 기다려 주세요.")
            return
        try:
            facility = self._resolve_random_flow_facility()
        except Exception as error:
            QMessageBox.warning(self, "분석 레이아웃 확인 필요", str(error))
            self.switch_page(1)
            return
        source = Path(self.demand_path) if self.demand_path else None
        if source is None or not source.is_file():
            QMessageBox.warning(
                self,
                "실제 FromTo CSV 필요",
                "From-To CSV 카드에서 실제 반송 CSV를 먼저 연결해 주세요.",
            )
            return

        model_name = str(
            facility.get("model_id")
            or (self.facility_path.stem if self.facility_path else "facility")
        )
        self.random_flow_generate_button.setEnabled(False)
        self.random_flow_generate_button.setText("실제 FromTo 경로 계산 중…")
        self.random_flow_status.setText(
            f"{source.name}의 실제 반송량을 방향성 최단경로에 누적하고 있습니다…"
        )
        self.statusBar().showMessage("실제 FromTo 기반 Layout 정적 분석 중…")
        worker = ActualFromToWorker(
            facility,
            source,
            default_generated_output_root(),
            model_name,
            self,
        )
        self._random_flow_facility = facility
        self._random_flow_worker = worker
        worker.completed.connect(self._actual_fromto_ready)
        worker.failed.connect(self._actual_fromto_failed)
        worker.finished.connect(self._actual_fromto_finished)
        worker.finished.connect(worker.deleteLater)
        worker.start()

    def actual_ready(self: Any, payload: object) -> None:
        workload, saved, source_csv = payload  # type: ignore[misc]
        target_facility = self._random_flow_facility
        if target_facility is None:
            return
        if self._active_layout_kind == "cad" and self.cad_facility:
            if str(target_facility.get("revision_id", "")) != str(
                self.cad_facility.get("revision_id", "")
            ):
                QMessageBox.warning(
                    self,
                    "분석 결과 폐기",
                    "분석 중 CAD Graph가 변경되어 이전 Layout 결과를 연결하지 않았습니다. "
                    "현재 Graph로 다시 실행해 주세요.",
                )
                return
        self.analysis = workload.analysis
        self.refresh()
        total_moves = float(workload.analysis.get("flow_summary", {}).get("total_moves_per_hour", 0.0))
        self.random_flow_status.setText(
            f"실제 FromTo {len(workload.demands):,}개 OD · 총 {total_moves:,.1f} moves/h · "
            f"원본 CSV 유지\n분석 스냅샷 저장 완료 · {saved.directory.name}"
        )
        self.statusBar().showMessage(
            f"실제 FromTo Layout 정적 분석 완료 · {saved.directory}", 10_000
        )
        dialog = show_random_flow_dialog(self, target_facility, workload, saved)
        _decorate_actual_dialog(dialog, Path(source_csv), saved)
        self._random_flow_dialog = dialog

    def actual_failed(self: Any, message: str) -> None:
        self.random_flow_status.setText(f"실제 FromTo 분석 실패 · {message}")
        self.statusBar().showMessage("실제 FromTo Layout 정적 분석 실패", 8_000)
        QMessageBox.critical(self, "실제 FromTo 정적 분석 실패", message)

    def actual_finished(self: Any) -> None:
        self._random_flow_worker = None
        self._random_flow_facility = None
        self.random_flow_generate_button.setEnabled(True)
        self.random_flow_generate_button.setText("실제 FromTo 정적분석 실행")
        self.refresh()

    cls.build_inputs = build_inputs
    cls.refresh = refresh
    cls.generate_random_flow = generate
    cls._set_layout_analysis_mode = set_mode
    cls._actual_fromto_ready = actual_ready
    cls._actual_fromto_failed = actual_failed
    cls._actual_fromto_finished = actual_finished
