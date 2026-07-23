"""Cross-check generated random workloads against the authoritative C++ Core."""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path

from cad_graph_facility import build_facility_from_cad_graph
from random_flow_analysis import generate_random_workload, save_random_workload


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def _run(*arguments: str | Path) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [str(item) for item in arguments],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(str(item) for item in arguments)}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


def _verify_facility(
    core: Path,
    facility: dict,
    root: Path,
) -> tuple[int, int]:
    workload = generate_random_workload(facility, 40, 20260723)
    saved = save_random_workload(
        workload,
        facility,
        root,
        model_name=str(facility.get("model_id", "core-smoke")),
        timestamp="fixed",
    )
    _run(
        core,
        "validate",
        "--facility",
        saved.facility_json_path,
        "--scenario",
        saved.scenario_json_path,
    )
    core_report_path = saved.directory / "core-analysis.json"
    _run(
        core,
        "analyze",
        "--facility",
        saved.facility_json_path,
        "--scenario",
        saved.scenario_json_path,
        "--from-to-csv",
        saved.demand_csv_path,
        "--output",
        core_report_path,
    )
    core_report = json.loads(core_report_path.read_text(encoding="utf-8"))
    expected_routes = {
        item["demand_id"]: item["edge_ids"]
        for item in workload.analysis["demand_routes"]
    }
    actual_routes = {
        item["demand_id"]: item["edge_ids"] for item in core_report["demand_routes"]
    }
    if expected_routes != actual_routes:
        raise RuntimeError(
            "Python preview and C++ Core selected different Dijkstra routes"
        )
    expected_flows = {
        item["edge_id"]: item["expected_moves_per_hour"]
        for item in workload.analysis["edge_flows"]
    }
    actual_flows = {
        item["edge_id"]: item["expected_moves_per_hour"]
        for item in core_report["edge_flows"]
    }
    if expected_flows != actual_flows:
        raise RuntimeError(
            "Python preview and C++ Core accumulated different Edge traffic"
        )

    simulation_output = saved.directory / "simulation"
    _run(
        core,
        "run",
        "--facility",
        saved.facility_json_path,
        "--scenario",
        saved.scenario_json_path,
        "--output",
        simulation_output,
    )
    manifest = json.loads(
        (simulation_output / "run_manifest.json").read_text(encoding="utf-8")
    )
    if manifest.get("status") != "COMPLETED":
        raise RuntimeError(
            f"generated Scenario did not complete for {saved.facility_json_path}: "
            f"{manifest.get('status')}"
        )
    return len(expected_routes), len(expected_flows)


def main() -> int:
    configured = os.environ.get("SIM_CORE_BIN", "").strip()
    if not configured:
        raise RuntimeError("SIM_CORE_BIN is required")
    core = Path(configured)
    if not core.is_file():
        raise RuntimeError(f"sim-core executable was not found: {core}")

    facility_paths = (
        REPOSITORY_ROOT / "examples" / "cross_domain" / "facility.json",
        REPOSITORY_ROOT / "examples" / "single_line" / "facility.json",
    )
    route_count = 0
    flow_count = 0
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        for facility_path in facility_paths:
            facility = json.loads(facility_path.read_text(encoding="utf-8"))
            routes, flows = _verify_facility(core, facility, root)
            route_count += routes
            flow_count += flows
        cad_graph = {
            "format_version": "1.0.0",
            "metadata": {
                "source_file": "cad-core-smoke.dxf",
                "source_sha256": "b" * 64,
                "coordinate_unit": "millimeter",
                "selected_layers": ["RAIL"],
                "labels": [
                    {"text": "station-1", "x": 25, "y": 0},
                    {"text": "station-2", "x": 100, "y": 50},
                    {"text": "station-3", "x": 25, "y": 100},
                ],
            },
            "nodes": [[0, 0], [100, 0], [100, 100], [0, 100]],
            "edges": [
                {"start": 0, "end": 1, "dir": [0, 1], "geometry": [[0, 0], [100, 0]]},
                {"start": 1, "end": 2, "dir": [1, 2], "geometry": [[100, 0], [100, 100]]},
                {"start": 2, "end": 3, "dir": [2, 3], "geometry": [[100, 100], [0, 100]]},
                {"start": 3, "end": 0, "dir": [3, 0], "geometry": [[0, 100], [0, 0]]},
            ],
        }
        routes, flows = _verify_facility(
            core, build_facility_from_cad_graph(cad_graph), root
        )
        route_count += routes
        flow_count += flows

    print(
        "random flow Core smoke: PASS "
        f"(loop + one-way + CAD adapter, {route_count} OD routes + "
        f"{flow_count} Edge flows + simulations)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
