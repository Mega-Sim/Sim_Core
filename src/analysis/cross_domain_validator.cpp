#include "sim_core/analysis/cross_domain_validator.hpp"

#include "sim_core/routing/dijkstra_router.hpp"

#include <nlohmann/json.hpp>

#include <algorithm>
#include <cmath>
#include <fstream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>

namespace sim_core::analysis {
namespace {

using Evidence = std::map<std::string, std::string, std::less<>>;

void add(
    CrossDomainReport& report,
    const CrossDomainSeverity severity,
    const CrossDomainCategory category,
    std::string rule_id,
    std::vector<std::string> source_entities,
    std::vector<std::string> canonical_entities,
    std::string message,
    Evidence evidence,
    std::string suggested_action) {
    report.diagnostics.push_back(CrossDomainDiagnostic{
        .diagnostic_id = {},
        .severity = severity,
        .category = category,
        .rule_id = std::move(rule_id),
        .source_entities = std::move(source_entities),
        .canonical_entities = std::move(canonical_entities),
        .message = std::move(message),
        .evidence = std::move(evidence),
        .suggested_action = std::move(suggested_action),
    });
}

void finalize(CrossDomainReport& report) {
    std::ranges::sort(report.diagnostics, [](const auto& left, const auto& right) {
        return std::tie(
                   left.rule_id,
                   left.canonical_entities,
                   left.source_entities,
                   left.message) <
               std::tie(
                   right.rule_id,
                   right.canonical_entities,
                   right.source_entities,
                   right.message);
    });
    for (std::size_t index = 0U; index < report.diagnostics.size(); ++index) {
        std::ostringstream identifier;
        identifier << "CDV-";
        identifier.width(6);
        identifier.fill('0');
        identifier << index + 1U;
        report.diagnostics[index].diagnostic_id = identifier.str();
    }
    std::ranges::sort(
        report.demand_routes,
        {},
        &DemandRouteObservation::demand_id);
}

std::string entity_ref(const std::string_view type, const std::string& id) {
    return std::string{type} + ':' + id;
}

std::string source_key(const model::SourceIdentity& identity) {
    return identity.source_kind + '\x1f' + identity.source_namespace + '\x1f' +
           identity.external_id;
}

std::string source_ref(const model::SourceIdentity& identity) {
    return identity.source_kind + ':' + identity.source_namespace + ':' +
           identity.external_id;
}

template <typename Collection, typename Function>
void visit_collection(
    const Collection& collection,
    const std::string_view type,
    Function&& function) {
    for (const auto& entity : collection) {
        function(type, entity.id, entity.source_identities);
    }
}

template <typename Function>
void visit_entities(const model::FacilityModelRevision& model, Function&& function) {
    visit_collection(model.nodes, "node", function);
    visit_collection(model.edges, "edge", function);
    visit_collection(model.stations, "station", function);
    visit_collection(model.control_points, "control_point", function);
    visit_collection(model.zones, "zone", function);
    visit_collection(model.parkings, "parking", function);
    visit_collection(model.chargers, "charger", function);
    visit_collection(model.vehicle_types, "vehicle_type", function);
}

using SourceMappings = std::map<std::string, std::string, std::less<>>;

SourceMappings collect_source_mappings(const model::FacilityModelRevision& model) {
    SourceMappings mappings;
    visit_entities(model, [&mappings](
                              const std::string_view type,
                              const std::string& id,
                              const std::vector<model::SourceIdentity>& identities) {
        for (const auto& identity : identities) {
            mappings.emplace(source_key(identity), entity_ref(type, id));
        }
    });
    return mappings;
}

long double distance(
    const model::Position3Um& left,
    const model::Position3Um& right) {
    const auto dx = static_cast<long double>(left.x) - static_cast<long double>(right.x);
    const auto dy = static_cast<long double>(left.y) - static_cast<long double>(right.y);
    const auto dz = static_cast<long double>(left.z) - static_cast<long double>(right.z);
    return std::sqrt(dx * dx + dy * dy + dz * dz);
}

void analyze_identities(
    CrossDomainReport& report,
    const model::FacilityModelRevision& model) {
    std::map<std::string, std::string, std::less<>> canonical_ids;
    std::map<std::string, std::string, std::less<>> source_mappings;
    std::set<std::string, std::less<>> artifact_namespaces;
    for (const auto& artifact : model.source_artifacts) {
        artifact_namespaces.insert(artifact.source_namespace);
    }

    visit_entities(model, [&](const std::string_view type,
                              const std::string& id,
                              const std::vector<model::SourceIdentity>& identities) {
        const auto canonical = entity_ref(type, id);
        const auto [existing_id, inserted_id] = canonical_ids.emplace(id, canonical);
        if (!inserted_id && existing_id->second != canonical) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::identity,
                "CDV-IDENTITY-001",
                {},
                {existing_id->second, canonical},
                "canonical ID is reused across entity types",
                {{"canonical_id", id}},
                "assign a globally unique canonical ID");
        }
        for (const auto& identity : identities) {
            const auto key = source_key(identity);
            const auto [existing, inserted] = source_mappings.emplace(key, canonical);
            if (!inserted && existing->second != canonical) {
                add(
                    report,
                    CrossDomainSeverity::error,
                    CrossDomainCategory::identity,
                    "CDV-IDENTITY-002",
                    {source_ref(identity)},
                    {existing->second, canonical},
                    "one source identity maps to multiple canonical entities",
                    {},
                    "resolve the source identity collision before creating a revision");
            }
            if (!artifact_namespaces.contains(identity.source_namespace)) {
                add(
                    report,
                    CrossDomainSeverity::warning,
                    CrossDomainCategory::provenance,
                    "CDV-PROVENANCE-001",
                    {source_ref(identity)},
                    {canonical},
                    "source identity namespace has no registered source artifact",
                    {{"source_namespace", identity.source_namespace}},
                    "register the authorized source artifact or remove the orphan identity");
            }
        }
    });
}

void analyze_geometry(
    CrossDomainReport& report,
    const model::FacilityModelRevision& model) {
    std::map<std::string, const model::GeometryTransform*, std::less<>> transforms;
    for (const auto& transform : model.geometry_transforms) {
        const auto [existing, inserted] =
            transforms.emplace(transform.source_namespace, &transform);
        if (!inserted) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::geometry,
                "CDV-GEOMETRY-001",
                {"source_namespace:" + transform.source_namespace},
                {},
                "multiple geometry transforms are defined for one source namespace",
                {{"first_source_frame", existing->second->source_frame},
                 {"second_source_frame", transform.source_frame}},
                "retain one explicit transform per source namespace and revision");
        }
        if (transform.target_frame != model.coordinate_reference.frame) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::geometry,
                "CDV-GEOMETRY-002",
                {"source_namespace:" + transform.source_namespace},
                {"facility:" + model.model_id},
                "geometry transform target does not match the canonical coordinate frame",
                {{"target_frame", transform.target_frame},
                 {"canonical_frame", model.coordinate_reference.frame}},
                "change the transform target or create a separate canonical revision");
        }
    }
    for (const auto& artifact : model.source_artifacts) {
        if (!artifact.coordinate_frame.empty() &&
            artifact.coordinate_frame != model.coordinate_reference.frame &&
            !transforms.contains(artifact.source_namespace)) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::geometry,
                "CDV-GEOMETRY-003",
                {"source_artifact:" + artifact.source_namespace},
                {"facility:" + model.model_id},
                "source coordinate frame differs but no geometry transform is recorded",
                {{"source_frame", artifact.coordinate_frame},
                 {"canonical_frame", model.coordinate_reference.frame}},
                "record the reviewed source-to-canonical transform");
        }
    }

    std::map<std::string, const model::Node*, std::less<>> nodes;
    for (const auto& node : model.nodes) {
        nodes.emplace(node.id, &node);
    }
    constexpr long double pose_tolerance_um = 1'000.0L;
    for (const auto& station : model.stations) {
        const auto node = nodes.find(station.attachment_node_id);
        if (!station.declared_position.has_value() || node == nodes.end()) {
            continue;
        }
        const auto delta = distance(*station.declared_position, node->second->position);
        if (delta > pose_tolerance_um) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::geometry,
                "CDV-GEOMETRY-004",
                {},
                {entity_ref("station", station.id),
                 entity_ref("node", station.attachment_node_id)},
                "station pose and rail attachment node differ beyond tolerance",
                {{"distance_um", std::to_string(static_cast<std::int64_t>(delta))},
                 {"tolerance_um", "1000"}},
                "review the equipment pose, transform, and attachment node");
        }
    }
}

void analyze_demands(
    CrossDomainReport& report,
    const model::FacilityModelRevision& model,
    const domain::ScenarioDefinition& scenario) {
    std::set<std::string, std::less<>> stations;
    std::map<std::string, double, std::less<>> capacity;
    for (const auto& station : model.stations) {
        stations.insert(station.id);
        capacity.emplace(station.id, station.handling_capacity_per_hour);
    }

    const routing::DijkstraRouter router{model};
    std::map<std::string, double, std::less<>> outbound;
    std::map<std::string, double, std::less<>> inbound;
    for (const auto& demand : scenario.from_to_demands) {
        const auto canonical = entity_ref("from_to_demand", demand.id);
        if (!stations.contains(demand.from_station_id) ||
            !stations.contains(demand.to_station_id)) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::demand,
                "CDV-DEMAND-001",
                {},
                {canonical},
                "From-To demand references a station missing from the canonical model",
                {{"from_station_id", demand.from_station_id},
                 {"to_station_id", demand.to_station_id}},
                "correct the source mapping or add the missing station");
            continue;
        }
        if (!std::isfinite(demand.expected_moves_per_hour) ||
            demand.expected_moves_per_hour <= 0.0) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::demand,
                "CDV-DEMAND-002",
                {},
                {canonical},
                "From-To frequency must be finite and positive",
                {{"expected_moves_per_hour",
                  std::to_string(demand.expected_moves_per_hour)}},
                "repair or remove the invalid demand row");
            continue;
        }

        const auto route =
            router.route_stations(demand.from_station_id, demand.to_station_id);
        if (!route.has_value()) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::topology,
                "CDV-DEMAND-003",
                {},
                {canonical,
                 entity_ref("station", demand.from_station_id),
                 entity_ref("station", demand.to_station_id)},
                "From-To demand pair is unreachable on the directed rail graph",
                {},
                "repair topology/direction or remove the impossible demand");
            continue;
        }
        outbound[demand.from_station_id] += demand.expected_moves_per_hour;
        inbound[demand.to_station_id] += demand.expected_moves_per_hour;
        report.demand_routes.push_back(DemandRouteObservation{
            .demand_id = demand.id,
            .from_station_id = demand.from_station_id,
            .to_station_id = demand.to_station_id,
            .expected_moves_per_hour = demand.expected_moves_per_hour,
            .edge_ids = route->edge_ids,
            .distance_um = route->distance_um,
            .travel_time_us = route->travel_time_us,
        });
    }

    for (const auto& [station_id, limit] : capacity) {
        if (limit <= 0.0) {
            continue;
        }
        const auto pressure = std::max(outbound[station_id], inbound[station_id]);
        if (pressure > limit) {
            add(
                report,
                CrossDomainSeverity::warning,
                CrossDomainCategory::resource,
                "CDV-CAPACITY-001",
                {},
                {entity_ref("station", station_id)},
                "expected From-To pressure exceeds declared station capacity",
                {{"pressure_per_hour", std::to_string(pressure)},
                 {"capacity_per_hour", std::to_string(limit)}},
                "review capacity, service time, or demand before simulation");
        }
    }
}

}  // namespace

std::string_view to_string(const CrossDomainSeverity severity) noexcept {
    switch (severity) {
    case CrossDomainSeverity::info:
        return "INFO";
    case CrossDomainSeverity::warning:
        return "WARNING";
    case CrossDomainSeverity::error:
        return "ERROR";
    }
    return "UNKNOWN";
}

std::string_view to_string(const CrossDomainCategory category) noexcept {
    switch (category) {
    case CrossDomainCategory::identity:
        return "IDENTITY";
    case CrossDomainCategory::provenance:
        return "PROVENANCE";
    case CrossDomainCategory::geometry:
        return "GEOMETRY";
    case CrossDomainCategory::topology:
        return "TOPOLOGY";
    case CrossDomainCategory::resource:
        return "RESOURCE";
    case CrossDomainCategory::demand:
        return "DEMAND";
    case CrossDomainCategory::revision:
        return "REVISION";
    }
    return "UNKNOWN";
}

bool CrossDomainReport::ok() const noexcept {
    return error_count() == 0U;
}

std::size_t CrossDomainReport::error_count() const noexcept {
    return static_cast<std::size_t>(std::ranges::count_if(
        diagnostics,
        [](const auto& diagnostic) {
            return diagnostic.severity == CrossDomainSeverity::error;
        }));
}

std::size_t CrossDomainReport::warning_count() const noexcept {
    return static_cast<std::size_t>(std::ranges::count_if(
        diagnostics,
        [](const auto& diagnostic) {
            return diagnostic.severity == CrossDomainSeverity::warning;
        }));
}

std::string CrossDomainReport::to_json() const {
    nlohmann::json diagnostic_values = nlohmann::json::array();
    for (const auto& diagnostic : diagnostics) {
        diagnostic_values.push_back({
            {"diagnostic_id", diagnostic.diagnostic_id},
            {"severity", to_string(diagnostic.severity)},
            {"category", to_string(diagnostic.category)},
            {"rule_id", diagnostic.rule_id},
            {"source_entities", diagnostic.source_entities},
            {"canonical_entities", diagnostic.canonical_entities},
            {"message", diagnostic.message},
            {"evidence", diagnostic.evidence},
            {"suggested_action", diagnostic.suggested_action},
        });
    }
    nlohmann::json route_values = nlohmann::json::array();
    for (const auto& route : demand_routes) {
        route_values.push_back({
            {"demand_id", route.demand_id},
            {"from_station_id", route.from_station_id},
            {"to_station_id", route.to_station_id},
            {"expected_moves_per_hour", route.expected_moves_per_hour},
            {"edge_ids", route.edge_ids},
            {"distance_um", route.distance_um},
            {"travel_time_us", route.travel_time_us},
        });
    }
    const nlohmann::json output{
        {"schema_version", schema_version},
        {"model_revision_id", model_revision_id},
        {"scenario_id", scenario_id},
        {"status", ok() ? "PASS" : "FAIL"},
        {"error_count", error_count()},
        {"warning_count", warning_count()},
        {"diagnostics", std::move(diagnostic_values)},
        {"demand_routes", std::move(route_values)},
    };
    return output.dump(2) + '\n';
}

void CrossDomainReport::write_json(const std::filesystem::path& path) const {
    if (!path.parent_path().empty()) {
        std::filesystem::create_directories(path.parent_path());
    }
    std::ofstream output{path, std::ios::binary};
    if (!output) {
        throw std::runtime_error("cannot write cross-domain report: " + path.string());
    }
    output << to_json();
}

CrossDomainReport CrossDomainValidator::analyze(
    const model::FacilityModelRevision& model,
    const domain::ScenarioDefinition& scenario) {
    CrossDomainReport report{
        .schema_version = "1.0.0",
        .model_revision_id = model.revision_id,
        .scenario_id = scenario.scenario_id,
        .diagnostics = {},
        .demand_routes = {},
    };
    analyze_identities(report, model);
    analyze_geometry(report, model);
    analyze_demands(report, model, scenario);
    finalize(report);
    return report;
}

void CrossDomainValidator::compare_revisions(
    CrossDomainReport& report,
    const model::FacilityModelRevision& baseline,
    const model::FacilityModelRevision& current) {
    if (baseline.model_id != current.model_id) {
        add(
            report,
            CrossDomainSeverity::error,
            CrossDomainCategory::revision,
            "CDV-REVISION-001",
            {},
            {"facility:" + baseline.model_id, "facility:" + current.model_id},
            "revision comparison requires the same model_id",
            {},
            "compare revisions from the same canonical model lineage");
    }
    if (baseline.revision_id == current.revision_id &&
        baseline.content_hash != current.content_hash) {
        add(
            report,
            CrossDomainSeverity::error,
            CrossDomainCategory::revision,
            "CDV-REVISION-002",
            {},
            {"facility_revision:" + current.revision_id},
            "one revision_id resolves to different content hashes",
            {{"baseline_hash", baseline.content_hash},
             {"current_hash", current.content_hash}},
            "create a new immutable revision_id for changed content");
    }

    const auto old_mappings = collect_source_mappings(baseline);
    const auto new_mappings = collect_source_mappings(current);
    for (const auto& [identity, old_entity] : old_mappings) {
        const auto found = new_mappings.find(identity);
        if (found == new_mappings.end()) {
            add(
                report,
                CrossDomainSeverity::warning,
                CrossDomainCategory::revision,
                "CDV-REVISION-003",
                {identity},
                {old_entity},
                "source identity disappeared in the new revision",
                {},
                "confirm deletion, replacement, or source import scope");
        } else if (found->second != old_entity) {
            add(
                report,
                CrossDomainSeverity::error,
                CrossDomainCategory::revision,
                "CDV-REVISION-004",
                {identity},
                {old_entity, found->second},
                "source identity was remapped to another canonical entity",
                {},
                "review identity lineage and document an intentional split or merge");
        }
    }

    std::map<std::string, model::Position3Um, std::less<>> old_positions;
    for (const auto& node : baseline.nodes) {
        old_positions.emplace(node.id, node.position);
    }
    for (const auto& node : current.nodes) {
        const auto old = old_positions.find(node.id);
        if (old != old_positions.end() && old->second != node.position) {
            add(
                report,
                CrossDomainSeverity::info,
                CrossDomainCategory::revision,
                "CDV-REVISION-005",
                {},
                {entity_ref("node", node.id)},
                "canonical node position changed between revisions",
                {{"translation_distance_um",
                  std::to_string(static_cast<std::int64_t>(
                      distance(old->second, node.position)))}},
                "confirm that the geometry change and source transform are intentional");
        }
    }
    finalize(report);
}

}  // namespace sim_core::analysis
