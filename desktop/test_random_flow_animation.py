"""Regression tests for path-bound Random From-To vehicle animation geometry."""

from __future__ import annotations

import math

from random_flow_animation import (
    edge_travel_time_us,
    interpolate_polyline,
    locate_route_pose,
    route_total_time_us,
)


def assert_close(actual: float, expected: float, tolerance: float = 1e-6) -> None:
    if abs(actual - expected) > tolerance:
        raise AssertionError(f"expected {expected}, got {actual}")


def test_interpolate_straight_centerline() -> None:
    x, y, heading = interpolate_polyline([(0.0, 0.0), (100.0, 0.0)], 0.5)
    assert_close(x, 50.0)
    assert_close(y, 0.0)
    assert_close(heading, 0.0)


def test_interpolate_polyline_uses_arc_length() -> None:
    # Total length is 150. At fraction 2/3 the vehicle is exactly at the corner.
    x, y, heading = interpolate_polyline(
        [(0.0, 0.0), (100.0, 0.0), (100.0, 50.0)],
        2.0 / 3.0,
    )
    assert_close(x, 100.0)
    assert_close(y, 0.0)
    # Boundary pose is allowed to use the incoming segment tangent.
    assert_close(heading, 0.0)


def test_route_pose_switches_edges_without_free_xy_drift() -> None:
    edges = {
        "E1": {
            "points": [(0.0, 0.0), (100.0, 0.0)],
            "length_um": 100,
            "speed_limit_um_per_s": 100,
        },
        "E2": {
            "points": [(100.0, 0.0), (100.0, 100.0)],
            "length_um": 100,
            "speed_limit_um_per_s": 100,
        },
    }
    assert edge_travel_time_us(100, 100) == 1_000_000
    assert route_total_time_us(["E1", "E2"], edges) == 2_000_000

    before = locate_route_pose(["E1", "E2"], edges, 500_000)
    assert before.edge_id == "E1"
    assert_close(before.x, 50.0)
    assert_close(before.y, 0.0)
    assert not before.completed

    boundary = locate_route_pose(["E1", "E2"], edges, 1_000_000)
    assert boundary.edge_id == "E2"
    assert_close(boundary.edge_fraction, 0.0)
    assert_close(boundary.x, 100.0)
    assert_close(boundary.y, 0.0)
    assert_close(boundary.heading_degrees, 90.0)

    after = locate_route_pose(["E1", "E2"], edges, 1_500_000)
    assert after.edge_id == "E2"
    assert_close(after.x, 100.0)
    assert_close(after.y, 50.0)
    assert_close(after.heading_degrees, 90.0)

    done = locate_route_pose(["E1", "E2"], edges, 2_500_000)
    assert done.completed
    assert_close(done.x, 100.0)
    assert_close(done.y, 100.0)


def test_heading_tracks_displayed_polyline_tangent() -> None:
    x, y, heading = interpolate_polyline([(0.0, 0.0), (10.0, -10.0)], 0.5)
    assert_close(x, 5.0)
    assert_close(y, -5.0)
    assert_close(heading, -45.0)
    if not math.isfinite(heading):
        raise AssertionError("heading must remain finite")


def main() -> None:
    test_interpolate_straight_centerline()
    test_interpolate_polyline_uses_arc_length()
    test_route_pose_switches_edges_without_free_xy_drift()
    test_heading_tracks_displayed_polyline_tangent()
    print("Random From-To vehicle animation tests passed.")


if __name__ == "__main__":
    main()
