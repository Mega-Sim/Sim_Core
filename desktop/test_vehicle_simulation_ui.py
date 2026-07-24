"""Offscreen Qt smoke test for the 2D Vehicle Simulation controls and clock."""
from __future__ import annotations

import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

import app
import app_base as base
from vehicle_simulation_patch import VehicleSimulationDialog


def _facility() -> dict:
    return {
        "revision_id": "vehicle-ui-test-r1",
        "source_artifacts": [],
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


def _scenario() -> dict:
    return {
        "jobs": [
            {
                "id": "JOB-UI-1",
                "pickup_station_id": "ST-B",
                "dropoff_station_id": "ST-C",
                "release_time_us": 0,
            }
        ]
    }


class VehicleSimulationUiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.application = QApplication.instance() or QApplication([])

    def test_controls_vehicle_item_and_millisecond_clock(self) -> None:
        window = app.MainWindow()
        self.assertTrue(hasattr(window, "vehicle_simulation_button"))
        self.assertTrue(hasattr(window, "vehicle_simulation_count"))

        dialog = VehicleSimulationDialog(
            window,
            base,
            _facility(),
            _scenario(),
            None,
            1,
        )
        self.application.processEvents()
        dialog.timer.stop()
        self.assertEqual(len(dialog._vehicle_items), 1)

        dialog._engine.tick(1_234_000)
        dialog._render()
        self.assertEqual(dialog.time_label.text(), "00:00:01.234")
        self.assertIn("Job 0/1", dialog.metrics_label.text())

        dialog.close()
        window.close()
        self.application.processEvents()


if __name__ == "__main__":
    unittest.main()
