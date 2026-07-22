#include "sim_core/domain/job.hpp"
#include "sim_core/domain/vehicle.hpp"

#include <stdexcept>

namespace sim_core::domain {

std::string_view to_string(const VehicleState state) noexcept {
    switch (state) {
    case VehicleState::idle:
        return "IDLE";
    case VehicleState::to_pickup:
        return "TO_PICKUP";
    case VehicleState::loading:
        return "LOADING";
    case VehicleState::to_dropoff:
        return "TO_DROPOFF";
    case VehicleState::unloading:
        return "UNLOADING";
    }
    return "UNKNOWN";
}

std::string_view to_string(const JobState state) noexcept {
    switch (state) {
    case JobState::pending:
        return "PENDING";
    case JobState::assigned:
        return "ASSIGNED";
    case JobState::loading:
        return "LOADING";
    case JobState::in_transit:
        return "IN_TRANSIT";
    case JobState::unloading:
        return "UNLOADING";
    case JobState::completed:
        return "COMPLETED";
    }
    return "UNKNOWN";
}

void transition_vehicle(
    VehicleRuntimeState& vehicle,
    const VehicleState expected,
    const VehicleState next) {
    if (vehicle.state != expected) {
        throw std::logic_error("invalid vehicle state transition for " + vehicle.id);
    }
    vehicle.state = next;
}

void transition_job(JobRuntimeState& job, const JobState expected, const JobState next) {
    if (job.state != expected) {
        throw std::logic_error("invalid job state transition for " + job.definition.id);
    }
    job.state = next;
}

}  // namespace sim_core::domain
