#pragma once

#include "sim_core/domain/job.hpp"
#include "sim_core/domain/vehicle.hpp"

#include <cstddef>
#include <cstdint>
#include <string>
#include <vector>

namespace sim_core::domain {

struct ScenarioDefinition {
    std::string schema_version;
    std::string scenario_id;
    std::string model_revision_id;
    std::int64_t duration_us{};
    std::size_t zero_delay_event_limit{100'000U};
    std::uint64_t master_seed{};
    std::vector<VehicleDefinition> vehicles;
    std::vector<JobDefinition> jobs;
};

}  // namespace sim_core::domain
