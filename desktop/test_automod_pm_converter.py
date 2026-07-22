"""Tests for Graph JSON to AutoMod ``pm.asy`` conversion."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from automod_pm_converter import (
    AutoModConversionError,
    render_pm_asy,
    save_pm_asy,
)


class AutoModPmConverterTest(unittest.TestCase):
    def graph(self) -> dict:
        return {
            "metadata": {"coordinate_unit": "meter"},
            "nodes": [[0, 0], [1, 0], [1, 1]],
            "edges": [
                {
                    "start": 0,
                    "end": 1,
                    "dir": [0, 1],
                    "geometry": [[0, 0], [1, 0]],
                },
                {
                    "start": 1,
                    "end": 2,
                    "dir": [2, 1],
                    "geometry": [[1, 0], [1.2, 0.5], [1, 1]],
                    "geometry_type": "ARC",
                },
            ],
        }

    def test_renders_directed_paths_control_points_and_unit_conversion(self) -> None:
        content = render_pm_asy(self.graph())
        self.assertIn("UNITS Millimeters Seconds\r\n", content)
        self.assertIn(
            "GPATH name path1 type DefaultGuidePath piece begx 0 begy 0 endx 1000 endy 0 upz 1",
            content,
        )
        self.assertIn(
            "GPATH name path2 type DefaultGuidePath piece begx 1000 begy 1000 endx 1200 endy 500 upz 1",
            content,
        )
        self.assertIn(
            "GPATH name path3 type DefaultGuidePath piece begx 1200 begy 500 endx 1000 endy 0 upz 1",
            content,
        )
        self.assertEqual(content.count("\r\nCPOINT name cp_node_"), 3)
        self.assertIn("CPOINT name cp_node_3 type DefaultControlPoint at path2 0", content)

    def test_output_is_ascii_crlf_and_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "pm.asy"
            save_pm_asy(self.graph(), path)
            first = path.read_bytes()
            save_pm_asy(self.graph(), path)
            second = path.read_bytes()
        self.assertEqual(first, second)
        self.assertNotIn(b"\n", first.replace(b"\r\n", b""))
        first.decode("ascii")

    def test_rejects_unresolved_direction(self) -> None:
        graph = self.graph()
        graph["edges"][0]["dir"] = None
        with self.assertRaisesRegex(AutoModConversionError, "진행 방향"):
            render_pm_asy(graph)

    def test_rejects_unknown_coordinate_unit(self) -> None:
        graph = self.graph()
        graph["metadata"]["coordinate_unit"] = "yard"
        with self.assertRaisesRegex(AutoModConversionError, "지원하지 않는"):
            render_pm_asy(graph)


if __name__ == "__main__":
    unittest.main()
