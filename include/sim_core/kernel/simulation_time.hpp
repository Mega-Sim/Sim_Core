#pragma once

#include <compare>
#include <cstdint>

namespace sim_core::kernel {

class SimulationTime final {
public:
    static SimulationTime from_microseconds(std::int64_t value);
    static SimulationTime zero() noexcept;

    [[nodiscard]] std::int64_t count() const noexcept;
    [[nodiscard]] SimulationTime checked_add(std::int64_t duration_us) const;

    auto operator<=>(const SimulationTime&) const = default;

private:
    explicit SimulationTime(std::int64_t value) noexcept;

    std::int64_t value_{};
};

}  // namespace sim_core::kernel
