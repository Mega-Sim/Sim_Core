#pragma once

#include "sim_core/domain/job.hpp"
#include "sim_core/domain/scenario.hpp"
#include "sim_core/domain/vehicle.hpp"
#include "sim_core/model/facility_model.hpp"
#include "sim_core/observability/event_trace.hpp"

#include <map>
#include <string>

namespace sim_core::application {

struct SimulationResult {
    observability::EventTrace trace;
    observability::RunManifest manifest;
    std::map<std::string, domain::VehicleRuntimeState, std::less<>> vehicles;
    std::map<std::string, domain::JobRuntimeState, std::less<>> jobs;
};

class Simulation final {
public:
    Simulation(
        const model::FacilityModelRevision& facility,
        const domain::ScenarioDefinition& scenario);

    [[nodiscard]] SimulationResult run() const;

private:
    const model::FacilityModelRevision& facility_;
    const domain::ScenarioDefinition& scenario_;
};

}  // namespace sim_core::application
