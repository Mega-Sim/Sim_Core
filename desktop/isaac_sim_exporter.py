"""Rough NVIDIA Isaac Sim export helpers for Sim_Core.

The data contract mirrors the AutoMod_Isaacsim project's pm.asy -> JSON work:
AutoMod millimeter geometry is normalized to meters, paths remain directed, and
operational stations are kept separate from routing-only control points.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


class IsaacSimExportError(ValueError):
    """Raised when a Sim_Core/AutoMod layout cannot be exported."""


UNIT_TO_METERS = {
    "millimeter": 0.001,
    "meter": 1.0,
    "micrometer": 0.000001,
    "inch": 0.0254,
}

STATION_RULES: Sequence[tuple[re.Pattern[str], str]] = (
    (re.compile(r"^cp_A\d+", re.IGNORECASE), "equipment"),
    (re.compile(r"^cp_Can_", re.IGNORECASE), "equipment"),
    (re.compile(r"^cp_Cap_", re.IGNORECASE), "equipment"),
    (re.compile(r"^cp_UTB_", re.IGNORECASE), "utb"),
    (re.compile(r"^cp_Park", re.IGNORECASE), "park"),
    (re.compile(r"^cp_EVL_Home_", re.IGNORECASE), "vehicle_home"),
    (re.compile(r"^cp_Out_"), "out_station"),
)

ROUTING_TYPES = {
    "avoid",
    "dummy",
    "steer",
    "high_in",
    "high_out",
    "reroute",
    "route_check",
}


def _finite_pair(value: Any, label: str) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)) or len(value) < 2:
        raise IsaacSimExportError(f"{label} 좌표는 [x, y] 형식이어야 합니다.")
    try:
        point = float(value[0]), float(value[1])
    except (TypeError, ValueError) as error:
        raise IsaacSimExportError(f"{label} 좌표가 숫자가 아닙니다.") from error
    if not all(math.isfinite(item) for item in point):
        raise IsaacSimExportError(f"{label} 좌표에는 NaN 또는 무한대를 사용할 수 없습니다.")
    return point


def _unit_scale(graph: Mapping[str, Any]) -> float:
    unit = str(graph.get("metadata", {}).get("coordinate_unit", "millimeter")).strip().casefold()
    try:
        return UNIT_TO_METERS[unit]
    except KeyError as error:
        raise IsaacSimExportError(f"지원하지 않는 Graph 좌표 단위입니다: {unit}") from error


def _polyline_length(points: Sequence[Sequence[float]]) -> float:
    return sum(
        math.dist((float(a[0]), float(a[1]), float(a[2])), (float(b[0]), float(b[1]), float(b[2])))
        for a, b in zip(points, points[1:])
    )


def _graph_edge_points(
    edge: Mapping[str, Any],
    nodes: Sequence[tuple[float, float]],
    edge_index: int,
) -> tuple[list[tuple[float, float]], int, int]:
    try:
        start = int(edge["start"])
        end = int(edge["end"])
    except (KeyError, TypeError, ValueError) as error:
        raise IsaacSimExportError(f"Edge {edge_index} endpoint가 올바르지 않습니다.") from error
    if start == end or min(start, end) < 0 or max(start, end) >= len(nodes):
        raise IsaacSimExportError(f"Edge {edge_index} endpoint 참조가 올바르지 않습니다.")

    direction = edge.get("dir")
    if direction == [start, end]:
        source, target = start, end
        reverse = False
    elif direction == [end, start]:
        source, target = end, start
        reverse = True
    else:
        source, target = start, end
        reverse = False

    raw_geometry = edge.get("geometry")
    if isinstance(raw_geometry, list) and len(raw_geometry) >= 2:
        points = [_finite_pair(point, f"Edge {edge_index} geometry") for point in raw_geometry]
    else:
        points = [nodes[start], nodes[end]]
    if reverse:
        points.reverse()
    points[0] = nodes[source]
    points[-1] = nodes[target]
    return points, source, target


def build_isaac_layout_from_graph(graph: Mapping[str, Any]) -> dict[str, Any]:
    """Convert the editable Sim_Core Graph JSON contract to an Isaac-friendly layout."""

    raw_nodes = graph.get("nodes")
    raw_edges = graph.get("edges")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise IsaacSimExportError("현재 Graph에 Node가 없습니다.")
    if not isinstance(raw_edges, list) or not raw_edges:
        raise IsaacSimExportError("현재 Graph에 Edge가 없습니다.")

    scale = _unit_scale(graph)
    source_nodes = [_finite_pair(value, f"Node {index}") for index, value in enumerate(raw_nodes)]
    nodes = [
        {"id": f"node_{index:06d}", "position_m": [point[0] * scale, point[1] * scale, 0.0]}
        for index, point in enumerate(source_nodes)
    ]

    edges: list[dict[str, Any]] = []
    source_paths: list[dict[str, Any]] = []
    for edge_index, edge in enumerate(raw_edges):
        if not isinstance(edge, Mapping):
            raise IsaacSimExportError(f"Edge {edge_index} 형식이 올바르지 않습니다.")
        points, source, target = _graph_edge_points(edge, source_nodes, edge_index)
        polyline_m = [[x * scale, y * scale, 0.0] for x, y in points]
        edge_id = f"edge_{edge_index + 1:06d}"
        path_id = f"path_{edge_index + 1:06d}"
        geometry_type = str(edge.get("geometry_type", "line")).casefold()
        item = {
            "id": edge_id,
            "from_node_id": nodes[source]["id"],
            "to_node_id": nodes[target]["id"],
            "source_path_id": path_id,
            "geometry_type": geometry_type,
            "direction": "forward",
            "one_way": True,
            "length_m": _polyline_length(polyline_m),
            "polyline_m": polyline_m,
        }
        edges.append(item)
        source_paths.append(
            {
                "id": path_id,
                "geometry_type": geometry_type,
                "direction": "forward",
                "one_way": True,
                "begin_m": polyline_m[0],
                "end_m": polyline_m[-1],
                "length_m": item["length_m"],
                "polyline_m": polyline_m,
            }
        )

    stations: list[dict[str, Any]] = []
    metadata = graph.get("metadata", {})
    labels = metadata.get("labels", []) if isinstance(metadata, Mapping) else []
    if isinstance(labels, list):
        for index, label in enumerate(labels):
            if not isinstance(label, Mapping):
                continue
            try:
                x = float(label["x"]) * scale
                y = float(label["y"]) * scale
            except (KeyError, TypeError, ValueError):
                continue
            stations.append(
                {
                    "id": str(label.get("text") or f"station_{index + 1:04d}"),
                    "name": str(label.get("text") or f"Station {index + 1}"),
                    "station_type": "cad_label",
                    "position_m": [x, y, 0.0],
                    "tangent_yaw_rad": 0.0,
                }
            )

    return {
        "metadata": {
            "generator": "desktop/isaac_sim_exporter.py",
            "source_kind": "sim_core_graph",
            "source_statistics": {
                "node_count": len(nodes),
                "edge_count": len(edges),
                "station_count": len(stations),
            },
        },
        "coordinate_system": {
            "source_plane": "Sim_Core XY",
            "output_plane": "Isaac Sim XY",
            "up_axis": "Z",
            "output_units": "meters",
        },
        "source_paths": source_paths,
        "nodes": nodes,
        "edges": edges,
        "stations": stations,
        "routing_control_points": [],
        "validation": {
            "errors": [],
            "warnings": [] if stations else ["Graph metadata에서 Station label을 찾지 못했습니다."],
            "summary": {
                "valid": True,
                "node_count": len(nodes),
                "edge_count": len(edges),
                "station_count": len(stations),
            },
        },
    }


def _value_after(tokens: Sequence[str], key: str, default: Any = None) -> Any:
    try:
        return tokens[tokens.index(key) + 1]
    except (ValueError, IndexError):
        return default


def _sample_arc(
    begin: tuple[float, float],
    center: tuple[float, float],
    sweep_radians: float,
    chord_error_mm: float = 5.0,
) -> list[tuple[float, float]]:
    radius = math.dist(begin, center)
    if radius <= 1e-9:
        return [begin]
    max_step = max(0.02, 2.0 * math.acos(max(-1.0, min(1.0, 1.0 - chord_error_mm / radius))))
    segment_count = max(2, int(math.ceil(abs(sweep_radians) / max_step)))
    start_angle = math.atan2(begin[1] - center[1], begin[0] - center[0])
    return [
        (
            center[0] + radius * math.cos(start_angle + sweep_radians * index / segment_count),
            center[1] + radius * math.sin(start_angle + sweep_radians * index / segment_count),
        )
        for index in range(segment_count + 1)
    ]


def _point_on_polyline(points: Sequence[Sequence[float]], distance_m: float) -> tuple[list[float], float]:
    if not points:
        return [0.0, 0.0, 0.0], 0.0
    remaining = max(0.0, distance_m)
    for start, end in zip(points, points[1:]):
        segment = math.dist(start, end)
        if segment <= 1e-12:
            continue
        if remaining <= segment:
            ratio = remaining / segment
            position = [
                float(start[axis]) + (float(end[axis]) - float(start[axis])) * ratio
                for axis in range(3)
            ]
            yaw = math.atan2(float(end[1]) - float(start[1]), float(end[0]) - float(start[0]))
            return position, yaw
        remaining -= segment
    start, end = points[-2], points[-1] if len(points) >= 2 else (points[-1], points[-1])
    yaw = math.atan2(float(end[1]) - float(start[1]), float(end[0]) - float(start[0])) if len(points) >= 2 else 0.0
    return [float(value) for value in points[-1]], yaw


def _classify_control_point(name: str, type_name: str) -> tuple[str, str | None]:
    for pattern, station_type in STATION_RULES:
        if pattern.search(name):
            return "station", station_type
    if type_name.casefold() in ROUTING_TYPES:
        return "routing", type_name
    return "control", None


def load_automod_pm_layout(path: Path) -> dict[str, Any]:
    """Parse the geometry-oriented subset of AutoMod pm.asy used by the rough Isaac workflow."""

    try:
        raw_bytes = path.read_bytes()
        text = raw_bytes.decode("utf-8", errors="replace")
    except OSError as error:
        raise IsaacSimExportError(str(error)) from error

    path_types: dict[str, dict[str, Any]] = {}
    raw_paths: list[dict[str, Any]] = []
    control_points: list[dict[str, Any]] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        tokens = line.split()
        record = tokens[0]
        if record == "GPATHTYPE":
            name = str(_value_after(tokens, "name", f"type_{len(path_types) + 1}"))
            path_types[name] = {
                "one_way": "one" in tokens and "two" not in tokens,
                "direction": "reverse" if "reverse" in tokens else "forward",
            }
        elif record == "GPATH":
            try:
                path_id = str(_value_after(tokens, "name"))
                path_type = str(_value_after(tokens, "type", ""))
                begin = (float(_value_after(tokens, "begx")), float(_value_after(tokens, "begy")))
                if "endx" in tokens:
                    end = (float(_value_after(tokens, "endx")), float(_value_after(tokens, "endy")))
                    geometry_type = "line"
                    sampled_mm = [begin, end]
                else:
                    center = (float(_value_after(tokens, "cenx")), float(_value_after(tokens, "ceny")))
                    sweep_radians = math.radians(float(_value_after(tokens, "angle")) / 10.0)
                    sampled_mm = _sample_arc(begin, center, sweep_radians)
                    end = sampled_mm[-1]
                    geometry_type = "arc"
            except (TypeError, ValueError) as error:
                raise IsaacSimExportError(f"GPATH 파싱 실패: {line}") from error
            inherited = path_types.get(path_type, {})
            raw_paths.append(
                {
                    "id": path_id,
                    "path_type": path_type,
                    "geometry_type": geometry_type,
                    "begin": begin,
                    "end": end,
                    "polyline_mm": sampled_mm,
                    "direction": inherited.get("direction", "forward"),
                    "one_way": bool(inherited.get("one_way", True)),
                }
            )
        elif record == "CPOINT":
            try:
                at_index = tokens.index("at")
                control_points.append(
                    {
                        "id": str(_value_after(tokens, "name", f"cp_{len(control_points) + 1}")),
                        "type": str(_value_after(tokens, "type", "DefaultControlPoint")),
                        "path_id": tokens[at_index + 1],
                        "distance_mm": float(tokens[at_index + 2]),
                    }
                )
            except (ValueError, IndexError, TypeError):
                continue

    if not raw_paths:
        raise IsaacSimExportError("pm.asy에서 GPATH를 찾지 못했습니다.")

    node_ids: dict[tuple[float, float], str] = {}
    nodes: list[dict[str, Any]] = []

    def node_for(point_mm: tuple[float, float]) -> str:
        key = (round(point_mm[0], 3), round(point_mm[1], 3))
        if key not in node_ids:
            node_id = f"node_{len(nodes):06d}"
            node_ids[key] = node_id
            nodes.append(
                {
                    "id": node_id,
                    "position_m": [point_mm[0] / 1000.0, point_mm[1] / 1000.0, 0.0],
                }
            )
        return node_ids[key]

    edges: list[dict[str, Any]] = []
    source_paths: list[dict[str, Any]] = []
    path_map: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(raw_paths):
        polyline_m = [[x / 1000.0, y / 1000.0, 0.0] for x, y in item["polyline_mm"]]
        from_node = node_for(item["begin"])
        to_node = node_for(item["end"])
        if item["direction"] == "reverse":
            polyline_m.reverse()
            from_node, to_node = to_node, from_node
        path_info = {
            "id": item["id"],
            "geometry_type": item["geometry_type"],
            "direction": "forward",
            "one_way": item["one_way"],
            "begin_m": polyline_m[0],
            "end_m": polyline_m[-1],
            "length_m": _polyline_length(polyline_m),
            "polyline_m": polyline_m,
        }
        source_paths.append(path_info)
        path_map[item["id"]] = path_info
        edges.append(
            {
                "id": f"{item['id']}__001",
                "from_node_id": from_node,
                "to_node_id": to_node,
                "source_path_id": item["id"],
                "geometry_type": item["geometry_type"],
                "direction": "forward",
                "one_way": item["one_way"],
                "length_m": path_info["length_m"],
                "polyline_m": polyline_m,
            }
        )

    stations: list[dict[str, Any]] = []
    routing_points: list[dict[str, Any]] = []
    unclassified_points: list[dict[str, Any]] = []
    warnings: list[str] = []
    for point in control_points:
        source_path = path_map.get(point["path_id"])
        if source_path is None:
            warnings.append(f"CPOINT {point['id']} references missing GPATH {point['path_id']}")
            continue
        distance_m = max(0.0, min(float(point["distance_mm"]) / 1000.0, float(source_path["length_m"])))
        position, yaw = _point_on_polyline(source_path["polyline_m"], distance_m)
        classification, subtype = _classify_control_point(point["id"], point["type"])
        record = {
            "id": point["id"],
            "source_path_id": point["path_id"],
            "source_control_point_type": point["type"],
            "position_m": position,
            "tangent_yaw_rad": yaw,
        }
        if classification == "station":
            record["name"] = point["id"]
            record["station_type"] = subtype
            stations.append(record)
        elif classification == "routing":
            record["routing_type"] = subtype
            routing_points.append(record)
        else:
            unclassified_points.append(record)

    return {
        "metadata": {
            "generator": "desktop/isaac_sim_exporter.py",
            "source_kind": "automod_pm_asy",
            "source_file": str(path),
            "source_sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "source_statistics": {
                "gpath_count": len(source_paths),
                "cpoint_count": len(control_points),
                "station_count": len(stations),
            },
        },
        "coordinate_system": {
            "source_plane": "AutoMod XY",
            "output_plane": "Isaac Sim XY",
            "up_axis": "Z",
            "source_units": "millimeters",
            "output_units": "meters",
        },
        "source_paths": source_paths,
        "nodes": nodes,
        "edges": edges,
        "stations": stations,
        "routing_control_points": routing_points,
        "control_points": unclassified_points,
        "validation": {
            "errors": [],
            "warnings": warnings,
            "summary": {
                "valid": True,
                "node_count": len(nodes),
                "edge_count": len(edges),
                "station_count": len(stations),
            },
        },
    }


def save_layout_json(layout: Mapping[str, Any], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(layout, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def _usd_identifier(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9_]", "_", value)
    if not text or text[0].isdigit():
        text = f"item_{text}"
    return text


def _format_points(points: Iterable[Sequence[float]]) -> str:
    return ", ".join(f"({float(x):.6f}, {float(y):.6f}, {float(z):.6f})" for x, y, z in points)


def write_usda(layout: Mapping[str, Any], path: Path) -> Path:
    """Write a dependency-free USDA preview stage that Isaac Sim can open directly."""

    lines = [
        "#usda 1.0",
        "(",
        '    defaultPrim = "World"',
        "    metersPerUnit = 1",
        '    upAxis = "Z"',
        ")",
        "",
        'def Xform "World"',
        "{",
        '    def Scope "GuidePaths"',
        "    {",
    ]
    for index, edge in enumerate(layout.get("edges", [])):
        if not isinstance(edge, Mapping):
            continue
        points = edge.get("polyline_m", [])
        if not isinstance(points, list) or len(points) < 2:
            continue
        name = _usd_identifier(str(edge.get("id", f"edge_{index + 1}")))
        lines.extend(
            [
                f'        def BasisCurves "{name}"',
                "        {",
                '            uniform token type = "linear"',
                '            uniform token wrap = "nonperiodic"',
                f"            int[] curveVertexCounts = [{len(points)}]",
                f"            point3f[] points = [{_format_points(points)}]",
                "            float[] widths = [0.03]",
                '            uniform token widths:interpolation = "constant"',
                "            color3f[] primvars:displayColor = [(0.12, 0.78, 0.72)]",
                "        }",
            ]
        )
    lines.extend(["    }", "", '    def Scope "Stations"', "    {"])
    for index, station in enumerate(layout.get("stations", [])):
        if not isinstance(station, Mapping):
            continue
        position = station.get("position_m", [0.0, 0.0, 0.0])
        if not isinstance(position, (list, tuple)) or len(position) < 3:
            continue
        name = _usd_identifier(str(station.get("id", f"station_{index + 1}")))
        lines.extend(
            [
                f'        def Xform "{name}"',
                "        {",
                f"            double3 xformOp:translate = ({float(position[0]):.6f}, {float(position[1]):.6f}, {float(position[2]):.6f})",
                '            uniform token[] xformOpOrder = ["xformOp:translate"]',
                '            def Cube "Marker"',
                "            {",
                "                double size = 0.18",
                "                color3f[] primvars:displayColor = [(0.95, 0.55, 0.12)]",
                "            }",
                "        }",
            ]
        )
    lines.extend(["    }", "}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def save_isaac_package(layout: Mapping[str, Any], target_dir: Path) -> dict[str, Path]:
    target_dir.mkdir(parents=True, exist_ok=True)
    layout_path = save_layout_json(layout, target_dir / "isaac_layout.json")
    stage_path = write_usda(layout, target_dir / "isaac_stage.usda")
    loader_path = target_dir / "load_in_isaac_sim.py"
    loader_path.write_text(
        '"""Run this script inside NVIDIA Isaac Sim Script Editor."""\n'
        "from pathlib import Path\n"
        "import omni.usd\n\n"
        'stage = Path(__file__).with_name("isaac_stage.usda").resolve()\n'
        "omni.usd.get_context().open_stage(str(stage))\n"
        'print(f"Opened Isaac stage: {stage}")\n',
        encoding="utf-8",
    )
    manifest = {
        "layout_json": layout_path.name,
        "stage_usda": stage_path.name,
        "isaac_loader": loader_path.name,
        "note": "Open isaac_stage.usda directly or run load_in_isaac_sim.py inside Isaac Sim.",
    }
    manifest_path = target_dir / "isaac_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "layout": layout_path,
        "stage": stage_path,
        "loader": loader_path,
        "manifest": manifest_path,
    }
