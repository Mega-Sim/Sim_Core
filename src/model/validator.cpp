#include "sim_core/model/validator.hpp"

#include "sim_core/routing/dijkstra_router.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <string_view>
#include <utility>

namespace sim_core::model {
namespace {

void add(
    ValidationReport& report,
    const DiagnosticSeverity severity,
    const DiagnosticCategory category,
    std::string code,
    std::string entity_type,
    std::string entity_id,
    std::string message) {
    report.diagnostics.push_back(Diagnostic{
        .severity = severity,
        .category = category,
        .code = std::move(code),
        .entity_type = std::move(entity_type),
        .entity_id = std::move(entity_id),
        .message = std::move(message),
    });
}

template <typename Entity>
std::set<std::string, std::less<>> collect_unique_ids(
    ValidationReport& report,
    const std::vector<Entity>& entities,
    const std::string_view entity_type) {
    std::set<std::string, std::less<>> ids;
    for (const auto& entity : entities) {
        if (entity.id.empty()) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::structural,
                "EMPTY_ENTITY_ID",
                std::string{entity_type},
                {},
                "entity ID cannot be empty");
            continue;
        }
        if (!ids.insert(entity.id).second) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::structural,
                "DUPLICATE_ENTITY_ID",
                std::string{entity_type},
                entity.id,
                "entity ID must be unique within its type");
        }
    }
    return ids;
}

void validate_source_identities(
    ValidationReport& report,
    const std::vector<SourceIdentity>& identities,
    const std::string_view entity_type,
    const std::string& entity_id) {
    for (const auto& identity : identities) {
        if (identity.source_kind.empty() || identity.source_namespace.empty() ||
            identity.external_id.empty()) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::structural,
                "INVALID_SOURCE_IDENTITY",
                std::string{entity_type},
                entity_id,
                "source kind, namespace, and external ID are required together");
        }
    }
}

long double segment_length(const Position3Um& from, const Position3Um& to) {
    const auto dx = static_cast<long double>(to.x) - static_cast<long double>(from.x);
    const auto dy = static_cast<long double>(to.y) - static_cast<long double>(from.y);
    const auto dz = static_cast<long double>(to.z) - static_cast<long double>(from.z);
    return std::sqrt(dx * dx + dy * dy + dz * dz);
}

long double polyline_length(const std::vector<Position3Um>& points) {
    long double result = 0.0L;
    for (std::size_t index = 1U; index < points.size(); ++index) {
        result += segment_length(points[index - 1U], points[index]);
    }
    return result;
}

bool is_lower_hex(const std::string_view value) {
    return std::ranges::all_of(value, [](const char character) {
        return (character >= '0' && character <= '9') ||
               (character >= 'a' && character <= 'f');
    });
}

}  // namespace

std::string_view to_string(const DiagnosticSeverity severity) noexcept {
    switch (severity) {
    case DiagnosticSeverity::warning:
        return "WARNING";
    case DiagnosticSeverity::error:
        return "ERROR";
    }
    return "UNKNOWN";
}

std::string_view to_string(const DiagnosticCategory category) noexcept {
    switch (category) {
    case DiagnosticCategory::structural:
        return "STRUCTURAL";
    case DiagnosticCategory::unit:
        return "UNIT";
    case DiagnosticCategory::geometry:
        return "GEOMETRY";
    case DiagnosticCategory::graph:
        return "GRAPH";
    case DiagnosticCategory::scenario:
        return "SCENARIO";
    }
    return "UNKNOWN";
}

bool ValidationReport::ok() const noexcept {
    return error_count() == 0U;
}

std::size_t ValidationReport::error_count() const noexcept {
    return static_cast<std::size_t>(std::ranges::count_if(
        diagnostics,
        [](const Diagnostic& diagnostic) {
            return diagnostic.severity == DiagnosticSeverity::error;
        }));
}

std::string ValidationReport::summary() const {
    std::ostringstream output;
    output << error_count() << " validation error(s)";
    for (const auto& diagnostic : diagnostics) {
        output << '\n' << to_string(diagnostic.severity) << ' '
               << to_string(diagnostic.category) << ' ' << diagnostic.code;
        if (!diagnostic.entity_id.empty()) {
            output << " [" << diagnostic.entity_type << ':' << diagnostic.entity_id << ']';
        }
        output << ": " << diagnostic.message;
    }
    return output.str();
}

ValidationError::ValidationError(ValidationReport report)
    : std::runtime_error(report.summary()), report_(std::move(report)) {}

const ValidationReport& ValidationError::report() const noexcept {
    return report_;
}

ValidationReport Validator::validate_facility(const FacilityModelRevision& model) {
    ValidationReport report;
    if (model.schema_version != "1.0.0") {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::structural,
            "UNSUPPORTED_SCHEMA_VERSION",
            "facility",
            model.model_id,
            "supported facility schema_version is 1.0.0");
    }
    if (model.model_id.empty() || model.revision_id.empty() || model.content_hash.empty()) {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::structural,
            "MISSING_REVISION_METADATA",
            "facility",
            model.model_id,
            "model_id, revision_id, and content_hash are required");
    }
    if (model.coordinate_reference.length_unit != "micrometer") {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::unit,
            "UNSUPPORTED_LENGTH_UNIT",
            "facility",
            model.model_id,
            "the first runtime profile requires micrometer coordinates");
    }
    if (model.coordinate_reference.frame.empty() ||
        (model.coordinate_reference.up_axis != "X" &&
         model.coordinate_reference.up_axis != "Y" &&
         model.coordinate_reference.up_axis != "Z") ||
        (model.coordinate_reference.handedness != "left" &&
         model.coordinate_reference.handedness != "right")) {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::geometry,
            "INVALID_COORDINATE_REFERENCE",
            "facility",
            model.model_id,
            "frame, X/Y/Z up axis, and left/right handedness are required");
    }
    if (model.source_artifacts.empty()) {
        add(
            report,
            DiagnosticSeverity::warning,
            DiagnosticCategory::structural,
            "NO_SOURCE_PROVENANCE",
            "facility",
            model.model_id,
            "at least one source artifact is recommended");
    }
    for (const auto& artifact : model.source_artifacts) {
        if (artifact.kind.empty() || artifact.source_namespace.empty() ||
            artifact.sha256.size() != 64U || !is_lower_hex(artifact.sha256) ||
            artifact.importer_name.empty() ||
            artifact.importer_version.empty()) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::structural,
                "INVALID_SOURCE_ARTIFACT",
                "source_artifact",
                artifact.source_namespace,
                "kind, namespace, 64-character SHA-256, importer, and version are required");
        }
    }

    const auto node_ids = collect_unique_ids(report, model.nodes, "node");
    const auto edge_ids = collect_unique_ids(report, model.edges, "edge");
    const auto station_ids = collect_unique_ids(report, model.stations, "station");
    (void)edge_ids;
    (void)station_ids;
    if (model.nodes.empty() || model.edges.empty() || model.stations.empty()) {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::structural,
            "EMPTY_FACILITY_COMPONENT",
            "facility",
            model.model_id,
            "nodes, directed edges, and stations must all be present");
    }

    std::map<std::string, const Node*, std::less<>> nodes;
    for (const auto& node : model.nodes) {
        nodes.emplace(node.id, &node);
        if (node.layer.empty() || node.role.empty()) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::structural,
                "MISSING_NODE_SEMANTICS",
                "node",
                node.id,
                "layer and role are required");
        }
        validate_source_identities(report, node.source_identities, "node", node.id);
    }

    for (const auto& edge : model.edges) {
        validate_source_identities(report, edge.source_identities, "edge", edge.id);
        if (!node_ids.contains(edge.from_node_id) || !node_ids.contains(edge.to_node_id)) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::graph,
                "EDGE_ENDPOINT_NOT_FOUND",
                "edge",
                edge.id,
                "from_node_id and to_node_id must reference existing nodes");
            continue;
        }
        if (edge.length_um <= 0 || edge.speed_limit_um_per_s <= 0) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::unit,
                "NON_POSITIVE_EDGE_PHYSICS",
                "edge",
                edge.id,
                "edge length and speed limit must be positive");
        }
        if (edge.speed_limit_um_per_s >
            routing::DijkstraRouter::maximum_supported_speed_um_per_s) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::unit,
                "EDGE_SPEED_CONVERSION_LIMIT",
                "edge",
                edge.id,
                "edge speed exceeds the deterministic microsecond conversion limit");
        }
        if (edge.direction != "ONE_WAY") {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::graph,
                "UNSUPPORTED_EDGE_DIRECTION",
                "edge",
                edge.id,
                "the first canonical profile requires explicit ONE_WAY edges");
        }
        if (edge.polyline.size() < 2U) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::geometry,
                "EDGE_GEOMETRY_TOO_SHORT",
                "edge",
                edge.id,
                "edge polyline requires at least two points");
            continue;
        }
        if (edge.polyline.front() != nodes.at(edge.from_node_id)->position ||
            edge.polyline.back() != nodes.at(edge.to_node_id)->position) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::geometry,
                "EDGE_GEOMETRY_ENDPOINT_MISMATCH",
                "edge",
                edge.id,
                "polyline endpoints must exactly match referenced node positions");
        }
        const auto calculated = polyline_length(edge.polyline);
        const auto declared = static_cast<long double>(edge.length_um);
        const auto tolerance = std::max(10.0L, declared * 0.001L);
        if (std::abs(calculated - declared) > tolerance) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::geometry,
                "EDGE_LENGTH_GEOMETRY_MISMATCH",
                "edge",
                edge.id,
                "declared length differs from polyline length beyond 0.1% tolerance");
        }
    }

    for (const auto& station : model.stations) {
        validate_source_identities(report, station.source_identities, "station", station.id);
        if (!node_ids.contains(station.attachment_node_id)) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::graph,
                "STATION_ATTACHMENT_NOT_FOUND",
                "station",
                station.id,
                "attachment_node_id must reference an existing node");
        }
        if (station.operation_type.empty()) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::structural,
                "MISSING_STATION_OPERATION",
                "station",
                station.id,
                "operation_type is required");
        }
    }
    return report;
}

ValidationReport Validator::validate_scenario(
    const FacilityModelRevision& model,
    const domain::ScenarioDefinition& scenario) {
    ValidationReport report;
    if (scenario.schema_version != "1.0.0") {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::scenario,
            "UNSUPPORTED_SCENARIO_SCHEMA",
            "scenario",
            scenario.scenario_id,
            "supported scenario schema_version is 1.0.0");
    }
    if (scenario.scenario_id.empty() || scenario.model_revision_id != model.revision_id) {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::scenario,
            "SCENARIO_MODEL_REVISION_MISMATCH",
            "scenario",
            scenario.scenario_id,
            "scenario must reference the loaded model revision");
    }
    if (scenario.duration_us <= 0 || scenario.zero_delay_event_limit == 0U) {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::scenario,
            "INVALID_RUNTIME_LIMIT",
            "scenario",
            scenario.scenario_id,
            "duration and zero-delay event limit must be positive");
    }
    if (scenario.vehicles.empty() || scenario.jobs.empty()) {
        add(
            report,
            DiagnosticSeverity::error,
            DiagnosticCategory::scenario,
            "EMPTY_SCENARIO_WORKLOAD",
            "scenario",
            scenario.scenario_id,
            "at least one vehicle and one job are required");
    }

    const auto vehicle_ids = collect_unique_ids(report, scenario.vehicles, "vehicle");
    const auto job_ids = collect_unique_ids(report, scenario.jobs, "job");
    (void)vehicle_ids;
    (void)job_ids;

    std::set<std::string, std::less<>> station_ids;
    for (const auto& station : model.stations) {
        station_ids.insert(station.id);
    }
    for (const auto& vehicle : scenario.vehicles) {
        if (!station_ids.contains(vehicle.initial_station_id)) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::scenario,
                "VEHICLE_INITIAL_STATION_NOT_FOUND",
                "vehicle",
                vehicle.id,
                "initial station does not exist");
        }
    }

    const routing::DijkstraRouter router{model};
    for (const auto& job : scenario.jobs) {
        if (!station_ids.contains(job.pickup_station_id) ||
            !station_ids.contains(job.dropoff_station_id)) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::scenario,
                "JOB_STATION_NOT_FOUND",
                "job",
                job.id,
                "pickup and dropoff stations must exist");
            continue;
        }
        if (job.release_time_us < 0 || job.release_time_us >= scenario.duration_us ||
            job.load_duration_us < 0 || job.unload_duration_us < 0) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::scenario,
                "INVALID_JOB_TIME",
                "job",
                job.id,
                "release must be inside the run and service durations cannot be negative");
        }
        if (!router.route_stations(job.pickup_station_id, job.dropoff_station_id).has_value()) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::graph,
                "GRAPH_UNREACHABLE_DROPOFF",
                "job",
                job.id,
                "dropoff station is unreachable from pickup station");
        }
        const bool pickup_reachable = std::ranges::any_of(
            scenario.vehicles,
            [&router, &job](const domain::VehicleDefinition& vehicle) {
                return router
                    .route_stations(vehicle.initial_station_id, job.pickup_station_id)
                    .has_value();
            });
        if (!pickup_reachable) {
            add(
                report,
                DiagnosticSeverity::error,
                DiagnosticCategory::graph,
                "GRAPH_UNREACHABLE_PICKUP",
                "job",
                job.id,
                "no initial vehicle position can reach the pickup station");
        }
    }
    return report;
}

void Validator::throw_if_invalid(ValidationReport report) {
    if (!report.ok()) {
        throw ValidationError{std::move(report)};
    }
}

}  // namespace sim_core::model
