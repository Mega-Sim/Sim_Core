"""DXF rail geometry to directed graph JSON converter.

The topology and direction-threading steps are based on the standalone
``Graph_Maker_CAD-dxf-_to_json`` prototype.  This adapter keeps its compatible
``nodes``/``edges`` payload while adding deterministic conversion metadata,
layer filtering, validation, and support for every disconnected component.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import ezdxf


CONVERTER_NAME = "sim-core-dxf-graph"
CONVERTER_VERSION = "2.0.0"
SUPPORTED_ENTITY_TYPES = ("LINE", "ARC")
MIN_CONTINUATION_DOT = -0.15

Point = tuple[float, float]
Segment = tuple[Point, Point]


class DxfConversionError(ValueError):
    """Raised when a DXF cannot produce a usable rail graph."""


@dataclass(frozen=True)
class DxfGeometry:
    """One logical DXF rail entity.

    ARC display points are deliberately kept inside one logical geometry.  The
    previous pipeline expanded every ARC into topology edges and later opened
    the DXF a second time to merge those edges again.  Keeping the source
    entity intact removes both the temporary nodes and the second file parse.
    """

    geometry_type: str
    start: Point
    end: Point
    points: tuple[Point, ...]
    center: Point | None = None
    sweep_degrees: float | None = None


@dataclass(frozen=True)
class DxfLoadResult:
    geometries: list[DxfGeometry]
    selected_layers: list[str]
    available_geometry_layers: list[str]
    entity_counts: dict[str, int]
    ignored_entity_counts: dict[str, int]
    labels: list[dict[str, Any]]

    @property
    def segments(self) -> list[Segment]:
        """Compatibility view used by the standalone segment-level tests/API."""

        return [
            (first, second)
            for geometry in self.geometries
            for first, second in zip(geometry.points, geometry.points[1:])
        ]


def _vector(start: Point, end: Point) -> Point:
    return end[0] - start[0], end[1] - start[1]


def _sign(value: float) -> int:
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def _normalize(vector: Point) -> Point:
    magnitude = math.hypot(vector[0], vector[1])
    if magnitude == 0:
        return 0.0, 0.0
    return vector[0] / magnitude, vector[1] / magnitude


def _dot(left: Point, right: Point) -> float:
    return left[0] * right[0] + left[1] * right[1]


def _distance(left: Point, right: Point) -> float:
    return math.hypot(left[0] - right[0], left[1] - right[1])


def _point_on_segment_parameter(
    point: Point,
    start: Point,
    end: Point,
    *,
    tolerance: float,
) -> float | None:
    vector = _vector(start, end)
    length_squared = vector[0] * vector[0] + vector[1] * vector[1]
    if length_squared == 0:
        return None
    offset = _vector(start, point)
    parameter = _dot(offset, vector) / length_squared
    if parameter <= tolerance or parameter >= 1.0 - tolerance:
        return None
    projection = (
        start[0] + vector[0] * parameter,
        start[1] + vector[1] * parameter,
    )
    if _distance(point, projection) > tolerance:
        return None
    return parameter


def _split_segments_at_touching_endpoints(
    segments: Sequence[Segment],
    *,
    tolerance: float,
    extra_endpoints: Iterable[Point] = (),
) -> list[Segment]:
    """Split a segment when another segment endpoint lies on its interior.

    CAD rail branches are often drawn as a connector endpoint touching the
    middle of a long LINE instead of splitting that LINE entity.  Without this
    normalization the graph has no junction node, so each side can get an
    independent direction and appear as an impossible dead-end.
    """

    # The former implementation compared every segment with every endpoint.
    # A production FAB drawing can contain tens of thousands of ARC-generated
    # segments, turning this stage into billions of geometric tests.  Keep the
    # exact same point-on-segment test, but use two sorted spatial indexes to
    # reduce each segment to endpoints inside its bounding box.
    endpoints = list(
        dict.fromkeys(
            [point for segment in segments for point in segment]
            + list(extra_endpoints)
        )
    )
    endpoints_by_x = sorted(
        range(len(endpoints)),
        key=lambda index: (endpoints[index][0], endpoints[index][1]),
    )
    endpoints_by_y = sorted(
        range(len(endpoints)),
        key=lambda index: (endpoints[index][1], endpoints[index][0]),
    )
    x_values = [endpoints[index][0] for index in endpoints_by_x]
    y_values = [endpoints[index][1] for index in endpoints_by_y]

    split_segments: list[Segment] = []
    for start, end in segments:
        cuts: list[tuple[float, Point]] = [(0.0, start), (1.0, end)]
        min_x = min(start[0], end[0]) - tolerance
        max_x = max(start[0], end[0]) + tolerance
        min_y = min(start[1], end[1]) - tolerance
        max_y = max(start[1], end[1]) + tolerance

        x_first = bisect_left(x_values, min_x)
        x_last = bisect_right(x_values, max_x)
        y_first = bisect_left(y_values, min_y)
        y_last = bisect_right(y_values, max_y)

        # Query the axis with fewer candidates, then apply the other bounding
        # coordinate before the more expensive projection/distance test.  The
        # final index sort preserves the original endpoint encounter order.
        if x_last - x_first <= y_last - y_first:
            candidate_indexes = endpoints_by_x[x_first:x_last]
        else:
            candidate_indexes = endpoints_by_y[y_first:y_last]

        for endpoint_index in sorted(candidate_indexes):
            point = endpoints[endpoint_index]
            if not (min_x <= point[0] <= max_x and min_y <= point[1] <= max_y):
                continue
            parameter = _point_on_segment_parameter(
                point, start, end, tolerance=tolerance
            )
            if parameter is not None:
                cuts.append((parameter, point))

        cuts.sort(key=lambda item: item[0])
        deduplicated: list[tuple[float, Point]] = []
        for parameter, point in cuts:
            if deduplicated and abs(parameter - deduplicated[-1][0]) <= tolerance:
                continue
            deduplicated.append((parameter, point))

        for (_, first), (_, second) in zip(deduplicated, deduplicated[1:]):
            if _distance(first, second) > tolerance:
                split_segments.append((first, second))

    return split_segments


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _normalized_layers(layers: Iterable[str] | None) -> set[str] | None:
    if layers is None:
        return None
    normalized = {layer.strip().casefold() for layer in layers if layer.strip()}
    return normalized or None


def _arc_points(entity: Any, steps: int) -> list[Point]:
    center = entity.dxf.center
    radius = float(entity.dxf.radius)
    start_angle = float(entity.dxf.start_angle)
    end_angle = float(entity.dxf.end_angle)
    sweep_degrees = end_angle - start_angle
    if sweep_degrees <= 0:
        sweep_degrees += 360.0
    sweep = math.radians(sweep_degrees)
    start_radians = math.radians(start_angle)
    return [
        (
            float(center.x) + radius * math.cos(start_radians + sweep * index / steps),
            float(center.y) + radius * math.sin(start_radians + sweep * index / steps),
        )
        for index in range(steps + 1)
    ]


def inspect_geometry_layers(filename: str | Path) -> list[str]:
    """Return sorted DXF layers containing LINE or ARC entities."""

    path = Path(filename)
    try:
        document = ezdxf.readfile(path)
    except (OSError, ezdxf.DXFError) as error:
        raise DxfConversionError(f"DXF 파일을 읽을 수 없습니다: {error}") from error
    return sorted(
        {
            str(entity.dxf.layer)
            for entity in document.modelspace()
            if entity.dxftype() in SUPPORTED_ENTITY_TYPES
        },
        key=str.casefold,
    )


def load_dxf_geometry(
    filename: str | Path,
    *,
    layers: Iterable[str] | None = None,
    arc_segments: int = 10,
) -> DxfLoadResult:
    """Read LINE/ARC geometry using the reference converter's segment model."""

    if arc_segments < 1:
        raise DxfConversionError("원호 분할 수는 1 이상이어야 합니다.")

    path = Path(filename)
    try:
        document = ezdxf.readfile(path)
    except (OSError, ezdxf.DXFError) as error:
        raise DxfConversionError(f"DXF 파일을 읽을 수 없습니다: {error}") from error

    requested_layers = _normalized_layers(layers)
    geometries: list[DxfGeometry] = []
    labels: list[dict[str, Any]] = []
    entity_counts: Counter[str] = Counter()
    ignored_counts: Counter[str] = Counter()
    available_layers: set[str] = set()
    selected_layers: set[str] = set()

    for entity in document.modelspace():
        entity_type = entity.dxftype()
        layer = str(entity.dxf.layer)
        if entity_type in SUPPORTED_ENTITY_TYPES:
            available_layers.add(layer)
        if entity_type in {"TEXT", "MTEXT"}:
            ignored_counts[entity_type] += 1
            try:
                insert = entity.dxf.insert
                text = entity.plain_text() if entity_type == "MTEXT" else entity.dxf.text
            except (AttributeError, ValueError):
                continue
            labels.append(
                {
                    "text": str(text).strip(),
                    "x": float(insert.x),
                    "y": float(insert.y),
                    "layer": layer,
                }
            )
            continue
        if entity_type not in SUPPORTED_ENTITY_TYPES:
            ignored_counts[entity_type] += 1
            continue
        if requested_layers is not None and layer.casefold() not in requested_layers:
            continue

        selected_layers.add(layer)
        entity_counts[entity_type] += 1
        if entity_type == "LINE":
            start = entity.dxf.start
            end = entity.dxf.end
            start_point = float(start.x), float(start.y)
            end_point = float(end.x), float(end.y)
            geometries.append(
                DxfGeometry(
                    geometry_type="LINE",
                    start=start_point,
                    end=end_point,
                    points=(start_point, end_point),
                )
            )
        else:
            points = tuple(_arc_points(entity, arc_segments))
            center = entity.dxf.center
            start_angle = float(entity.dxf.start_angle)
            end_angle = float(entity.dxf.end_angle)
            sweep_degrees = end_angle - start_angle
            if sweep_degrees <= 0:
                sweep_degrees += 360.0
            geometries.append(
                DxfGeometry(
                    geometry_type="ARC",
                    start=points[0],
                    end=points[-1],
                    points=points,
                    center=(float(center.x), float(center.y)),
                    sweep_degrees=sweep_degrees,
                )
            )

    if not geometries:
        available = ", ".join(sorted(available_layers, key=str.casefold)) or "없음"
        requested = ", ".join(layers or []) or "전체"
        raise DxfConversionError(
            f"선택한 Rail Layer({requested})에서 LINE/ARC를 찾지 못했습니다. "
            f"사용 가능한 geometry Layer: {available}"
        )

    return DxfLoadResult(
        geometries=geometries,
        selected_layers=sorted(selected_layers, key=str.casefold),
        available_geometry_layers=sorted(available_layers, key=str.casefold),
        entity_counts=dict(sorted(entity_counts.items())),
        ignored_entity_counts=dict(sorted(ignored_counts.items())),
        labels=[label for label in labels if label["text"]],
    )


def load_dxf_lines(
    filename: str | Path,
    *,
    layers: Iterable[str] | None = None,
    arc_segments: int = 10,
) -> list[Segment]:
    """Compatibility helper matching the reference converter's first stage."""

    return load_dxf_geometry(
        filename, layers=layers, arc_segments=arc_segments
    ).segments


def build_nodes_edges(
    segments: Sequence[Segment],
    *,
    coordinate_precision: int = 3,
) -> tuple[list[list[float]], list[dict[str, Any]]]:
    """Deduplicate rounded endpoints and create undirected source edges."""

    if coordinate_precision < 0 or coordinate_precision > 9:
        raise DxfConversionError("좌표 반올림 자릿수는 0~9 범위여야 합니다.")

    node_map: dict[Point, int] = {}
    nodes: list[list[float]] = []
    edges: list[dict[str, Any]] = []

    def rounded(value: float) -> float:
        result = round(float(value), coordinate_precision)
        return 0.0 if result == 0 else result

    def get_node(point: Point) -> int:
        key = rounded(point[0]), rounded(point[1])
        if key not in node_map:
            node_map[key] = len(nodes)
            nodes.append([key[0], key[1]])
        return node_map[key]

    snap_tolerance = 10 ** (-coordinate_precision)
    normalized_segments = _split_segments_at_touching_endpoints(
        segments, tolerance=snap_tolerance
    )

    for start, end in normalized_segments:
        start_node = get_node(start)
        end_node = get_node(end)
        if start_node == end_node:
            continue
        edges.append(
            {
                "start": start_node,
                "end": end_node,
                "dir": None,
                "geometry": [nodes[start_node], nodes[end_node]],
            }
        )

    if not edges:
        raise DxfConversionError("좌표 반올림 후 유효한 Edge가 남지 않았습니다.")
    return nodes, edges


def build_rail_nodes_edges(
    geometries: Sequence[DxfGeometry],
    *,
    coordinate_precision: int = 3,
) -> tuple[list[list[float]], list[dict[str, Any]]]:
    """Build topology directly from logical LINE/ARC entities.

    LINE entities are still split when another entity endpoint touches their
    interior, because that point is a real branch/merge node.  ARC sampling is
    retained only as display geometry; the samples never become graph nodes or
    temporary edges.
    """

    if coordinate_precision < 0 or coordinate_precision > 9:
        raise DxfConversionError("좌표 반올림 자릿수는 0~9 범위여야 합니다.")

    def clean(value: float) -> float:
        result = round(float(value), coordinate_precision)
        return 0.0 if result == 0 else result

    node_map: dict[Point, int] = {}
    nodes: list[list[float]] = []
    edges: list[dict[str, Any]] = []

    def get_node(point: Point) -> int:
        key = clean(point[0]), clean(point[1])
        node_id = node_map.get(key)
        if node_id is None:
            node_id = len(nodes)
            node_map[key] = node_id
            nodes.append([key[0], key[1]])
        return node_id

    line_segments = [
        (geometry.start, geometry.end)
        for geometry in geometries
        if geometry.geometry_type == "LINE"
    ]
    all_entity_endpoints = [
        point
        for geometry in geometries
        for point in (geometry.start, geometry.end)
    ]
    snap_tolerance = 10 ** (-coordinate_precision)
    normalized_lines = _split_segments_at_touching_endpoints(
        line_segments,
        tolerance=snap_tolerance,
        extra_endpoints=all_entity_endpoints,
    )

    for start, end in normalized_lines:
        start_node = get_node(start)
        end_node = get_node(end)
        if start_node == end_node:
            continue
        edges.append(
            {
                "start": start_node,
                "end": end_node,
                "dir": None,
                "geometry": [nodes[start_node], nodes[end_node]],
            }
        )

    unique_endpoints = list(dict.fromkeys(all_entity_endpoints))
    endpoints_by_x = sorted(
        range(len(unique_endpoints)),
        key=lambda index: (unique_endpoints[index][0], unique_endpoints[index][1]),
    )
    endpoints_by_y = sorted(
        range(len(unique_endpoints)),
        key=lambda index: (unique_endpoints[index][1], unique_endpoints[index][0]),
    )
    x_values = [unique_endpoints[index][0] for index in endpoints_by_x]
    y_values = [unique_endpoints[index][1] for index in endpoints_by_y]

    for source_index, geometry in enumerate(geometries):
        if geometry.geometry_type != "ARC":
            continue
        if geometry.center is None or geometry.sweep_degrees is None:
            continue
        center_x, center_y = geometry.center
        radius = _distance(geometry.start, geometry.center)
        if radius <= snap_tolerance:
            continue
        start_angle = math.atan2(
            geometry.start[1] - center_y,
            geometry.start[0] - center_x,
        )
        total_sweep = math.radians(geometry.sweep_degrees)
        radial_tolerance = max(snap_tolerance * 2.0, 1e-7)
        angular_tolerance = radial_tolerance / radius
        min_x, max_x = center_x - radius - radial_tolerance, center_x + radius + radial_tolerance
        min_y, max_y = center_y - radius - radial_tolerance, center_y + radius + radial_tolerance
        x_first, x_last = bisect_left(x_values, min_x), bisect_right(x_values, max_x)
        y_first, y_last = bisect_left(y_values, min_y), bisect_right(y_values, max_y)
        candidate_indexes = (
            endpoints_by_x[x_first:x_last]
            if x_last - x_first <= y_last - y_first
            else endpoints_by_y[y_first:y_last]
        )
        cuts: list[tuple[float, Point]] = [
            (0.0, geometry.start),
            (total_sweep, geometry.end),
        ]
        for endpoint_index in candidate_indexes:
            candidate = unique_endpoints[endpoint_index]
            if not (min_x <= candidate[0] <= max_x and min_y <= candidate[1] <= max_y):
                continue
            if abs(_distance(candidate, geometry.center) - radius) > radial_tolerance:
                continue
            candidate_angle = math.atan2(candidate[1] - center_y, candidate[0] - center_x)
            parameter = (candidate_angle - start_angle) % (2.0 * math.pi)
            if angular_tolerance < parameter < total_sweep - angular_tolerance:
                cuts.append((parameter, candidate))
        cuts.sort(key=lambda item: item[0])
        deduplicated_cuts: list[tuple[float, Point]] = []
        for parameter, candidate in cuts:
            if deduplicated_cuts and abs(parameter - deduplicated_cuts[-1][0]) <= angular_tolerance:
                continue
            deduplicated_cuts.append((parameter, candidate))

        source_segments = max(1, len(geometry.points) - 1)
        for (first_parameter, first_point), (second_parameter, second_point) in zip(
            deduplicated_cuts,
            deduplicated_cuts[1:],
        ):
            sub_sweep = second_parameter - first_parameter
            if sub_sweep <= angular_tolerance:
                continue
            start_node = get_node(first_point)
            end_node = get_node(second_point)
            if start_node == end_node:
                continue
            step_count = max(2, int(math.ceil(source_segments * sub_sweep / total_sweep)))
            display_geometry = [
                [
                    clean(
                        center_x
                        + radius
                        * math.cos(
                            start_angle
                            + first_parameter
                            + sub_sweep * index / step_count
                        )
                    ),
                    clean(
                        center_y
                        + radius
                        * math.sin(
                            start_angle
                            + first_parameter
                            + sub_sweep * index / step_count
                        )
                    ),
                ]
                for index in range(step_count + 1)
            ]
            display_geometry[0] = nodes[start_node]
            display_geometry[-1] = nodes[end_node]
            edges.append(
                {
                    "start": start_node,
                    "end": end_node,
                    "dir": None,
                    "geometry": display_geometry,
                    "geometry_type": "ARC",
                    "source_edge_count": step_count,
                    "source_arc_group": source_index,
                    "arc_center": [clean(center_x), clean(center_y)],
                    "arc_sweep_degrees": math.degrees(sub_sweep),
                }
            )

    if not edges:
        raise DxfConversionError("좌표 반올림 후 유효한 Rail Edge가 남지 않았습니다.")
    return nodes, edges


def _edge_travel_vector(
    edge: dict[str, Any],
    nodes: Sequence[Sequence[float]],
    source_node: int,
    target_node: int,
    *,
    arrival: bool,
) -> Point:
    """Return the local tangent for travel through an edge endpoint."""

    geometry = edge.get("geometry")
    if isinstance(geometry, list) and len(geometry) >= 2:
        forward = (
            int(edge["start"]) == source_node
            and int(edge["end"]) == target_node
        )
        points = geometry if forward else reversed(geometry)
        oriented = list(points)
        if arrival:
            first, second = oriented[-2], oriented[-1]
        else:
            first, second = oriented[0], oriented[1]
        return _vector(
            (float(first[0]), float(first[1])),
            (float(second[0]), float(second[1])),
        )
    return _vector(
        (float(nodes[source_node][0]), float(nodes[source_node][1])),
        (float(nodes[target_node][0]), float(nodes[target_node][1])),
    )


def build_directed_graph(
    nodes: Sequence[Sequence[float]],
    edges: Sequence[dict[str, Any]],
) -> tuple[list[dict[str, Any]], int]:
    """Apply the reference thread/dot-product direction heuristic.

    The prototype seeded only edge 0, which left disconnected geometry with
    ``dir: null``.  This implementation restarts the same deterministic thread
    algorithm for every remaining component or branch so all output edges are
    usable while retaining the prototype's direction-selection rule.
    """

    directed = [dict(edge, dir=None) for edge in edges]
    node_edges: defaultdict[int, list[int]] = defaultdict(list)
    for edge_id, edge in enumerate(directed):
        node_edges[int(edge["start"])].append(edge_id)
        node_edges[int(edge["end"])].append(edge_id)

    thread_count = 0
    next_seed = 0
    while next_seed < len(directed):
        # Resume where the previous scan stopped.  Restarting enumerate() at
        # edge 0 made drawings with many disconnected spans quadratic even
        # after the geometry stage had completed.
        while next_seed < len(directed) and directed[next_seed]["dir"] is not None:
            next_seed += 1
        if next_seed >= len(directed):
            break
        seed = next_seed
        thread_count += 1
        seed_edge = directed[seed]
        seed_edge["dir"] = [int(seed_edge["start"]), int(seed_edge["end"])]
        queue: deque[int] = deque([seed])

        while queue:
            edge_id = queue.popleft()
            edge = directed[edge_id]
            direction = edge["dir"]
            if direction is None:
                continue
            start_node, end_node = int(direction[0]), int(direction[1])
            previous = _edge_travel_vector(
                edge,
                nodes,
                start_node,
                end_node,
                arrival=True,
            )
            candidates = [
                candidate
                for candidate in node_edges[end_node]
                if directed[candidate]["dir"] is None
            ]
            if not candidates:
                continue

            ranked: list[tuple[float, int, list[int], Point]] = []
            for candidate in candidates:
                next_edge = directed[candidate]
                if int(next_edge["start"]) == end_node:
                    pair = [int(next_edge["start"]), int(next_edge["end"])]
                else:
                    pair = [int(next_edge["end"]), int(next_edge["start"])]
                vector = _edge_travel_vector(
                    next_edge,
                    nodes,
                    pair[0],
                    pair[1],
                    arrival=False,
                )
                score = _dot(_normalize(previous), _normalize(vector))
                ranked.append((score, candidate, pair, vector))

            ranked.sort(key=lambda item: (-item[0], item[1]))
            if ranked[0][0] < MIN_CONTINUATION_DOT:
                continue
            _, best_id, best_pair, _ = ranked[0]
            directed[best_id]["dir"] = best_pair
            queue.append(best_id)

            for score, candidate, pair, _ in ranked[1:]:
                if score >= MIN_CONTINUATION_DOT:
                    directed[candidate]["dir"] = pair
                    queue.append(candidate)

    _smooth_degree_two_direction_chains(directed, len(nodes))
    return directed, thread_count


def _smooth_degree_two_direction_chains(
    edges: list[dict[str, Any]],
    node_count: int,
) -> None:
    """Orient degree-2 rail chains as continuous paths.

    The prototype direction thread works well while it can keep extending from
    one seed edge.  When we restart the thread to cover every remaining branch
    or disconnected span, two restarted threads can meet at an ordinary rail
    midpoint and create a local source/sink.  A degree-2 rail midpoint should
    have exactly one incoming and one outgoing directed edge, so this pass
    collapses maximal degree-2 chains and orients each chain continuously.
    """

    incident: list[list[int]] = [[] for _ in range(node_count)]
    for edge_id, edge in enumerate(edges):
        incident[int(edge["start"])].append(edge_id)
        incident[int(edge["end"])].append(edge_id)

    visited_edges: set[int] = set()

    def other_node(edge_id: int, node: int) -> int:
        edge = edges[edge_id]
        start, end = int(edge["start"]), int(edge["end"])
        return end if start == node else start

    def set_chain_direction(edge_ids: list[int], node_path: list[int]) -> None:
        if not edge_ids:
            return
        forward_score = 0
        reverse_score = 0
        for index, edge_id in enumerate(edge_ids):
            direction = edges[edge_id].get("dir")
            if direction == [node_path[index], node_path[index + 1]]:
                forward_score += 1
            elif direction == [node_path[index + 1], node_path[index]]:
                reverse_score += 1
        if reverse_score > forward_score:
            node_path = list(reversed(node_path))
            edge_ids = list(reversed(edge_ids))
        for index, edge_id in enumerate(edge_ids):
            edges[edge_id]["dir"] = [node_path[index], node_path[index + 1]]

    anchors = [node for node, linked in enumerate(incident) if len(linked) != 2]
    for anchor in anchors:
        for first_edge in incident[anchor]:
            if first_edge in visited_edges:
                continue
            edge_ids = [first_edge]
            node_path = [anchor, other_node(first_edge, anchor)]
            visited_edges.add(first_edge)

            previous = anchor
            current = node_path[-1]
            while len(incident[current]) == 2:
                next_edges = [edge for edge in incident[current] if edge not in visited_edges]
                if not next_edges:
                    break
                next_edge = next_edges[0]
                visited_edges.add(next_edge)
                edge_ids.append(next_edge)
                next_node = other_node(next_edge, current)
                node_path.append(next_node)
                previous, current = current, next_node
                if current == previous:
                    break

            set_chain_direction(edge_ids, node_path)

    # Closed loops have no anchor because every node has degree 2.
    for first_edge in range(len(edges)):
        if first_edge in visited_edges:
            continue
        start = int(edges[first_edge]["start"])
        edge_ids = [first_edge]
        node_path = [start, other_node(first_edge, start)]
        visited_edges.add(first_edge)

        previous = start
        current = node_path[-1]
        while current != start:
            next_edges = [
                edge
                for edge in incident[current]
                if edge not in visited_edges and other_node(edge, current) != previous
            ]
            if not next_edges:
                next_edges = [edge for edge in incident[current] if edge not in visited_edges]
            if not next_edges:
                break
            next_edge = next_edges[0]
            visited_edges.add(next_edge)
            edge_ids.append(next_edge)
            next_node = other_node(next_edge, current)
            node_path.append(next_node)
            previous, current = current, next_node

        if len(node_path) == len(edge_ids) + 1:
            set_chain_direction(edge_ids, node_path)


def _component_count(node_count: int, edges: Sequence[dict[str, Any]]) -> int:
    adjacency: defaultdict[int, list[int]] = defaultdict(list)
    active_nodes: set[int] = set()
    for edge in edges:
        start, end = int(edge["start"]), int(edge["end"])
        active_nodes.update((start, end))
        adjacency[start].append(end)
        adjacency[end].append(start)

    visited: set[int] = set()
    components = 0
    for seed in sorted(active_nodes):
        if seed in visited:
            continue
        components += 1
        queue = deque([seed])
        visited.add(seed)
        while queue:
            node = queue.popleft()
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    isolated = max(0, node_count - len(active_nodes))
    return components + isolated


def validate_graph(graph: dict[str, Any]) -> None:
    nodes = graph.get("nodes")
    edges = graph.get("edges")
    if not isinstance(nodes, list) or not nodes:
        raise DxfConversionError("Graph에 Node가 없습니다.")
    if not isinstance(edges, list) or not edges:
        raise DxfConversionError("Graph에 Edge가 없습니다.")
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            raise DxfConversionError(f"Edge {index} 형식이 올바르지 않습니다.")
        start, end, direction = edge.get("start"), edge.get("end"), edge.get("dir")
        if not isinstance(start, int) or not isinstance(end, int):
            raise DxfConversionError(f"Edge {index}의 endpoint가 정수가 아닙니다.")
        if (
            start == end
            or start < 0
            or end < 0
            or start >= len(nodes)
            or end >= len(nodes)
        ):
            raise DxfConversionError(
                f"Edge {index}의 endpoint 참조가 올바르지 않습니다."
            )
        if direction not in ([start, end], [end, start]):
            raise DxfConversionError(
                f"Edge {index}의 방향이 endpoint와 일치하지 않습니다."
            )


def convert_dxf_to_graph(
    filename: str | Path,
    *,
    layers: Iterable[str] | None = None,
    arc_segments: int = 10,
    coordinate_precision: int = 3,
    coordinate_unit: str = "millimeter",
) -> dict[str, Any]:
    """Convert a DXF file to the compatible directed graph JSON document."""

    path = Path(filename).expanduser().resolve()
    if path.suffix.casefold() != ".dxf":
        raise DxfConversionError("현재 변환기는 DXF 파일만 지원합니다.")

    loaded = load_dxf_geometry(path, layers=layers, arc_segments=arc_segments)
    nodes, source_edges = build_rail_nodes_edges(
        loaded.geometries,
        coordinate_precision=coordinate_precision,
    )
    directed_edges, thread_count = build_directed_graph(nodes, source_edges)
    component_count = _component_count(len(nodes), directed_edges)
    graph: dict[str, Any] = {
        "format_version": "1.0.0",
        "metadata": {
            "source_file": path.name,
            "source_sha256": _sha256(path),
            "coordinate_unit": coordinate_unit,
            "selected_layers": loaded.selected_layers,
            "available_geometry_layers": loaded.available_geometry_layers,
            "entity_counts": loaded.entity_counts,
            "ignored_entity_counts": loaded.ignored_entity_counts,
            "labels": loaded.labels,
            "arc_segments": arc_segments,
            "coordinate_precision": coordinate_precision,
            "intermediate_format": "rail-geometry",
            "pm_generation": "deferred",
            "direction_inference": {
                "method": "rail-thread-continuity-local-tangent",
                "authoritative": False,
                "review_required": True,
            },
            "statistics": {
                "node_count": len(nodes),
                "edge_count": len(directed_edges),
                "component_count": component_count,
                "direction_thread_count": thread_count,
                "unresolved_direction_count": sum(
                    1 for edge in directed_edges if edge["dir"] is None
                ),
                "line_count": sum(
                    1 for edge in directed_edges if edge.get("geometry_type", "LINE") == "LINE"
                ),
                "curve_count": sum(
                    1 for edge in directed_edges if edge.get("geometry_type") == "ARC"
                ),
            },
            "converter": {
                "name": CONVERTER_NAME,
                "version": CONVERTER_VERSION,
                "reference_repository": "Mega-Sim/Graph_Maker_CAD-dxf-_to_json",
            },
        },
        "nodes": nodes,
        "edges": directed_edges,
    }
    validate_graph(graph)
    return graph


def save_graph(graph: dict[str, Any], filename: str | Path) -> Path:
    validate_graph(graph)
    path = Path(filename).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(graph, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return path.resolve()


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="DXF LINE/ARC를 방향성 Graph JSON으로 변환합니다."
    )
    parser.add_argument("input", type=Path, help="입력 DXF 파일")
    parser.add_argument("-o", "--output", type=Path, help="출력 JSON 파일")
    parser.add_argument(
        "--layer",
        action="append",
        dest="layers",
        help="Rail Layer 이름(여러 번 지정 가능)",
    )
    parser.add_argument(
        "--arc-segments", type=int, default=10, help="ARC당 분할 Edge 수(기본 10)"
    )
    parser.add_argument(
        "--precision", type=int, default=3, help="Node 좌표 반올림 자릿수(기본 3)"
    )
    parser.add_argument(
        "--unit",
        choices=("millimeter", "meter", "micrometer", "inch"),
        default="millimeter",
        help="원본 CAD 좌표 단위",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    output = args.output or args.input.with_suffix(".graph.json")
    try:
        graph = convert_dxf_to_graph(
            args.input,
            layers=args.layers,
            arc_segments=args.arc_segments,
            coordinate_precision=args.precision,
            coordinate_unit=args.unit,
        )
        saved = save_graph(graph, output)
    except DxfConversionError as error:
        print(f"변환 실패: {error}")
        return 2
    statistics = graph["metadata"]["statistics"]
    print(
        "변환 완료: "
        f"{statistics['node_count']} nodes, {statistics['edge_count']} edges, "
        f"{statistics['component_count']} components -> {saved}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
