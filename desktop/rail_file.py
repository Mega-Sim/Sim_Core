"""Fast reader for the text ``.rail`` files emitted by SemiLA.

The adapter intentionally reads only the public data contract visible in a
Rail file: drawable LINE/CURVE records, NODE/LINK/RAILLIST topology, equipment
labels, and SCALE bounds.  AutoMod/PM generation is deliberately not part of
this module; a Rail graph is the lightweight preview and topology boundary.
"""

from __future__ import annotations

import hashlib
import math
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any, Iterable


Point = tuple[float, float]


class RailFileError(ValueError):
    """Raised when a Rail file cannot produce a usable preview graph."""


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _curve_points(fields: list[str]) -> list[Point]:
    """Expand a SemiLA CURVE record to a compact display polyline.

    A CURVE record stores start, the opposite bounding-box corner, end,
    center, and a signed sweep angle.  Five-degree display segments preserve
    the source radius while keeping the in-memory preview small.
    """

    if len(fields) < 12:
        raise RailFileError("CURVE 레코드의 필드 수가 부족합니다.")
    start = float(fields[3]), float(fields[4])
    end = float(fields[7]), float(fields[8])
    center = float(fields[9]), float(fields[10])
    sweep_degrees = float(fields[11])
    radius = math.dist(start, center)
    if radius <= 0.0:
        return [start, end]

    step_count = max(4, min(144, int(math.ceil(abs(sweep_degrees) / 5.0))))
    start_angle = math.atan2(start[1] - center[1], start[0] - center[0])
    sweep = math.radians(sweep_degrees)
    points = [
        (
            center[0] + radius * math.cos(start_angle + sweep * index / step_count),
            center[1] + radius * math.sin(start_angle + sweep * index / step_count),
        )
        for index in range(step_count + 1)
    ]
    points[0] = start
    points[-1] = end
    return points


def _component_count(node_count: int, edges: Iterable[dict[str, Any]]) -> int:
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
        visited.add(seed)
        queue = deque([seed])
        while queue:
            node = queue.popleft()
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return components + max(0, node_count - len(active_nodes))


def load_rail_graph(filename: str | Path) -> dict[str, Any]:
    """Read a SemiLA Rail file into the Workbench graph contract."""

    path = Path(filename).expanduser().resolve()
    if path.suffix.casefold() != ".rail":
        raise RailFileError("Rail 어댑터는 .rail 파일만 지원합니다.")

    nodes_by_id: dict[int, Point] = {}
    link_records: dict[int, tuple[str, int, int]] = {}
    rail_records: dict[int, tuple[str, int, int]] = {}
    geometry_by_link: dict[int, list[Point]] = {}
    labels: list[dict[str, Any]] = []
    record_counts: Counter[str] = Counter()
    scale_bounds: list[float] | None = None
    has_header = False

    try:
        stream = path.open("r", encoding="utf-8-sig", errors="strict", newline=None)
    except OSError as error:
        raise RailFileError(f"Rail 파일을 읽을 수 없습니다: {error}") from error

    with stream:
        for line_number, raw_line in enumerate(stream, start=1):
            line = raw_line.rstrip("\r\n")
            if not line:
                continue
            fields = line.split("\t")
            record = fields[0].strip().upper()
            record_counts[record] += 1
            try:
                if record == "RAILDATA":
                    has_header = True
                elif record == "LINE" and len(fields) >= 7 and fields[2].upper() == "LINE":
                    link_id = int(fields[1])
                    geometry_by_link[link_id] = [
                        (float(fields[3]), float(fields[4])),
                        (float(fields[5]), float(fields[6])),
                    ]
                elif record == "CURVE" and len(fields) >= 12 and fields[2].upper() == "CURVE":
                    geometry_by_link[int(fields[1])] = _curve_points(fields)
                elif record == "NODE" and len(fields) >= 4:
                    nodes_by_id[int(fields[1])] = float(fields[2]), float(fields[3])
                elif record == "LINK" and len(fields) >= 5:
                    link_records[int(fields[1])] = (
                        fields[2].upper(),
                        int(fields[3]),
                        int(fields[4]),
                    )
                elif record == "RAILLIST" and len(fields) >= 5:
                    rail_records[int(fields[1])] = (
                        fields[2].upper(),
                        int(fields[3]),
                        int(fields[4]),
                    )
                elif record == "TEXT" and len(fields) >= 5:
                    labels.append(
                        {
                            "text": fields[1].strip(),
                            "kind": fields[2].strip(),
                            "x": float(fields[3]),
                            "y": float(fields[4]),
                            "layer": "Rail TEXT",
                        }
                    )
                elif record == "SCALE" and len(fields) >= 5:
                    scale_bounds = [float(value) for value in fields[1:5]]
            except (IndexError, TypeError, ValueError) as error:
                raise RailFileError(
                    f"Rail {line_number}행의 {record or 'UNKNOWN'} 레코드가 올바르지 않습니다: {error}"
                ) from error

    if not has_header:
        raise RailFileError("RAILDATA 헤더가 없는 Rail 파일입니다.")
    if not nodes_by_id:
        raise RailFileError("Rail 파일에 NODE 레코드가 없습니다.")

    # RAILLIST is the complete topology list.  P2L7F.rail, for example, has
    # one valid RAILLIST fallback link that is intentionally absent from LINK.
    source_links = rail_records or link_records
    if not source_links:
        raise RailFileError("Rail 파일에 LINK/RAILLIST 레코드가 없습니다.")

    node_ids = sorted(nodes_by_id)
    node_index = {node_id: index for index, node_id in enumerate(node_ids)}
    nodes = [[nodes_by_id[node_id][0], nodes_by_id[node_id][1]] for node_id in node_ids]
    edges: list[dict[str, Any]] = []
    ignored_links = 0
    geometry_counts: Counter[str] = Counter()

    for link_id, (geometry_type, source_start, source_end) in source_links.items():
        if source_start not in node_index or source_end not in node_index:
            ignored_links += 1
            continue
        start, end = node_index[source_start], node_index[source_end]
        if start == end:
            ignored_links += 1
            continue
        geometry = geometry_by_link.get(link_id)
        if not geometry:
            geometry = [nodes_by_id[source_start], nodes_by_id[source_end]]
        normalized_type = "CURVE" if geometry_type == "CURVE" else "LINE"
        geometry_counts[normalized_type] += 1
        edges.append(
            {
                "start": start,
                "end": end,
                "dir": [start, end],
                "geometry": [[float(x), float(y)] for x, y in geometry],
                "geometry_type": normalized_type,
                "rail_link_id": link_id,
            }
        )

    if not edges:
        raise RailFileError("Rail 파일에서 유효한 Edge를 만들 수 없습니다.")

    component_count = _component_count(len(nodes), edges)
    return {
        "format_version": "1.0.0",
        "metadata": {
            "source_file": path.name,
            "source_sha256": _sha256(path),
            "source_format": "semila-rail",
            "coordinate_unit": "millimeter",
            "selected_layers": ["Rail file"],
            "available_geometry_layers": ["Rail file"],
            "labels": labels,
            "scale_bounds": scale_bounds,
            "direction_inference": {
                "method": "rail-link-order",
                "authoritative": False,
                "review_required": True,
            },
            "statistics": {
                "node_count": len(nodes),
                "edge_count": len(edges),
                "line_count": geometry_counts["LINE"],
                "curve_count": geometry_counts["CURVE"],
                "component_count": component_count,
                "direction_thread_count": 0,
                "unresolved_direction_count": 0,
                "ignored_link_count": ignored_links,
            },
            "record_counts": dict(sorted(record_counts.items())),
            "converter": {
                "name": "sim-core-rail-reader",
                "version": "1.0.0",
            },
        },
        "nodes": nodes,
        "edges": edges,
    }
