#include "sim_core/adapters/csv/from_to_csv.hpp"
#include "sim_core/analysis/cross_domain_validator.hpp"
#include "sim_core/application/simulation.hpp"
#include "sim_core/domain/job.hpp"
#include "sim_core/domain/vehicle.hpp"
#include "sim_core/kernel/event_queue.hpp"
#include "sim_core/kernel/simulation_time.hpp"
#include "sim_core/model/json_loader.hpp"
#include "sim_core/model/sha256.hpp"
#include "sim_core/model/validator.hpp"
#include "sim_core/observability/replay.hpp"
#include "sim_core/routing/dijkstra_router.hpp"

#include <algorithm>
#include <cstdint>
#include <filesystem>
#include <functional>
#include <iostream>
#include <limits>
#include <optional>
#include <stdexcept>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

namespace {

class TestFailure : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
};

void check(const bool condition, const std::string_view expression, const int line) {
    if (!condition) {
        throw TestFailure(
            "line " + std::to_string(line) + ": check failed: " +
            std::string{expression});
    }
}

#define CHECK(expression) check(static_cast<bool>(expression), #expression, __LINE__)

template <typename Exception, typename Function>
void check_throws(Function&& function, const int line) {
    try {
        function();
    } catch (const Exception&) {
        return;
    }
    throw TestFailure("line " + std::to_string(line) + ": expected exception was not thrown");
}

#define CHECK_THROWS(exception, expression) \
    check_throws<exception>([&] { static_cast<void>(expression); }, __LINE__)

std::filesystem::path source_path(const std::string_view relative) {
    return std::filesystem::path{SIM_CORE_SOURCE_DIR} / relative;
}

sim_core::model::FacilityModelRevision load_facility() {
    return sim_core::model::JsonLoader::load_facility(
        source_path("examples/single_line/facility.json"));
}

sim_core::domain::ScenarioDefinition load_scenario() {
    return sim_core::model::JsonLoader::load_scenario(
        source_path("examples/single_line/scenario.json"));
}

sim_core::model::FacilityModelRevision load_cross_domain_facility() {
    return sim_core::model::JsonLoader::load_facility(
        source_path("examples/cross_domain/facility.json"));
}

sim_core::domain::ScenarioDefinition load_cross_domain_scenario() {
    return sim_core::model::JsonLoader::load_scenario(
        source_path("examples/cross_domain/scenario.json"));
}

bool has_rule(
    const sim_core::analysis::CrossDomainReport& report,
    const std::string_view rule_id) {
    return std::ranges::any_of(
        report.diagnostics,
        [rule_id](const auto& diagnostic) { return diagnostic.rule_id == rule_id; });
}

sim_core::kernel::EventRequest request(
    const std::int64_t time_us,
    const sim_core::kernel::EventPriority priority,
    const std::string& entity_id,
    std::optional<std::string> cancellation_key = std::nullopt) {
    return sim_core::kernel::EventRequest{
        .simulation_time =
            sim_core::kernel::SimulationTime::from_microseconds(time_us),
        .priority = priority,
        .event_type = sim_core::kernel::EventType::dispatch_requested,
        .entity_type = "test",
        .entity_id = entity_id,
        .cause_event_id = 0,
        .correlation_id = entity_id,
        .payload = {},
        .cancellation_key = std::move(cancellation_key),
    };
}

void simulation_time_is_checked() {
    using sim_core::kernel::SimulationTime;
    CHECK(SimulationTime::zero().count() == 0);
    CHECK(SimulationTime::from_microseconds(10).checked_add(5).count() == 15);
    CHECK_THROWS(std::invalid_argument, SimulationTime::from_microseconds(-1));
    CHECK_THROWS(
        std::overflow_error,
        SimulationTime::from_microseconds(std::numeric_limits<std::int64_t>::max())
            .checked_add(1));
}

void event_queue_is_deterministic() {
    using sim_core::kernel::EventPriority;
    sim_core::kernel::EventQueue queue;
    queue.schedule(request(10, EventPriority::demand_dispatch, "late-priority"));
    queue.schedule(request(10, EventPriority::resource_release, "first"));
    queue.schedule(request(10, EventPriority::resource_release, "second"));

    const auto first = queue.pop_next();
    const auto second = queue.pop_next();
    const auto third = queue.pop_next();
    CHECK(first.has_value() && first->entity_id == "first");
    CHECK(second.has_value() && second->entity_id == "second");
    CHECK(third.has_value() && third->entity_id == "late-priority");
    CHECK(!queue.pop_next().has_value());
    CHECK_THROWS(
        std::logic_error,
        queue.schedule(request(9, EventPriority::observation, "past")));
}

void event_cancellation_and_zero_delay_guard_work() {
    using sim_core::kernel::EventPriority;
    sim_core::kernel::EventQueue cancelled;
    cancelled.schedule(request(
        0,
        EventPriority::state_transition,
        "cancelled",
        std::string{"vehicle:1"}));
    cancelled.cancel("vehicle:1");
    CHECK(!cancelled.pop_next().has_value());

    sim_core::kernel::EventQueue guarded{2};
    guarded.schedule(request(0, EventPriority::observation, "one"));
    guarded.schedule(request(0, EventPriority::observation, "two"));
    guarded.schedule(request(0, EventPriority::observation, "three"));
    CHECK(guarded.pop_next().has_value());
    CHECK(guarded.pop_next().has_value());
    CHECK_THROWS(std::runtime_error, guarded.pop_next());
}

void canonical_model_and_scenario_validate() {
    const auto facility = load_facility();
    const auto scenario = load_scenario();
    CHECK(sim_core::model::Validator::validate_facility(facility).ok());
    CHECK(sim_core::model::Validator::validate_scenario(facility, scenario).ok());

    auto duplicate = facility;
    duplicate.nodes.push_back(duplicate.nodes.front());
    CHECK(!sim_core::model::Validator::validate_facility(duplicate).ok());

    auto unsupported_speed = facility;
    unsupported_speed.edges.front().speed_limit_um_per_s =
        sim_core::routing::DijkstraRouter::maximum_supported_speed_um_per_s + 1;
    CHECK(!sim_core::model::Validator::validate_facility(unsupported_speed).ok());

    auto unreachable = scenario;
    unreachable.jobs.front().dropoff_station_id = "ST-START";
    CHECK(!sim_core::model::Validator::validate_scenario(facility, unreachable).ok());
}

void routing_respects_direction_and_integer_time() {
    const auto facility = load_facility();
    const sim_core::routing::DijkstraRouter router{facility};
    const auto forward = router.route_stations("ST-START", "ST-DROPOFF");
    CHECK(forward.has_value());
    CHECK(forward->edge_ids.size() == 2U);
    CHECK(forward->distance_um == 30'000'000);
    CHECK(forward->travel_time_us == 15'000'000);
    CHECK(!router.route_stations("ST-DROPOFF", "ST-START").has_value());
}

void nearest_feasible_dispatch_is_deterministic() {
    const auto facility = load_facility();
    auto scenario = load_scenario();
    scenario.vehicles = {
        {.id = "OHT-002", .initial_station_id = "ST-START"},
        {.id = "OHT-001", .initial_station_id = "ST-START"},
    };
    const auto result = sim_core::application::Simulation{facility, scenario}.run();
    CHECK(result.trace.records().front().vehicle_id == "OHT-001");
}

void golden_run_is_reproducible_and_replayable() {
    const auto facility = load_facility();
    const auto scenario = load_scenario();
    const auto first = sim_core::application::Simulation{facility, scenario}.run();
    const auto second = sim_core::application::Simulation{facility, scenario}.run();

    CHECK(first.manifest.status == "COMPLETED");
    CHECK(first.manifest.processed_event_count == 5U);
    CHECK(first.manifest.final_simulation_time_us == 20'000'000);
    CHECK(first.manifest.trace_hash == second.manifest.trace_hash);
    CHECK(first.manifest.run_fingerprint == second.manifest.run_fingerprint);
    CHECK(first.manifest.trace_hash == "70240b9d9276d97c");
    CHECK(first.manifest.run_fingerprint == "5004192c136cc90e");
    CHECK(first.vehicles.at("OHT-001").state == sim_core::domain::VehicleState::idle);
    CHECK(first.jobs.at("JOB-001").state == sim_core::domain::JobState::completed);

    const std::vector<std::string> expected_states{
        "TO_PICKUP",
        "LOADING",
        "TO_DROPOFF",
        "UNLOADING",
        "IDLE",
    };
    CHECK(first.trace.records().size() == expected_states.size());
    for (std::size_t index = 0; index < expected_states.size(); ++index) {
        CHECK(first.trace.records()[index].vehicle_state == expected_states[index]);
    }

    const auto test_directory =
        std::filesystem::temp_directory_path() / "sim_core_vertical_slice_tests";
    std::filesystem::remove_all(test_directory);
    std::filesystem::create_directories(test_directory);
    const auto trace_path = test_directory / "event_trace.jsonl";
    first.trace.write_jsonl(trace_path);
    const auto replay = sim_core::observability::TraceReplay::replay(trace_path);
    CHECK(replay.event_count == 5U);
    CHECK(replay.completed_job_count == 1U);
    CHECK(replay.vehicle_states.at("OHT-001") == "IDLE");
    CHECK(replay.job_states.at("JOB-001") == "COMPLETED");
    std::filesystem::remove_all(test_directory);
}

void sha256_and_content_hash_are_verified() {
    CHECK(
        sim_core::model::sha256_hex("abc") ==
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
    const auto facility = load_cross_domain_facility();
    CHECK(facility.schema_version == "1.1.0");
    CHECK(facility.content_hash == facility.computed_content_hash);
    CHECK(sim_core::model::Validator::validate_facility(facility).ok());

    auto changed = facility;
    changed.content_hash.back() = changed.content_hash.back() == '0' ? '1' : '0';
    const auto invalid = sim_core::model::Validator::validate_facility(changed);
    CHECK(!invalid.ok());
    CHECK(std::ranges::any_of(invalid.diagnostics, [](const auto& diagnostic) {
        return diagnostic.code == "CONTENT_HASH_MISMATCH";
    }));
}

void from_to_csv_and_cross_domain_route_are_deterministic() {
    const auto facility = load_cross_domain_facility();
    auto scenario = load_cross_domain_scenario();
    scenario.from_to_demands =
        sim_core::adapters::csv::FromToCsvAdapter::load(
            source_path("examples/cross_domain/from_to.csv"));
    const auto first =
        sim_core::analysis::CrossDomainValidator::analyze(facility, scenario);
    const auto second =
        sim_core::analysis::CrossDomainValidator::analyze(facility, scenario);
    CHECK(first.ok());
    CHECK(first.warning_count() == 0U);
    CHECK(first.demand_routes.size() == 1U);
    CHECK(first.demand_routes.front().distance_um == 30'000'000);
    CHECK(first.demand_routes.front().travel_time_us == 15'000'000);
    CHECK(first.demand_routes.front().edge_ids ==
          std::vector<std::string>({"E-A-B", "E-B-C"}));
    CHECK(first.to_json() == second.to_json());
}

void cross_domain_rules_explain_invalid_inputs() {
    auto facility = load_cross_domain_facility();
    auto scenario = load_cross_domain_scenario();

    facility.stations.front().source_identities =
        facility.nodes.front().source_identities;
    facility.stations.at(1).declared_position =
        sim_core::model::Position3Um{.x = 20'000'000, .y = 0, .z = 0};
    scenario.from_to_demands.front().expected_moves_per_hour = 200.0;

    const auto report =
        sim_core::analysis::CrossDomainValidator::analyze(facility, scenario);
    CHECK(!report.ok());
    CHECK(has_rule(report, "CDV-IDENTITY-002"));
    CHECK(has_rule(report, "CDV-GEOMETRY-004"));
    CHECK(has_rule(report, "CDV-CAPACITY-001"));
    CHECK(report.warning_count() == 2U);
}

void cross_domain_detects_unreachable_demand_and_missing_transform() {
    auto facility = load_cross_domain_facility();
    const auto scenario = load_cross_domain_scenario();
    facility.geometry_transforms.clear();
    facility.edges.erase(facility.edges.begin() + 1);

    const auto report =
        sim_core::analysis::CrossDomainValidator::analyze(facility, scenario);
    CHECK(!report.ok());
    CHECK(has_rule(report, "CDV-GEOMETRY-003"));
    CHECK(has_rule(report, "CDV-DEMAND-003"));
    CHECK(report.demand_routes.empty());
}

void revision_diff_detects_identity_remap_and_hash_reuse() {
    const auto baseline = load_cross_domain_facility();
    auto current = baseline;
    current.content_hash =
        "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    current.nodes.at(1).source_identities = current.nodes.front().source_identities;
    current.nodes.front().source_identities.clear();

    auto report = sim_core::analysis::CrossDomainValidator::analyze(
        current,
        load_cross_domain_scenario());
    sim_core::analysis::CrossDomainValidator::compare_revisions(
        report,
        baseline,
        current);
    CHECK(!report.ok());
    CHECK(has_rule(report, "CDV-REVISION-002"));
    CHECK(has_rule(report, "CDV-REVISION-004"));
}

}  // namespace

int main() {
    const std::vector<std::pair<std::string_view, std::function<void()>>> tests{
        {"simulation time", simulation_time_is_checked},
        {"deterministic event queue", event_queue_is_deterministic},
        {"cancellation and zero-delay guard", event_cancellation_and_zero_delay_guard_work},
        {"canonical validation", canonical_model_and_scenario_validate},
        {"directed Dijkstra routing", routing_respects_direction_and_integer_time},
        {"deterministic dispatch", nearest_feasible_dispatch_is_deterministic},
        {"golden run and replay", golden_run_is_reproducible_and_replayable},
        {"SHA-256 content hash", sha256_and_content_hash_are_verified},
        {"From-To CSV and route analysis", from_to_csv_and_cross_domain_route_are_deterministic},
        {"cross-domain diagnostics", cross_domain_rules_explain_invalid_inputs},
        {"unreachable demand and transform diagnostics", cross_domain_detects_unreachable_demand_and_missing_transform},
        {"revision cross-validation", revision_diff_detects_identity_remap_and_hash_reuse},
    };

    std::size_t failures = 0U;
    for (const auto& [name, test] : tests) {
        try {
            test();
            std::cout << "[PASS] " << name << '\n';
        } catch (const std::exception& error) {
            ++failures;
            std::cerr << "[FAIL] " << name << ": " << error.what() << '\n';
        }
    }
    std::cout << (tests.size() - failures) << '/' << tests.size() << " tests passed\n";
    return failures == 0U ? 0 : 1;
}
