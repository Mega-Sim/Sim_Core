#pragma once

#include "sim_core/domain/scenario.hpp"
#include "sim_core/model/facility_model.hpp"

#include <cstddef>
#include <cstdint>
#include <filesystem>
#include <map>
#include <string>
#include <string_view>
#include <vector>

namespace sim_core::analysis {

enum class CrossDomainSeverity { info, warning, error };
enum class CrossDomainCategory {
    identity,
    provenance,
    geometry,
    topology,
    resource,
    demand,
    revision,
};

[[nodiscard]] std::string_view to_string(CrossDomainSeverity severity) noexcept;
[[nodiscard]] std::string_view to_string(CrossDomainCategory category) noexcept;

struct CrossDomainDiagnostic {
    std::string diagnostic_id;
    CrossDomainSeverity severity{CrossDomainSeverity::error};
    CrossDomainCategory category{CrossDomainCategory::topology};
    std::string rule_id;
    std::vector<std::string> source_entities;
    std::vector<std::string> canonical_entities;
    std::string message;
    std::map<std::string, std::string, std::less<>> evidence;
    std::string suggested_action;
};

struct DemandRouteObservation {
    std::string demand_id;
    std::string from_station_id;
    std::string to_station_id;
    double expected_moves_per_hour{};
    std::vector<std::string> edge_ids;
    std::int64_t distance_um{};
    std::int64_t travel_time_us{};
};

// A3 Flow Intelligence: reachable From-To 수요를 집계해 얻은 edge 빈도 관측값.
struct EdgeFlowObservation {
    std::string edge_id;
    std::string from_node_id;
    std::string to_node_id;
    std::int64_t length_um{};
    double expected_moves_per_hour{};  // 이 edge를 지나는 모든 수요의 시간당 이동량 합
    double flow_share{};               // 전체 edge 이동량 대비 이 edge의 집중도(route concentration)
    std::size_t demand_count{};
    std::vector<std::string> contributing_demand_ids;
};

// merge 지점 판별을 위한 node 유입/유출 관측값.
struct NodeFlowObservation {
    std::string node_id;
    double inflow_moves_per_hour{};
    double outflow_moves_per_hour{};
    std::size_t incoming_edge_count{};  // flow를 싣고 이 node로 들어오는 서로 다른 edge 수
    double merge_pressure{};            // 유입 edge가 둘 이상일 때의 총 유입량, 아니면 0
};

// station 단위 유입/유출과 capacity margin 관측값.
struct StationFlowObservation {
    std::string station_id;
    double inbound_moves_per_hour{};
    double outbound_moves_per_hour{};
    double peak_moves_per_hour{};  // max(inbound, outbound)
    double handling_capacity_per_hour{};
    double capacity_margin_per_hour{};  // capacity - peak (capacity 미선언 시 0)
    double utilization_ratio{};         // peak / capacity (capacity 미선언 시 0)
    bool over_capacity{};
};

struct CrossDomainReport {
    std::string schema_version{"1.0.0"};
    std::string model_revision_id;
    std::string scenario_id;
    std::vector<CrossDomainDiagnostic> diagnostics;
    std::vector<DemandRouteObservation> demand_routes;
    std::vector<EdgeFlowObservation> edge_flows;
    std::vector<NodeFlowObservation> node_flows;
    std::vector<StationFlowObservation> station_flows;

    [[nodiscard]] bool ok() const noexcept;
    [[nodiscard]] std::size_t error_count() const noexcept;
    [[nodiscard]] std::size_t warning_count() const noexcept;
    [[nodiscard]] std::string to_json() const;
    void write_json(const std::filesystem::path& path) const;
};

class CrossDomainValidator final {
public:
    [[nodiscard]] static CrossDomainReport analyze(
        const model::FacilityModelRevision& model,
        const domain::ScenarioDefinition& scenario);
    static void compare_revisions(
        CrossDomainReport& report,
        const model::FacilityModelRevision& baseline,
        const model::FacilityModelRevision& current);
};

}  // namespace sim_core::analysis
