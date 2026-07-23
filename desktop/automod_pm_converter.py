"""Directed Graph JSON to a source-free AutoMod model archive.

The generated ``model.arc`` layout follows the two reference AutoMod models
under ``development_src/AutoMod_Models``.  ``model.amo`` registers the AGVS
movement system in ``pm.asy`` and an empty Process system in ``model~.asy``.
No ``model.dir`` or C/AutoMod source file is generated; AutoMod creates its
working directory when the archive is opened and built.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence


AUTOMOD_VERSION = "12.6.1.12"
ARC_RADIUS_MILLIMETERS = 450.0
ARC_RADIUS_TOLERANCE_MILLIMETERS = 2.0
STATION_CONTROL_POINT_SCALE = 0.2
BRANCH_CONTROL_POINT_SCALE = STATION_CONTROL_POINT_SCALE / 3.0
BRANCH_OFFSET_MILLIMETERS = 10.0
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
    center: tuple[float, float] | None = None
    sweep_radians: float | None = None

    @property
    def length(self) -> float:
        if self.center is not None and self.sweep_radians is not None:
            return math.dist(self.start, self.center) * abs(self.sweep_radians)
        return math.dist(self.start, self.end)

    @property
    def is_arc(self) -> bool:
        return self.center is not None and self.sweep_radians is not None


@dataclass(frozen=True)
class ControlPoint:
    name: str
    type_name: str
    path_name: str
    distance: float


@dataclass(frozen=True)
class AutoModModelFiles:
    """Paths belonging to one generated, source-free AutoMod archive."""

    archive: Path
    manifest: Path
    process_system: Path
    movement_system: Path


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


def _fixed_radius_arc(
    points: Sequence[tuple[float, float]],
    *,
    edge_index: int,
) -> tuple[tuple[float, float], float]:
    """Build one exact 450 mm AutoMod arc matching the sampled Graph edge."""

    if len(points) < 3:
        raise AutoModConversionError(
            f"Edge {edge_index} ARC에는 중심을 계산할 점이 3개 이상 필요합니다."
        )

    start, end = points[0], points[-1]
    chord_x, chord_y = end[0] - start[0], end[1] - start[1]
    chord_length = math.hypot(chord_x, chord_y)
    if chord_length <= 1e-9:
        raise AutoModConversionError(f"Edge {edge_index} ARC의 시작점과 끝점이 같습니다.")

    radius = ARC_RADIUS_MILLIMETERS
    if chord_length > 2.0 * radius + ARC_RADIUS_TOLERANCE_MILLIMETERS:
        raise AutoModConversionError(
            f"Edge {edge_index} ARC의 양 끝점 거리가 {chord_length:.3f} mm여서 "
            f"반지름 {radius:g} mm 원호를 만들 수 없습니다."
        )

    half_chord = min(chord_length * 0.5, radius)
    center_offset = math.sqrt(max(0.0, radius * radius - half_chord * half_chord))
    midpoint = ((start[0] + end[0]) * 0.5, (start[1] + end[1]) * 0.5)
    normal = (-chord_y / chord_length, chord_x / chord_length)
    candidates = [
        (
            midpoint[0] + sign * normal[0] * center_offset,
            midpoint[1] + sign * normal[1] * center_offset,
        )
        for sign in (-1.0, 1.0)
    ]
    center = min(
        candidates,
        key=lambda candidate: sum(
            abs(math.dist(point, candidate) - radius) for point in points
        ),
    )
    maximum_error = max(abs(math.dist(point, center) - radius) for point in points)
    if maximum_error > ARC_RADIUS_TOLERANCE_MILLIMETERS:
        raise AutoModConversionError(
            f"Edge {edge_index} ARC가 반지름 {radius:g} mm 원호와 일치하지 않습니다 "
            f"(최대 오차 {maximum_error:.3f} mm)."
        )

    angles = [math.atan2(point[1] - center[1], point[0] - center[0]) for point in points]
    deltas: list[float] = []
    for previous, current in zip(angles, angles[1:]):
        delta = (current - previous + math.pi) % (2.0 * math.pi) - math.pi
        if abs(delta) > 1e-10:
            deltas.append(delta)
    if not deltas or any(delta * deltas[0] < 0 for delta in deltas[1:]):
        raise AutoModConversionError(
            f"Edge {edge_index} ARC geometry의 진행 방향이 연속적이지 않습니다."
        )
    sweep = sum(deltas)
    if abs(sweep) <= 1e-9 or abs(sweep) > 2.0 * math.pi + 1e-6:
        raise AutoModConversionError(f"Edge {edge_index} ARC의 회전각이 올바르지 않습니다.")
    return center, sweep


def _guide_paths(
    graph: dict[str, Any],
) -> tuple[list[GuidePath], list[tuple[float, float]]]:
    raw_nodes = graph.get("nodes")
    raw_edges = graph.get("edges")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise AutoModConversionError("Graph에 Node가 없습니다.")
    if not isinstance(raw_edges, list) or not raw_edges:
        raise AutoModConversionError("Graph에 Edge가 없습니다.")

    source_nodes = [
        _point(value, label=f"Node {index}")
        for index, value in enumerate(raw_nodes)
    ]
    scale = _unit_scale(graph)
    nodes = [_scaled(point, scale) for point in source_nodes]
    paths: list[GuidePath] = []
    connected_nodes: set[int] = set()

    for edge_index, edge in enumerate(raw_edges):
        if not isinstance(edge, dict):
            raise AutoModConversionError(f"Edge {edge_index} 형식이 올바르지 않습니다.")
        points, source, target = _edge_points(
            edge, source_nodes, edge_index=edge_index
        )
        points = [_scaled(point, scale) for point in points]
        if math.dist(points[0], points[-1]) <= 1e-9:
            raise AutoModConversionError(f"Edge {edge_index}의 길이가 0입니다.")
        center: tuple[float, float] | None = None
        sweep: float | None = None
        if str(edge.get("geometry_type", "")).casefold() == "arc":
            center, sweep = _fixed_radius_arc(points, edge_index=edge_index)
        path = GuidePath(
            name=f"path{len(paths) + 1}",
            start=points[0],
            end=points[-1],
            source_node=source,
            target_node=target,
            center=center,
            sweep_radians=sweep,
        )
        paths.append(path)
        connected_nodes.update((source, target))

    isolated_nodes = sorted(set(range(len(nodes))) - connected_nodes)
    if isolated_nodes:
        preview = ", ".join(str(index) for index in isolated_nodes[:8])
        raise AutoModConversionError(
            f"Guide Path에 연결되지 않은 Node가 있습니다: {preview}"
        )
    return paths, nodes


def _project_to_path(
    point: tuple[float, float], path: GuidePath
) -> tuple[float, float]:
    """Return ``(distance_error, distance_along_path)`` for the nearest point."""

    if not path.is_arc:
        vector = (path.end[0] - path.start[0], path.end[1] - path.start[1])
        length_squared = vector[0] * vector[0] + vector[1] * vector[1]
        parameter = (
            (point[0] - path.start[0]) * vector[0]
            + (point[1] - path.start[1]) * vector[1]
        ) / length_squared
        parameter = max(0.0, min(1.0, parameter))
        projected = (
            path.start[0] + vector[0] * parameter,
            path.start[1] + vector[1] * parameter,
        )
        return math.dist(point, projected), path.length * parameter

    assert path.center is not None
    assert path.sweep_radians is not None
    radius = math.dist(path.start, path.center)
    start_angle = math.atan2(
        path.start[1] - path.center[1], path.start[0] - path.center[0]
    )
    point_angle = math.atan2(
        point[1] - path.center[1], point[0] - path.center[0]
    )
    candidates = [
        (math.dist(point, path.start), 0.0),
        (math.dist(point, path.end), path.length),
    ]
    if path.sweep_radians > 0:
        swept_angle = (point_angle - start_angle) % (2.0 * math.pi)
    else:
        swept_angle = (start_angle - point_angle) % (2.0 * math.pi)
    if swept_angle <= abs(path.sweep_radians) + 1e-9:
        projection_angle = (
            start_angle + swept_angle
            if path.sweep_radians > 0
            else start_angle - swept_angle
        )
        projected = (
            path.center[0] + radius * math.cos(projection_angle),
            path.center[1] + radius * math.sin(projection_angle),
        )
        candidates.append((math.dist(point, projected), radius * swept_angle))
    return min(candidates, key=lambda candidate: (candidate[0], candidate[1]))


def _control_point_name(text: str, *, fallback_index: int) -> str:
    normalized = []
    previous_was_separator = False
    for character in text.strip().casefold():
        if character.isascii() and character.isalnum():
            normalized.append(character)
            previous_was_separator = False
        elif normalized and not previous_was_separator:
            normalized.append("_")
            previous_was_separator = True
    name = "".join(normalized).strip("_")
    if not name:
        name = f"station_{fallback_index}"
    if not name.startswith("station"):
        name = f"station_{name}"
    return name


def _station_control_points(
    graph: dict[str, Any], paths: Sequence[GuidePath]
) -> list[ControlPoint]:
    metadata = graph.get("metadata", {})
    raw_labels = metadata.get("labels", []) if isinstance(metadata, dict) else []
    station_labels = [
        label
        for label in raw_labels
        if isinstance(label, dict)
        and str(label.get("text", "")).strip().casefold().startswith("station")
    ]
    if not station_labels:
        raise AutoModConversionError(
            "CAD에서 station 이름의 TEXT/MTEXT를 찾지 못했습니다."
        )

    scale = _unit_scale(graph)
    control_points: list[ControlPoint] = []
    used_names: set[str] = set()
    for index, label in enumerate(station_labels, start=1):
        name = _control_point_name(str(label.get("text", "")), fallback_index=index)
        if name in used_names:
            raise AutoModConversionError(f"중복된 Station 이름입니다: {name}")
        used_names.add(name)
        try:
            position = _scaled((float(label["x"]), float(label["y"])), scale)
        except (KeyError, TypeError, ValueError) as error:
            raise AutoModConversionError(
                f"Station {name} 좌표가 올바르지 않습니다."
            ) from error
        path, (_, distance) = min(
            ((path, _project_to_path(position, path)) for path in paths),
            key=lambda candidate: (
                candidate[1][0],
                candidate[0].name,
                candidate[1][1],
            ),
        )
        control_points.append(
            ControlPoint(name, "StationControlPoint", path.name, distance)
        )
    return control_points


def _branch_control_points(paths: Sequence[GuidePath]) -> list[ControlPoint]:
    """Anchor route decisions on the common approach, never an outgoing edge.

    A control point placed exactly at a split can be owned by either outgoing
    AutoMod guide path.  Keeping it 10 mm before the junction makes the point
    unambiguously belong to the single incoming path, so a later Dijkstra
    router can evaluate both outgoing alternatives from the same route node.
    """

    outgoing: dict[int, list[GuidePath]] = {}
    incoming: dict[int, list[GuidePath]] = {}
    for path in paths:
        if path.source_node is not None:
            outgoing.setdefault(path.source_node, []).append(path)
        if path.target_node is not None:
            incoming.setdefault(path.target_node, []).append(path)

    branch_nodes = sorted(node for node, linked in outgoing.items() if len(linked) >= 2)
    control_points: list[ControlPoint] = []
    for index, node in enumerate(branch_nodes, start=1):
        approach_paths = incoming.get(node, [])
        if len(approach_paths) != 1:
            raise AutoModConversionError(
                f"분기 Node {node}의 진입 Edge가 {len(approach_paths)}개여서 "
                "10 mm 전 Branch 위치를 하나로 결정할 수 없습니다."
            )
        approach = approach_paths[0]
        if approach.length < BRANCH_OFFSET_MILLIMETERS:
            raise AutoModConversionError(
                f"분기 Node {node}의 진입 Edge가 10 mm보다 짧습니다."
            )
        control_points.append(
            ControlPoint(
                f"branch_{index}",
                "BranchControlPoint",
                # Deliberately attach to the common incoming path.  Attaching
                # at the junction can bind the CP to one outgoing alternative.
                approach.name,
                approach.length - BRANCH_OFFSET_MILLIMETERS,
            )
        )
    return control_points


def render_pm_asy(graph: dict[str, Any]) -> str:
    """Render a complete AutoMod 12.6 AGVS system as CRLF text."""

    paths, _ = _guide_paths(graph)
    stations = _station_control_points(graph, paths)
    branches = _branch_control_points(paths)
    seed_cp = stations[0]

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
        f"AGVSDEF secname {seed_cp.path_name} name {seed_cp.name} UserId 2",
        f"\tNEXTPATH name {seed_cp.path_name} type DefaultGuidePath",
        f"\tNEXTCP name {seed_cp.name} type StationControlPoint",
        "\tALTERNATE NONE ResumeSpeedWhenClaimed",
        "\tvel 0 Infinite Meters Seconds",
        "\tcrabvel 0 Infinite Meters Seconds",
        "\tsprvel 0 Infinite Meters Seconds",
        "\tcrvvel 0 Infinite Meters Seconds",
        "AGVSTOL minang 150 maxang 1800",
        # ``nav`` is AutoMod's route-cost factor, not a direction-marker scale.
        # Keep it at the native default so exporting never changes AGV routing.
        "GPATHTYPE name DefaultGuidePath one normal attach rigid color 0 nav 1 "
        "vel 1 0 Meters Seconds",
    ]
    for path in paths:
        if path.is_arc:
            assert path.center is not None
            assert path.sweep_radians is not None
            lines.append(
                "GPATH name {name} type DefaultGuidePath piece cenx {cenx} ceny {ceny} "
                "begx {begx} begy {begy} upz 1 angle {angle}".format(
                    name=path.name,
                    cenx=_number(path.center[0]),
                    ceny=_number(path.center[1]),
                    begx=_number(path.start[0]),
                    begy=_number(path.start[1]),
                    angle=_number(math.degrees(path.sweep_radians) * 10.0),
                )
            )
        else:
            lines.append(
                "GPATH name {name} type DefaultGuidePath piece begx {begx} begy {begy} "
                "endx {endx} endy {endy} upz 1".format(
                    name=path.name,
                    begx=_number(path.start[0]),
                    begy=_number(path.start[1]),
                    endx=_number(path.end[0]),
                    endy=_number(path.end[1]),
                )
            )
    lines.append(
        "CPOINTTYPE name StationControlPoint cap 2147483647 release distance 0 Feet "
        f"align leadingpap limit Infinite scale {_number(STATION_CONTROL_POINT_SCALE)} "
        f"color -1 nrot 0 nscale {_number(STATION_CONTROL_POINT_SCALE)}"
    )
    lines.append(
        "CPOINTTYPE name BranchControlPoint cap 2147483647 release distance 0 Feet "
        f"align leadingpap limit Infinite scale {_number(BRANCH_CONTROL_POINT_SCALE)} "
        f"color -1 nrot 0 nscale {_number(BRANCH_CONTROL_POINT_SCALE)}"
    )
    for control_point in [*stations, *branches]:
        lines.append(
            f"CPOINT name {control_point.name} type {control_point.type_name} "
            f"at {control_point.path_name} {_number(control_point.distance)}"
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


def render_model_process_asy() -> str:
    """Render the empty Process system registered as ``model~``.

    AutoMod still expects a Process system entry in the model manifest even
    when no model logic has been written yet.  This file intentionally has no
    process declarations, embedded logic, or references to ``.m`` sources.
    """

    lines = [
        f"VERSION {AUTOMOD_VERSION}",
        "SYSTYPE Process",
        "UNITS Millimeters Seconds",
        "SYSDEF UtilByAvail off RefCheck on debugger on warningMessages off report standard",
        "FLAGS",
        "\tSystem Inherit",
        "\tText Inherit",
        "\tResources Inherit",
        "\tResource Names Invisible Inherit",
        "\tQueues Inherit",
        "\tQueue Names Invisible Inherit",
        "\tQueue Amounts Invisible Inherit",
        "\tBlocks Invisible Inherit",
        "\tBlock Names Invisible Inherit",
        "\tLabels Inherit",
        "PROCDEF UserId 1",
    ]
    return "\r\n".join(lines) + "\r\n"


def render_model_amo(graph: dict[str, Any]) -> str:
    """Render ``model.amo`` and link ``pm`` with the empty ``model~`` system."""

    paths, _ = _guide_paths(graph)
    xs = [coordinate for path in paths for coordinate in (path.start[0], path.end[0])]
    ys = [coordinate for path in paths for coordinate in (path.start[1], path.end[1])]
    span = max(max(xs) - min(xs), max(ys) - min(ys))
    margin = max(span * 0.05, 1000.0)
    lines = [
        f"VERSION {AUTOMOD_VERSION}",
        "UNITS Millimeters Seconds",
        "RNSET 1",
        "DRAWPOS minx {minx} maxx {maxx} miny {miny} maxy {maxy} "
        "minz 0 maxz 300 trx 0 try 0".format(
            minx=_number(min(xs) - margin),
            maxx=_number(max(xs) + margin),
            miny=_number(min(ys) - margin),
            maxy=_number(max(ys) + margin),
        ),
        "MOVESYS name pm",
        "\tSYSPOS endx 1",
        "PROCSYS name model~",
        "\tSYSPOS endx 1",
        "CONTROL snaplen 1 Hours counts 10 autorep reset",
    ]
    return "\r\n".join(lines) + "\r\n"


def save_pm_asy(graph: dict[str, Any], filename: str | Path) -> Path:
    """Validate and save ``pm.asy`` using AutoMod's native CRLF convention."""

    path = Path(filename).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    content = render_pm_asy(graph)
    with path.open("w", encoding="ascii", newline="") as stream:
        stream.write(content)
    return path.resolve()


def save_automod_model(graph: dict[str, Any], archive: str | Path) -> AutoModModelFiles:
    """Create a source-free ``model.arc`` directory and its three core files.

    Existing generated archives can be refreshed, but a directory containing
    any unrelated file is rejected so user-authored AutoMod content is never
    overwritten or accidentally included in a source-free export.
    """

    archive_path = Path(archive).expanduser()
    if archive_path.suffix.casefold() != ".arc":
        archive_path = archive_path.with_suffix(".arc")
    if archive_path.exists() and not archive_path.is_dir():
        raise AutoModConversionError(f"AutoMod ARC 경로가 폴더가 아닙니다: {archive_path}")

    generated_names = {"model.amo", "model~.asy", "pm.asy"}
    if archive_path.is_dir():
        unrelated = sorted(entry.name for entry in archive_path.iterdir() if entry.name not in generated_names)
        if unrelated:
            preview = ", ".join(unrelated[:8])
            raise AutoModConversionError(
                f"기존 ARC 폴더에 변환기가 생성하지 않은 항목이 있습니다: {preview}"
            )

    # Render first so validation failure cannot leave a partially generated
    # archive on disk.
    pm_content = render_pm_asy(graph)
    process_content = render_model_process_asy()
    manifest_content = render_model_amo(graph)

    archive_path.mkdir(parents=True, exist_ok=True)
    outputs = {
        "model.amo": manifest_content,
        "model~.asy": process_content,
        "pm.asy": pm_content,
    }
    for name, content in outputs.items():
        with (archive_path / name).open("w", encoding="ascii", newline="") as stream:
            stream.write(content)

    resolved = archive_path.resolve()
    return AutoModModelFiles(
        archive=resolved,
        manifest=resolved / "model.amo",
        process_system=resolved / "model~.asy",
        movement_system=resolved / "pm.asy",
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="방향성 Graph JSON을 AutoMod model.arc로 변환합니다.")
    parser.add_argument("input", type=Path, help="입력 Graph JSON")
    parser.add_argument("-o", "--output", type=Path, help="출력 model.arc 폴더")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    output = args.output or args.input.with_name("model.arc")
    try:
        with args.input.open("r", encoding="utf-8-sig") as stream:
            graph = json.load(stream)
        if not isinstance(graph, dict):
            raise AutoModConversionError("Graph JSON 최상위 값은 object여야 합니다.")
        saved = save_automod_model(graph, output)
    except (AutoModConversionError, OSError, json.JSONDecodeError) as error:
        print(f"AutoMod 변환 실패: {error}")
        return 2
    print(f"AutoMod 변환 완료: {saved.archive}")
    print("  model.amo -> MOVESYS pm + PROCSYS model~")
    print("  pm.asy")
    print("  model~.asy (소스코드 없음)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
