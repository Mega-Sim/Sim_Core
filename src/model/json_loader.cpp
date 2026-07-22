#include "sim_core/model/json_loader.hpp"
#include "sim_core/model/sha256.hpp"

#include <nlohmann/json.hpp>

#include <cstddef>
#include <fstream>
#include <limits>
#include <sstream>
#include <string>
#include <utility>

namespace sim_core::model {
namespace {

using Json = nlohmann::json;

Json read_json(const std::filesystem::path& path) {
    std::ifstream input{path};
    if (!input) {
        throw ModelLoadError("cannot open JSON file: " + path.string());
    }

    try {
        return Json::parse(input);
    } catch (const Json::parse_error& error) {
        throw ModelLoadError(
            "invalid JSON in " + path.string() + ": " + std::string{error.what()});
    }
}

Position3Um parse_position(const Json& value) {
    return Position3Um{
        .x = value.at("x").get<std::int64_t>(),
        .y = value.at("y").get<std::int64_t>(),
        .z = value.at("z").get<std::int64_t>(),
    };
}

std::vector<SourceIdentity> parse_source_identities(const Json& entity) {
    std::vector<SourceIdentity> identities;
    const auto found = entity.find("source_identities");
    if (found == entity.end()) {
        return identities;
    }

    identities.reserve(found->size());
    for (const auto& value : *found) {
        identities.push_back(SourceIdentity{
            .source_kind = value.at("source_kind").get<std::string>(),
            .source_namespace = value.at("source_namespace").get<std::string>(),
            .external_id = value.at("external_id").get<std::string>(),
        });
    }
    return identities;
}

template <typename Function>
auto translate_json_error(const std::filesystem::path& path, Function&& function)
    -> decltype(function()) {
    try {
        return function();
    } catch (const Json::exception& error) {
        throw ModelLoadError(
            "JSON contract error in " + path.string() + ": " +
            std::string{error.what()});
    }
}

}  // namespace

FacilityModelRevision JsonLoader::load_facility(const std::filesystem::path& path) {
    const auto document = read_json(path);
    return translate_json_error(path, [&document] {
        FacilityModelRevision model;
        model.schema_version = document.at("schema_version").get<std::string>();
        model.model_id = document.at("model_id").get<std::string>();
        model.revision_id = document.at("revision_id").get<std::string>();
        model.content_hash = document.at("content_hash").get<std::string>();
        auto canonical_document = document;
        canonical_document.erase("content_hash");
        model.computed_content_hash = "sha256:" + sha256_hex(canonical_document.dump());

        const auto& coordinate = document.at("coordinate_reference");
        model.coordinate_reference = CoordinateReference{
            .frame = coordinate.at("frame").get<std::string>(),
            .length_unit = coordinate.at("length_unit").get<std::string>(),
            .up_axis = coordinate.at("up_axis").get<std::string>(),
            .handedness = coordinate.at("handedness").get<std::string>(),
        };

        for (const auto& value : document.at("source_artifacts")) {
            model.source_artifacts.push_back(SourceArtifact{
                .kind = value.at("kind").get<std::string>(),
                .source_namespace = value.at("source_namespace").get<std::string>(),
                .sha256 = value.at("sha256").get<std::string>(),
                .importer_name = value.at("importer_name").get<std::string>(),
                .importer_version = value.at("importer_version").get<std::string>(),
                .coordinate_frame = value.value("coordinate_frame", std::string{}),
            });
        }

        for (const auto& value : document.value("geometry_transforms", Json::array())) {
            model.geometry_transforms.push_back(GeometryTransform{
                .source_namespace = value.at("source_namespace").get<std::string>(),
                .source_frame = value.at("source_frame").get<std::string>(),
                .target_frame = value.at("target_frame").get<std::string>(),
                .scale_numerator = value.value("scale_numerator", std::int64_t{1}),
                .scale_denominator = value.value("scale_denominator", std::int64_t{1}),
                .translation_um = parse_position(value.at("translation_um")),
            });
        }

        for (const auto& value : document.at("nodes")) {
            model.nodes.push_back(Node{
                .id = value.at("id").get<std::string>(),
                .position = parse_position(value.at("position_um")),
                .layer = value.at("layer").get<std::string>(),
                .role = value.at("role").get<std::string>(),
                .source_identities = parse_source_identities(value),
            });
        }

        for (const auto& value : document.at("edges")) {
            Edge edge{
                .id = value.at("id").get<std::string>(),
                .from_node_id = value.at("from_node_id").get<std::string>(),
                .to_node_id = value.at("to_node_id").get<std::string>(),
                .length_um = value.at("length_um").get<std::int64_t>(),
                .speed_limit_um_per_s =
                    value.at("speed_limit_um_per_s").get<std::int64_t>(),
                .polyline = {},
                .direction = value.at("direction").get<std::string>(),
                .source_identities = parse_source_identities(value),
            };
            for (const auto& point : value.at("polyline_um")) {
                edge.polyline.push_back(parse_position(point));
            }
            model.edges.push_back(std::move(edge));
        }

        for (const auto& value : document.at("stations")) {
            std::optional<Position3Um> declared_position;
            if (value.contains("position_um")) {
                declared_position = parse_position(value.at("position_um"));
            }
            model.stations.push_back(Station{
                .id = value.at("id").get<std::string>(),
                .attachment_node_id =
                    value.at("attachment_node_id").get<std::string>(),
                .operation_type = value.at("operation_type").get<std::string>(),
                .declared_position = declared_position,
                .handling_capacity_per_hour =
                    value.value("handling_capacity_per_hour", 0.0),
                .semantic_tags =
                    value.value("semantic_tags", std::vector<std::string>{}),
                .source_identities = parse_source_identities(value),
            });
        }

        for (const auto& value : document.value("control_points", Json::array())) {
            model.control_points.push_back(ControlPoint{
                .id = value.at("id").get<std::string>(),
                .attachment_node_id =
                    value.at("attachment_node_id").get<std::string>(),
                .control_type = value.at("control_type").get<std::string>(),
                .source_identities = parse_source_identities(value),
            });
        }
        for (const auto& value : document.value("zones", Json::array())) {
            model.zones.push_back(Zone{
                .id = value.at("id").get<std::string>(),
                .node_ids = value.value("node_ids", std::vector<std::string>{}),
                .edge_ids = value.value("edge_ids", std::vector<std::string>{}),
                .capacity = value.at("capacity").get<std::int64_t>(),
                .source_identities = parse_source_identities(value),
            });
        }
        for (const auto& value : document.value("parkings", Json::array())) {
            model.parkings.push_back(Parking{
                .id = value.at("id").get<std::string>(),
                .station_id = value.at("station_id").get<std::string>(),
                .capacity = value.at("capacity").get<std::int64_t>(),
                .allowed_vehicle_type_ids = value.value(
                    "allowed_vehicle_type_ids",
                    std::vector<std::string>{}),
                .source_identities = parse_source_identities(value),
            });
        }
        for (const auto& value : document.value("chargers", Json::array())) {
            model.chargers.push_back(Charger{
                .id = value.at("id").get<std::string>(),
                .station_id = value.at("station_id").get<std::string>(),
                .capacity = value.at("capacity").get<std::int64_t>(),
                .compatible_vehicle_type_ids = value.value(
                    "compatible_vehicle_type_ids",
                    std::vector<std::string>{}),
                .source_identities = parse_source_identities(value),
            });
        }
        for (const auto& value : document.value("vehicle_types", Json::array())) {
            model.vehicle_types.push_back(VehicleType{
                .id = value.at("id").get<std::string>(),
                .maximum_speed_um_per_s =
                    value.at("maximum_speed_um_per_s").get<std::int64_t>(),
                .length_um = value.at("length_um").get<std::int64_t>(),
                .width_um = value.at("width_um").get<std::int64_t>(),
                .height_um = value.at("height_um").get<std::int64_t>(),
                .source_identities = parse_source_identities(value),
            });
        }
        return model;
    });
}

domain::ScenarioDefinition JsonLoader::load_scenario(const std::filesystem::path& path) {
    const auto document = read_json(path);
    return translate_json_error(path, [&document] {
        domain::ScenarioDefinition scenario;
        scenario.schema_version = document.at("schema_version").get<std::string>();
        scenario.scenario_id = document.at("scenario_id").get<std::string>();
        scenario.model_revision_id =
            document.at("model_revision_id").get<std::string>();
        scenario.duration_us = document.at("duration_us").get<std::int64_t>();
        scenario.master_seed = document.value("master_seed", std::uint64_t{0});

        const auto event_limit = document.value(
            "zero_delay_event_limit",
            std::uint64_t{100'000U});
        if (event_limit > std::numeric_limits<std::size_t>::max()) {
            throw ModelLoadError("zero_delay_event_limit exceeds platform size_t");
        }
        scenario.zero_delay_event_limit = static_cast<std::size_t>(event_limit);

        for (const auto& value : document.at("vehicles")) {
            scenario.vehicles.push_back(domain::VehicleDefinition{
                .id = value.at("id").get<std::string>(),
                .initial_station_id =
                    value.at("initial_station_id").get<std::string>(),
            });
        }
        for (const auto& value : document.at("jobs")) {
            scenario.jobs.push_back(domain::JobDefinition{
                .id = value.at("id").get<std::string>(),
                .pickup_station_id =
                    value.at("pickup_station_id").get<std::string>(),
                .dropoff_station_id =
                    value.at("dropoff_station_id").get<std::string>(),
                .release_time_us = value.at("release_time_us").get<std::int64_t>(),
                .load_duration_us =
                    value.at("load_duration_us").get<std::int64_t>(),
                .unload_duration_us =
                    value.at("unload_duration_us").get<std::int64_t>(),
            });
        }
        for (const auto& value : document.value("from_to_demands", Json::array())) {
            scenario.from_to_demands.push_back(domain::FromToDemand{
                .id = value.at("id").get<std::string>(),
                .from_station_id =
                    value.at("from_station_id").get<std::string>(),
                .to_station_id = value.at("to_station_id").get<std::string>(),
                .expected_moves_per_hour =
                    value.at("expected_moves_per_hour").get<double>(),
            });
        }
        return scenario;
    });
}

}  // namespace sim_core::model
