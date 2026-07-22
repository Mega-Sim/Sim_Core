#pragma once

#include "sim_core/domain/scenario.hpp"
#include "sim_core/model/facility_model.hpp"

#include <filesystem>
#include <stdexcept>

namespace sim_core::model {

class ModelLoadError : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
};

class JsonLoader final {
public:
    [[nodiscard]] static FacilityModelRevision load_facility(
        const std::filesystem::path& path);
    [[nodiscard]] static domain::ScenarioDefinition load_scenario(
        const std::filesystem::path& path);
};

}  // namespace sim_core::model
