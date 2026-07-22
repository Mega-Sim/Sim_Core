#pragma once

#include "sim_core/kernel/event.hpp"

#include <cstddef>
#include <cstdint>
#include <map>
#include <optional>
#include <queue>
#include <string>
#include <string_view>
#include <vector>

namespace sim_core::kernel {

class EventQueue final {
public:
    explicit EventQueue(std::size_t max_events_per_timestamp = 100'000U);

    EventHandle schedule(EventRequest request);
    void cancel(std::string_view cancellation_key);
    [[nodiscard]] std::optional<EventEnvelope> pop_next();

    [[nodiscard]] SimulationTime current_time() const noexcept;
    [[nodiscard]] std::size_t pending_size() const noexcept;

private:
    struct LaterEvent {
        bool operator()(const EventEnvelope& left, const EventEnvelope& right) const noexcept;
    };

    [[nodiscard]] bool is_cancelled(const EventEnvelope& event) const;
    void enforce_zero_delay_guard(const EventEnvelope& event);

    std::priority_queue<EventEnvelope, std::vector<EventEnvelope>, LaterEvent> queue_;
    std::map<std::string, std::uint64_t, std::less<>> cancellation_generations_;
    SimulationTime current_time_{SimulationTime::zero()};
    std::optional<SimulationTime> last_popped_time_;
    std::size_t events_at_last_time_{};
    std::size_t max_events_per_timestamp_{};
    std::uint64_t next_event_id_{1U};
    std::uint64_t next_sequence_{};
};

}  // namespace sim_core::kernel
