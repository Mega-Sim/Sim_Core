#pragma once

#include "sim_core/kernel/simulation_time.hpp"

#include <cstdint>
#include <optional>
#include <string>
#include <string_view>

namespace sim_core::kernel {

enum class EventPriority : std::int32_t {
    resource_release = 100,
    movement_completion = 200,
    state_transition = 300,
    demand_dispatch = 400,
    observation = 500,
};

enum class EventType {
    dispatch_requested,
    vehicle_arrived_pickup,
    loading_completed,
    vehicle_arrived_dropoff,
    unloading_completed,
};

[[nodiscard]] std::string_view to_string(EventType type) noexcept;
[[nodiscard]] std::int32_t priority_value(EventPriority priority) noexcept;

struct EventPayload {
    std::string vehicle_id;
    std::string job_id;
    std::string station_id;
    std::int64_t route_distance_um{};
};

struct EventRequest {
    SimulationTime simulation_time{SimulationTime::zero()};
    EventPriority priority{EventPriority::state_transition};
    EventType event_type{EventType::dispatch_requested};
    std::string entity_type;
    std::string entity_id;
    std::uint64_t cause_event_id{};
    std::string correlation_id;
    EventPayload payload;
    std::optional<std::string> cancellation_key;
};

struct EventEnvelope {
    std::uint64_t event_id{};
    SimulationTime simulation_time{SimulationTime::zero()};
    EventPriority priority{EventPriority::state_transition};
    std::uint64_t insertion_sequence{};
    EventType event_type{EventType::dispatch_requested};
    std::string entity_type;
    std::string entity_id;
    std::uint64_t cause_event_id{};
    std::string correlation_id;
    EventPayload payload;
    std::optional<std::string> cancellation_key;
    std::uint64_t cancellation_generation{};
};

struct EventHandle {
    std::uint64_t event_id{};
    std::optional<std::string> cancellation_key;
    std::uint64_t cancellation_generation{};
};

}  // namespace sim_core::kernel
