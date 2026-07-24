"""Deterministic edge-centreline vehicle simulation used by the 2D debug renderer.

This module deliberately contains no Qt code.  The simulation clock, job release,
dispatch, route traversal, ten-second pickup/setdown service, and edge reservation
remain testable independently from the animation refresh rate.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Mapping

from random_flow_analysis import RandomFlowError, _FacilityRouter


DEFAULT_TRANSFER_DURATION_US = 10_000_000
_INTERNAL_STEP_US = 50_000


def format_simulation_time(time_us: int) -> str:
    """Format integer microseconds as AutoMod-like HH:MM:SS.mmm."""

    milliseconds = max(0, int(time_us)) // 1_000
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1_000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{millis:03d}"


@dataclass(frozen=True)
class EdgeGeometry:
    edge_id: str
    points_um: tuple[tuple[float, float], ...]
    segment_lengths_um: tuple[float, ...]
    length_um: float
    speed_limit_um_per_s: float

    @classmethod
    def from_facility_edge(cls, raw: Mapping[str, Any]) -> "EdgeGeometry":
        edge_id = str(raw.get("id", "")).strip()
        raw_points = raw.get("polyline_um", [])
        points: list[tuple[float, float]] = []
        if isinstance(raw_points, list):
            for item in raw_points:
                if not isinstance(item, Mapping):
                    continue
                points.append((float(item.get("x", 0.0)), float(item.get("y", 0.0))))
        if len(points) < 2:
            raise RandomFlowError(f"Vehicle simulation Edge geometry가 없습니다: {edge_id}")
        segments = tuple(
            math.dist(first, second) for first, second in zip(points, points[1:])
        )
        calculated = sum(segments)
        declared = float(raw.get("length_um", 0.0) or 0.0)
        length = calculated if calculated > 0.0 else declared
        speed = float(raw.get("speed_limit_um_per_s", 0.0) or 0.0)
        if not edge_id or length <= 0.0 or speed <= 0.0:
            raise RandomFlowError(f"Vehicle simulation Edge 정의가 올바르지 않습니다: {edge_id}")
        return cls(edge_id, tuple(points), segments, length, speed)

    def point_at(self, distance_um: float) -> tuple[float, float, float]:
        """Return x, y and heading degrees at distance along the directed edge."""

        remaining = max(0.0, min(float(distance_um), self.length_um))
        for index, segment_length in enumerate(self.segment_lengths_um):
            first = self.points_um[index]
            second = self.points_um[index + 1]
            if segment_length <= 1e-9:
                continue
            if remaining <= segment_length or index == len(self.segment_lengths_um) - 1:
                ratio = max(0.0, min(1.0, remaining / segment_length))
                x = first[0] + (second[0] - first[0]) * ratio
                y = first[1] + (second[1] - first[1]) * ratio
                heading = math.degrees(
                    math.atan2(second[1] - first[1], second[0] - first[0])
                )
                return x, y, heading
            remaining -= segment_length
        first, second = self.points_um[-2], self.points_um[-1]
        heading = math.degrees(math.atan2(second[1] - first[1], second[0] - first[0]))
        return second[0], second[1], heading


@dataclass
class _JobRuntime:
    job_id: str
    pickup_station_id: str
    dropoff_station_id: str
    release_time_us: int
    state: str = "PENDING"
    assigned_vehicle_id: str = ""


@dataclass
class _VehicleRuntime:
    vehicle_id: str
    current_station_id: str
    x_um: float
    y_um: float
    heading_deg: float = 0.0
    state: str = "IDLE"
    job_id: str = ""
    carrying: bool = False
    blocked: bool = False
    route_edge_ids: tuple[str, ...] = ()
    route_index: int = 0
    edge_distance_um: float = 0.0
    on_edge: bool = False
    destination_station_id: str = ""
    service_remaining_us: int = 0


class VisualVehicleSimulation:
    """Small deterministic DES for validating centreline vehicle animation."""

    def __init__(
        self,
        facility: Mapping[str, Any],
        scenario: Mapping[str, Any],
        *,
        vehicle_count: int = 8,
        pickup_duration_us: int = DEFAULT_TRANSFER_DURATION_US,
        setdown_duration_us: int = DEFAULT_TRANSFER_DURATION_US,
    ) -> None:
        if vehicle_count < 1:
            raise RandomFlowError("Vehicle 수는 1대 이상이어야 합니다.")
        if pickup_duration_us < 0 or setdown_duration_us < 0:
            raise RandomFlowError("이적재 시간은 0 이상이어야 합니다.")

        self.facility = dict(facility)
        self.scenario = dict(scenario)
        self.router = _FacilityRouter(facility)
        self.pickup_duration_us = int(pickup_duration_us)
        self.setdown_duration_us = int(setdown_duration_us)
        self.time_us = 0
        self.running = True
        self.events: list[dict[str, Any]] = []
        self.edge_occupancy: dict[str, str] = {}

        self.edges = {
            str(raw.get("id", "")): EdgeGeometry.from_facility_edge(raw)
            for raw in facility.get("edges", [])
            if isinstance(raw, Mapping)
        }
        self.station_positions = {
            str(raw.get("id", "")): (
                float((raw.get("position_um") or {}).get("x", 0.0)),
                float((raw.get("position_um") or {}).get("y", 0.0)),
            )
            for raw in facility.get("stations", [])
            if isinstance(raw, Mapping) and raw.get("id")
        }
        station_ids = sorted(self.station_positions)
        if len(station_ids) < 2:
            raise RandomFlowError("2D Vehicle Simulation에는 Station이 2개 이상 필요합니다.")

        count = int(vehicle_count)
        self.vehicles: dict[str, _VehicleRuntime] = {}
        for index in range(count):
            station_id = station_ids[index % len(station_ids)]
            x_um, y_um = self.station_positions[station_id]
            vehicle_id = f"SIM-OHT-{index + 1:03d}"
            self.vehicles[vehicle_id] = _VehicleRuntime(
                vehicle_id=vehicle_id,
                current_station_id=station_id,
                x_um=x_um,
                y_um=y_um,
            )

        self.jobs: dict[str, _JobRuntime] = {}
        raw_jobs = scenario.get("jobs", [])
        if not isinstance(raw_jobs, list) or not raw_jobs:
            raise RandomFlowError("랜덤 FromTo Scenario에 Job이 없습니다.")
        for index, raw in enumerate(raw_jobs):
            if not isinstance(raw, Mapping):
                continue
            job_id = str(raw.get("id", "") or f"JOB-{index + 1:06d}")
            pickup = str(raw.get("pickup_station_id", ""))
            dropoff = str(raw.get("dropoff_station_id", ""))
            if pickup not in self.station_positions or dropoff not in self.station_positions:
                raise RandomFlowError(f"Job Station이 현재 Layout에 없습니다: {job_id}")
            self.jobs[job_id] = _JobRuntime(
                job_id=job_id,
                pickup_station_id=pickup,
                dropoff_station_id=dropoff,
                release_time_us=max(0, int(raw.get("release_time_us", 0) or 0)),
            )
        if not self.jobs:
            raise RandomFlowError("실행 가능한 Job이 없습니다.")

        self._record("SIMULATION_READY", "", "", f"vehicles={len(self.vehicles)}")

    @property
    def completed_job_count(self) -> int:
        return sum(job.state == "COMPLETED" for job in self.jobs.values())

    @property
    def released_job_count(self) -> int:
        return sum(job.release_time_us <= self.time_us for job in self.jobs.values())

    @property
    def pending_job_count(self) -> int:
        return sum(
            job.release_time_us <= self.time_us and job.state == "PENDING"
            for job in self.jobs.values()
        )

    @property
    def is_finished(self) -> bool:
        return self.completed_job_count == len(self.jobs)

    def _record(
        self,
        event_type: str,
        vehicle_id: str,
        job_id: str,
        detail: str = "",
    ) -> None:
        self.events.append(
            {
                "time_us": self.time_us,
                "event_type": event_type,
                "vehicle_id": vehicle_id,
                "job_id": job_id,
                "detail": detail,
            }
        )
        if len(self.events) > 2_000:
            del self.events[:1_000]

    def tick(self, delta_us: int) -> None:
        """Advance with fixed internal steps so UI frame rate cannot change results."""

        remaining = max(0, int(delta_us))
        while remaining > 0 and not self.is_finished:
            step = min(_INTERNAL_STEP_US, remaining)
            self._step(step)
            remaining -= step

    def _step(self, step_us: int) -> None:
        self.time_us += step_us
        self._dispatch_jobs()

        for vehicle_id in sorted(self.vehicles):
            vehicle = self.vehicles[vehicle_id]
            if vehicle.state in {"LOADING", "UNLOADING"}:
                self._advance_service(vehicle, step_us)
            elif vehicle.state in {"TO_PICKUP", "TO_SETDOWN"}:
                self._advance_route(vehicle, step_us)

        self._dispatch_jobs()

    def _dispatch_jobs(self) -> None:
        available = [
            vehicle
            for vehicle in self.vehicles.values()
            if vehicle.state == "IDLE" and not vehicle.job_id
        ]
        available.sort(key=lambda vehicle: vehicle.vehicle_id)
        if not available:
            return

        for job in sorted(
            self.jobs.values(), key=lambda item: (item.release_time_us, item.job_id)
        ):
            if job.release_time_us > self.time_us or job.state != "PENDING":
                continue
            candidates: list[tuple[int, str, _VehicleRuntime, tuple[str, ...]]] = []
            for vehicle in available:
                route = self.router.route_stations(
                    vehicle.current_station_id, job.pickup_station_id
                )
                if route is None:
                    continue
                candidates.append(
                    (route.travel_time_us, vehicle.vehicle_id, vehicle, route.edge_ids)
                )
            if not candidates:
                continue
            _travel_time, _vehicle_id, vehicle, route_edge_ids = min(candidates)
            available.remove(vehicle)
            job.state = "ASSIGNED"
            job.assigned_vehicle_id = vehicle.vehicle_id
            vehicle.job_id = job.job_id
            vehicle.carrying = False
            self._record(
                "JOB_ASSIGNED",
                vehicle.vehicle_id,
                job.job_id,
                f"{vehicle.current_station_id}->{job.pickup_station_id}",
            )
            self._start_route(
                vehicle,
                route_edge_ids,
                job.pickup_station_id,
                state="TO_PICKUP",
            )
            if not available:
                break

    def _start_route(
        self,
        vehicle: _VehicleRuntime,
        edge_ids: tuple[str, ...],
        destination_station_id: str,
        *,
        state: str,
    ) -> None:
        vehicle.state = state
        vehicle.route_edge_ids = tuple(edge_ids)
        vehicle.route_index = 0
        vehicle.edge_distance_um = 0.0
        vehicle.on_edge = False
        vehicle.blocked = False
        vehicle.destination_station_id = destination_station_id
        if not edge_ids:
            self._arrive_route_destination(vehicle)

    def _advance_route(self, vehicle: _VehicleRuntime, step_us: int) -> None:
        remaining_time_us = int(step_us)
        while remaining_time_us > 0 and vehicle.state in {"TO_PICKUP", "TO_SETDOWN"}:
            if vehicle.route_index >= len(vehicle.route_edge_ids):
                self._arrive_route_destination(vehicle)
                return

            edge_id = vehicle.route_edge_ids[vehicle.route_index]
            edge = self.edges[edge_id]
            if not vehicle.on_edge:
                owner = self.edge_occupancy.get(edge_id)
                if owner and owner != vehicle.vehicle_id:
                    vehicle.blocked = True
                    return
                self.edge_occupancy[edge_id] = vehicle.vehicle_id
                vehicle.on_edge = True
                vehicle.blocked = False
                vehicle.edge_distance_um = 0.0
                self._record("EDGE_ENTERED", vehicle.vehicle_id, vehicle.job_id, edge_id)

            remaining_distance = max(0.0, edge.length_um - vehicle.edge_distance_um)
            travel_distance = edge.speed_limit_um_per_s * remaining_time_us / 1_000_000.0
            if travel_distance + 1e-6 < remaining_distance:
                vehicle.edge_distance_um += travel_distance
                vehicle.x_um, vehicle.y_um, vehicle.heading_deg = edge.point_at(
                    vehicle.edge_distance_um
                )
                return

            time_to_finish = max(
                1,
                int(
                    math.ceil(
                        remaining_distance * 1_000_000.0
                        / edge.speed_limit_um_per_s
                    )
                ),
            )
            vehicle.edge_distance_um = edge.length_um
            vehicle.x_um, vehicle.y_um, vehicle.heading_deg = edge.point_at(
                edge.length_um
            )
            if self.edge_occupancy.get(edge_id) == vehicle.vehicle_id:
                del self.edge_occupancy[edge_id]
            vehicle.on_edge = False
            vehicle.route_index += 1
            remaining_time_us = max(0, remaining_time_us - time_to_finish)
            self._record("EDGE_EXITED", vehicle.vehicle_id, vehicle.job_id, edge_id)

            if vehicle.route_index >= len(vehicle.route_edge_ids):
                self._arrive_route_destination(vehicle)
                return

    def _arrive_route_destination(self, vehicle: _VehicleRuntime) -> None:
        destination = vehicle.destination_station_id
        vehicle.current_station_id = destination
        if destination in self.station_positions:
            vehicle.x_um, vehicle.y_um = self.station_positions[destination]
        vehicle.route_edge_ids = ()
        vehicle.route_index = 0
        vehicle.edge_distance_um = 0.0
        vehicle.on_edge = False
        vehicle.blocked = False

        job = self.jobs[vehicle.job_id]
        if vehicle.state == "TO_PICKUP":
            vehicle.state = "LOADING"
            vehicle.service_remaining_us = self.pickup_duration_us
            self._record(
                "PICKUP_STARTED",
                vehicle.vehicle_id,
                job.job_id,
                f"station={destination};duration_us={self.pickup_duration_us}",
            )
        elif vehicle.state == "TO_SETDOWN":
            vehicle.state = "UNLOADING"
            vehicle.service_remaining_us = self.setdown_duration_us
            self._record(
                "SETDOWN_STARTED",
                vehicle.vehicle_id,
                job.job_id,
                f"station={destination};duration_us={self.setdown_duration_us}",
            )

    def _advance_service(self, vehicle: _VehicleRuntime, step_us: int) -> None:
        vehicle.service_remaining_us = max(
            0, vehicle.service_remaining_us - int(step_us)
        )
        if vehicle.service_remaining_us > 0:
            return

        job = self.jobs[vehicle.job_id]
        if vehicle.state == "LOADING":
            vehicle.carrying = True
            job.state = "IN_TRANSIT"
            route = self.router.route_stations(
                job.pickup_station_id, job.dropoff_station_id
            )
            if route is None:
                raise RandomFlowError(
                    f"Pickup 후 Setdown 경로를 찾을 수 없습니다: {job.job_id}"
                )
            self._record(
                "PICKUP_COMPLETED",
                vehicle.vehicle_id,
                job.job_id,
                job.pickup_station_id,
            )
            self._start_route(
                vehicle,
                route.edge_ids,
                job.dropoff_station_id,
                state="TO_SETDOWN",
            )
            return

        if vehicle.state == "UNLOADING":
            self._record(
                "SETDOWN_COMPLETED",
                vehicle.vehicle_id,
                job.job_id,
                job.dropoff_station_id,
            )
            job.state = "COMPLETED"
            vehicle.state = "IDLE"
            vehicle.job_id = ""
            vehicle.carrying = False
            vehicle.service_remaining_us = 0
            vehicle.destination_station_id = ""

    def vehicle_snapshots(self) -> tuple[dict[str, Any], ...]:
        snapshots = []
        for vehicle_id in sorted(self.vehicles):
            vehicle = self.vehicles[vehicle_id]
            edge_id = (
                vehicle.route_edge_ids[vehicle.route_index]
                if vehicle.route_index < len(vehicle.route_edge_ids)
                else ""
            )
            snapshots.append(
                {
                    "vehicle_id": vehicle.vehicle_id,
                    "state": vehicle.state,
                    "job_id": vehicle.job_id,
                    "carrying": vehicle.carrying,
                    "blocked": vehicle.blocked,
                    "x_um": vehicle.x_um,
                    "y_um": vehicle.y_um,
                    "heading_deg": vehicle.heading_deg,
                    "edge_id": edge_id,
                    "service_remaining_us": vehicle.service_remaining_us,
                }
            )
        return tuple(snapshots)
