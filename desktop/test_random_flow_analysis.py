"""Tests for layout-only random From-To generation and static flow analysis."""

from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from random_flow_analysis import (
    HOUR_US,
    RandomFlowError,
    generate_random_workload,
    save_random_workload,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def _node(node_id: str, x: int, y: int = 0) -> dict:
    return {"id": node_id, "position_um": {"x": x, "y": y, "z": 0}}


def _edge(edge_id: str, source: str, target: str, x1: int, x2: int) -> dict:
    length = abs(x2 - x1) or 1_000_000
    return {
        "id": edge_id,
        "from_node_id": source,
        "to_node_id": target,
        "length_um": length,
        "speed_limit_um_per_s": 1_000_000,
        "polyline_um": [
            {"x": x1, "y": 0, "z": 0},
            {"x": x2, "y": 0, "z": 0},
        ],
    }


def _station(station_id: str, node_id: str) -> dict:
    return {
        "id": station_id,
        "attachment_node_id": node_id,
        "operation_type": "LOAD",
    }


class RandomFlowAnalysisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.facility = json.loads(
            (REPOSITORY_ROOT / "examples" / "cross_domain" / "facility.json").read_text(
                encoding="utf-8"
            )
        )

    def test_generation_is_reproducible_and_preserves_total_hourly_moves(self) -> None:
        first = generate_random_workload(self.facility, 240, 20260723)
        second = generate_random_workload(self.facility, 240, 20260723)

        self.assertEqual(first, second)
        self.assertEqual(
            sum(item["expected_moves_per_hour"] for item in first.demands), 240
        )
        self.assertEqual(len(first.scenario["jobs"]), 240)
        self.assertEqual(len(first.sampled_pairs), 240)
        self.assertTrue(all(source != target for source, target in first.sampled_pairs))
        releases = [job["release_time_us"] for job in first.scenario["jobs"]]
        self.assertEqual(releases, sorted(releases))
        self.assertGreaterEqual(releases[0], 0)
        self.assertLess(releases[-1], HOUR_US)
        self.assertEqual(len(first.scenario["vehicles"]), 240)
        self.assertEqual(
            {vehicle["initial_station_id"] for vehicle in first.scenario["vehicles"]},
            {source for source, _target in first.sampled_pairs},
        )

    def test_static_flow_equals_demand_route_accumulation(self) -> None:
        workload = generate_random_workload(self.facility, 180, 91)
        accumulated: dict[str, float] = {}
        for route in workload.analysis["demand_routes"]:
            for edge_id in route["edge_ids"]:
                accumulated[edge_id] = (
                    accumulated.get(edge_id, 0.0) + route["expected_moves_per_hour"]
                )
        reported = {
            flow["edge_id"]: flow["expected_moves_per_hour"]
            for flow in workload.analysis["edge_flows"]
        }
        self.assertEqual(reported, accumulated)
        self.assertEqual(
            workload.analysis["flow_summary"]["max_edge_moves_per_hour"],
            max(accumulated.values()),
        )
        self.assertTrue(
            all(
                0.0 < flow["relative_load"] <= 1.0
                for flow in workload.analysis["edge_flows"]
            )
        )

    def test_only_reachable_station_pairs_are_sampled(self) -> None:
        facility = {
            "model_id": "one-way",
            "revision_id": "one-way-v1",
            "nodes": [_node("A", 0), _node("B", 1_000_000), _node("C", 2_000_000)],
            "edges": [_edge("E-A-B", "A", "B", 0, 1_000_000)],
            "stations": [
                _station("ST-A", "A"),
                _station("ST-B", "B"),
                _station("ST-C", "C"),
            ],
        }
        workload = generate_random_workload(facility, 25, 7)

        self.assertEqual(workload.reachable_pair_count, 1)
        self.assertEqual(set(workload.sampled_pairs), {("ST-A", "ST-B")})
        self.assertEqual(workload.excluded_station_ids, ("ST-C",))
        self.assertEqual(workload.demands[0]["expected_moves_per_hour"], 25)

    def test_equal_time_routes_use_lexicographic_edge_signature(self) -> None:
        facility = {
            "model_id": "diamond",
            "revision_id": "diamond-v1",
            "nodes": [
                _node("A", 0),
                _node("B", 1_000_000),
                _node("C", 1_000_000),
                _node("D", 2_000_000),
            ],
            "edges": [
                _edge("E-Z", "A", "B", 0, 1_000_000),
                _edge("E-Z-D", "B", "D", 1_000_000, 2_000_000),
                _edge("E-AA", "A", "C", 0, 1_000_000),
                _edge("E-C-D", "C", "D", 1_000_000, 2_000_000),
            ],
            "stations": [_station("ST-A", "A"), _station("ST-D", "D")],
        }
        workload = generate_random_workload(facility, 1, 11)

        self.assertEqual(
            workload.analysis["demand_routes"][0]["edge_ids"],
            ["E-AA", "E-C-D"],
        )

    def test_no_directed_station_route_is_reported(self) -> None:
        facility = {
            "model_id": "isolated",
            "revision_id": "isolated-v1",
            "nodes": [_node("A", 0), _node("B", 1_000_000), _node("C", 2_000_000)],
            "edges": [_edge("E-A-B", "A", "B", 0, 1_000_000)],
            "stations": [_station("ST-B", "B"), _station("ST-C", "C")],
        }
        with self.assertRaisesRegex(RandomFlowError, "경로가 없습니다"):
            generate_random_workload(facility, 10, 1)

    def test_large_hourly_count_bounds_active_od_routes_without_losing_jobs(
        self,
    ) -> None:
        node_count = 20
        nodes = [
            _node(f"N-{index:02d}", index * 1_000_000) for index in range(node_count)
        ]
        edges = []
        for source in range(node_count):
            for target in range(node_count):
                if source == target:
                    continue
                edge = _edge(
                    f"E-{source:02d}-{target:02d}",
                    f"N-{source:02d}",
                    f"N-{target:02d}",
                    source * 1_000_000,
                    target * 1_000_000,
                )
                edge["length_um"] = 1_000_000
                edges.append(edge)
        facility = {
            "model_id": "complete-20",
            "revision_id": "complete-20-v1",
            "nodes": nodes,
            "edges": edges,
            "stations": [
                _station(f"ST-{index:02d}", f"N-{index:02d}")
                for index in range(node_count)
            ],
        }
        workload = generate_random_workload(facility, 1_000, 13)

        self.assertEqual(len(workload.demands), 80)  # 20 Stations × 4 active OD pairs
        self.assertEqual(len(workload.scenario["jobs"]), 1_000)
        self.assertEqual(len(workload.scenario["vehicles"]), 1_000)
        self.assertEqual(
            sum(item["expected_moves_per_hour"] for item in workload.demands), 1_000
        )
        self.assertEqual(workload.analysis["generation"]["active_pair_limit"], 80)

    def test_saved_artifacts_are_complete_and_never_overwrite(self) -> None:
        workload = generate_random_workload(self.facility, 40, 77)
        with tempfile.TemporaryDirectory() as temporary:
            first = save_random_workload(
                workload,
                temporary,
                model_name="cross-domain-loop",
                timestamp="20260723-010203",
            )
            second = save_random_workload(
                workload,
                temporary,
                model_name="cross-domain-loop",
                timestamp="20260723-010203",
            )
            self.assertNotEqual(first.directory, second.directory)
            self.assertTrue(first.scenario_json_path.is_file())
            self.assertTrue(first.analysis_json_path.is_file())
            with first.demand_csv_path.open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), len(workload.demands))
            self.assertEqual(
                sum(float(row["expected_moves_per_hour"]) for row in rows), 40
            )
            loaded_scenario = json.loads(
                first.scenario_json_path.read_text(encoding="utf-8")
            )
            self.assertEqual(loaded_scenario, workload.scenario)
            saved_analysis = json.loads(
                first.analysis_json_path.read_text(encoding="utf-8")
            )
            self.assertEqual(
                len(saved_analysis["demand_routes"]),
                len(workload.analysis["demand_routes"]),
            )
            self.assertTrue(
                all(
                    "edge_ids" not in route for route in saved_analysis["demand_routes"]
                )
            )
            self.assertTrue(
                all(
                    route["edge_path_saved"] is False
                    for route in saved_analysis["demand_routes"]
                )
            )
            self.assertTrue(
                all(
                    "contributing_demand_ids" not in flow
                    for flow in saved_analysis["edge_flows"]
                )
            )


if __name__ == "__main__":
    unittest.main()
