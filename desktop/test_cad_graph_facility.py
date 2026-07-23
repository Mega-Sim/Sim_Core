"""Tests for binding the displayed DXF graph to Random From-To analysis."""

from __future__ import annotations

import copy
import unittest

from cad_graph_facility import CadGraphFacilityError, build_facility_from_cad_graph
from random_flow_analysis import generate_random_workload


def _graph(*, direction: list[int] | None = None) -> dict:
    return {
        "format_version": "1.0.0",
        "metadata": {
            "source_file": "binding-test.dxf",
            "source_sha256": "a" * 64,
            "coordinate_unit": "millimeter",
            "selected_layers": ["RAIL"],
            "labels": [
                {"text": "station-1", "x": 25, "y": 2, "layer": "TEXT"},
                {"text": "NOTE", "x": 50, "y": 1, "layer": "TEXT"},
                {"text": "station-2", "x": 75, "y": -2, "layer": "TEXT"},
            ],
        },
        "nodes": [[0, 0], [100, 0]],
        "edges": [
            {
                "start": 0,
                "end": 1,
                "dir": direction or [0, 1],
                "geometry": [[0, 0], [100, 0]],
            }
        ],
    }


class CadGraphFacilityTests(unittest.TestCase):
    def test_station_labels_split_the_actual_directed_rail(self) -> None:
        facility = build_facility_from_cad_graph(_graph())

        self.assertEqual(len(facility["stations"]), 2)
        self.assertEqual(len(facility["nodes"]), 4)
        self.assertEqual(len(facility["edges"]), 3)
        stations = {station["id"]: station for station in facility["stations"]}
        self.assertEqual(stations["station-1"]["position_um"]["x"], 25_000)
        self.assertEqual(stations["station-2"]["position_um"]["x"], 75_000)
        self.assertNotEqual(
            stations["station-1"]["attachment_node_id"],
            stations["station-2"]["attachment_node_id"],
        )
        self.assertNotIn("NOTE", stations)
        self.assertTrue(facility["content_hash"].startswith("sha256:"))

        workload = generate_random_workload(facility, 10, 7)
        self.assertEqual(
            set(workload.sampled_pairs), {("station-1", "station-2")}
        )
        self.assertEqual(workload.analysis["flow_summary"]["total_edge_count"], 3)

    def test_manual_graph_direction_reverse_changes_the_route_direction(self) -> None:
        graph = _graph(direction=[1, 0])
        facility = build_facility_from_cad_graph(graph)
        workload = generate_random_workload(facility, 5, 11)

        self.assertEqual(
            set(workload.sampled_pairs), {("station-2", "station-1")}
        )
        self.assertEqual(
            facility["edges"][0]["polyline_um"][0]["x"], 100_000
        )
        self.assertEqual(facility["edges"][-1]["polyline_um"][-1]["x"], 0)

    def test_direction_edit_changes_revision_and_content_hash(self) -> None:
        forward = build_facility_from_cad_graph(_graph(direction=[0, 1]))
        reverse = build_facility_from_cad_graph(_graph(direction=[1, 0]))

        self.assertNotEqual(forward["revision_id"], reverse["revision_id"])
        self.assertNotEqual(forward["content_hash"], reverse["content_hash"])

    def test_labels_project_to_edge_interior_not_nearest_endpoint(self) -> None:
        graph = _graph()
        graph["nodes"] = [[0, 0], [100, 0], [50, 20]]
        graph["edges"].append(
            {
                "start": 2,
                "end": 1,
                "dir": [2, 1],
                "geometry": [[50, 20], [100, 0]],
            }
        )
        facility = build_facility_from_cad_graph(graph)
        stations = {station["id"]: station for station in facility["stations"]}

        self.assertEqual(stations["station-1"]["position_um"]["y"], 0)
        self.assertEqual(stations["station-1"]["position_um"]["x"], 25_000)

    def test_requires_two_station_labels_and_never_falls_back_to_sample(self) -> None:
        graph = copy.deepcopy(_graph())
        graph["metadata"]["labels"] = [
            {"text": "equipment-1", "x": 20, "y": 0, "layer": "TEXT"}
        ]
        with self.assertRaisesRegex(CadGraphFacilityError, "2개 이상"):
            build_facility_from_cad_graph(graph)


if __name__ == "__main__":
    unittest.main()
