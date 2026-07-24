"""Regression tests for the deterministic centreline vehicle simulation."""
from __future__ import annotations

import unittest

from vehicle_simulation_engine import (
    VisualVehicleSimulation,
    format_simulation_time,
)


def _line_facility() -> dict:
    return {
        "revision_id": "vehicle-test-r1",
        "nodes": [
            {"id": "N-A", "position_um": {"x": 0, "y": 0, "z": 0}},
            {"id": "N-B", "position_um": {"x": 2_000_000, "y": 0, "z": 0}},
            {"id": "N-C", "position_um": {"x": 4_000_000, "y": 0, "z": 0}},
        ],
        "edges": [
            {
                "id": "E-A-B",
                "from_node_id": "N-A",
                "to_node_id": "N-B",
                "length_um": 2_000_000,
                "speed_limit_um_per_s": 2_000_000,
                "polyline_um": [
                    {"x": 0, "y": 0, "z": 0},
                    {"x": 2_000_000, "y": 0, "z": 0},
                ],
            },
            {
                "id": "E-B-C",
                "from_node_id": "N-B",
                "to_node_id": "N-C",
                "length_um": 2_000_000,
                "speed_limit_um_per_s": 2_000_000,
                "polyline_um": [
                    {"x": 2_000_000, "y": 0, "z": 0},
                    {"x": 4_000_000, "y": 0, "z": 0},
                ],
            },
        ],
        "stations": [
            {
                "id": "ST-A",
                "attachment_node_id": "N-A",
                "position_um": {"x": 0, "y": 0, "z": 0},
            },
            {
                "id": "ST-B",
                "attachment_node_id": "N-B",
                "position_um": {"x": 2_000_000, "y": 0, "z": 0},
            },
            {
                "id": "ST-C",
                "attachment_node_id": "N-C",
                "position_um": {"x": 4_000_000, "y": 0, "z": 0},
            },
        ],
    }


class VehicleSimulationTests(unittest.TestCase):
    def test_clock_is_displayed_to_milliseconds(self) -> None:
        self.assertEqual(format_simulation_time(3_723_456_789), "01:02:03.456")

    def test_vehicle_moves_on_edge_centreline_and_stops_ten_seconds(self) -> None:
        scenario = {
            "jobs": [
                {
                    "id": "JOB-1",
                    "pickup_station_id": "ST-B",
                    "dropoff_station_id": "ST-C",
                    "release_time_us": 0,
                }
            ]
        }
        engine = VisualVehicleSimulation(
            _line_facility(),
            scenario,
            vehicle_count=1,
        )

        observed_states: set[str] = set()
        while not engine.is_finished and engine.time_us < 30_000_000:
            engine.tick(50_000)
            snapshot = engine.vehicle_snapshots()[0]
            observed_states.add(str(snapshot["state"]))
            self.assertAlmostEqual(float(snapshot["y_um"]), 0.0, places=6)

        self.assertTrue(engine.is_finished)
        self.assertEqual(engine.time_us, 22_000_000)
        self.assertTrue(
            {"TO_PICKUP", "LOADING", "TO_SETDOWN", "UNLOADING"}.issubset(
                observed_states
            )
        )

        event_time = {
            item["event_type"]: int(item["time_us"]) for item in engine.events
        }
        self.assertEqual(
            event_time["PICKUP_COMPLETED"] - event_time["PICKUP_STARTED"],
            10_000_000,
        )
        self.assertEqual(
            event_time["SETDOWN_COMPLETED"] - event_time["SETDOWN_STARTED"],
            10_000_000,
        )


if __name__ == "__main__":
    unittest.main()
