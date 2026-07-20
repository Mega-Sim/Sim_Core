#pragma once

#include "sim_core/domain/scenario.hpp"

#include <filesystem>
#include <stdexcept>
#include <vector>

namespace sim_core::adapters::csv {

class CsvImportError : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
};

class FromToCsvAdapter final {
public:
    [[nodiscard]] static std::vector<domain::FromToDemand> load(
        const std::filesystem::path& path);
};

}  // namespace sim_core::adapters::csv
