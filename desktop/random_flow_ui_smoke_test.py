"""Offscreen smoke test for the random From-To heatmap UI binding."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import ezdxf
from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QApplication

from app_wrapper import MainWindow
from random_flow_analysis import generate_random_workload
from random_flow_ui import FlowHeatmapView

def main() -> int:
    application = QApplication.instance() or QApplication([])
    with tempfile.TemporaryDirectory() as temporary:
        os.environ["SIM_CORE_GENERATED_DIR"] = temporary
        window = MainWindow()
        application.processEvents()
        if not hasattr(window, "random_flow_generate_button"):
            raise RuntimeError("random From-To generation control was not installed")

        # Regression for the real user flow: the workbench starts with the
        # ST-A/B/C sample, then the user selects a DXF. Random analysis must bind
        # to this newly converted graph and its station labels, never the sample.
        dxf_path = Path(temporary) / "active-cad-layout.dxf"
        document = ezdxf.new("R2013")
        model = document.modelspace()
        model.add_line((0, 0), (100, 0))
        for station_id, x in (("station-1", 10), ("station-2", 50), ("station-3", 90)):
            model.add_text(station_id).set_placement((x, 0))
        document.saveas(dxf_path)
        window.cad_path = dxf_path
        window.convert_cad_graph()
        facility = window.cad_facility
        if facility is None:
            raise RuntimeError(
                f"converted CAD graph was not bound to Random LA: {window.cad_facility_error}"
            )
        if window._active_layout_kind != "cad":
            raise RuntimeError("converted CAD graph did not become the active analysis layout")
        station_ids = {station["id"] for station in facility["stations"]}
        if station_ids != {"station-1", "station-2", "station-3"}:
            raise RuntimeError(f"CAD station labels were not bound exactly: {station_ids}")
        if station_ids & {"ST-A", "ST-B", "ST-C"}:
            raise RuntimeError("hidden sample stations leaked into CAD analysis")
        workload = generate_random_workload(facility, 120, 20260723)

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
        if window.facility_path is None or not window.facility_path.is_file():
            raise RuntimeError("exact CAD-derived Facility was not saved and connected")
        if window.facility != facility:
            raise RuntimeError("saved Facility binding differs from the analyzed CAD layout")
        if window.demand_path is None or not window.demand_path.is_file():
            raise RuntimeError(
                "generated From-To CSV was not connected to the workbench"
            )
        if window.analysis != workload.analysis:
            raise RuntimeError("static analysis was not bound to the result tables")

        dialog = window._random_flow_dialog
        if dialog is None or not dialog.isVisible():
            raise RuntimeError("LA static analysis popup did not open")
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

        dialog.close()
        window.close()
        application.processEvents()
        os.environ.pop("SIM_CORE_GENERATED_DIR", None)

    print(
        "random flow UI smoke: PASS "
        "(active CAD binding + green/red heatmap popup)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
