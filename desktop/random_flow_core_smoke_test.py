"""Cross-check generated random workloads against the authoritative C++ Core."""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path

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


def _verify_facility(core: Path, facility_path: Path, root: Path) -> tuple[int, int]:
    facility = json.loads(facility_path.read_text(encoding="utf-8"))
    workload = generate_random_workload(facility, 40, 20260723)
    saved = save_random_workload(
        workload,
        root,
        model_name=str(facility.get("model_id", "core-smoke")),
        timestamp="fixed",
    )
    _run(
        core,
        "validate",
        "--facility",
        facility_path,
        "--scenario",
        saved.scenario_json_path,
    )
    core_report_path = saved.directory / "core-analysis.json"
    _run(
        core,
        "analyze",
        "--facility",
        facility_path,
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
        facility_path,
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
            f"generated Scenario did not complete for {facility_path}: {manifest.get('status')}"
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
            routes, flows = _verify_facility(core, facility_path, root)
            route_count += routes
            flow_count += flows

    print(
        "random flow Core smoke: PASS "
        f"(loop + one-way, {route_count} OD routes + {flow_count} Edge flows + simulations)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
