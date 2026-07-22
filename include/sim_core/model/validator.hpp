#pragma once

#include "sim_core/domain/scenario.hpp"
#include "sim_core/model/facility_model.hpp"

#include <cstddef>
#include <stdexcept>
#include <string>
#include <string_view>
#include <vector>

namespace sim_core::model {

enum class DiagnosticSeverity { warning, error };
enum class DiagnosticCategory { structural, unit, geometry, graph, scenario };

[[nodiscard]] std::string_view to_string(DiagnosticSeverity severity) noexcept;
[[nodiscard]] std::string_view to_string(DiagnosticCategory category) noexcept;

struct Diagnostic {
    DiagnosticSeverity severity{DiagnosticSeverity::error};
    DiagnosticCategory category{DiagnosticCategory::structural};
    std::string code;
    std::string entity_type;
    std::string entity_id;
    std::string message;
};

struct ValidationReport {
    std::vector<Diagnostic> diagnostics;

    [[nodiscard]] bool ok() const noexcept;
    [[nodiscard]] std::size_t error_count() const noexcept;
    [[nodiscard]] std::string summary() const;
};

class ValidationError : public std::runtime_error {
public:
    explicit ValidationError(ValidationReport report);
    [[nodiscard]] const ValidationReport& report() const noexcept;

private:
    ValidationReport report_;
};

class Validator final {
public:
    [[nodiscard]] static ValidationReport validate_facility(
        const FacilityModelRevision& model);
    [[nodiscard]] static ValidationReport validate_scenario(
        const FacilityModelRevision& model,
        const domain::ScenarioDefinition& scenario);
    static void throw_if_invalid(ValidationReport report);
};

}  // namespace sim_core::model
