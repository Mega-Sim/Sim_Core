#pragma once

#include "sim_core/domain/job.hpp"
#include "sim_core/domain/vehicle.hpp"

#include <cstddef>
#include <cstdint>
#include <string>
#include <vector>

namespace sim_core::domain {

struct FromToDemand {
    std::string id;
    std::string from_station_id;
    std::string to_station_id;
    double expected_moves_per_hour{};
};

struct ScenarioDefinition {
    std::string schema_version;
    std::string scenario_id;
    std::string model_revision_id;
    std::int64_t duration_us{};
    std::size_t zero_delay_event_limit{100'000U};
    std::uint64_t master_seed{};
    std::vector<VehicleDefinition> vehicles;
    std::vector<JobDefinition> jobs;
    std::vector<FromToDemand> from_to_demands;
};

}  // namespace sim_core::domain
