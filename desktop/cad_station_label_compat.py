"""Accept production equipment-code labels as CAD stations efficiently.

The first CAD-to-Facility bridge intentionally required explicit ``station-*``
or ``ST-*`` labels. Production FAB drawings commonly use equipment IDs such as
``A_2106`` instead. This compatibility layer keeps explicit labels authoritative
and falls back to repeated equipment-ID families only when fewer than two
explicit stations exist.

Large drawings can contain thousands of labels, so the nearest-rail projection
is also replaced with an exact uniform-grid spatial index. The result preserves
the original distance and tie-breaking rules while avoiding a full scan of every
rail segment for every station.
"""
from __future__ import annotations

import math
import re
from collections import defaultdict
from dataclasses import dataclass
from threading import Lock
from typing import Any, Callable, Mapping, Sequence


Label = tuple[int, str, float, float]
PointUm = tuple[int, int]

_EQUIPMENT_ID = re.compile(
    r"^(?P<prefix>[A-Za-z가-힣][A-Za-z0-9가-힣]*)(?P<separator>[\s._:-]+)(?P<number>\d+)$"
)
_STATION_LAYER_HINT = re.compile(
    r"(?:station|stn|equipment|eqp|port|stocker|stk|설비|장비|포트|스테이션)",
    re.IGNORECASE,
)
_MIN_GLOBAL_FAMILY_SIZE = 10
_MAX_GRID_AXIS_CELLS = 256
_MIN_GRID_AXIS_CELLS = 32
_MAX_CELLS_PER_SEGMENT = 4_096


@dataclass(frozen=True)
class _LabelRecord:
    index: int
    text: str
    x: float
    y: float
    layer: str
    signature: tuple[str, str] | None


@dataclass(frozen=True)
class _SegmentRecord:
    edge_index: int
    segment_index: int
    start: PointUm
    end: PointUm
    distance_along: float
    length_squared: int
    segment_length: float


class _SegmentGrid:
    def __init__(self, edges: Sequence[Any]) -> None:
        records: list[_SegmentRecord] = []
        min_x: int | None = None
        min_y: int | None = None
        max_x: int | None = None
        max_y: int | None = None
        for edge_index, edge in enumerate(edges):
            distance_along = 0.0
            for segment_index, (start, end) in enumerate(
                zip(edge.points_um, edge.points_um[1:])
            ):
                dx = int(end[0]) - int(start[0])
                dy = int(end[1]) - int(start[1])
                length_squared = dx * dx + dy * dy
                if length_squared <= 0:
                    continue
                segment_length = math.sqrt(length_squared)
                start_point = int(start[0]), int(start[1])
                end_point = int(end[0]), int(end[1])
                records.append(
                    _SegmentRecord(
                        edge_index=edge_index,
                        segment_index=segment_index,
                        start=start_point,
                        end=end_point,
                        distance_along=distance_along,
                        length_squared=length_squared,
                        segment_length=segment_length,
                    )
                )
                local_min_x = min(start_point[0], end_point[0])
                local_max_x = max(start_point[0], end_point[0])
                local_min_y = min(start_point[1], end_point[1])
                local_max_y = max(start_point[1], end_point[1])
                min_x = local_min_x if min_x is None else min(min_x, local_min_x)
                min_y = local_min_y if min_y is None else min(min_y, local_min_y)
                max_x = local_max_x if max_x is None else max(max_x, local_max_x)
                max_y = local_max_y if max_y is None else max(max_y, local_max_y)
                distance_along += segment_length
        if (
            not records
            or min_x is None
            or min_y is None
            or max_x is None
            or max_y is None
        ):
            raise ValueError("CAD Graph에 투영 가능한 Rail segment가 없습니다.")

        span = max(max_x - min_x, max_y - min_y, 1)
        target_axis_cells = max(
            _MIN_GRID_AXIS_CELLS,
            min(_MAX_GRID_AXIS_CELLS, int(math.sqrt(len(records))) or 1),
        )
        self.cell_size = max(1, int(math.ceil(span / target_axis_cells)))
        self.records = records
        self.cells: dict[tuple[int, int], list[int]] = defaultdict(list)
        self.global_record_ids: list[int] = []

        for record_id, record in enumerate(records):
            start_x, start_y = record.start
            end_x, end_y = record.end
            min_cell_x = min(start_x, end_x) // self.cell_size
            max_cell_x = max(start_x, end_x) // self.cell_size
            min_cell_y = min(start_y, end_y) // self.cell_size
            max_cell_y = max(start_y, end_y) // self.cell_size
            cell_count = (max_cell_x - min_cell_x + 1) * (
                max_cell_y - min_cell_y + 1
            )
            if cell_count > _MAX_CELLS_PER_SEGMENT:
                self.global_record_ids.append(record_id)
                continue
            for cell_x in range(min_cell_x, max_cell_x + 1):
                for cell_y in range(min_cell_y, max_cell_y + 1):
                    self.cells[(cell_x, cell_y)].append(record_id)

        occupied = list(self.cells)
        if occupied:
            self.min_cell_x = min(cell[0] for cell in occupied)
            self.max_cell_x = max(cell[0] for cell in occupied)
            self.min_cell_y = min(cell[1] for cell in occupied)
            self.max_cell_y = max(cell[1] for cell in occupied)
        else:
            self.min_cell_x = min_x // self.cell_size
            self.max_cell_x = max_x // self.cell_size
            self.min_cell_y = min_y // self.cell_size
            self.max_cell_y = max_y // self.cell_size

    @staticmethod
    def _ring_cells(center_x: int, center_y: int, radius: int):
        if radius == 0:
            yield center_x, center_y
            return
        low_x = center_x - radius
        high_x = center_x + radius
        low_y = center_y - radius
        high_y = center_y + radius
        for cell_x in range(low_x, high_x + 1):
            yield cell_x, low_y
            yield cell_x, high_y
        for cell_y in range(low_y + 1, high_y):
            yield low_x, cell_y
            yield high_x, cell_y

    @staticmethod
    def _candidate(point_um: PointUm, record: _SegmentRecord):
        start = record.start
        end = record.end
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        parameter = (
            (point_um[0] - start[0]) * dx + (point_um[1] - start[1]) * dy
        ) / record.length_squared
        parameter = max(0.0, min(1.0, parameter))
        projected = (
            int(round(start[0] + dx * parameter)),
            int(round(start[1] + dy * parameter)),
        )
        separation_x = point_um[0] - projected[0]
        separation_y = point_um[1] - projected[1]
        separation_squared = float(
            separation_x * separation_x + separation_y * separation_y
        )
        return (
            separation_squared,
            record.edge_index,
            record.segment_index,
            parameter,
            projected,
            record.distance_along + record.segment_length * parameter,
        )

    def nearest(self, point_um: PointUm):
        center_x = point_um[0] // self.cell_size
        center_y = point_um[1] // self.cell_size
        max_radius = max(
            abs(center_x - self.min_cell_x),
            abs(center_x - self.max_cell_x),
            abs(center_y - self.min_cell_y),
            abs(center_y - self.max_cell_y),
        ) + 1
        checked: set[int] = set()
        best = None

        def consider(record_id: int) -> None:
            nonlocal best
            if record_id in checked:
                return
            checked.add(record_id)
            candidate = self._candidate(point_um, self.records[record_id])
            if best is None or candidate[:4] < best[:4]:
                best = candidate

        for record_id in self.global_record_ids:
            consider(record_id)

        for radius in range(max_radius + 1):
            for cell in self._ring_cells(center_x, center_y, radius):
                for record_id in self.cells.get(cell, ()):  # exact bbox candidates
                    consider(record_id)
            if best is None:
                continue
            left = (center_x - radius) * self.cell_size
            right = (center_x + radius + 1) * self.cell_size
            bottom = (center_y - radius) * self.cell_size
            top = (center_y + radius + 1) * self.cell_size
            unsearched_lower_bound = min(
                point_um[0] - left,
                right - point_um[0],
                point_um[1] - bottom,
                top - point_um[1],
            )
            if math.sqrt(best[0]) <= unsearched_lower_bound:
                return best
        return best


_cache_lock = Lock()
_cached_edges: Sequence[Any] | None = None
_cached_grid: _SegmentGrid | None = None


def _equipment_signature(text: str) -> tuple[str, str] | None:
    match = _EQUIPMENT_ID.fullmatch(text)
    if match is None:
        return None
    separator = re.sub(r"\s+", " ", match.group("separator")).casefold()
    return match.group("prefix").casefold(), separator


def infer_equipment_station_labels(graph: Mapping[str, Any]) -> list[Label]:
    """Infer repeated equipment IDs without treating ordinary notes as stations."""

    metadata = graph.get("metadata")
    raw_labels = metadata.get("labels", []) if isinstance(metadata, Mapping) else []
    if not isinstance(raw_labels, list):
        return []

    records: list[_LabelRecord] = []
    for label_index, label in enumerate(raw_labels):
        if not isinstance(label, Mapping):
            continue
        text = str(label.get("text", "")).strip()
        if not text:
            continue
        try:
            x = float(label.get("x"))
            y = float(label.get("y"))
        except (TypeError, ValueError, OverflowError):
            continue
        layer = str(label.get("layer", "")).strip()
        records.append(
            _LabelRecord(
                index=label_index,
                text=text,
                x=x,
                y=y,
                layer=layer,
                signature=_equipment_signature(text),
            )
        )

    global_family_texts: dict[tuple[str, str], set[str]] = defaultdict(set)
    layer_family_texts: dict[tuple[str, tuple[str, str]], set[str]] = defaultdict(set)
    for record in records:
        if record.signature is None:
            continue
        normalized_text = record.text.casefold()
        global_family_texts[record.signature].add(normalized_text)
        layer_family_texts[(record.layer.casefold(), record.signature)].add(
            normalized_text
        )

    global_families = {
        signature
        for signature, texts in global_family_texts.items()
        if len(texts) >= _MIN_GLOBAL_FAMILY_SIZE
    }
    hinted_layer_families = {
        key
        for key, texts in layer_family_texts.items()
        if len(texts) >= 2 and _STATION_LAYER_HINT.search(key[0]) is not None
    }

    inferred = [
        (record.index, record.text, record.x, record.y)
        for record in records
        if record.signature is not None
        and (
            record.signature in global_families
            or (record.layer.casefold(), record.signature) in hinted_layer_families
        )
    ]
    return sorted(inferred, key=lambda item: item[0])


def _get_grid(edges: Sequence[Any]) -> _SegmentGrid:
    global _cached_edges, _cached_grid
    with _cache_lock:
        if edges is not _cached_edges or _cached_grid is None:
            _cached_grid = _SegmentGrid(edges)
            _cached_edges = edges
        return _cached_grid


def install_cad_station_label_compat() -> None:
    """Patch the CAD Facility bridge once for production drawing conventions."""

    import cad_graph_facility as target

    if getattr(target, "_equipment_station_compat_installed", False):
        return

    original_station_labels: Callable[[Mapping[str, Any]], list[Label]] = (
        target._station_labels
    )
    original_project_to_edges = target._project_to_edges

    def station_labels(graph: Mapping[str, Any]) -> list[Label]:
        explicit = original_station_labels(graph)
        if len(explicit) >= 2:
            return explicit
        inferred = infer_equipment_station_labels(graph)
        if not inferred:
            return explicit
        by_index = {item[0]: item for item in inferred}
        for item in explicit:
            by_index[item[0]] = item
        return [by_index[index] for index in sorted(by_index)]

    def project_to_edges(
        label_index: int,
        station_id: str,
        source_text: str,
        point_um: PointUm,
        edges: Sequence[Any],
    ):
        try:
            best = _get_grid(edges).nearest(point_um)
        except (AttributeError, TypeError, ValueError):
            return original_project_to_edges(
                label_index, station_id, source_text, point_um, edges
            )
        if best is None:
            return original_project_to_edges(
                label_index, station_id, source_text, point_um, edges
            )
        return target._StationProjection(
            label_index=label_index,
            station_id=station_id,
            source_text=source_text,
            edge_index=best[1],
            segment_index=best[2],
            segment_parameter=best[3],
            point_um=best[4],
            distance_um=math.sqrt(best[0]),
        )

    target._station_labels_without_equipment_compat = original_station_labels
    target._project_to_edges_without_spatial_index = original_project_to_edges
    target._station_labels = station_labels
    target._project_to_edges = project_to_edges
    target._equipment_station_compat_installed = True
