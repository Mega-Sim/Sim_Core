#include "sim_core/adapters/csv/from_to_csv.hpp"

#include <algorithm>
#include <array>
#include <cctype>
#include <cmath>
#include <fstream>
#include <map>
#include <ranges>
#include <sstream>
#include <string>
#include <string_view>

namespace sim_core::adapters::csv {
namespace {

std::string trim(std::string value) {
    const auto not_space = [](const unsigned char character) {
        return std::isspace(character) == 0;
    };
    const auto first = std::ranges::find_if(value, not_space);
    const auto last = std::find_if(value.rbegin(), value.rend(), not_space).base();
    if (first >= last) {
        return {};
    }
    return std::string{first, last};
}

std::vector<std::string> parse_row(
    const std::string_view row,
    const std::size_t line_number) {
    std::vector<std::string> fields;
    std::string field;
    bool quoted = false;
    for (std::size_t index = 0U; index < row.size(); ++index) {
        const char character = row[index];
        if (character == '"') {
            if (quoted && index + 1U < row.size() && row[index + 1U] == '"') {
                field.push_back('"');
                ++index;
            } else {
                quoted = !quoted;
            }
        } else if (character == ',' && !quoted) {
            fields.push_back(trim(std::move(field)));
            field.clear();
        } else {
            field.push_back(character);
        }
    }
    if (quoted) {
        throw CsvImportError(
            "unterminated quoted field at CSV line " + std::to_string(line_number));
    }
    fields.push_back(trim(std::move(field)));
    return fields;
}

double parse_rate(const std::string& value, const std::size_t line_number) {
    std::size_t parsed = 0U;
    double result = 0.0;
    try {
        result = std::stod(value, &parsed);
    } catch (const std::exception&) {
        throw CsvImportError(
            "invalid expected_moves_per_hour at CSV line " +
            std::to_string(line_number));
    }
    if (parsed != value.size() || !std::isfinite(result)) {
        throw CsvImportError(
            "invalid expected_moves_per_hour at CSV line " +
            std::to_string(line_number));
    }
    return result;
}

}  // namespace

std::vector<domain::FromToDemand> FromToCsvAdapter::load(
    const std::filesystem::path& path) {
    std::ifstream input{path};
    if (!input) {
        throw CsvImportError("cannot open From-To CSV file: " + path.string());
    }

    std::string line;
    if (!std::getline(input, line)) {
        throw CsvImportError("From-To CSV is empty: " + path.string());
    }
    if (line.ends_with('\r')) {
        line.pop_back();
    }
    if (line.starts_with("\xEF\xBB\xBF")) {
        line.erase(0U, 3U);
    }

    const auto header = parse_row(line, 1U);
    std::map<std::string, std::size_t, std::less<>> columns;
    for (std::size_t index = 0U; index < header.size(); ++index) {
        if (!columns.emplace(header[index], index).second) {
            throw CsvImportError("duplicate From-To CSV column: " + header[index]);
        }
    }
    constexpr std::array<std::string_view, 4> required{
        "id",
        "from_station_id",
        "to_station_id",
        "expected_moves_per_hour",
    };
    for (const auto name : required) {
        if (!columns.contains(name)) {
            throw CsvImportError("missing From-To CSV column: " + std::string{name});
        }
    }

    std::vector<domain::FromToDemand> result;
    std::size_t line_number = 1U;
    while (std::getline(input, line)) {
        ++line_number;
        if (line.ends_with('\r')) {
            line.pop_back();
        }
        if (trim(line).empty()) {
            continue;
        }
        const auto fields = parse_row(line, line_number);
        if (fields.size() != header.size()) {
            throw CsvImportError(
                "column count mismatch at CSV line " + std::to_string(line_number));
        }
        const auto value = [&fields, &columns](const std::string_view name) -> const std::string& {
            const auto found = columns.find(name);
            if (found == columns.end()) {
                throw CsvImportError("missing From-To CSV column: " + std::string{name});
            }
            return fields.at(found->second);
        };
        result.push_back(domain::FromToDemand{
            .id = value("id"),
            .from_station_id = value("from_station_id"),
            .to_station_id = value("to_station_id"),
            .expected_moves_per_hour =
                parse_rate(value("expected_moves_per_hour"), line_number),
        });
    }
    return result;
}

}  // namespace sim_core::adapters::csv
