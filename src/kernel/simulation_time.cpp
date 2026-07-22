#include "sim_core/kernel/simulation_time.hpp"

#include <limits>
#include <stdexcept>

namespace sim_core::kernel {

SimulationTime::SimulationTime(const std::int64_t value) noexcept : value_(value) {}

SimulationTime SimulationTime::from_microseconds(const std::int64_t value) {
    if (value < 0) {
        throw std::invalid_argument("simulation time cannot be negative");
    }
    return SimulationTime{value};
}

SimulationTime SimulationTime::zero() noexcept {
    return SimulationTime{0};
}

std::int64_t SimulationTime::count() const noexcept {
    return value_;
}

SimulationTime SimulationTime::checked_add(const std::int64_t duration_us) const {
    if (duration_us < 0) {
        throw std::invalid_argument("simulation duration cannot be negative");
    }
    if (value_ > std::numeric_limits<std::int64_t>::max() - duration_us) {
        throw std::overflow_error("simulation time overflow");
    }
    return SimulationTime{value_ + duration_us};
}

}  // namespace sim_core::kernel
