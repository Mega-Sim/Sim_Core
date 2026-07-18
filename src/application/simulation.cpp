#include "sim_core/application/simulation.hpp"

#include "sim_core/kernel/event_queue.hpp"
#include "sim_core/model/validator.hpp"
#include "sim_core/routing/dijkstra_router.hpp"

#include <algorithm>
#include <cstdint>
#include <map>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace sim_core::application {
namespace {

using domain::JobRuntimeState;
using domain::JobState;
using domain::VehicleRuntimeState;
using domain::VehicleState;
using kernel::EventEnvelope;
using kernel::EventPriority;
using kernel::EventQueue;
using kernel::EventRequest;
using kernel::EventType;
using kernel::SimulationTime;
using observability::TraceRecord;

class Runner final {
public:
    Runner(
        const model::FacilityModelRevision& facility,
        const domain::ScenarioDefinition& scenario)
        : facility_(facility),
          scenario_(scenario),
          router_(facility),
          event_queue_(scenario.zero_delay_event_limit) {
        for (const auto& definition : scenario_.vehicles) {
            vehicles_.emplace(
                definition.id,
                VehicleRuntimeState{
                    .id = definition.id,
                    .state = VehicleState::idle,
                    .current_station_id = definition.initial_station_id,
                    .current_job_id = {},
                });
        }
        for (const auto& definition : scenario_.jobs) {
            jobs_.emplace(
                definition.id,
                JobRuntimeState{
                    .definition = definition,
                    .state = JobState::pending,
                    .released = false,
                    .assigned_vehicle_id = {},
                });
        }
    }

    SimulationResult run() {
        schedule_initial_releases();
        std::string status = "INCOMPLETE";
        std::int64_t final_time_us = 0;

        while (const auto next = event_queue_.pop_next()) {
            auto event = *next;
            if (event.simulation_time.count() > scenario_.duration_us) {
                final_time_us = scenario_.duration_us;
                status = "TIME_LIMIT";
                break;
            }

            process(event);
            trace_.append(make_trace_record(event));
            final_time_us = event.simulation_time.count();
            if (all_jobs_completed()) {
                status = "COMPLETED";
                break;
            }
        }

        observability::RunManifest manifest{
            .schema_version = "1.0.0",
            .engine_version = SIM_CORE_VERSION,
            .model_revision_id = facility_.revision_id,
            .scenario_id = scenario_.scenario_id,
            .master_seed = scenario_.master_seed,
            .run_fingerprint = run_fingerprint(),
            .status = status,
            .processed_event_count = trace_.size(),
            .final_simulation_time_us = final_time_us,
            .trace_hash_algorithm = "fnv1a64",
            .trace_hash = trace_.hash(),
        };

        return SimulationResult{
            .trace = std::move(trace_),
            .manifest = std::move(manifest),
            .vehicles = std::move(vehicles_),
            .jobs = std::move(jobs_),
        };
    }

private:
    struct Candidate {
        std::string vehicle_id;
        routing::Route route;
    };

    void schedule_initial_releases() {
        std::vector<const domain::JobDefinition*> ordered;
        ordered.reserve(scenario_.jobs.size());
        for (const auto& job : scenario_.jobs) {
            ordered.push_back(&job);
        }
        std::ranges::sort(ordered, [](const auto* left, const auto* right) {
            return std::tie(left->release_time_us, left->id) <
                   std::tie(right->release_time_us, right->id);
        });
        for (const auto* job : ordered) {
            schedule_dispatch(
                *job,
                SimulationTime::from_microseconds(job->release_time_us),
                0U);
        }
    }

    void schedule_dispatch(
        const domain::JobDefinition& job,
        const SimulationTime time,
        const std::uint64_t cause_event_id) {
        event_queue_.schedule(EventRequest{
            .simulation_time = time,
            .priority = EventPriority::demand_dispatch,
            .event_type = EventType::dispatch_requested,
            .entity_type = "job",
            .entity_id = job.id,
            .cause_event_id = cause_event_id,
            .correlation_id = job.id,
            .payload = kernel::EventPayload{
                .vehicle_id = {},
                .job_id = job.id,
                .station_id = {},
                .route_distance_um = 0,
            },
            .cancellation_key = std::nullopt,
        });
    }

    void schedule_completion(
        const EventEnvelope& cause,
        const EventType type,
        const std::int64_t delay_us,
        const std::string& vehicle_id,
        const std::string& job_id,
        const std::string& station_id,
        const std::int64_t route_distance_um) {
        event_queue_.schedule(EventRequest{
            .simulation_time = cause.simulation_time.checked_add(delay_us),
            .priority = EventPriority::movement_completion,
            .event_type = type,
            .entity_type = "job",
            .entity_id = job_id,
            .cause_event_id = cause.event_id,
            .correlation_id = cause.correlation_id,
            .payload = kernel::EventPayload{
                .vehicle_id = vehicle_id,
                .job_id = job_id,
                .station_id = station_id,
                .route_distance_um = route_distance_um,
            },
            .cancellation_key = std::nullopt,
        });
    }

    void process(EventEnvelope& event) {
        switch (event.event_type) {
        case EventType::dispatch_requested:
            handle_dispatch(event);
            return;
        case EventType::vehicle_arrived_pickup:
            handle_arrived_pickup(event);
            return;
        case EventType::loading_completed:
            handle_loading_completed(event);
            return;
        case EventType::vehicle_arrived_dropoff:
            handle_arrived_dropoff(event);
            return;
        case EventType::unloading_completed:
            handle_unloading_completed(event);
            return;
        }
        throw std::logic_error("unsupported event type");
    }

    void handle_dispatch(EventEnvelope& event) {
        auto& job = jobs_.at(event.payload.job_id);
        job.released = true;
        if (job.state != JobState::pending) {
            return;
        }

        const auto candidate = nearest_feasible_vehicle(job);
        if (!candidate.has_value()) {
            return;
        }

        auto& vehicle = vehicles_.at(candidate->vehicle_id);
        domain::transition_vehicle(vehicle, VehicleState::idle, VehicleState::to_pickup);
        domain::transition_job(job, JobState::pending, JobState::assigned);
        vehicle.current_job_id = job.definition.id;
        job.assigned_vehicle_id = vehicle.id;

        event.payload.vehicle_id = vehicle.id;
        event.payload.station_id = vehicle.current_station_id;
        event.payload.route_distance_um = candidate->route.distance_um;
        schedule_completion(
            event,
            EventType::vehicle_arrived_pickup,
            candidate->route.travel_time_us,
            vehicle.id,
            job.definition.id,
            job.definition.pickup_station_id,
            candidate->route.distance_um);
    }

    void handle_arrived_pickup(const EventEnvelope& event) {
        auto& vehicle = vehicles_.at(event.payload.vehicle_id);
        auto& job = jobs_.at(event.payload.job_id);
        domain::transition_vehicle(vehicle, VehicleState::to_pickup, VehicleState::loading);
        domain::transition_job(job, JobState::assigned, JobState::loading);
        vehicle.current_station_id = job.definition.pickup_station_id;
        schedule_completion(
            event,
            EventType::loading_completed,
            job.definition.load_duration_us,
            vehicle.id,
            job.definition.id,
            job.definition.pickup_station_id,
            0);
    }

    void handle_loading_completed(EventEnvelope& event) {
        auto& vehicle = vehicles_.at(event.payload.vehicle_id);
        auto& job = jobs_.at(event.payload.job_id);
        domain::transition_vehicle(vehicle, VehicleState::loading, VehicleState::to_dropoff);
        domain::transition_job(job, JobState::loading, JobState::in_transit);
        const auto route = router_.route_stations(
            job.definition.pickup_station_id,
            job.definition.dropoff_station_id);
        if (!route.has_value()) {
            throw std::logic_error("validated dropoff route disappeared");
        }
        event.payload.route_distance_um = route->distance_um;
        schedule_completion(
            event,
            EventType::vehicle_arrived_dropoff,
            route->travel_time_us,
            vehicle.id,
            job.definition.id,
            job.definition.dropoff_station_id,
            route->distance_um);
    }

    void handle_arrived_dropoff(const EventEnvelope& event) {
        auto& vehicle = vehicles_.at(event.payload.vehicle_id);
        auto& job = jobs_.at(event.payload.job_id);
        domain::transition_vehicle(vehicle, VehicleState::to_dropoff, VehicleState::unloading);
        domain::transition_job(job, JobState::in_transit, JobState::unloading);
        vehicle.current_station_id = job.definition.dropoff_station_id;
        schedule_completion(
            event,
            EventType::unloading_completed,
            job.definition.unload_duration_us,
            vehicle.id,
            job.definition.id,
            job.definition.dropoff_station_id,
            0);
    }

    void handle_unloading_completed(const EventEnvelope& event) {
        auto& vehicle = vehicles_.at(event.payload.vehicle_id);
        auto& job = jobs_.at(event.payload.job_id);
        domain::transition_vehicle(vehicle, VehicleState::unloading, VehicleState::idle);
        domain::transition_job(job, JobState::unloading, JobState::completed);
        vehicle.current_job_id.clear();

        for (const auto& [job_id, waiting] : jobs_) {
            (void)job_id;
            if (waiting.released && waiting.state == JobState::pending) {
                schedule_dispatch(waiting.definition, event.simulation_time, event.event_id);
            }
        }
    }

    [[nodiscard]] std::optional<Candidate> nearest_feasible_vehicle(
        const JobRuntimeState& job) const {
        std::optional<Candidate> best;
        for (const auto& [vehicle_id, vehicle] : vehicles_) {
            if (vehicle.state != VehicleState::idle) {
                continue;
            }
            const auto route = router_.route_stations(
                vehicle.current_station_id,
                job.definition.pickup_station_id);
            if (!route.has_value()) {
                continue;
            }
            if (!best.has_value() ||
                std::tie(route->travel_time_us, vehicle_id) <
                    std::tie(best->route.travel_time_us, best->vehicle_id)) {
                best = Candidate{.vehicle_id = vehicle_id, .route = *route};
            }
        }
        return best;
    }

    [[nodiscard]] TraceRecord make_trace_record(const EventEnvelope& event) const {
        TraceRecord record{
            .event_id = event.event_id,
            .simulation_time_us = event.simulation_time.count(),
            .priority = kernel::priority_value(event.priority),
            .insertion_sequence = event.insertion_sequence,
            .event_type = std::string{kernel::to_string(event.event_type)},
            .entity_type = event.entity_type,
            .entity_id = event.entity_id,
            .cause_event_id = event.cause_event_id,
            .correlation_id = event.correlation_id,
            .vehicle_id = event.payload.vehicle_id,
            .vehicle_state = {},
            .job_id = event.payload.job_id,
            .job_state = {},
            .station_id = event.payload.station_id,
            .route_distance_um = event.payload.route_distance_um,
        };
        const auto vehicle = vehicles_.find(record.vehicle_id);
        if (vehicle != vehicles_.end()) {
            record.vehicle_state = std::string{domain::to_string(vehicle->second.state)};
            record.station_id = vehicle->second.current_station_id;
        }
        const auto job = jobs_.find(record.job_id);
        if (job != jobs_.end()) {
            record.job_state = std::string{domain::to_string(job->second.state)};
        }
        return record;
    }

    [[nodiscard]] bool all_jobs_completed() const {
        return std::ranges::all_of(jobs_, [](const auto& entry) {
            return entry.second.state == JobState::completed;
        });
    }

    [[nodiscard]] std::string run_fingerprint() const {
        std::ostringstream canonical;
        canonical << facility_.revision_id << '\n' << facility_.content_hash << '\n'
                  << scenario_.schema_version << '\n' << scenario_.scenario_id << '\n'
                  << scenario_.model_revision_id << '\n' << scenario_.duration_us << '\n'
                  << scenario_.zero_delay_event_limit << '\n' << scenario_.master_seed << '\n';

        auto vehicles = scenario_.vehicles;
        std::ranges::sort(vehicles, {}, &domain::VehicleDefinition::id);
        for (const auto& vehicle : vehicles) {
            canonical << vehicle.id << '|' << vehicle.initial_station_id << '\n';
        }

        auto jobs = scenario_.jobs;
        std::ranges::sort(jobs, {}, &domain::JobDefinition::id);
        for (const auto& job : jobs) {
            canonical << job.id << '|' << job.pickup_station_id << '|'
                      << job.dropoff_station_id << '|' << job.release_time_us << '|'
                      << job.load_duration_us << '|' << job.unload_duration_us << '\n';
        }
        return observability::EventTrace::stable_hash(canonical.str());
    }

    const model::FacilityModelRevision& facility_;
    const domain::ScenarioDefinition& scenario_;
    routing::DijkstraRouter router_;
    EventQueue event_queue_;
    std::map<std::string, VehicleRuntimeState, std::less<>> vehicles_;
    std::map<std::string, JobRuntimeState, std::less<>> jobs_;
    observability::EventTrace trace_;
};

}  // namespace

Simulation::Simulation(
    const model::FacilityModelRevision& facility,
    const domain::ScenarioDefinition& scenario)
    : facility_(facility), scenario_(scenario) {}

SimulationResult Simulation::run() const {
    model::Validator::throw_if_invalid(model::Validator::validate_facility(facility_));
    model::Validator::throw_if_invalid(
        model::Validator::validate_scenario(facility_, scenario_));
    return Runner{facility_, scenario_}.run();
}

}  // namespace sim_core::application
