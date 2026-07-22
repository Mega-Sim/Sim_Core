"""Tests for Graph JSON to a source-free AutoMod ``model.arc`` conversion."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from automod_pm_converter import (
    AutoModConversionError,
    render_model_amo,
    render_model_process_asy,
    render_pm_asy,
    save_automod_model,
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

    def test_model_manifest_links_pm_and_empty_process_system(self) -> None:
        manifest = render_model_amo(self.graph())
        process_system = render_model_process_asy()
        self.assertIn("MOVESYS name pm\r\n", manifest)
        self.assertIn("PROCSYS name model~\r\n", manifest)
        self.assertIn("SYSTYPE Process\r\n", process_system)
        self.assertIn("PROCDEF UserId 1\r\n", process_system)
        self.assertNotIn("PROC name", process_system)
        self.assertNotIn("#include", process_system)

    def test_creates_only_the_three_required_arc_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            generated = save_automod_model(self.graph(), Path(temporary) / "model.arc")
            names = sorted(path.name for path in generated.archive.iterdir())
            self.assertEqual(names, ["model.amo", "model~.asy", "pm.asy"])
            self.assertEqual(generated.movement_system.name, "pm.asy")
            self.assertFalse((Path(temporary) / "model.dir").exists())
            for path in generated.archive.iterdir():
                data = path.read_bytes()
                self.assertNotIn(b"\n", data.replace(b"\r\n", b""))
                data.decode("ascii")

    def test_rejects_existing_arc_with_user_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive = Path(temporary) / "model.arc"
            archive.mkdir()
            (archive / "logic.m").write_text("begin model initialization function\n")
            with self.assertRaisesRegex(AutoModConversionError, "변환기가 생성하지 않은"):
                save_automod_model(self.graph(), archive)

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
