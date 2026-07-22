"""Collapse only DXF ARC-generated graph segments into logical curved edges."""
from __future__ import annotations

import math
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable

import ezdxf


def _round_point(point: tuple[float, float], precision: int) -> tuple[float, float]:
    def clean(value: float) -> float:
        result = round(float(value), precision)
        return 0.0 if result == 0 else result
    return clean(point[0]), clean(point[1])


def _pair_key(a: tuple[float, float], b: tuple[float, float]) -> tuple[tuple[float, float], tuple[float, float]]:
    return tuple(sorted((a, b)))  # type: ignore[return-value]


def _arc_points(entity: Any, steps: int) -> list[tuple[float, float]]:
    center = entity.dxf.center
    radius = float(entity.dxf.radius)
    start_angle = float(entity.dxf.start_angle)
    end_angle = float(entity.dxf.end_angle)
    sweep_degrees = end_angle - start_angle
    if sweep_degrees <= 0:
        sweep_degrees += 360.0
    sweep = math.radians(sweep_degrees)
    start = math.radians(start_angle)
    return [
        (
            float(center.x) + radius * math.cos(start + sweep * index / steps),
            float(center.y) + radius * math.sin(start + sweep * index / steps),
        )
        for index in range(steps + 1)
    ]


def _arc_segment_groups(
    filename: str | Path,
    *,
    layers: Iterable[str] | None,
    arc_segments: int,
    precision: int,
) -> dict[tuple[tuple[float, float], tuple[float, float]], int]:
    document = ezdxf.readfile(Path(filename))
    requested = {str(layer).strip().casefold() for layer in (layers or []) if str(layer).strip()} or None
    groups: dict[tuple[tuple[float, float], tuple[float, float]], int] = {}
    group_id = 0
    for entity in document.modelspace():
        if entity.dxftype() != "ARC":
            continue
        if requested is not None and str(entity.dxf.layer).casefold() not in requested:
            continue
        points = [_round_point(point, precision) for point in _arc_points(entity, arc_segments)]
        for first, second in zip(points, points[1:]):
            groups[_pair_key(first, second)] = group_id
        group_id += 1
    return groups


def consolidate_arc_edges(
    graph: Dict[str, Any],
    filename: str | Path,
    *,
    layers: Iterable[str] | None = None,
    arc_segments: int = 10,
    coordinate_precision: int = 3,
) -> Dict[str, Any]:
    """Merge only segments that map back to the same source DXF ARC entity.

    LINE edges are never merged. ARC chains are also split at graph junctions,
    so a branch/merge connection remains an explicit topology boundary.
    """
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    if not nodes or not edges:
        return graph

    try:
        arc_groups = _arc_segment_groups(
            filename,
            layers=layers,
            arc_segments=arc_segments,
            precision=coordinate_precision,
        )
    except (OSError, ezdxf.DXFError):
        return graph
    if not arc_groups:
        return graph

    edge_group: dict[int, int] = {}
    full_incident: defaultdict[int, list[int]] = defaultdict(list)
    for edge_id, edge in enumerate(edges):
        start = int(edge["start"])
        end = int(edge["end"])
        full_incident[start].append(edge_id)
        full_incident[end].append(edge_id)
        a = _round_point((float(nodes[start][0]), float(nodes[start][1])), coordinate_precision)
        b = _round_point((float(nodes[end][0]), float(nodes[end][1])), coordinate_precision)
        group = arc_groups.get(_pair_key(a, b))
        if group is not None:
            edge_group[edge_id] = group

    grouped: defaultdict[int, list[int]] = defaultdict(list)
    for edge_id, group in edge_group.items():
        grouped[group].append(edge_id)

    replacement: dict[int, dict[str, Any]] = {}
    removed: set[int] = set()
    merged_segment_count = 0
    curve_count = 0

    for group_id, group_edges in grouped.items():
        group_incident: defaultdict[int, list[int]] = defaultdict(list)
        for edge_id in group_edges:
            edge = edges[edge_id]
            group_incident[int(edge["start"])].append(edge_id)
            group_incident[int(edge["end"])].append(edge_id)

        visited: set[int] = set()
        starts = [node for node, linked in group_incident.items() if len(linked) != 2 or len(full_incident[node]) != 2]
        if not starts and group_incident:
            starts = [next(iter(group_incident))]

        def other(edge_id: int, node_id: int) -> int:
            edge = edges[edge_id]
            return int(edge["end"]) if int(edge["start"]) == node_id else int(edge["start"])

        for start_node in starts:
            for first_edge in group_incident[start_node]:
                if first_edge in visited:
                    continue
                chain = [first_edge]
                path = [start_node, other(first_edge, start_node)]
                visited.add(first_edge)
                current = path[-1]
                while len(group_incident[current]) == 2 and len(full_incident[current]) == 2:
                    candidates = [edge_id for edge_id in group_incident[current] if edge_id not in visited]
                    if not candidates:
                        break
                    next_edge = candidates[0]
                    visited.add(next_edge)
                    chain.append(next_edge)
                    current = other(next_edge, current)
                    path.append(current)
                if len(chain) < 2:
                    continue

                forward = reverse = 0
                for index, edge_id in enumerate(chain):
                    direction = edges[edge_id].get("dir")
                    if direction == [path[index], path[index + 1]]:
                        forward += 1
                    elif direction == [path[index + 1], path[index]]:
                        reverse += 1
                oriented = list(reversed(path)) if reverse > forward else path
                first = chain[0]
                replacement[first] = {
                    "start": oriented[0],
                    "end": oriented[-1],
                    "dir": [oriented[0], oriented[-1]],
                    "geometry": [nodes[node_id] for node_id in oriented],
                    "geometry_type": "ARC",
                    "source_edge_count": len(chain),
                    "source_arc_group": group_id,
                }
                removed.update(chain[1:])
                merged_segment_count += len(chain) - 1
                curve_count += 1

    if not removed:
        return graph

    merged_edges = [replacement.get(edge_id, dict(edge)) for edge_id, edge in enumerate(edges) if edge_id not in removed]
    used_nodes: set[int] = set()
    for edge in merged_edges:
        used_nodes.update((int(edge["start"]), int(edge["end"])))
    ordered = sorted(used_nodes)
    remap = {old: new for new, old in enumerate(ordered)}
    compact_nodes = [nodes[old] for old in ordered]
    for edge in merged_edges:
        old_start, old_end = int(edge["start"]), int(edge["end"])
        direction = edge.get("dir")
        edge["start"], edge["end"] = remap[old_start], remap[old_end]
        if isinstance(direction, list) and len(direction) == 2:
            edge["dir"] = [remap[int(direction[0])], remap[int(direction[1])]]

    graph["nodes"] = compact_nodes
    graph["edges"] = merged_edges
    statistics = graph.setdefault("metadata", {}).setdefault("statistics", {})
    statistics["node_count"] = len(compact_nodes)
    statistics["edge_count"] = len(merged_edges)
    statistics["merged_curve_segment_count"] = merged_segment_count
    statistics["curve_chain_count"] = curve_count
    statistics["unresolved_direction_count"] = sum(1 for edge in merged_edges if edge.get("dir") is None)
    return graph
