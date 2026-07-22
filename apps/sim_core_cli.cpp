#include "sim_core/adapters/csv/from_to_csv.hpp"
#include "sim_core/analysis/cross_domain_validator.hpp"
#include "sim_core/application/simulation.hpp"
#include "sim_core/model/json_loader.hpp"
#include "sim_core/model/validator.hpp"
#include "sim_core/observability/event_trace.hpp"
#include "sim_core/observability/replay.hpp"

#include <nlohmann/json.hpp>

#include <filesystem>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <string_view>

namespace {

using Options = std::map<std::string, std::string, std::less<>>;

void print_help() {
    std::cout
        << "Sim_Core deterministic headless Vertical Slice\n\n"
        << "Usage:\n"
        << "  sim-core validate --facility FILE --scenario FILE\n"
        << "  sim-core analyze --facility FILE --scenario FILE"
           " [--from-to-csv FILE] [--baseline-facility FILE] [--output FILE]\n"
        << "  sim-core run --facility FILE --scenario FILE [--output DIR]\n"
        << "  sim-core replay --trace FILE\n";
}

Options parse_options(const int argc, char* argv[], const int first) {
    Options options;
    for (int index = first; index < argc; index += 2) {
        const std::string key{argv[index]};
        if (!key.starts_with("--") || index + 1 >= argc) {
            throw std::invalid_argument("options must use --name VALUE pairs");
        }
        if (!options.emplace(key, argv[index + 1]).second) {
            throw std::invalid_argument("duplicate option: " + key);
        }
    }
    return options;
}

const std::string& require(const Options& options, const std::string_view name) {
    const auto found = options.find(name);
    if (found == options.end()) {
        throw std::invalid_argument("missing required option: " + std::string{name});
    }
    return found->second;
}

void validate_inputs(
    const sim_core::model::FacilityModelRevision& facility,
    const sim_core::domain::ScenarioDefinition& scenario) {
    const auto facility_report =
        sim_core::model::Validator::validate_facility(facility);
    sim_core::model::Validator::throw_if_invalid(facility_report);
    const auto scenario_report =
        sim_core::model::Validator::validate_scenario(facility, scenario);
    sim_core::model::Validator::throw_if_invalid(scenario_report);
}

int validate_command(const Options& options) {
    const auto facility = sim_core::model::JsonLoader::load_facility(
        require(options, "--facility"));
    const auto scenario = sim_core::model::JsonLoader::load_scenario(
        require(options, "--scenario"));
    validate_inputs(facility, scenario);
    std::cout << "VALID model=" << facility.revision_id
              << " scenario=" << scenario.scenario_id << '\n';
    return 0;
}

int run_command(const Options& options) {
    const auto facility = sim_core::model::JsonLoader::load_facility(
        require(options, "--facility"));
    const auto scenario = sim_core::model::JsonLoader::load_scenario(
        require(options, "--scenario"));
    validate_inputs(facility, scenario);

    const auto output = std::filesystem::path{
        options.contains("--output") ? options.at("--output") : "run-output"};
    std::filesystem::create_directories(output);

    const sim_core::application::Simulation simulation{facility, scenario};
    const auto result = simulation.run();
    result.trace.write_jsonl(output / "event_trace.jsonl");
    sim_core::observability::write_manifest(
        result.manifest,
        output / "run_manifest.json");

    std::cout << "status=" << result.manifest.status
              << " events=" << result.manifest.processed_event_count
              << " final_time_us=" << result.manifest.final_simulation_time_us
              << " trace_hash=" << result.manifest.trace_hash << '\n';
    std::cout << "output=" << std::filesystem::absolute(output).string() << '\n';
    return result.manifest.status == "COMPLETED" ? 0 : 3;
}

int analyze_command(const Options& options) {
    const auto facility = sim_core::model::JsonLoader::load_facility(
        require(options, "--facility"));
    auto scenario = sim_core::model::JsonLoader::load_scenario(
        require(options, "--scenario"));
    if (options.contains("--from-to-csv")) {
        scenario.from_to_demands =
            sim_core::adapters::csv::FromToCsvAdapter::load(
                options.at("--from-to-csv"));
    }
    sim_core::model::Validator::throw_if_invalid(
        sim_core::model::Validator::validate_facility(facility));
    auto runtime_contract = scenario;
    runtime_contract.from_to_demands.clear();
    sim_core::model::Validator::throw_if_invalid(
        sim_core::model::Validator::validate_scenario(
            facility,
            runtime_contract));

    auto report = sim_core::analysis::CrossDomainValidator::analyze(
        facility,
        scenario);
    if (options.contains("--baseline-facility")) {
        const auto baseline = sim_core::model::JsonLoader::load_facility(
            options.at("--baseline-facility"));
        sim_core::model::Validator::throw_if_invalid(
            sim_core::model::Validator::validate_facility(baseline));
        sim_core::analysis::CrossDomainValidator::compare_revisions(
            report,
            baseline,
            facility);
    }
    if (options.contains("--output")) {
        report.write_json(options.at("--output"));
        std::cout << "analysis_status=" << (report.ok() ? "PASS" : "FAIL")
                  << " errors=" << report.error_count()
                  << " warnings=" << report.warning_count()
                  << " routes=" << report.demand_routes.size() << '\n';
        std::cout << "output="
                  << std::filesystem::absolute(options.at("--output")).string()
                  << '\n';
    } else {
        std::cout << report.to_json();
    }
    return report.ok() ? 0 : 4;
}

int replay_command(const Options& options) {
    const auto summary = sim_core::observability::TraceReplay::replay(
        require(options, "--trace"));
    const nlohmann::json output{
        {"event_count", summary.event_count},
        {"final_simulation_time_us", summary.final_simulation_time_us},
        {"completed_job_count", summary.completed_job_count},
        {"vehicle_states", summary.vehicle_states},
        {"job_states", summary.job_states},
    };
    std::cout << output.dump(2) << '\n';
    return 0;
}

}  // namespace

int main(const int argc, char* argv[]) {
    try {
        if (argc < 2 || std::string_view{argv[1]} == "--help" ||
            std::string_view{argv[1]} == "-h") {
            print_help();
            return argc < 2 ? 2 : 0;
        }
        const std::string command{argv[1]};
        const auto options = parse_options(argc, argv, 2);
        if (command == "validate") {
            return validate_command(options);
        }
        if (command == "analyze") {
            return analyze_command(options);
        }
        if (command == "run") {
            return run_command(options);
        }
        if (command == "replay") {
            return replay_command(options);
        }
        throw std::invalid_argument("unknown command: " + command);
    } catch (const std::exception& error) {
        std::cerr << "sim-core error: " << error.what() << '\n';
        return 2;
    }
}
