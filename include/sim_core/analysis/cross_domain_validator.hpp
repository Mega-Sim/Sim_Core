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

struct CrossDomainReport {
    std::string schema_version{"1.0.0"};
    std::string model_revision_id;
    std::string scenario_id;
    std::vector<CrossDomainDiagnostic> diagnostics;
    std::vector<DemandRouteObservation> demand_routes;

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
