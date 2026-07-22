#pragma once

#include "sim_core/kernel/event.hpp"

#include <cstddef>
#include <cstdint>
#include <filesystem>
#include <string>
#include <string_view>
#include <vector>

namespace sim_core::observability {

struct TraceRecord {
    std::uint64_t event_id{};
    std::int64_t simulation_time_us{};
    std::int32_t priority{};
    std::uint64_t insertion_sequence{};
    std::string event_type;
    std::string entity_type;
    std::string entity_id;
    std::uint64_t cause_event_id{};
    std::string correlation_id;
    std::string vehicle_id;
    std::string vehicle_state;
    std::string job_id;
    std::string job_state;
    std::string station_id;
    std::int64_t route_distance_um{};
};

struct RunManifest {
    std::string schema_version{"1.0.0"};
    std::string engine_version;
    std::string model_revision_id;
    std::string scenario_id;
    std::uint64_t master_seed{};
    std::string run_fingerprint;
    std::string status;
    std::size_t processed_event_count{};
    std::int64_t final_simulation_time_us{};
    std::string trace_hash_algorithm{"fnv1a64"};
    std::string trace_hash;
};

class EventTrace final {
public:
    void append(TraceRecord record);

    [[nodiscard]] const std::vector<TraceRecord>& records() const noexcept;
    [[nodiscard]] std::size_t size() const noexcept;
    [[nodiscard]] std::string hash() const;
    void write_jsonl(const std::filesystem::path& path) const;

    [[nodiscard]] static std::string stable_hash(std::string_view value);

private:
    [[nodiscard]] static std::string serialize(const TraceRecord& record);

    std::vector<TraceRecord> records_;
};

void write_manifest(const RunManifest& manifest, const std::filesystem::path& path);

}  // namespace sim_core::observability
