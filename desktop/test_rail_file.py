"""Tests for the lightweight SemiLA Rail reader."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from rail_file import load_rail_graph


class RailFileTest(unittest.TestCase):
    def test_line_curve_topology_and_labels_are_loaded(self) -> None:
        fixture = "\n".join(
            [
                "RAILDATA",
                "LINE\t10\tLINE\t0\t0\t10\t0\t128\t128\t128",
                "LINE\t10\tARROW\t5\t0\t4\t1\t128\t128\t128",
                "CURVE\t11\tCURVE\t10\t0\t20\t0\t20\t10\t10\t10\t90\t128\t128\t128",
                "NODE\t1\t0\t0",
                "NODE\t2\t10\t0",
                "NODE\t3\t20\t10",
                "LINK\t10\tLINE\t1\t2\t1.0\t1.0",
                "LINK\t11\tCURVE\t2\t3\t1.0\t1.0",
                "RAILLIST\t10\tLINE\t1\t2\t0\t0\t0\t0\t0\t10",
                "RAILLIST\t11\tCURVE\t2\t3\t0\t0\t0\t0\t0\t15.7",
                "TEXT\tEQ-01\tSTATION\t10\t0",
                "SCALE\t0\t20\t0\t10",
                "",
            ]
        )
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "fixture.rail"
            path.write_text(fixture, encoding="utf-8")
            graph = load_rail_graph(path)

        statistics = graph["metadata"]["statistics"]
        self.assertEqual(statistics["node_count"], 3)
        self.assertEqual(statistics["edge_count"], 2)
        self.assertEqual(statistics["line_count"], 1)
        self.assertEqual(statistics["curve_count"], 1)
        self.assertEqual(graph["edges"][0]["dir"], [0, 1])
        self.assertEqual(graph["edges"][1]["geometry"][0], [10.0, 0.0])
        self.assertEqual(graph["edges"][1]["geometry"][-1], [20.0, 10.0])
        self.assertEqual(graph["metadata"]["labels"][0]["text"], "EQ-01")

    def test_linear_analyzer_reference_rail_contract(self) -> None:
        source = (
            Path(__file__).resolve().parents[1]
            / "development_src"
            / "Linear_Analyzer"
            / "SemiLA"
            / "P2L7F.rail"
        )
        self.assertTrue(source.is_file(), source)
        graph = load_rail_graph(source)
        statistics = graph["metadata"]["statistics"]
        self.assertEqual(statistics["node_count"], 8272)
        self.assertEqual(statistics["edge_count"], 9580)
        self.assertEqual(statistics["line_count"], 6505)
        self.assertEqual(statistics["curve_count"], 3075)
        self.assertEqual(statistics["component_count"], 1)


if __name__ == "__main__":
    unittest.main()
