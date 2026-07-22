"""Deterministic random From-To workload generation and LA-style flow analysis.

The desktop workbench can use this module with only a canonical Facility JSON.
It mirrors Sim_Core's directed, travel-time weighted Dijkstra tie-breaking so the
preview and the authoritative C++ analysis select the same route.
"""

from __future__ import annotations

import csv
import heapq
import json
import os
import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence


HOUR_US = 3_600_000_000
DEFAULT_LOAD_DURATION_US = 2_000_000
DEFAULT_UNLOAD_DURATION_US = 3_000_000
MAXIMUM_SUPPORTED_SPEED_UM_PER_S = 1_000_000_000_000
MIN_ACTIVE_OD_PAIR_LIMIT = 64
MAX_ACTIVE_OD_PAIR_LIMIT = 1_000
ACTIVE_OD_PAIRS_PER_STATION = 4


class RandomFlowError(ValueError):
    """Raised when a facility cannot produce a runnable random workload."""


@dataclass(frozen=True)
class _Edge:
    id: str
    from_node_id: str
    to_node_id: str
    length_um: int
    speed_limit_um_per_s: int


@dataclass(frozen=True)
class _Route:
    edge_ids: tuple[str, ...]
    distance_um: int
    travel_time_us: int


@dataclass(frozen=True)
class GeneratedRandomWorkload:
    """In-memory artifacts produced from one Facility JSON and random seed."""

    scenario: dict[str, Any]
    demands: tuple[dict[str, Any], ...]
    analysis: dict[str, Any]
    sampled_pairs: tuple[tuple[str, str], ...]
    reachable_pair_count: int
    excluded_station_ids: tuple[str, ...]
    moves_per_hour: int
    seed: int


@dataclass(frozen=True)
class SavedRandomWorkload:
    """Paths of a generated workload saved without overwriting existing data."""

    directory: Path
    demand_csv_path: Path
    scenario_json_path: Path
    analysis_json_path: Path


class _FacilityRouter:
    """Directed Dijkstra router with the same deterministic ordering as C++."""

    def __init__(self, facility: Mapping[str, Any]) -> None:
        raw_nodes = facility.get("nodes")
        raw_edges = facility.get("edges")
        raw_stations = facility.get("stations")
        if not isinstance(raw_nodes, list) or not raw_nodes:
            raise RandomFlowError("Facility JSON에 Node가 없습니다.")
        if not isinstance(raw_edges, list) or not raw_edges:
            raise RandomFlowError("Facility JSON에 Edge가 없습니다.")
        if not isinstance(raw_stations, list) or len(raw_stations) < 2:
            raise RandomFlowError(
                "랜덤 From-To 생성에는 Station이 2개 이상 필요합니다."
            )

        self.node_ids: set[str] = set()
        for index, node in enumerate(raw_nodes):
            if not isinstance(node, Mapping):
                raise RandomFlowError(f"Node {index} 형식이 올바르지 않습니다.")
            node_id = str(node.get("id", "")).strip()
            if not node_id or node_id in self.node_ids:
                raise RandomFlowError(f"Node {index}의 ID가 비었거나 중복되었습니다.")
            self.node_ids.add(node_id)

        self.edges: dict[str, _Edge] = {}
        self.outgoing: dict[str, list[_Edge]] = defaultdict(list)
        for index, raw in enumerate(raw_edges):
            if not isinstance(raw, Mapping):
                raise RandomFlowError(f"Edge {index} 형식이 올바르지 않습니다.")
            edge_id = str(raw.get("id", "")).strip()
            from_node = str(raw.get("from_node_id", "")).strip()
            to_node = str(raw.get("to_node_id", "")).strip()
            try:
                length_um = int(raw.get("length_um", 0))
                speed = int(raw.get("speed_limit_um_per_s", 0))
            except (TypeError, ValueError) as error:
                raise RandomFlowError(
                    f"Edge {index}의 길이 또는 속도가 숫자가 아닙니다."
                ) from error
            if not edge_id or edge_id in self.edges:
                raise RandomFlowError(f"Edge {index}의 ID가 비었거나 중복되었습니다.")
            if from_node not in self.node_ids or to_node not in self.node_ids:
                raise RandomFlowError(
                    f"Edge {edge_id}가 존재하지 않는 Node를 참조합니다."
                )
            if length_um <= 0 or speed <= 0:
                raise RandomFlowError(
                    f"Edge {edge_id}의 길이와 제한속도는 0보다 커야 합니다."
                )
            if speed > MAXIMUM_SUPPORTED_SPEED_UM_PER_S:
                raise RandomFlowError(
                    f"Edge {edge_id}의 제한속도가 지원 범위를 초과합니다."
                )
            edge = _Edge(edge_id, from_node, to_node, length_um, speed)
            self.edges[edge_id] = edge
            self.outgoing[from_node].append(edge)
        for linked in self.outgoing.values():
            linked.sort(key=lambda edge: edge.id)

        self.station_nodes: dict[str, str] = {}
        for index, station in enumerate(raw_stations):
            if not isinstance(station, Mapping):
                raise RandomFlowError(f"Station {index} 형식이 올바르지 않습니다.")
            station_id = str(station.get("id", "")).strip()
            node_id = str(station.get("attachment_node_id", "")).strip()
            if not station_id or station_id in self.station_nodes:
                raise RandomFlowError(
                    f"Station {index}의 ID가 비었거나 중복되었습니다."
                )
            if node_id not in self.node_ids:
                raise RandomFlowError(
                    f"Station {station_id}가 존재하지 않는 Node를 참조합니다."
                )
            self.station_nodes[station_id] = node_id

        self._route_cache: dict[tuple[str, str], _Route | None] = {}
        self._source_cache: dict[str, tuple[dict[str, int], dict[str, _Edge]]] = {}

    @staticmethod
    def _travel_time_us(edge: _Edge) -> int:
        whole_seconds, remainder = divmod(edge.length_um, edge.speed_limit_um_per_s)
        fractional = (
            remainder * 1_000_000 + edge.speed_limit_um_per_s - 1
        ) // edge.speed_limit_um_per_s
        return whole_seconds * 1_000_000 + fractional

    def _shortest_tree(
        self, source_node: str
    ) -> tuple[dict[str, int], dict[str, _Edge]]:
        cached = self._source_cache.get(source_node)
        if cached is not None:
            return cached

        best_time: dict[str, int] = {source_node: 0}
        predecessor: dict[str, _Edge] = {}
        frontier: list[tuple[int, str]] = [(0, source_node)]

        def edge_path(node_id: str) -> tuple[str, ...]:
            reverse_path: list[str] = []
            cursor = node_id
            while cursor != source_node:
                edge = predecessor.get(cursor)
                if edge is None:
                    raise RandomFlowError("최단경로 predecessor 연결이 끊어졌습니다.")
                reverse_path.append(edge.id)
                cursor = edge.from_node_id
            return tuple(reversed(reverse_path))

        while frontier:
            current_time, node_id = heapq.heappop(frontier)
            if current_time != best_time.get(node_id):
                continue
            for edge in self.outgoing.get(node_id, ()):
                candidate_time = current_time + self._travel_time_us(edge)
                known_time = best_time.get(edge.to_node_id)
                improves = known_time is None or candidate_time < known_time
                if candidate_time == known_time:
                    candidate_path = edge_path(node_id) + (edge.id,)
                    improves = candidate_path < edge_path(edge.to_node_id)
                if not improves:
                    continue
                best_time[edge.to_node_id] = candidate_time
                predecessor[edge.to_node_id] = edge
                if known_time is None or candidate_time < known_time:
                    heapq.heappush(frontier, (candidate_time, edge.to_node_id))

        result = best_time, predecessor
        self._source_cache[source_node] = result
        return result

    def route_stations(self, from_station_id: str, to_station_id: str) -> _Route | None:
        key = from_station_id, to_station_id
        if key in self._route_cache:
            return self._route_cache[key]
        source_node = self.station_nodes.get(from_station_id)
        target_node = self.station_nodes.get(to_station_id)
        if source_node is None or target_node is None:
            self._route_cache[key] = None
            return None
        if source_node == target_node:
            route = _Route((), 0, 0)
            self._route_cache[key] = route
            return route

        best_time, predecessor = self._shortest_tree(source_node)
        if target_node not in best_time:
            self._route_cache[key] = None
            return None
        cursor = target_node
        edge_ids: list[str] = []
        distance_um = 0
        while cursor != source_node:
            edge = predecessor.get(cursor)
            if edge is None:
                raise RandomFlowError("최단경로 predecessor 연결이 끊어졌습니다.")
            edge_ids.append(edge.id)
            distance_um += edge.length_um
            cursor = edge.from_node_id
        edge_ids.reverse()
        route = _Route(tuple(edge_ids), distance_um, best_time[target_node])
        self._route_cache[key] = route
        return route

    def reachable_station_pairs(self) -> list[tuple[str, str]]:
        """Enumerate reachable OD pairs without retaining every full route.

        A large one-way layout can have tens of thousands of Station pairs and
        routes containing thousands of Edges.  Keeping all reconstructed paths
        would consume excessive memory before any demand is sampled, so this
        pass checks target reachability from one ephemeral shortest-path tree at
        a time.  Full routes are reconstructed only for generated OD rows.
        """

        pairs: list[tuple[str, str]] = []
        station_ids = sorted(self.station_nodes)
        for from_id in station_ids:
            source_node = self.station_nodes[from_id]
            reachable_nodes = {source_node}
            pending = [source_node]
            while pending:
                node_id = pending.pop()
                for edge in self.outgoing.get(node_id, ()):
                    if edge.to_node_id not in reachable_nodes:
                        reachable_nodes.add(edge.to_node_id)
                        pending.append(edge.to_node_id)
            for to_id in station_ids:
                if from_id == to_id:
                    continue
                # Stations attached to the same Node do not create rail traffic.
                target_node = self.station_nodes[to_id]
                if target_node != source_node and target_node in reachable_nodes:
                    pairs.append((from_id, to_id))
        return pairs


def _positive_integer(value: Any, label: str) -> int:
    if isinstance(value, bool):
        raise RandomFlowError(f"{label}은 1 이상의 정수여야 합니다.")
    try:
        parsed = int(value)
    except (TypeError, ValueError) as error:
        raise RandomFlowError(f"{label}은 1 이상의 정수여야 합니다.") from error
    if parsed < 1 or parsed != value:
        raise RandomFlowError(f"{label}은 1 이상의 정수여야 합니다.")
    return parsed


def _safe_identifier(value: Any, fallback: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._:-]+", "-", str(value or "").strip()).strip("-._:")
    return (text or fallback)[:96]


def _build_analysis(
    facility: Mapping[str, Any],
    router: _FacilityRouter,
    demands: Sequence[dict[str, Any]],
    scenario_id: str,
) -> dict[str, Any]:
    edge_moves: Counter[str] = Counter()
    edge_demands: dict[str, list[str]] = defaultdict(list)
    demand_routes: list[dict[str, Any]] = []
    station_inbound: Counter[str] = Counter()
    station_outbound: Counter[str] = Counter()

    for demand in demands:
        from_id = str(demand["from_station_id"])
        to_id = str(demand["to_station_id"])
        rate = float(demand["expected_moves_per_hour"])
        route = router.route_stations(from_id, to_id)
        if route is None or not route.edge_ids:
            raise RandomFlowError(
                f"생성된 From-To 경로를 찾을 수 없습니다: {from_id} → {to_id}"
            )
        demand_routes.append(
            {
                "demand_id": demand["id"],
                "from_station_id": from_id,
                "to_station_id": to_id,
                "expected_moves_per_hour": rate,
                "edge_ids": list(route.edge_ids),
                "distance_um": route.distance_um,
                "travel_time_us": route.travel_time_us,
            }
        )
        station_outbound[from_id] += rate
        station_inbound[to_id] += rate
        for edge_id in route.edge_ids:
            edge_moves[edge_id] += rate
            edge_demands[edge_id].append(str(demand["id"]))

    total_edge_moves = float(sum(edge_moves.values()))
    max_edge_moves = float(max(edge_moves.values(), default=0.0))
    edge_flows: list[dict[str, Any]] = []
    node_inflow: Counter[str] = Counter()
    node_outflow: Counter[str] = Counter()
    node_incoming_edges: Counter[str] = Counter()
    for edge_id in sorted(edge_moves):
        edge = router.edges[edge_id]
        moves = float(edge_moves[edge_id])
        contributing = sorted(edge_demands[edge_id])
        edge_flows.append(
            {
                "edge_id": edge.id,
                "from_node_id": edge.from_node_id,
                "to_node_id": edge.to_node_id,
                "length_um": edge.length_um,
                "expected_moves_per_hour": moves,
                "flow_share": moves / total_edge_moves if total_edge_moves else 0.0,
                "relative_load": moves / max_edge_moves if max_edge_moves else 0.0,
                "demand_count": len(contributing),
                "contributing_demand_ids": contributing,
            }
        )
        node_inflow[edge.to_node_id] += moves
        node_outflow[edge.from_node_id] += moves
        node_incoming_edges[edge.to_node_id] += 1

    node_ids = sorted(set(node_inflow) | set(node_outflow))
    node_flows = [
        {
            "node_id": node_id,
            "inflow_moves_per_hour": float(node_inflow[node_id]),
            "outflow_moves_per_hour": float(node_outflow[node_id]),
            "incoming_edge_count": int(node_incoming_edges[node_id]),
            "merge_pressure": (
                float(node_inflow[node_id])
                if node_incoming_edges[node_id] >= 2
                else 0.0
            ),
        }
        for node_id in node_ids
    ]

    station_capacity = {
        str(station.get("id")): float(
            station.get("handling_capacity_per_hour", 0.0) or 0.0
        )
        for station in facility.get("stations", [])
        if isinstance(station, Mapping)
    }
    station_ids = sorted(set(station_inbound) | set(station_outbound))
    station_flows: list[dict[str, Any]] = []
    for station_id in station_ids:
        inbound = float(station_inbound[station_id])
        outbound = float(station_outbound[station_id])
        peak = max(inbound, outbound)
        capacity = station_capacity.get(station_id, 0.0)
        station_flows.append(
            {
                "station_id": station_id,
                "inbound_moves_per_hour": inbound,
                "outbound_moves_per_hour": outbound,
                "peak_moves_per_hour": peak,
                "handling_capacity_per_hour": capacity,
                "capacity_margin_per_hour": capacity - peak if capacity > 0 else 0.0,
                "utilization_ratio": peak / capacity if capacity > 0 else 0.0,
                "over_capacity": capacity > 0 and peak > capacity,
            }
        )

    return {
        "schema_version": "1.0.0",
        "model_revision_id": str(facility.get("revision_id", "")),
        "scenario_id": scenario_id,
        "status": "PASS",
        "error_count": 0,
        "warning_count": 0,
        "diagnostics": [],
        "demand_routes": demand_routes,
        "edge_flows": edge_flows,
        "node_flows": node_flows,
        "station_flows": station_flows,
        "flow_summary": {
            "total_moves_per_hour": float(
                sum(float(item["expected_moves_per_hour"]) for item in demands)
            ),
            "total_edge_traversals_per_hour": total_edge_moves,
            "max_edge_moves_per_hour": max_edge_moves,
            "used_edge_count": len(edge_flows),
            "total_edge_count": len(router.edges),
        },
    }


def generate_random_workload(
    facility: Mapping[str, Any],
    moves_per_hour: int,
    seed: int,
    *,
    duration_us: int = HOUR_US,
    load_duration_us: int = DEFAULT_LOAD_DURATION_US,
    unload_duration_us: int = DEFAULT_UNLOAD_DURATION_US,
) -> GeneratedRandomWorkload:
    """Generate aggregate From-To demand, individual jobs, and static edge flow.

    Every sampled From-To pair has a non-empty directed route. Duplicate pairs
    are aggregated in the CSV/analysis contract while the Scenario contains one
    released job per requested hourly move.
    """

    total_moves = _positive_integer(moves_per_hour, "시간당 반송수")
    random_seed = _positive_integer(seed, "Random Seed")
    demand_window = _positive_integer(duration_us, "반송 생성 구간")
    if load_duration_us < 0 or unload_duration_us < 0:
        raise RandomFlowError("Load/Unload 시간은 0 이상이어야 합니다.")
    revision_id = str(facility.get("revision_id", "")).strip()
    if not revision_id:
        raise RandomFlowError(
            "실행 가능한 Scenario 생성에는 Facility revision_id가 필요합니다."
        )

    router = _FacilityRouter(facility)
    reachable = router.reachable_station_pairs()
    if not reachable:
        raise RandomFlowError(
            "방향성 레이아웃에서 서로 다른 Station을 잇는 경로가 없습니다. "
            "Edge 방향과 Station 연결 Node를 확인해 주세요."
        )

    rng = random.Random(random_seed)
    station_count = len(router.station_nodes)
    active_pair_limit = min(
        total_moves,
        len(reachable),
        max(
            MIN_ACTIVE_OD_PAIR_LIMIT,
            min(MAX_ACTIVE_OD_PAIR_LIMIT, station_count * ACTIVE_OD_PAIRS_PER_STATION),
        ),
    )
    active_pairs = [
        reachable[index]
        for index in rng.sample(range(len(reachable)), k=active_pair_limit)
    ]
    # Keep the total job count exact while bounding the number of full routes
    # retained in the report.  Otherwise 10,000 moves on a long 173-Station
    # loop could create thousands of multi-thousand-Edge OD route arrays.
    sampled: list[tuple[str, str]] = list(active_pairs)
    while len(sampled) < total_moves:
        sampled.append(active_pairs[rng.randrange(len(active_pairs))])
    rng.shuffle(sampled)
    pair_counts = Counter(sampled)

    demands: list[dict[str, Any]] = []
    for index, ((from_id, to_id), count) in enumerate(
        sorted(pair_counts.items()), start=1
    ):
        demands.append(
            {
                "id": f"RND-OD-{index:04d}",
                "from_station_id": from_id,
                "to_station_id": to_id,
                "expected_moves_per_hour": float(count),
            }
        )

    model_id = _safe_identifier(facility.get("model_id"), "facility")
    scenario_id = _safe_identifier(
        f"random-la-{model_id}-s{random_seed}-m{total_moves}",
        "random-la-scenario",
    )
    analysis = _build_analysis(facility, router, demands, scenario_id)
    max_route_time = max(
        (int(route.get("travel_time_us", 0)) for route in analysis["demand_routes"]),
        default=0,
    )
    # Each job receives a source-positioned synthetic vehicle.  This isolates
    # layout/routing verification from an arbitrary fleet-size assumption and
    # guarantees every generated pickup remains dispatchable even on a one-way
    # graph that cannot return a vehicle to its previous source.
    vehicles = [
        {"id": f"RND-OHT-{index:06d}", "initial_station_id": from_id}
        for index, (from_id, _to_id) in enumerate(sampled, start=1)
    ]
    jobs = []
    for index, (from_id, to_id) in enumerate(sampled, start=1):
        release_time = ((index - 1) * demand_window) // total_moves
        jobs.append(
            {
                "id": f"RND-JOB-{index:06d}",
                "pickup_station_id": from_id,
                "dropoff_station_id": to_id,
                "release_time_us": min(release_time, demand_window - 1),
                "load_duration_us": int(load_duration_us),
                "unload_duration_us": int(unload_duration_us),
            }
        )

    scenario = {
        "schema_version": "1.1.0",
        "scenario_id": scenario_id,
        "model_revision_id": revision_id,
        "duration_us": demand_window
        + max_route_time
        + int(load_duration_us)
        + int(unload_duration_us)
        + 1,
        "zero_delay_event_limit": max(100_000, total_moves * 20),
        "master_seed": random_seed,
        "vehicles": vehicles,
        "jobs": jobs,
        "from_to_demands": demands,
    }
    station_ids = set(router.station_nodes)
    usable_station_ids = {station_id for pair in reachable for station_id in pair[:2]}
    excluded = tuple(sorted(station_ids - usable_station_ids))
    analysis["generation"] = {
        "method": "bounded-uniform-random-reachable-station-pairs",
        "seed": random_seed,
        "moves_per_hour": total_moves,
        "station_count": len(station_ids),
        "reachable_pair_count": len(reachable),
        "active_pair_limit": active_pair_limit,
        "generated_demand_count": len(demands),
        "generated_job_count": len(jobs),
        "generated_vehicle_count": len(vehicles),
        "demand_window_us": demand_window,
        "scenario_duration_us": scenario["duration_us"],
        "vehicle_policy": "one-source-positioned-synthetic-vehicle-per-job",
        "excluded_station_ids": list(excluded),
    }
    return GeneratedRandomWorkload(
        scenario=scenario,
        demands=tuple(demands),
        analysis=analysis,
        sampled_pairs=tuple(sampled),
        reachable_pair_count=len(reachable),
        excluded_station_ids=excluded,
        moves_per_hour=total_moves,
        seed=random_seed,
    )


def _unique_output_directory(
    output_root: Path,
    model_name: str,
    workload: GeneratedRandomWorkload,
    timestamp: str | None,
) -> Path:
    stamp = timestamp or datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    stem = (
        re.sub(r"[^A-Za-z0-9가-힣._-]+", "-", model_name.strip()).strip("-._")
        or "facility"
    )
    base = (
        output_root
        / f"{stem}-random-flow-{stamp}-s{workload.seed}-m{workload.moves_per_hour}"
    )
    candidate = base
    suffix = 2
    while candidate.exists():
        candidate = output_root / f"{base.name}-{suffix}"
        suffix += 1
    return candidate


def save_random_workload(
    workload: GeneratedRandomWorkload,
    output_root: str | Path,
    *,
    model_name: str = "facility",
    timestamp: str | None = None,
) -> SavedRandomWorkload:
    """Save CSV, runnable Scenario JSON, and LA report in a new directory."""

    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)
    directory = _unique_output_directory(root, model_name, workload, timestamp)
    directory.mkdir(parents=False, exist_ok=False)
    csv_path = directory / "random_from_to.csv"
    scenario_path = directory / "random_scenario.json"
    analysis_path = directory / "random_la_analysis.json"

    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=(
                "id",
                "from_station_id",
                "to_station_id",
                "expected_moves_per_hour",
            ),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(workload.demands)
    with scenario_path.open("w", encoding="utf-8") as stream:
        json.dump(workload.scenario, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    analysis_output = {
        key: value for key, value in workload.analysis.items() if key != "demand_routes"
    }
    analysis_output["demand_routes"] = [
        {key: value for key, value in route.items() if key != "edge_ids"}
        | {
            "edge_count": len(route.get("edge_ids", [])),
            "edge_path_saved": False,
        }
        for route in workload.analysis.get("demand_routes", [])
    ]
    analysis_output["edge_flows"] = [
        {key: value for key, value in flow.items() if key != "contributing_demand_ids"}
        | {"contributing_demand_ids_saved": False}
        for flow in workload.analysis.get("edge_flows", [])
    ]
    generation = dict(analysis_output.get("generation", {}))
    generation["saved_report_route_policy"] = (
        "route edge_ids and per-edge contributing demand IDs omitted; "
        "reproduce full paths with random_scenario.json and random_from_to.csv"
    )
    analysis_output["generation"] = generation
    with analysis_path.open("w", encoding="utf-8") as stream:
        json.dump(analysis_output, stream, ensure_ascii=False, indent=2)
        stream.write("\n")

    return SavedRandomWorkload(
        directory=directory,
        demand_csv_path=csv_path,
        scenario_json_path=scenario_path,
        analysis_json_path=analysis_path,
    )


def default_generated_output_root() -> Path:
    """Return the user-visible output root used by the desktop application."""

    configured = os.environ.get("SIM_CORE_GENERATED_DIR", "").strip()
    if configured:
        return Path(configured).expanduser()
    return Path.home() / "Documents" / "Sim_Core" / "Generated"
