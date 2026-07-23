from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from isaac_sim_exporter import (
    build_isaac_layout_from_graph,
    load_automod_pm_layout,
    save_isaac_package,
)


class IsaacSimExporterTests(unittest.TestCase):
    def test_graph_to_isaac_layout_uses_meters_and_direction(self) -> None:
        graph = {
            "metadata": {
                "coordinate_unit": "millimeter",
                "labels": [{"text": "ST01", "x": 500, "y": 0}],
            },
            "nodes": [[0, 0], [1000, 0], [1000, 1000]],
            "edges": [
                {"start": 0, "end": 1, "dir": [0, 1], "geometry_type": "line"},
                {"start": 1, "end": 2, "dir": [2, 1], "geometry_type": "line"},
            ],
        }

        layout = build_isaac_layout_from_graph(graph)

        self.assertEqual([0.0, 0.0, 0.0], layout["nodes"][0]["position_m"])
        self.assertEqual([1.0, 0.0, 0.0], layout["nodes"][1]["position_m"])
        self.assertEqual("node_000002", layout["edges"][1]["from_node_id"])
        self.assertEqual("node_000001", layout["edges"][1]["to_node_id"])
        self.assertEqual([0.5, 0.0, 0.0], layout["stations"][0]["position_m"])

    def test_pm_asy_to_layout_preserves_arc_and_station(self) -> None:
        pm_text = """\
GPATHTYPE name GuidePath one normal
GPATH name path1 type GuidePath begx 0 begy 0 endx 1000 endy 0
GPATH name path2 type GuidePath begx 1000 begy 0 cenx 1000 ceny 450 angle 900
CPOINT name cp_A001 type DefaultControlPoint at path1 500
CPOINT name cp_out_1 type high_out at path2 100
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            pm_path = Path(temp_dir) / "pm.asy"
            pm_path.write_text(pm_text, encoding="utf-8")
            layout = load_automod_pm_layout(pm_path)

        self.assertEqual(2, len(layout["edges"]))
        self.assertEqual("arc", layout["source_paths"][1]["geometry_type"])
        self.assertEqual("cp_A001", layout["stations"][0]["id"])
        self.assertEqual("cp_out_1", layout["routing_control_points"][0]["id"])

    def test_package_contains_json_usda_and_loader(self) -> None:
        graph = {
            "metadata": {"coordinate_unit": "meter"},
            "nodes": [[0, 0], [1, 0]],
            "edges": [{"start": 0, "end": 1, "dir": [0, 1]}],
        }
        layout = build_isaac_layout_from_graph(graph)

        with tempfile.TemporaryDirectory() as temp_dir:
            generated = save_isaac_package(layout, Path(temp_dir) / "IsaacModel")
            for path in generated.values():
                self.assertTrue(path.is_file())
            stage = generated["stage"].read_text(encoding="utf-8")

        self.assertIn('def Scope "GuidePaths"', stage)
        self.assertIn('def Xform "World"', stage)


if __name__ == "__main__":
    unittest.main()
