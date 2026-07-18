#include "sim_core/observability/replay.hpp"

#include <nlohmann/json.hpp>

#include <algorithm>
#include <cstdint>
#include <fstream>
#include <set>
#include <stdexcept>
#include <string>

namespace sim_core::observability {

ReplaySummary TraceReplay::replay(const std::filesystem::path& trace_path) {
    std::ifstream input{trace_path};
    if (!input) {
        throw std::runtime_error("cannot open event trace: " + trace_path.string());
    }

    ReplaySummary summary;
    std::string line;
    std::set<std::uint64_t> seen_event_ids;
    std::int64_t previous_time = 0;
    while (std::getline(input, line)) {
        if (line.empty()) {
            continue;
        }
        const auto record = nlohmann::json::parse(line);
        const auto event_id = record.at("event_id").get<std::uint64_t>();
        const auto simulation_time =
            record.at("simulation_time_us").get<std::int64_t>();
        if (!seen_event_ids.insert(event_id).second || simulation_time < previous_time) {
            throw std::runtime_error(
                "event trace has a duplicate ID or decreasing time at event " +
                std::to_string(event_id));
        }
        previous_time = simulation_time;

        const auto vehicle_id = record.at("vehicle_id").get<std::string>();
        const auto vehicle_state = record.at("vehicle_state").get<std::string>();
        if (!vehicle_id.empty() && !vehicle_state.empty()) {
            summary.vehicle_states[vehicle_id] = vehicle_state;
        }
        const auto job_id = record.at("job_id").get<std::string>();
        const auto job_state = record.at("job_state").get<std::string>();
        if (!job_id.empty() && !job_state.empty()) {
            summary.job_states[job_id] = job_state;
        }
        ++summary.event_count;
        summary.final_simulation_time_us = simulation_time;
    }
    if (!input.eof()) {
        throw std::runtime_error("failed while reading event trace: " + trace_path.string());
    }
    summary.completed_job_count = static_cast<std::size_t>(std::ranges::count_if(
        summary.job_states,
        [](const auto& entry) { return entry.second == "COMPLETED"; }));
    return summary;
}

}  // namespace sim_core::observability
