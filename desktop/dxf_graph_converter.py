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
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import ezdxf


CONVERTER_NAME = "sim-core-dxf-graph"
CONVERTER_VERSION = "1.0.0"
SUPPORTED_ENTITY_TYPES = ("LINE", "ARC")

Point = tuple[float, float]
Segment = tuple[Point, Point]


class DxfConversionError(ValueError):
    """Raised when a DXF cannot produce a usable rail graph."""


@dataclass(frozen=True)
class DxfLoadResult:
    segments: list[Segment]
    selected_layers: list[str]
    available_geometry_layers: list[str]
    entity_counts: dict[str, int]
    ignored_entity_counts: dict[str, int]


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
    sweep = math.radians(end_angle - start_angle)
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
    segments: list[Segment] = []
    entity_counts: Counter[str] = Counter()
    ignored_counts: Counter[str] = Counter()
    available_layers: set[str] = set()
    selected_layers: set[str] = set()

    for entity in document.modelspace():
        entity_type = entity.dxftype()
        layer = str(entity.dxf.layer)
        if entity_type in SUPPORTED_ENTITY_TYPES:
            available_layers.add(layer)
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
            segments.append(
                ((float(start.x), float(start.y)), (float(end.x), float(end.y)))
            )
        else:
            points = _arc_points(entity, arc_segments)
            segments.extend(zip(points, points[1:]))

    if not segments:
        available = ", ".join(sorted(available_layers, key=str.casefold)) or "없음"
        requested = ", ".join(layers or []) or "전체"
        raise DxfConversionError(
            f"선택한 Rail Layer({requested})에서 LINE/ARC를 찾지 못했습니다. "
            f"사용 가능한 geometry Layer: {available}"
        )

    return DxfLoadResult(
        segments=segments,
        selected_layers=sorted(selected_layers, key=str.casefold),
        available_geometry_layers=sorted(available_layers, key=str.casefold),
        entity_counts=dict(sorted(entity_counts.items())),
        ignored_entity_counts=dict(sorted(ignored_counts.items())),
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

    for start, end in segments:
        start_node = get_node(start)
        end_node = get_node(end)
        if start_node == end_node:
            continue
        edges.append({"start": start_node, "end": end_node, "dir": None})

    if not edges:
        raise DxfConversionError("좌표 반올림 후 유효한 Edge가 남지 않았습니다.")
    return nodes, edges


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
    while True:
        seed = next(
            (index for index, edge in enumerate(directed) if edge["dir"] is None), None
        )
        if seed is None:
            break
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
            previous = _vector(tuple(nodes[start_node]), tuple(nodes[end_node]))  # type: ignore[arg-type]
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
                vector = _vector(tuple(nodes[pair[0]]), tuple(nodes[pair[1]]))  # type: ignore[arg-type]
                score = _dot(_normalize(previous), _normalize(vector))
                ranked.append((score, candidate, pair, vector))

            ranked.sort(key=lambda item: (-item[0], item[1]))
            _, best_id, best_pair, _ = ranked[0]
            directed[best_id]["dir"] = best_pair
            queue.append(best_id)

            for _, candidate, pair, vector in ranked[1:]:
                if _sign(previous[0]) == _sign(vector[0]) and _sign(
                    previous[1]
                ) == _sign(vector[1]):
                    directed[candidate]["dir"] = pair
                    queue.append(candidate)

    return directed, thread_count


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
    nodes, source_edges = build_nodes_edges(
        loaded.segments,
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
            "arc_segments": arc_segments,
            "coordinate_precision": coordinate_precision,
            "direction_inference": {
                "method": "thread-continuity-dot-product",
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
