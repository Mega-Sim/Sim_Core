#pragma once

#include <cstdint>
#include <optional>
#include <string>
#include <vector>

namespace sim_core::model {

struct SourceIdentity {
    std::string source_kind;
    std::string source_namespace;
    std::string external_id;
};

struct SourceArtifact {
    std::string kind;
    std::string source_namespace;
    std::string sha256;
    std::string importer_name;
    std::string importer_version;
    std::string coordinate_frame;
};

struct Position3Um {
    std::int64_t x{};
    std::int64_t y{};
    std::int64_t z{};

    bool operator==(const Position3Um&) const = default;
};

struct CoordinateReference {
    std::string frame;
    std::string length_unit;
    std::string up_axis;
    std::string handedness;
};

struct Node {
    std::string id;
    Position3Um position;
    std::string layer;
    std::string role;
    std::vector<SourceIdentity> source_identities;
};

struct Edge {
    std::string id;
    std::string from_node_id;
    std::string to_node_id;
    std::int64_t length_um{};
    std::int64_t speed_limit_um_per_s{};
    std::vector<Position3Um> polyline;
    std::string direction;
    std::vector<SourceIdentity> source_identities;
};

struct Station {
    std::string id;
    std::string attachment_node_id;
    std::string operation_type;
    std::optional<Position3Um> declared_position;
    double handling_capacity_per_hour{};
    std::vector<std::string> semantic_tags;
    std::vector<SourceIdentity> source_identities;
};

struct GeometryTransform {
    std::string source_namespace;
    std::string source_frame;
    std::string target_frame;
    std::int64_t scale_numerator{1};
    std::int64_t scale_denominator{1};
    Position3Um translation_um;
};

struct ControlPoint {
    std::string id;
    std::string attachment_node_id;
    std::string control_type;
    std::vector<SourceIdentity> source_identities;
};

struct Zone {
    std::string id;
    std::vector<std::string> node_ids;
    std::vector<std::string> edge_ids;
    std::int64_t capacity{};
    std::vector<SourceIdentity> source_identities;
};

struct Parking {
    std::string id;
    std::string station_id;
    std::int64_t capacity{};
    std::vector<std::string> allowed_vehicle_type_ids;
    std::vector<SourceIdentity> source_identities;
};

struct Charger {
    std::string id;
    std::string station_id;
    std::int64_t capacity{};
    std::vector<std::string> compatible_vehicle_type_ids;
    std::vector<SourceIdentity> source_identities;
};

struct VehicleType {
    std::string id;
    std::int64_t maximum_speed_um_per_s{};
    std::int64_t length_um{};
    std::int64_t width_um{};
    std::int64_t height_um{};
    std::vector<SourceIdentity> source_identities;
};

struct FacilityModelRevision {
    std::string schema_version;
    std::string model_id;
    std::string revision_id;
    std::string content_hash;
    std::string computed_content_hash;
    CoordinateReference coordinate_reference;
    std::vector<SourceArtifact> source_artifacts;
    std::vector<GeometryTransform> geometry_transforms;
    std::vector<Node> nodes;
    std::vector<Edge> edges;
    std::vector<Station> stations;
    std::vector<ControlPoint> control_points;
    std::vector<Zone> zones;
    std::vector<Parking> parkings;
    std::vector<Charger> chargers;
    std::vector<VehicleType> vehicle_types;
};

}  // namespace sim_core::model
