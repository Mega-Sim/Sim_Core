"""Adapt the currently displayed DXF graph to a canonical Facility model.

The DXF converter intentionally emits the compact Graph_Maker contract used by
the CAD editor.  Random From-To analysis consumes the canonical Facility
contract instead.  This module is the explicit bridge between those contracts:

* Graph direction edits are preserved.
* CAD coordinates are converted to integer micrometres.
* ``station-*``/``ST-*`` text labels are projected onto the nearest rail.
* Rails are split at projected station positions so routing starts and ends at
  the actual labelled positions instead of an arbitrary nearby endpoint.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from typing import Any, Mapping, Sequence


DEFAULT_SPEED_LIMIT_UM_PER_S = 2_000_000
_UNIT_TO_UM = {
    "micrometer": 1,
    "millimeter": 1_000,
    "meter": 1_000_000,
    "inch": 25_400,
}
_STATION_LABEL = re.compile(
    r"^(?:station|st)(?:[\s._:-]*[A-Za-z0-9가-힣].*)?$",
    re.IGNORECASE,
)

PointUm = tuple[int, int]


class CadGraphFacilityError(ValueError):
    """Raised when the displayed CAD graph cannot become an LA Facility."""


@dataclass
class _DirectedEdge:
    source_index: int
    from_node_index: int
    to_node_index: int
    points_um: list[PointUm]


@dataclass
class _StationProjection:
    label_index: int
    station_id: str
    source_text: str
    edge_index: int
    segment_index: int
    segment_parameter: float
    point_um: PointUm
    distance_um: float
    expanded_point_index: int = -1


def _canonical_json(value: Mapping[str, Any]) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _safe_id(value: Any, fallback: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._:-]+", "-", str(value or "").strip())
    text = text.strip("-._:")
    if not text or not text[0].isalnum():
        text = fallback
    return text[:112]


def _point_from_raw(raw: Any, factor: int, description: str) -> PointUm:
    if not isinstance(raw, Sequence) or isinstance(raw, (str, bytes)) or len(raw) < 2:
        raise CadGraphFacilityError(f"{description} 좌표 형식이 올바르지 않습니다.")
    try:
        return int(round(float(raw[0]) * factor)), int(round(float(raw[1]) * factor))
    except (TypeError, ValueError, OverflowError) as error:
        raise CadGraphFacilityError(f"{description} 좌표가 숫자가 아닙니다.") from error


def _distance_squared(first: PointUm, second: PointUm) -> int:
    dx = first[0] - second[0]
    dy = first[1] - second[1]
    return dx * dx + dy * dy


def _deduplicate_consecutive(points: Sequence[PointUm]) -> list[PointUm]:
    result: list[PointUm] = []
    for point in points:
        if not result or point != result[-1]:
            result.append(point)
    return result


def _directed_edges(
    graph: Mapping[str, Any],
    nodes_um: Sequence[PointUm],
    factor: int,
) -> list[_DirectedEdge]:
    raw_edges = graph.get("edges")
    if not isinstance(raw_edges, list) or not raw_edges:
        raise CadGraphFacilityError("현재 CAD Graph에 Edge가 없습니다.")

    result: list[_DirectedEdge] = []
    for edge_index, raw_edge in enumerate(raw_edges):
        if not isinstance(raw_edge, Mapping):
            raise CadGraphFacilityError(f"CAD Graph Edge {edge_index} 형식이 올바르지 않습니다.")
        try:
            start = int(raw_edge.get("start"))
            end = int(raw_edge.get("end"))
        except (TypeError, ValueError) as error:
            raise CadGraphFacilityError(
                f"CAD Graph Edge {edge_index} endpoint가 정수가 아닙니다."
            ) from error
        if (
            start == end
            or start < 0
            or end < 0
            or start >= len(nodes_um)
            or end >= len(nodes_um)
        ):
            raise CadGraphFacilityError(
                f"CAD Graph Edge {edge_index} endpoint 참조가 올바르지 않습니다."
            )

        direction = raw_edge.get("dir")
        if direction not in ([start, end], [end, start]):
            raise CadGraphFacilityError(
                f"CAD Graph Edge {edge_index} 방향이 결정되지 않았습니다."
            )
        source, target = int(direction[0]), int(direction[1])

        raw_geometry = raw_edge.get("geometry")
        if isinstance(raw_geometry, list) and len(raw_geometry) >= 2:
            points = [
                _point_from_raw(point, factor, f"Edge {edge_index} geometry")
                for point in raw_geometry
            ]
        else:
            points = [nodes_um[start], nodes_um[end]]
        points = _deduplicate_consecutive(points)
        if len(points) < 2:
            raise CadGraphFacilityError(
                f"CAD Graph Edge {edge_index} geometry 길이가 0입니다."
            )

        source_point = nodes_um[source]
        target_point = nodes_um[target]
        forward_error = _distance_squared(points[0], source_point) + _distance_squared(
            points[-1], target_point
        )
        reverse_error = _distance_squared(points[-1], source_point) + _distance_squared(
            points[0], target_point
        )
        if reverse_error < forward_error:
            points.reverse()
        points[0] = source_point
        points[-1] = target_point
        points = _deduplicate_consecutive(points)
        if len(points) < 2:
            raise CadGraphFacilityError(
                f"CAD Graph Edge {edge_index} 방향 적용 후 geometry 길이가 0입니다."
            )
        result.append(
            _DirectedEdge(
                source_index=edge_index,
                from_node_index=source,
                to_node_index=target,
                points_um=points,
            )
        )
    return result


def _station_labels(graph: Mapping[str, Any]) -> list[tuple[int, str, float, float]]:
    metadata = graph.get("metadata")
    raw_labels = metadata.get("labels", []) if isinstance(metadata, Mapping) else []
    labels: list[tuple[int, str, float, float]] = []
    if not isinstance(raw_labels, list):
        return labels
    for label_index, label in enumerate(raw_labels):
        if not isinstance(label, Mapping):
            continue
        text = str(label.get("text", "")).strip()
        if not text or _STATION_LABEL.fullmatch(text) is None:
            continue
        try:
            x = float(label.get("x"))
            y = float(label.get("y"))
        except (TypeError, ValueError, OverflowError):
            continue
        labels.append((label_index, text, x, y))
    return labels


def _unique_station_ids(
    labels: Sequence[tuple[int, str, float, float]],
) -> dict[int, str]:
    ids: dict[int, str] = {}
    used: set[str] = set()
    for label_index, text, _x, _y in sorted(
        labels, key=lambda item: (item[1].casefold(), item[0])
    ):
        base = _safe_id(text, f"ST-{label_index + 1:04d}")
        candidate = base
        suffix = 2
        while candidate in used:
            candidate = f"{base[:104]}-{suffix}"
            suffix += 1
        used.add(candidate)
        ids[label_index] = candidate
    return ids


def _project_to_edges(
    label_index: int,
    station_id: str,
    source_text: str,
    point_um: PointUm,
    edges: Sequence[_DirectedEdge],
) -> _StationProjection:
    best: tuple[float, int, int, float, PointUm, float] | None = None
    for edge_index, edge in enumerate(edges):
        distance_along = 0.0
        for segment_index, (start, end) in enumerate(
            zip(edge.points_um, edge.points_um[1:])
        ):
            dx = end[0] - start[0]
            dy = end[1] - start[1]
            length_squared = dx * dx + dy * dy
            if length_squared <= 0:
                continue
            parameter = (
                (point_um[0] - start[0]) * dx + (point_um[1] - start[1]) * dy
            ) / length_squared
            parameter = max(0.0, min(1.0, parameter))
            projected = (
                int(round(start[0] + dx * parameter)),
                int(round(start[1] + dy * parameter)),
            )
            separation_squared = float(_distance_squared(point_um, projected))
            segment_length = math.sqrt(length_squared)
            candidate = (
                separation_squared,
                edge_index,
                segment_index,
                parameter,
                projected,
                distance_along + segment_length * parameter,
            )
            if best is None or candidate[:4] < best[:4]:
                best = candidate
            distance_along += segment_length
    if best is None:
        raise CadGraphFacilityError(
            f"Station 라벨 {source_text}을 연결할 Rail geometry가 없습니다."
        )
    return _StationProjection(
        label_index=label_index,
        station_id=station_id,
        source_text=source_text,
        edge_index=best[1],
        segment_index=best[2],
        segment_parameter=best[3],
        point_um=best[4],
        distance_um=math.sqrt(best[0]),
    )


def _position(point: PointUm) -> dict[str, int]:
    return {"x": point[0], "y": point[1], "z": 0}


def _polyline_length(points: Sequence[PointUm]) -> int:
    length = sum(math.dist(first, second) for first, second in zip(points, points[1:]))
    return max(1, int(round(length)))


def _source_identity(namespace: str, external_id: str) -> list[dict[str, str]]:
    return [
        {
            "source_kind": "dxf_graph",
            "source_namespace": namespace,
            "external_id": external_id,
        }
    ]


def build_facility_from_cad_graph(
    graph: Mapping[str, Any],
    *,
    speed_limit_um_per_s: int = DEFAULT_SPEED_LIMIT_UM_PER_S,
) -> dict[str, Any]:
    """Build an LA/Core Facility from the current editable CAD graph.

    A minimum of two station-like text labels is required because Random
    From-To generation cannot produce an origin/destination pair otherwise.
    """

    if speed_limit_um_per_s <= 0:
        raise CadGraphFacilityError("CAD Facility 기본 주행속도는 0보다 커야 합니다.")
    metadata = graph.get("metadata")
    if not isinstance(metadata, Mapping):
        raise CadGraphFacilityError("CAD Graph metadata가 없습니다.")
    coordinate_unit = str(metadata.get("coordinate_unit", "millimeter")).casefold()
    factor = _UNIT_TO_UM.get(coordinate_unit)
    if factor is None:
        supported = ", ".join(sorted(_UNIT_TO_UM))
        raise CadGraphFacilityError(
            f"지원하지 않는 CAD 좌표 단위입니다: {coordinate_unit} (지원: {supported})"
        )

    raw_nodes = graph.get("nodes")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise CadGraphFacilityError("현재 CAD Graph에 Node가 없습니다.")
    nodes_um = [
        _point_from_raw(raw, factor, f"CAD Graph Node {index}")
        for index, raw in enumerate(raw_nodes)
    ]
    directed_edges = _directed_edges(graph, nodes_um, factor)

    labels = _station_labels(graph)
    if len(labels) < 2:
        raise CadGraphFacilityError(
            "Random From-To 분석에는 도면 TEXT/MTEXT로 작성한 "
            "station-* 또는 ST-* 라벨이 2개 이상 필요합니다."
        )
    station_ids = _unique_station_ids(labels)
    projections: list[_StationProjection] = []
    for label_index, text, x, y in labels:
        projections.append(
            _project_to_edges(
                label_index,
                station_ids[label_index],
                text,
                (int(round(x * factor)), int(round(y * factor))),
                directed_edges,
            )
        )

    source_file = str(metadata.get("source_file", "layout.dxf"))
    source_sha = str(metadata.get("source_sha256", "")).casefold()
    if re.fullmatch(r"[0-9a-f]{64}", source_sha) is None:
        source_sha = hashlib.sha256(_canonical_json(graph).encode("utf-8")).hexdigest()
    graph_digest = hashlib.sha256(_canonical_json(graph).encode("utf-8")).hexdigest()
    source_stem = source_file.rsplit(".", 1)[0]
    model_id = _safe_id(f"cad-{source_stem}", f"cad-{source_sha[:12]}")
    revision_id = _safe_id(
        f"{model_id}-{graph_digest[:12]}", f"cad-revision-{graph_digest[:12]}"
    )
    namespace = f"sim-core:cad:{source_sha[:12]}"
    selected_layers = metadata.get("selected_layers")
    layer = "CAD_RAIL"
    if isinstance(selected_layers, list) and selected_layers:
        layer = str(selected_layers[0]).strip() or layer

    facility_nodes: list[dict[str, Any]] = []
    node_positions: dict[str, PointUm] = {}
    for node_index, point in enumerate(nodes_um):
        node_id = f"N-{node_index:05d}"
        node_positions[node_id] = point
        facility_nodes.append(
            {
                "id": node_id,
                "position_um": _position(point),
                "layer": layer,
                "role": "rail",
                "source_identities": _source_identity(
                    namespace, f"graph-node:{node_index}"
                ),
            }
        )

    projections_by_edge: dict[int, list[_StationProjection]] = {}
    for projection in projections:
        projections_by_edge.setdefault(projection.edge_index, []).append(projection)

    facility_edges: list[dict[str, Any]] = []
    station_node_ids: dict[int, str] = {}
    for edge_index, edge in enumerate(directed_edges):
        edge_projections = projections_by_edge.get(edge_index, [])
        by_segment: dict[int, list[_StationProjection]] = {}
        for projection in edge_projections:
            by_segment.setdefault(projection.segment_index, []).append(projection)
        for group in by_segment.values():
            group.sort(
                key=lambda item: (
                    item.segment_parameter,
                    item.station_id.casefold(),
                    item.label_index,
                )
            )

        expanded: list[PointUm] = [edge.points_um[0]]
        for segment_index, segment_end in enumerate(edge.points_um[1:]):
            for projection in by_segment.get(segment_index, []):
                if projection.point_um != expanded[-1]:
                    expanded.append(projection.point_um)
                projection.expanded_point_index = len(expanded) - 1
            if segment_end != expanded[-1]:
                expanded.append(segment_end)

        split_indices = {0, len(expanded) - 1}
        split_indices.update(
            projection.expanded_point_index for projection in edge_projections
        )
        ordered_splits = sorted(index for index in split_indices if index >= 0)
        node_at_split: dict[int, str] = {
            0: f"N-{edge.from_node_index:05d}",
            len(expanded) - 1: f"N-{edge.to_node_index:05d}",
        }
        for cut_ordinal, point_index in enumerate(ordered_splits[1:-1], start=1):
            node_id = f"N-E{edge.source_index:05d}-S{cut_ordinal:03d}"
            point = expanded[point_index]
            node_at_split[point_index] = node_id
            node_positions[node_id] = point
            facility_nodes.append(
                {
                    "id": node_id,
                    "position_um": _position(point),
                    "layer": layer,
                    "role": "rail_station",
                    "source_identities": _source_identity(
                        namespace,
                        f"graph-edge:{edge.source_index}:station-split:{cut_ordinal}",
                    ),
                }
            )

        for projection in edge_projections:
            station_node_ids[projection.label_index] = node_at_split[
                projection.expanded_point_index
            ]

        for part_index, (first_index, last_index) in enumerate(
            zip(ordered_splits, ordered_splits[1:])
        ):
            polyline = _deduplicate_consecutive(expanded[first_index : last_index + 1])
            if len(polyline) < 2:
                continue
            edge_id = (
                f"E-{edge.source_index:05d}"
                if len(ordered_splits) == 2
                else f"E-{edge.source_index:05d}-{part_index + 1:03d}"
            )
            facility_edges.append(
                {
                    "id": edge_id,
                    "from_node_id": node_at_split[first_index],
                    "to_node_id": node_at_split[last_index],
                    "length_um": _polyline_length(polyline),
                    "speed_limit_um_per_s": int(speed_limit_um_per_s),
                    "polyline_um": [_position(point) for point in polyline],
                    "direction": "ONE_WAY",
                    "source_identities": _source_identity(
                        namespace, f"graph-edge:{edge.source_index}:part:{part_index + 1}"
                    ),
                }
            )

    facility_stations: list[dict[str, Any]] = []
    for projection in sorted(
        projections, key=lambda item: (item.station_id.casefold(), item.label_index)
    ):
        attachment = station_node_ids[projection.label_index]
        position = node_positions[attachment]
        facility_stations.append(
            {
                "id": projection.station_id,
                "attachment_node_id": attachment,
                "operation_type": "TRANSFER",
                "position_um": _position(position),
                "handling_capacity_per_hour": 0,
                "semantic_tags": ["cad-text-station"],
                "source_identities": _source_identity(
                    namespace, f"dxf-label:{projection.label_index}:{projection.source_text}"
                ),
            }
        )
        for node in facility_nodes:
            if node["id"] == attachment:
                node["role"] = "rail_station"
                break

    facility: dict[str, Any] = {
        "schema_version": "1.1.0",
        "model_id": model_id,
        "revision_id": revision_id,
        "coordinate_reference": {
            "frame": "local-fab",
            "length_unit": "micrometer",
            "up_axis": "Z",
            "handedness": "right",
        },
        "source_artifacts": [
            {
                "kind": "dxf",
                "source_namespace": namespace,
                "sha256": source_sha,
                "importer_name": "sim-core-dxf-graph-facility",
                "importer_version": "1.0.0",
                "coordinate_frame": f"dxf-modelspace-{coordinate_unit}",
            }
        ],
        "geometry_transforms": [
            {
                "source_namespace": namespace,
                "source_frame": f"dxf-modelspace-{coordinate_unit}",
                "target_frame": "local-fab",
                "scale_numerator": factor,
                "scale_denominator": 1,
                "translation_um": {"x": 0, "y": 0, "z": 0},
            }
        ],
        "nodes": facility_nodes,
        "edges": facility_edges,
        "stations": facility_stations,
        "control_points": [],
        "zones": [],
        "parkings": [],
        "chargers": [],
        "vehicle_types": [],
    }
    facility["content_hash"] = "sha256:" + hashlib.sha256(
        _canonical_json(facility).encode("utf-8")
    ).hexdigest()
    return facility
