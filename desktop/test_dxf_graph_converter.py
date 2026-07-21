"""Tests for the standalone DXF-to-graph adapter."""

from __future__ import annotations

import json
import math
import tempfile
import unittest
from pathlib import Path

import ezdxf

from dxf_graph_converter import (
    DxfConversionError,
    convert_dxf_to_graph,
    load_dxf_lines,
    save_graph,
)


class DxfGraphConverterTest(unittest.TestCase):
    def make_layout(self, directory: Path) -> Path:
        path = directory / "fab-layout.dxf"
        document = ezdxf.new("R2013")
        document.layers.add("OHT_RAIL_CENTER")
        document.layers.add("OTHER")
        model = document.modelspace()
        attributes = {"layer": "OHT_RAIL_CENTER"}
        model.add_line((0, 0), (10, 0), dxfattribs=attributes)
        model.add_line((10, 0), (20, 0), dxfattribs=attributes)
        model.add_arc(
            center=(20, 10),
            radius=10,
            start_angle=270,
            end_angle=360,
            dxfattribs=attributes,
        )
        model.add_line((100, 0), (110, 0), dxfattribs=attributes)
        model.add_line((1000, 0), (1010, 0), dxfattribs={"layer": "OTHER"})
        model.add_text("EQ-01", dxfattribs={"layer": "OTHER"})
        document.saveas(path)
        return path

    def test_filtered_conversion_directs_every_component(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = self.make_layout(Path(temporary))
            graph = convert_dxf_to_graph(
                source,
                layers=["oht_rail_center"],
                arc_segments=10,
                coordinate_precision=3,
            )

        statistics = graph["metadata"]["statistics"]
        self.assertEqual(statistics["node_count"], 15)
        self.assertEqual(statistics["edge_count"], 13)
        self.assertEqual(statistics["component_count"], 2)
        self.assertEqual(statistics["unresolved_direction_count"], 0)
        self.assertEqual(graph["metadata"]["selected_layers"], ["OHT_RAIL_CENTER"])
        self.assertTrue(all(edge["dir"] is not None for edge in graph["edges"]))
        self.assertEqual(graph["metadata"]["labels"][0]["text"], "EQ-01")

    def test_degree_two_midpoints_keep_one_in_and_one_out(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "opposing-thread-layout.dxf"
            document = ezdxf.new("R2013")
            model = document.modelspace()
            model.add_line((10, 0), (20, 0))
            model.add_line((0, 0), (10, 0))
            document.saveas(path)
            graph = convert_dxf_to_graph(path)

        in_degree = [0 for _ in graph["nodes"]]
        out_degree = [0 for _ in graph["nodes"]]
        undirected_degree = [0 for _ in graph["nodes"]]
        for edge in graph["edges"]:
            direction_start, direction_end = edge["dir"]
            out_degree[direction_start] += 1
            in_degree[direction_end] += 1
            undirected_degree[edge["start"]] += 1
            undirected_degree[edge["end"]] += 1

        for node, degree in enumerate(undirected_degree):
            if degree == 2:
                self.assertEqual(in_degree[node], 1)
                self.assertEqual(out_degree[node], 1)

    def test_touching_endpoint_splits_mainline_into_junction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "branch-layout.dxf"
            document = ezdxf.new("R2013")
            model = document.modelspace()
            model.add_line((0, 0), (20, 0))
            model.add_line((10, 10), (10, 0))
            document.saveas(path)
            graph = convert_dxf_to_graph(path)

        junctions = []
        incident = [[] for _ in graph["nodes"]]
        for index, edge in enumerate(graph["edges"]):
            incident[edge["start"]].append(index)
            incident[edge["end"]].append(index)
        for node, linked_edges in enumerate(incident):
            if graph["nodes"][node] == [10.0, 0.0]:
                junctions.append((node, linked_edges))

        self.assertEqual(len(junctions), 1)
        junction, linked_edges = junctions[0]
        self.assertEqual(len(linked_edges), 3)
        outgoing = sum(1 for index in linked_edges if graph["edges"][index]["dir"][0] == junction)
        incoming = sum(1 for index in linked_edges if graph["edges"][index]["dir"][1] == junction)
        self.assertGreater(outgoing, 0)
        self.assertGreater(incoming, 0)

    def test_forward_branch_continues_from_one_seed_thread(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "forward-branch-layout.dxf"
            document = ezdxf.new("R2013")
            model = document.modelspace()
            model.add_line((0, 0), (10, 0))
            model.add_line((10, 0), (20, 0))
            model.add_line((10, 0), (20, 5))
            document.saveas(path)
            graph = convert_dxf_to_graph(path)

        junction = graph["nodes"].index([10.0, 0.0])
        outgoing = [
            edge
            for edge in graph["edges"]
            if edge["dir"][0] == junction
        ]
        self.assertEqual(graph["metadata"]["statistics"]["direction_thread_count"], 1)
        self.assertEqual(len(outgoing), 2)

    def test_missing_layer_reports_available_geometry_layers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source = self.make_layout(Path(temporary))
            with self.assertRaisesRegex(DxfConversionError, "OHT_RAIL_CENTER"):
                convert_dxf_to_graph(source, layers=["DOES_NOT_EXIST"])

    def test_wrapped_arc_uses_dxf_counterclockwise_sweep(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "wrapped-arc.dxf"
            document = ezdxf.new("R2013")
            document.modelspace().add_arc(
                center=(0, 0),
                radius=10,
                start_angle=350,
                end_angle=10,
            )
            document.saveas(path)
            segments = load_dxf_lines(path, arc_segments=10)

        approximated_length = sum(math.dist(start, end) for start, end in segments)
        self.assertLess(approximated_length, 5)

    def test_saved_json_is_deterministic_and_compatible(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            source = self.make_layout(directory)
            graph = convert_dxf_to_graph(source, arc_segments=4)
            first = save_graph(graph, directory / "first.json")
            second = save_graph(graph, directory / "second.json")
            self.assertEqual(first.read_bytes(), second.read_bytes())
            payload = json.loads(first.read_text(encoding="utf-8"))

        self.assertIsInstance(payload["nodes"][0], list)
        self.assertEqual(set(payload["edges"][0]), {"start", "end", "dir", "geometry"})
        self.assertEqual(
            payload["metadata"]["converter"]["reference_repository"],
            "Mega-Sim/Graph_Maker_CAD-dxf-_to_json",
        )


if __name__ == "__main__":
    unittest.main()
