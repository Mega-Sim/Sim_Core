#include "sim_core/routing/dijkstra_router.hpp"

#include <algorithm>
#include <cstdint>
#include <limits>
#include <map>
#include <queue>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace sim_core::routing {
namespace {

struct QueueEntry {
    std::int64_t travel_time_us{};
    std::string path_signature;
    std::string node_id;
};

struct LaterRoute {
    bool operator()(const QueueEntry& left, const QueueEntry& right) const noexcept {
        return std::tie(left.travel_time_us, left.path_signature, left.node_id) >
               std::tie(right.travel_time_us, right.path_signature, right.node_id);
    }
};

std::int64_t checked_add(const std::int64_t left, const std::int64_t right) {
    if (right < 0 || left > std::numeric_limits<std::int64_t>::max() - right) {
        throw std::overflow_error("route cost overflow");
    }
    return left + right;
}

}  // namespace

DijkstraRouter::DijkstraRouter(const model::FacilityModelRevision& model) : model_(model) {
    for (const auto& node : model_.nodes) {
        nodes_.emplace(node.id, &node);
    }
    for (const auto& station : model_.stations) {
        stations_.emplace(station.id, &station);
    }
    for (const auto& edge : model_.edges) {
        outgoing_[edge.from_node_id].push_back(&edge);
    }
    for (auto& [node_id, edges] : outgoing_) {
        (void)node_id;
        std::ranges::sort(edges, {}, [](const model::Edge* edge) { return edge->id; });
    }
}

std::optional<Route> DijkstraRouter::route_nodes(
    const std::string_view from_node_id,
    const std::string_view to_node_id) const {
    if (!nodes_.contains(from_node_id) || !nodes_.contains(to_node_id)) {
        return std::nullopt;
    }
    if (from_node_id == to_node_id) {
        return Route{};
    }

    std::priority_queue<QueueEntry, std::vector<QueueEntry>, LaterRoute> frontier;
    std::map<std::string, std::int64_t, std::less<>> best_time;
    std::map<std::string, std::string, std::less<>> best_signature;
    std::map<std::string, const model::Edge*, std::less<>> predecessor;

    const std::string start{from_node_id};
    const std::string goal{to_node_id};
    best_time[start] = 0;
    best_signature[start] = {};
    frontier.push(QueueEntry{.travel_time_us = 0, .path_signature = {}, .node_id = start});

    while (!frontier.empty()) {
        auto current = frontier.top();
        frontier.pop();
        if (current.travel_time_us != best_time[current.node_id] ||
            current.path_signature != best_signature[current.node_id]) {
            continue;
        }
        if (current.node_id == goal) {
            break;
        }

        const auto outgoing = outgoing_.find(current.node_id);
        if (outgoing == outgoing_.end()) {
            continue;
        }
        for (const auto* edge : outgoing->second) {
            const auto candidate_time =
                checked_add(current.travel_time_us, edge_travel_time_us(*edge));
            const auto candidate_signature =
                current.path_signature + '\x1f' + edge->id;
            const auto known = best_time.find(edge->to_node_id);
            const bool improves =
                known == best_time.end() || candidate_time < known->second ||
                (candidate_time == known->second &&
                 candidate_signature < best_signature[edge->to_node_id]);
            if (!improves) {
                continue;
            }
            best_time[edge->to_node_id] = candidate_time;
            best_signature[edge->to_node_id] = candidate_signature;
            predecessor[edge->to_node_id] = edge;
            frontier.push(QueueEntry{
                .travel_time_us = candidate_time,
                .path_signature = candidate_signature,
                .node_id = edge->to_node_id,
            });
        }
    }

    if (!best_time.contains(goal)) {
        return std::nullopt;
    }

    Route result;
    result.travel_time_us = best_time.at(goal);
    std::string cursor = goal;
    while (cursor != start) {
        const auto found = predecessor.find(cursor);
        if (found == predecessor.end()) {
            throw std::logic_error("route predecessor chain is incomplete");
        }
        result.edge_ids.push_back(found->second->id);
        result.distance_um = checked_add(result.distance_um, found->second->length_um);
        cursor = found->second->from_node_id;
    }
    std::ranges::reverse(result.edge_ids);
    return result;
}

std::optional<Route> DijkstraRouter::route_stations(
    const std::string_view from_station_id,
    const std::string_view to_station_id) const {
    const auto from = stations_.find(from_station_id);
    const auto to = stations_.find(to_station_id);
    if (from == stations_.end() || to == stations_.end()) {
        return std::nullopt;
    }
    return route_nodes(from->second->attachment_node_id, to->second->attachment_node_id);
}

std::int64_t DijkstraRouter::edge_travel_time_us(const model::Edge& edge) {
    if (edge.length_um <= 0 || edge.speed_limit_um_per_s <= 0) {
        throw std::invalid_argument("edge length and speed must be positive");
    }
    constexpr std::int64_t micros_per_second = 1'000'000;
    if (edge.speed_limit_um_per_s > maximum_supported_speed_um_per_s) {
        throw std::overflow_error("edge speed exceeds deterministic conversion limit");
    }

    const auto whole_seconds = edge.length_um / edge.speed_limit_um_per_s;
    const auto remainder = edge.length_um % edge.speed_limit_um_per_s;
    if (whole_seconds >
        std::numeric_limits<std::int64_t>::max() / micros_per_second) {
        throw std::overflow_error("edge travel time overflow");
    }
    const auto fractional_us =
        (remainder * micros_per_second + edge.speed_limit_um_per_s - 1) /
        edge.speed_limit_um_per_s;
    return checked_add(whole_seconds * micros_per_second, fractional_us);
}

}  // namespace sim_core::routing
