"""Offscreen smoke test for Random From-To heatmap and path-bound vehicle UI."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QApplication

from app_wrapper import MainWindow
from random_flow_analysis import generate_random_workload
from random_flow_ui import FlowHeatmapView


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    application = QApplication.instance() or QApplication([])
    facility = json.loads(
        (REPOSITORY_ROOT / "examples" / "cross_domain" / "facility.json").read_text(
            encoding="utf-8"
        )
    )
    workload = generate_random_workload(facility, 120, 20260723)

    with tempfile.TemporaryDirectory() as temporary:
        os.environ["SIM_CORE_GENERATED_DIR"] = temporary
        window = MainWindow()
        application.processEvents()
        if not hasattr(window, "random_flow_generate_button"):
            raise RuntimeError("random From-To generation control was not installed")

        window.random_moves_per_hour.setValue(120)
        window.random_seed.setValue(20260723)
        window.generate_random_flow()
        worker = window._random_flow_worker
        if worker is None:
            raise RuntimeError("random From-To worker did not start")
        event_loop = QEventLoop()
        state = {"finished": False}

        def worker_finished() -> None:
            state["finished"] = True
            event_loop.quit()

        worker.finished.connect(worker_finished)
        QTimer.singleShot(10_000, event_loop.quit)
        if worker.isFinished():
            worker_finished()
        event_loop.exec()
        application.processEvents()
        if not state["finished"]:
            raise RuntimeError("random From-To worker timed out")
        if window.scenario_path is None or not window.scenario_path.is_file():
            raise RuntimeError("generated Scenario was not connected to the workbench")
        if window.demand_path is None or not window.demand_path.is_file():
            raise RuntimeError(
                "generated From-To CSV was not connected to the workbench"
            )
        if window.analysis != workload.analysis:
            raise RuntimeError("static analysis was not bound to the result tables")

        dialog = window._random_flow_dialog
        if dialog is None or not dialog.isVisible():
            raise RuntimeError("LA analysis + vehicle popup did not open")
        view = dialog.findChild(FlowHeatmapView)
        if view is None:
            raise RuntimeError("flow heatmap canvas was not created")
        edge_items = [
            item for item in view.scene().items() if item.data(0) == "random-flow-edge"
        ]
        if len(edge_items) != len(facility["edges"]):
            raise RuntimeError("flow heatmap did not render every layout Edge")
        relative_loads = [float(item.data(3)) for item in edge_items]
        if max(relative_loads, default=0.0) != 1.0:
            raise RuntimeError("highest-traffic Edge was not normalized to 100%")
        if any(value < 0.0 or value > 1.0 for value in relative_loads):
            raise RuntimeError("heatmap relative load escaped the 0..1 color range")
        station_items = [
            item
            for item in view.scene().items()
            if item.data(0) == "random-flow-station"
        ]
        if len(station_items) != len(facility["stations"]):
            raise RuntimeError("flow heatmap did not render every Station")

        if not view._edge_geometries:
            raise RuntimeError("vehicle animation Edge centerline geometry was not built")
        if not view._vehicle_states:
            raise RuntimeError("vehicle animation preview fleet was not created")
        if len(view._vehicle_states) > 300:
            raise RuntimeError("vehicle animation preview exceeded the UI safety limit")
        if not view.animation_running():
            raise RuntimeError("vehicle centerline animation did not auto-start")

        # Advance the preview briefly. Every visible vehicle item is positioned only
        # through locate_route_pose(), which derives X/Y from its current Edge polyline.
        local_loop = QEventLoop()
        QTimer.singleShot(150, local_loop.quit)
        local_loop.exec()
        application.processEvents()
        configured_items = [state.get("item") for state in view._vehicle_states]
        if not any(item is not None and item.isVisible() for item in configured_items):
            raise RuntimeError("no released vehicle became visible on the path network")

        dialog.close()
        window.close()
        application.processEvents()
        os.environ.pop("SIM_CORE_GENERATED_DIR", None)

    print(
        "random flow UI smoke: PASS "
        "(generation + heatmap + path-bound vehicle centerline animation)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
