#pragma once

#include <string>
#include <string_view>

namespace sim_core::domain {

enum class VehicleState {
    idle,
    to_pickup,
    loading,
    to_dropoff,
    unloading,
};

[[nodiscard]] std::string_view to_string(VehicleState state) noexcept;

struct VehicleDefinition {
    std::string id;
    std::string initial_station_id;
};

struct VehicleRuntimeState {
    std::string id;
    VehicleState state{VehicleState::idle};
    std::string current_station_id;
    std::string current_job_id;
};

void transition_vehicle(
    VehicleRuntimeState& vehicle,
    VehicleState expected,
    VehicleState next);

}  // namespace sim_core::domain
