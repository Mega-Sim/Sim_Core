"""Directed Graph JSON to AutoMod AGVS ``pm.asy`` converter.

The generated file follows the AGVS system layout used by the two reference
AutoMod models under ``development_src/AutoMod_Models``.  Graph edge direction
becomes AutoMod guide-path direction, and every graph node is exposed as an
AutoMod control point so model logic can refer to the imported topology.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence


AUTOMOD_VERSION = "12.6.1.12"
UNIT_TO_MILLIMETERS = {
    "millimeter": 1.0,
    "meter": 1000.0,
    "micrometer": 0.001,
    "inch": 25.4,
}


class AutoModConversionError(ValueError):
    """Raised when a graph cannot be represented as an AutoMod AGVS system."""


@dataclass(frozen=True)
class GuidePath:
    name: str
    start: tuple[float, float]
    end: tuple[float, float]
    source_node: int | None
    target_node: int | None

    @property
    def length(self) -> float:
        return math.dist(self.start, self.end)


def _number(value: float) -> str:
    if not math.isfinite(value):
        raise AutoModConversionError("AutoMod 좌표에는 NaN 또는 무한대를 사용할 수 없습니다.")
    normalized = 0.0 if abs(value) < 0.5e-9 else value
    text = f"{normalized:.9f}".rstrip("0").rstrip(".")
    return text or "0"


def _point(value: Any, *, label: str) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)) or len(value) < 2:
        raise AutoModConversionError(f"{label} 좌표는 [x, y] 배열이어야 합니다.")
    try:
        point = float(value[0]), float(value[1])
    except (TypeError, ValueError) as error:
        raise AutoModConversionError(f"{label} 좌표가 숫자가 아닙니다.") from error
    if not all(math.isfinite(component) for component in point):
        raise AutoModConversionError(f"{label} 좌표에는 NaN 또는 무한대를 사용할 수 없습니다.")
    return point


def _unit_scale(graph: dict[str, Any]) -> float:
    metadata = graph.get("metadata", {})
    unit = str(metadata.get("coordinate_unit", "millimeter")).strip().casefold()
    try:
        return UNIT_TO_MILLIMETERS[unit]
    except KeyError as error:
        supported = ", ".join(UNIT_TO_MILLIMETERS)
        raise AutoModConversionError(
            f"지원하지 않는 Graph 좌표 단위입니다: {unit!r} (지원: {supported})"
        ) from error


def _scaled(point: tuple[float, float], scale: float) -> tuple[float, float]:
    return point[0] * scale, point[1] * scale


def _edge_points(
    edge: dict[str, Any],
    nodes: list[tuple[float, float]],
    *,
    edge_index: int,
) -> tuple[list[tuple[float, float]], int, int]:
    try:
        start = int(edge["start"])
        end = int(edge["end"])
    except (KeyError, TypeError, ValueError) as error:
        raise AutoModConversionError(f"Edge {edge_index} endpoint가 올바르지 않습니다.") from error
    if start == end or min(start, end) < 0 or max(start, end) >= len(nodes):
        raise AutoModConversionError(f"Edge {edge_index} endpoint 참조가 올바르지 않습니다.")

    direction = edge.get("dir")
    if direction == [start, end]:
        source, target = start, end
        reverse = False
    elif direction == [end, start]:
        source, target = end, start
        reverse = True
    else:
        raise AutoModConversionError(f"Edge {edge_index}에 확정된 진행 방향이 없습니다.")

    raw_geometry = edge.get("geometry")
    if isinstance(raw_geometry, list) and len(raw_geometry) >= 2:
        points = [
            _point(value, label=f"Edge {edge_index} geometry {point_index}")
            for point_index, value in enumerate(raw_geometry)
        ]
    else:
        points = [nodes[start], nodes[end]]
    if reverse:
        points.reverse()

    # The Graph contract stores geometry in start->end order.  Keep the path
    # endpoints authoritative even when a hand-edited JSON has small rounding
    # differences in its geometry array.
    points[0] = nodes[source]
    points[-1] = nodes[target]
    return points, source, target


def _guide_paths(
    graph: dict[str, Any],
) -> tuple[list[GuidePath], dict[int, tuple[str, float]]]:
    raw_nodes = graph.get("nodes")
    raw_edges = graph.get("edges")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise AutoModConversionError("Graph에 Node가 없습니다.")
    if not isinstance(raw_edges, list) or not raw_edges:
        raise AutoModConversionError("Graph에 Edge가 없습니다.")

    nodes = [_point(value, label=f"Node {index}") for index, value in enumerate(raw_nodes)]
    scale = _unit_scale(graph)
    paths: list[GuidePath] = []
    node_anchors: dict[int, tuple[str, float]] = {}

    for edge_index, edge in enumerate(raw_edges):
        if not isinstance(edge, dict):
            raise AutoModConversionError(f"Edge {edge_index} 형식이 올바르지 않습니다.")
        points, source, target = _edge_points(edge, nodes, edge_index=edge_index)
        points = [_scaled(point, scale) for point in points]
        edge_paths: list[GuidePath] = []
        for first, second in zip(points, points[1:]):
            if math.dist(first, second) <= 1e-9:
                continue
            path = GuidePath(
                name=f"path{len(paths) + 1}",
                start=first,
                end=second,
                source_node=source if not edge_paths else None,
                target_node=None,
            )
            paths.append(path)
            edge_paths.append(path)
        if not edge_paths:
            raise AutoModConversionError(f"Edge {edge_index}의 길이가 0입니다.")

        last = edge_paths[-1]
        edge_paths[-1] = GuidePath(
            name=last.name,
            start=last.start,
            end=last.end,
            source_node=last.source_node,
            target_node=target,
        )
        paths[-1] = edge_paths[-1]
        node_anchors.setdefault(source, (edge_paths[0].name, 0.0))
        node_anchors.setdefault(target, (edge_paths[-1].name, edge_paths[-1].length))

    isolated_nodes = sorted(set(range(len(nodes))) - set(node_anchors))
    if isolated_nodes:
        preview = ", ".join(str(index) for index in isolated_nodes[:8])
        raise AutoModConversionError(
            f"Guide Path에 연결되지 않은 Node가 있습니다: {preview}"
        )
    return paths, node_anchors


def render_pm_asy(graph: dict[str, Any]) -> str:
    """Render a complete AutoMod 12.6 AGVS system as CRLF text."""

    paths, node_anchors = _guide_paths(graph)
    seed_path = paths[0]
    if seed_path.source_node is None:
        raise AutoModConversionError("AutoMod 시작 Guide Path를 결정할 수 없습니다.")
    seed_cp = f"cp_node_{seed_path.source_node + 1}"

    lines = [
        f"VERSION {AUTOMOD_VERSION}",
        "SYSTYPE AGVS",
        "UNITS Millimeters Seconds",
        "SYSDEF timeout 60 Seconds confname Config1",
        "FLAGS",
        "\tSystem Inherit",
        "\tText Inherit",
        "\tPaths Inherit",
        "\tPath Names Invisible Inherit",
        "\tDirection Invisible Inherit",
        "\tVehicles Inherit",
        "\tPath Attach Points Invisible Inherit",
        "\tControl Points Inherit",
        "\tControl Point Names Invisible Inherit",
        "\tTransfers Invisible Inherit",
        f"AGVSDEF secname {seed_path.name} name {seed_cp} UserId 2",
        f"\tNEXTPATH name {seed_path.name} type DefaultGuidePath",
        f"\tNEXTCP name {seed_cp} type DefaultControlPoint",
        "\tALTERNATE NONE ResumeSpeedWhenClaimed",
        "\tvel 0 Infinite Meters Seconds",
        "\tcrabvel 0 Infinite Meters Seconds",
        "\tsprvel 0 Infinite Meters Seconds",
        "\tcrvvel 0 Infinite Meters Seconds",
        "AGVSTOL minang 150 maxang 1800",
        "GPATHTYPE name DefaultGuidePath one normal attach rigid color 0 nav 1 vel 1 0 Meters Seconds",
    ]
    lines.extend(
        "GPATH name {name} type DefaultGuidePath piece begx {begx} begy {begy} "
        "endx {endx} endy {endy} upz 1".format(
            name=path.name,
            begx=_number(path.start[0]),
            begy=_number(path.start[1]),
            endx=_number(path.end[0]),
            endy=_number(path.end[1]),
        )
        for path in paths
    )
    lines.append(
        "CPOINTTYPE name DefaultControlPoint cap 2147483647 release distance 0 Feet "
        "align leadingpap limit Infinite scale 1 color -1 nrot 0 nscale 1"
    )
    for node_index in range(len(node_anchors)):
        path_name, distance = node_anchors[node_index]
        lines.append(
            f"CPOINT name cp_node_{node_index + 1} type DefaultControlPoint "
            f"at {path_name} {_number(distance)}"
        )

    lines.extend(
        [
            "AGVVEHSEG name DefSegment cap 1 pickup 0 Seconds setdown 0 Seconds",
            "\tfigcurspeed 100",
            "\tfigmaxspeed 100 color 21",
            "\tdisplay picpos begx 0 begy 0 endx 1 endy 0 scx 900 scy 500 scz 300",
            "",
            "\ttemplate Millimeters",
            "700 0",
            "1",
            "310 0",
            "1 1 1 1 1 0 0",
            "end",
            "\tfconn length 0.0 Meters noscale 0",
            "\trconn length 0.0 Meters noscale 0",
            "\tPAPATTACH",
            "\tPAP ind 0",
            "\t\ttrx 0 try 0 trz 0",
            "AGVSVEH type DefVehicle numveh 0",
            "\tvehsegs item DefSegment",
            "\tstart Random",
            "\tStacking OTT_LDDISP",
            "\tpicpos endx 1",
            "",
            "\tload Default",
            "\t\taccel\t0 0.8333333 Meters Seconds Seconds",
            "\t\tdecel\t0 0.8333333 Meters Seconds Seconds",
            "\t\tvel\t0 2.5 Meters Seconds",
            "\t\tcrvvel\t0 1.5 Meters Seconds",
            "\t\tsprvel\t0 2.5 Meters Seconds",
            "\t\trvel\t0 2.5 Meters Seconds",
            "\t\trcrvvel\t0 1.5 Meters Seconds",
            "\t\trsprvel\t0 2.5 Meters Seconds",
            "\t\tcrabvel\t0 2.5 Meters Seconds",
            "\t\trotate\t0 1 Seconds",
            "\t\tbrakedist\t0 4.5 Meters",
            "\t\tstopdist\t0 0 Meters",
            "\tload Empty",
            "\t\taccel\t1 0 Meters Seconds Seconds",
            "\t\tdecel\t1 0 Meters Seconds Seconds",
            "\t\tvel\t1 0 Meters Seconds",
            "\t\tcrvvel\t1 0 Meters Seconds",
            "\t\tsprvel\t1 0 Meters Seconds",
            "\t\trvel\t1 0 Meters Seconds",
            "\t\trcrvvel\t1 0 Meters Seconds",
            "\t\trsprvel\t1 0 Meters Seconds",
            "\t\tcrabvel\t1 0 Meters Seconds",
            "\t\trotate\t1 0 Seconds",
            "\t\tbrakedist\t1 0 Meters",
            "\t\tstopdist\t1 0 Meters",
        ]
    )
    return "\r\n".join(lines) + "\r\n"


def save_pm_asy(graph: dict[str, Any], filename: str | Path) -> Path:
    """Validate and save ``pm.asy`` using AutoMod's native CRLF convention."""

    path = Path(filename).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    content = render_pm_asy(graph)
    with path.open("w", encoding="ascii", newline="") as stream:
        stream.write(content)
    return path.resolve()


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="방향성 Graph JSON을 AutoMod pm.asy로 변환합니다.")
    parser.add_argument("input", type=Path, help="입력 Graph JSON")
    parser.add_argument("-o", "--output", type=Path, help="출력 pm.asy 파일")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    output = args.output or args.input.with_name("pm.asy")
    try:
        with args.input.open("r", encoding="utf-8-sig") as stream:
            graph = json.load(stream)
        if not isinstance(graph, dict):
            raise AutoModConversionError("Graph JSON 최상위 값은 object여야 합니다.")
        saved = save_pm_asy(graph, output)
    except (AutoModConversionError, OSError, json.JSONDecodeError) as error:
        print(f"AutoMod 변환 실패: {error}")
        return 2
    print(f"AutoMod 변환 완료: {saved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
