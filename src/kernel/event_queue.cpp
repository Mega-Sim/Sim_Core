#include "sim_core/kernel/event_queue.hpp"

#include <stdexcept>
#include <tuple>
#include <utility>

namespace sim_core::kernel {

std::string_view to_string(const EventType type) noexcept {
    switch (type) {
    case EventType::dispatch_requested:
        return "DISPATCH_REQUESTED";
    case EventType::vehicle_arrived_pickup:
        return "VEHICLE_ARRIVED_PICKUP";
    case EventType::loading_completed:
        return "LOADING_COMPLETED";
    case EventType::vehicle_arrived_dropoff:
        return "VEHICLE_ARRIVED_DROPOFF";
    case EventType::unloading_completed:
        return "UNLOADING_COMPLETED";
    }
    return "UNKNOWN";
}

std::int32_t priority_value(const EventPriority priority) noexcept {
    return static_cast<std::int32_t>(priority);
}

EventQueue::EventQueue(const std::size_t max_events_per_timestamp)
    : max_events_per_timestamp_(max_events_per_timestamp) {
    if (max_events_per_timestamp_ == 0U) {
        throw std::invalid_argument("zero-delay event limit must be positive");
    }
}

EventHandle EventQueue::schedule(EventRequest request) {
    if (request.simulation_time < current_time_) {
        throw std::logic_error("cannot schedule an event in the past");
    }

    std::uint64_t generation = 0U;
    if (request.cancellation_key.has_value()) {
        generation = cancellation_generations_[*request.cancellation_key];
    }

    EventEnvelope envelope{
        .event_id = next_event_id_++,
        .simulation_time = request.simulation_time,
        .priority = request.priority,
        .insertion_sequence = next_sequence_++,
        .event_type = request.event_type,
        .entity_type = std::move(request.entity_type),
        .entity_id = std::move(request.entity_id),
        .cause_event_id = request.cause_event_id,
        .correlation_id = std::move(request.correlation_id),
        .payload = std::move(request.payload),
        .cancellation_key = std::move(request.cancellation_key),
        .cancellation_generation = generation,
    };

    const EventHandle handle{
        .event_id = envelope.event_id,
        .cancellation_key = envelope.cancellation_key,
        .cancellation_generation = envelope.cancellation_generation,
    };
    queue_.push(std::move(envelope));
    return handle;
}

void EventQueue::cancel(const std::string_view cancellation_key) {
    if (cancellation_key.empty()) {
        throw std::invalid_argument("cancellation key cannot be empty");
    }
    ++cancellation_generations_[std::string{cancellation_key}];
}

std::optional<EventEnvelope> EventQueue::pop_next() {
    while (!queue_.empty()) {
        auto event = queue_.top();
        queue_.pop();
        if (is_cancelled(event)) {
            continue;
        }
        enforce_zero_delay_guard(event);
        current_time_ = event.simulation_time;
        return event;
    }
    return std::nullopt;
}

SimulationTime EventQueue::current_time() const noexcept {
    return current_time_;
}

std::size_t EventQueue::pending_size() const noexcept {
    return queue_.size();
}

bool EventQueue::LaterEvent::operator()(
    const EventEnvelope& left,
    const EventEnvelope& right) const noexcept {
    return std::tuple{
               left.simulation_time.count(),
               priority_value(left.priority),
               left.insertion_sequence} >
           std::tuple{
               right.simulation_time.count(),
               priority_value(right.priority),
               right.insertion_sequence};
}

bool EventQueue::is_cancelled(const EventEnvelope& event) const {
    if (!event.cancellation_key.has_value()) {
        return false;
    }
    const auto found = cancellation_generations_.find(*event.cancellation_key);
    return found != cancellation_generations_.end() &&
           found->second != event.cancellation_generation;
}

void EventQueue::enforce_zero_delay_guard(const EventEnvelope& event) {
    if (last_popped_time_.has_value() && *last_popped_time_ == event.simulation_time) {
        ++events_at_last_time_;
    } else {
        last_popped_time_ = event.simulation_time;
        events_at_last_time_ = 1U;
    }
    if (events_at_last_time_ > max_events_per_timestamp_) {
        throw std::runtime_error("zero-delay event limit exceeded");
    }
}

}  // namespace sim_core::kernel
