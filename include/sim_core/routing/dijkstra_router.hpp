#pragma once

#include "sim_core/model/facility_model.hpp"

#include <cstdint>
#include <map>
#include <optional>
#include <string>
#include <string_view>
#include <vector>

namespace sim_core::routing {

struct Route {
    std::vector<std::string> edge_ids;
    std::int64_t distance_um{};
    std::int64_t travel_time_us{};
};

class DijkstraRouter final {
public:
    static constexpr std::int64_t maximum_supported_speed_um_per_s =
        1'000'000'000'000;

    explicit DijkstraRouter(const model::FacilityModelRevision& model);

    [[nodiscard]] std::optional<Route> route_nodes(
        std::string_view from_node_id,
        std::string_view to_node_id) const;
    [[nodiscard]] std::optional<Route> route_stations(
        std::string_view from_station_id,
        std::string_view to_station_id) const;

    [[nodiscard]] static std::int64_t edge_travel_time_us(const model::Edge& edge);

private:
    const model::FacilityModelRevision& model_;
    std::map<std::string, const model::Node*, std::less<>> nodes_;
    std::map<std::string, const model::Station*, std::less<>> stations_;
    std::map<std::string, std::vector<const model::Edge*>, std::less<>> outgoing_;
};

}  // namespace sim_core::routing
