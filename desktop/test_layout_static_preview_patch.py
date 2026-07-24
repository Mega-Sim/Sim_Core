"""Regression tests for the shared Conversion Preview static-analysis renderer."""
from __future__ import annotations

import unittest

from layout_static_preview_patch import graph_edge_moves


class LayoutStaticPreviewPatchTest(unittest.TestCase):
    def test_split_facility_edges_use_max_load_for_original_graph_edge(self) -> None:
        facility = {
            "edges": [
                {
                    "id": "E-00003-001",
                    "source_identities": [
                        {"external_id": "graph-edge:3:part:1"}
                    ],
                },
                {
                    "id": "E-00003-002",
                    "source_identities": [
                        {"external_id": "graph-edge:3:part:2"}
                    ],
                },
                {
                    "id": "E-00009",
                    "source_identities": [{"external_id": "graph-edge:9:part:1"}],
                },
            ]
        }
        analysis = {
            "edge_flows": [
                {"edge_id": "E-00003-001", "expected_moves_per_hour": 20},
                {"edge_id": "E-00003-002", "expected_moves_per_hour": 65},
                {"edge_id": "E-00009", "expected_moves_per_hour": 11},
            ]
        }

        self.assertEqual(graph_edge_moves(facility, analysis), {3: 65.0, 9: 11.0})

    def test_legacy_facility_edge_id_is_supported(self) -> None:
        facility = {"edges": [{"id": "E-00012-003", "source_identities": []}]}
        analysis = {
            "edge_flows": [
                {"edge_id": "E-00012-003", "expected_moves_per_hour": 7.5}
            ]
        }

        self.assertEqual(graph_edge_moves(facility, analysis), {12: 7.5})

    def test_unused_edges_do_not_create_fake_load(self) -> None:
        facility = {
            "edges": [
                {
                    "id": "E-00001",
                    "source_identities": [{"external_id": "graph-edge:1:part:1"}],
                }
            ]
        }

        self.assertEqual(graph_edge_moves(facility, {"edge_flows": []}), {1: 0.0})


if __name__ == "__main__":
    unittest.main()
