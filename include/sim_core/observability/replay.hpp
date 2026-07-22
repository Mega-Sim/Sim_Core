#pragma once

#include <cstddef>
#include <filesystem>
#include <map>
#include <string>

namespace sim_core::observability {

struct ReplaySummary {
    std::size_t event_count{};
    std::int64_t final_simulation_time_us{};
    std::size_t completed_job_count{};
    std::map<std::string, std::string, std::less<>> vehicle_states;
    std::map<std::string, std::string, std::less<>> job_states;
};

class TraceReplay final {
public:
    [[nodiscard]] static ReplaySummary replay(const std::filesystem::path& trace_path);
};

}  // namespace sim_core::observability
