#pragma once

#include <cstdint>
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
    std::vector<std::string> semantic_tags;
    std::vector<SourceIdentity> source_identities;
};

struct FacilityModelRevision {
    std::string schema_version;
    std::string model_id;
    std::string revision_id;
    std::string content_hash;
    CoordinateReference coordinate_reference;
    std::vector<SourceArtifact> source_artifacts;
    std::vector<Node> nodes;
    std::vector<Edge> edges;
    std::vector<Station> stations;
};

}  // namespace sim_core::model
