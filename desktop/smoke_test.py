"""Exercise the native UI and authoritative C++ analysis path without a display."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import ezdxf
from PySide6.QtCore import QProcess, QTimer
from PySide6.QtWidgets import QApplication

from app import MainWindow


TIMEOUT_MS = 30_000


def main() -> int:
    application = QApplication([])
    window = MainWindow()

    if not window.core:
        raise RuntimeError("sim-core executable was not detected")
    if not window.facility_path or not window.scenario_path or not window.demand_path:
        raise RuntimeError("cross-domain sample inputs were not detected")

    with tempfile.TemporaryDirectory() as temporary:
        dxf_path = Path(temporary) / "ui-smoke.dxf"
        document = ezdxf.new("R2013")
        model = document.modelspace()
        model.add_line((0, 0), (1000, 0))
        model.add_arc(center=(1000, 1000), radius=1000, start_angle=270, end_angle=360)
        document.saveas(dxf_path)
        window.cad_path = dxf_path
        window.convert_cad_graph()
        if not window.cad_graph:
            raise RuntimeError("DXF graph was not created")
        statistics = window.cad_graph["metadata"]["statistics"]
        if statistics["node_count"] != 12 or statistics["edge_count"] != 11:
            raise RuntimeError("DXF graph counts did not match the UI fixture")
        if statistics["unresolved_direction_count"] != 0:
            raise RuntimeError("DXF graph contains unresolved directions")
        if not window.cad_graph_view.scene().items():
            raise RuntimeError("DXF graph preview did not render")

    result = {"exit_code": None, "timed_out": False}

    def stop_on_timeout() -> None:
        result["timed_out"] = True
        if window.process.state() != QProcess.ProcessState.NotRunning:
            window.process.kill()
            window.process.waitForFinished(5_000)
        application.quit()

    def finish(exit_code: int, _status: QProcess.ExitStatus) -> None:
        result["exit_code"] = exit_code
        application.quit()

    window.process.finished.connect(finish)
    QTimer.singleShot(TIMEOUT_MS, stop_on_timeout)
    window.run_core("analyze")
    application.exec()

    if result["timed_out"]:
        raise RuntimeError("native desktop analysis timed out")
    if result["exit_code"] != 0:
        raise RuntimeError(f"sim-core analyze exited with {result['exit_code']}")

    report = window.analysis or {}
    if report.get("status") != "PASS":
        raise RuntimeError("analysis report status was not PASS")
    if len(report.get("demand_routes", [])) != 1:
        raise RuntimeError("expected one demand route")
    if len(report.get("edge_flows", [])) != 2 or window.edge_table.rowCount() != 2:
        raise RuntimeError("expected two edge-flow rows in the report and UI")

    print("native desktop smoke: PASS (DXF preview + Core analyze + UI result binding)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
