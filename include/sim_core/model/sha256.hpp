#pragma once

#include <string>
#include <string_view>

namespace sim_core::model {

[[nodiscard]] std::string sha256_hex(std::string_view input);

}  // namespace sim_core::model
