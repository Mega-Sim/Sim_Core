"""Pure geometry helpers for Random From-To vehicle path animation.

The animation keeps a vehicle logically attached to one directed Edge at a time.
World/screen X,Y coordinates are derived from the Edge polyline and the vehicle's
fractional progress, so the rendered vehicle never integrates free X/Y motion and
cannot drift away from the guide-path centerline.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class RoutePose:
    """One vehicle pose derived from a route and elapsed route travel time."""

    edge_id: str
    edge_fraction: float
    x: float
    y: float
    heading_degrees: float
    completed: bool = False


def edge_travel_time_us(length_um: int | float, speed_limit_um_per_s: int | float) -> int:
    """Return deterministic ceil(length/speed) travel time in microseconds."""

    length = int(length_um)
    speed = int(speed_limit_um_per_s)
    if length <= 0:
        raise ValueError("Edge length must be positive.")
    if speed <= 0:
        raise ValueError("Edge speed must be positive.")
    whole_seconds, remainder = divmod(length, speed)
    fractional = (remainder * 1_000_000 + speed - 1) // speed
    return whole_seconds * 1_000_000 + fractional


def interpolate_polyline(
    points: Sequence[tuple[float, float]],
    fraction: float,
) -> tuple[float, float, float]:
    """Interpolate a point and tangent heading along a polyline by arc length.

    ``fraction`` is clamped to 0..1. Degenerate zero-length segments are ignored.
    The returned heading is in degrees and follows the displayed polyline tangent.
    """

    if len(points) < 2:
        raise ValueError("Polyline must contain at least two points.")

    segments: list[tuple[float, float, float, float, float]] = []
    total = 0.0
    for start, end in zip(points, points[1:]):
        x1, y1 = float(start[0]), float(start[1])
        x2, y2 = float(end[0]), float(end[1])
        length = math.hypot(x2 - x1, y2 - y1)
        if length <= 0.0:
            continue
        segments.append((x1, y1, x2, y2, length))
        total += length

    if not segments or total <= 0.0:
        raise ValueError("Polyline must contain a non-zero-length segment.")

    clamped = max(0.0, min(1.0, float(fraction)))
    target = clamped * total
    traversed = 0.0

    for index, (x1, y1, x2, y2, length) in enumerate(segments):
        is_last = index == len(segments) - 1
        if target <= traversed + length or is_last:
            local = max(0.0, min(1.0, (target - traversed) / length))
            x = x1 + (x2 - x1) * local
            y = y1 + (y2 - y1) * local
            heading = math.degrees(math.atan2(y2 - y1, x2 - x1))
            return x, y, heading
        traversed += length

    x1, y1, x2, y2, _length = segments[-1]
    return x2, y2, math.degrees(math.atan2(y2 - y1, x2 - x1))


def route_total_time_us(
    route_edge_ids: Sequence[str],
    edge_geometries: Mapping[str, Mapping[str, object]],
) -> int:
    """Return total directed route travel time from edge length/speed metadata."""

    total = 0
    for edge_id in route_edge_ids:
        geometry = edge_geometries.get(str(edge_id))
        if geometry is None:
            raise KeyError(f"Unknown route Edge: {edge_id}")
        total += edge_travel_time_us(
            int(geometry["length_um"]),
            int(geometry["speed_limit_um_per_s"]),
        )
    return total


def locate_route_pose(
    route_edge_ids: Sequence[str],
    edge_geometries: Mapping[str, Mapping[str, object]],
    elapsed_us: int | float,
) -> RoutePose:
    """Locate a vehicle on its route without ever producing free-space motion.

    The logical state is route Edge + elapsed travel time. For the active Edge,
    elapsed time becomes an Edge fraction; X/Y/heading are then interpolated from
    that Edge's centerline polyline. At an Edge boundary the next Edge starts at
    fraction 0, preserving exact network attachment.
    """

    if not route_edge_ids:
        raise ValueError("Route must contain at least one Edge.")

    remaining = max(0, int(elapsed_us))
    last_pose: RoutePose | None = None

    for edge_id_raw in route_edge_ids:
        edge_id = str(edge_id_raw)
        geometry = edge_geometries.get(edge_id)
        if geometry is None:
            raise KeyError(f"Unknown route Edge: {edge_id}")
        raw_points = geometry.get("points")
        if not isinstance(raw_points, Sequence) or isinstance(raw_points, (str, bytes)):
            raise ValueError(f"Edge {edge_id} has no valid polyline points.")
        points = [(float(item[0]), float(item[1])) for item in raw_points]  # type: ignore[index]
        travel_time = edge_travel_time_us(
            int(geometry["length_um"]),
            int(geometry["speed_limit_um_per_s"]),
        )
        if remaining < travel_time:
            fraction = remaining / travel_time if travel_time > 0 else 0.0
            x, y, heading = interpolate_polyline(points, fraction)
            return RoutePose(edge_id, fraction, x, y, heading, False)

        x, y, heading = interpolate_polyline(points, 1.0)
        last_pose = RoutePose(edge_id, 1.0, x, y, heading, False)
        remaining -= travel_time

    if last_pose is None:
        raise ValueError("Route did not produce a pose.")
    return RoutePose(
        last_pose.edge_id,
        1.0,
        last_pose.x,
        last_pose.y,
        last_pose.heading_degrees,
        True,
    )
