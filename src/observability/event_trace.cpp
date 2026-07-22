#include "sim_core/observability/event_trace.hpp"

#include <nlohmann/json.hpp>

#include <cstdint>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>

namespace sim_core::observability {
namespace {

using Json = nlohmann::json;

Json to_json(const TraceRecord& record) {
    return Json{
        {"event_id", record.event_id},
        {"simulation_time_us", record.simulation_time_us},
        {"priority", record.priority},
        {"insertion_sequence", record.insertion_sequence},
        {"event_type", record.event_type},
        {"entity_type", record.entity_type},
        {"entity_id", record.entity_id},
        {"cause_event_id", record.cause_event_id},
        {"correlation_id", record.correlation_id},
        {"vehicle_id", record.vehicle_id},
        {"vehicle_state", record.vehicle_state},
        {"job_id", record.job_id},
        {"job_state", record.job_state},
        {"station_id", record.station_id},
        {"route_distance_um", record.route_distance_um},
    };
}

}  // namespace

void EventTrace::append(TraceRecord record) {
    records_.push_back(std::move(record));
}

const std::vector<TraceRecord>& EventTrace::records() const noexcept {
    return records_;
}

std::size_t EventTrace::size() const noexcept {
    return records_.size();
}

std::string EventTrace::hash() const {
    std::string canonical;
    for (const auto& record : records_) {
        canonical += serialize(record);
        canonical.push_back('\n');
    }
    return stable_hash(canonical);
}

void EventTrace::write_jsonl(const std::filesystem::path& path) const {
    std::ofstream output{path, std::ios::binary | std::ios::trunc};
    if (!output) {
        throw std::runtime_error("cannot create event trace: " + path.string());
    }
    for (const auto& record : records_) {
        output << serialize(record) << '\n';
    }
    if (!output) {
        throw std::runtime_error("failed while writing event trace: " + path.string());
    }
}

std::string EventTrace::stable_hash(const std::string_view value) {
    constexpr std::uint64_t offset_basis = 14695981039346656037ULL;
    constexpr std::uint64_t prime = 1099511628211ULL;
    std::uint64_t hash = offset_basis;
    for (const unsigned char byte : value) {
        hash ^= static_cast<std::uint64_t>(byte);
        hash *= prime;
    }
    std::ostringstream output;
    output << std::hex << std::setfill('0') << std::setw(16) << hash;
    return output.str();
}

std::string EventTrace::serialize(const TraceRecord& record) {
    return to_json(record).dump();
}

void write_manifest(const RunManifest& manifest, const std::filesystem::path& path) {
    const Json document{
        {"schema_version", manifest.schema_version},
        {"engine_version", manifest.engine_version},
        {"model_revision_id", manifest.model_revision_id},
        {"scenario_id", manifest.scenario_id},
        {"master_seed", manifest.master_seed},
        {"run_fingerprint", manifest.run_fingerprint},
        {"status", manifest.status},
        {"processed_event_count", manifest.processed_event_count},
        {"final_simulation_time_us", manifest.final_simulation_time_us},
        {"trace_hash_algorithm", manifest.trace_hash_algorithm},
        {"trace_hash", manifest.trace_hash},
    };

    std::ofstream output{path, std::ios::binary | std::ios::trunc};
    if (!output) {
        throw std::runtime_error("cannot create run manifest: " + path.string());
    }
    output << document.dump(2) << '\n';
    if (!output) {
        throw std::runtime_error("failed while writing run manifest: " + path.string());
    }
}

}  // namespace sim_core::observability
