"""Drawing1.dxf integration smoke test for the 2D vehicle simulation."""
from __future__ import annotations

import math
import unittest
from pathlib import Path

from cad_graph_facility import build_facility_from_cad_graph
from cad_station_label_compat import install_cad_station_label_compat
from dxf_graph_converter import convert_dxf_to_graph
from random_flow_analysis import generate_random_workload
from vehicle_simulation_engine import VisualVehicleSimulation


install_cad_station_label_compat()


def _distance_to_segment(
    point: tuple[float, float],
    first: tuple[float, float],
    second: tuple[float, float],
) -> float:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    length_squared = dx * dx + dy * dy
    if length_squared <= 1e-12:
        return math.dist(point, first)
    ratio = (
        (point[0] - first[0]) * dx + (point[1] - first[1]) * dy
    ) / length_squared
    ratio = max(0.0, min(1.0, ratio))
    projected = (first[0] + dx * ratio, first[1] + dy * ratio)
    return math.dist(point, projected)


class Drawing1VehicleSimulationTests(unittest.TestCase):
    def test_drawing1_random_job_vehicle_stays_on_centreline(self) -> None:
        drawing = Path(__file__).resolve().parents[1] / "development_src" / "Drawing1.dxf"
        self.assertTrue(drawing.is_file(), f"Drawing1.dxf not found: {drawing}")

        graph = convert_dxf_to_graph(
            drawing,
            arc_segments=10,
            coordinate_precision=3,
            coordinate_unit="millimeter",
        )
        facility = build_facility_from_cad_graph(graph)
        workload = generate_random_workload(
            facility,
            6,
            20_260_724,
            load_duration_us=10_000_000,
            unload_duration_us=10_000_000,
        )
        engine = VisualVehicleSimulation(
            facility,
            workload.scenario,
            vehicle_count=min(6, len(facility["stations"])),
        )
        edges = {str(edge["id"]): edge for edge in facility["edges"]}

        moving_samples = 0
        for _ in range(400):
            engine.tick(50_000)
            for snapshot in engine.vehicle_snapshots():
                edge_id = str(snapshot["edge_id"])
                if not edge_id or str(snapshot["state"]) not in {
                    "TO_PICKUP",
                    "TO_SETDOWN",
                }:
                    continue
                polyline = [
                    (float(point["x"]), float(point["y"]))
                    for point in edges[edge_id]["polyline_um"]
                ]
                separation = min(
                    _distance_to_segment(
                        (float(snapshot["x_um"]), float(snapshot["y_um"])),
                        first,
                        second,
                    )
                    for first, second in zip(polyline, polyline[1:])
                )
                self.assertLessEqual(separation, 1e-6)
                moving_samples += 1
            if moving_samples >= 20:
                break

        self.assertGreater(moving_samples, 0)
        self.assertGreaterEqual(len(facility["stations"]), 2)


if __name__ == "__main__":
    unittest.main()
