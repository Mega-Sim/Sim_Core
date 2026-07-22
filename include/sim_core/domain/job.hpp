#pragma once

#include <cstdint>
#include <string>
#include <string_view>

namespace sim_core::domain {

enum class JobState {
    pending,
    assigned,
    loading,
    in_transit,
    unloading,
    completed,
};

[[nodiscard]] std::string_view to_string(JobState state) noexcept;

struct JobDefinition {
    std::string id;
    std::string pickup_station_id;
    std::string dropoff_station_id;
    std::int64_t release_time_us{};
    std::int64_t load_duration_us{};
    std::int64_t unload_duration_us{};
};

struct JobRuntimeState {
    JobDefinition definition;
    JobState state{JobState::pending};
    bool released{};
    std::string assigned_vehicle_id;
};

void transition_job(JobRuntimeState& job, JobState expected, JobState next);

}  // namespace sim_core::domain
