cmake_minimum_required(VERSION 3.24)

project(
    SimCore
    VERSION 0.1.0
    DESCRIPTION "Deterministic headless OHT simulation core"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

option(SIM_CORE_BUILD_TESTS "Build Sim_Core tests" ON)

include(cmake/Dependencies.cmake)

add_library(sim_core
    src/application/simulation.cpp
    src/domain/state.cpp
    src/kernel/event_queue.cpp
    src/kernel/simulation_time.cpp
    src/model/json_loader.cpp
    src/model/validator.cpp
    src/observability/event_trace.cpp
    src/observability/replay.cpp
    src/routing/dijkstra_router.cpp
)
add_library(SimCore::sim_core ALIAS sim_core)

target_include_directories(sim_core
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_compile_features(sim_core PUBLIC cxx_std_20)
target_compile_definitions(sim_core PUBLIC SIM_CORE_VERSION="${PROJECT_VERSION}")
target_link_libraries(sim_core PUBLIC nlohmann_json::nlohmann_json)

if(MSVC)
    target_compile_options(sim_core PRIVATE /W4 /permissive-)
else()
    target_compile_options(sim_core PRIVATE -Wall -Wextra -Wpedantic -Wconversion -Wshadow)
endif()

add_executable(sim_core_cli apps/sim_core_cli.cpp)
set_target_properties(sim_core_cli PROPERTIES OUTPUT_NAME sim-core)
target_link_libraries(sim_core_cli PRIVATE SimCore::sim_core)

include(CTest)
if(BUILD_TESTING AND SIM_CORE_BUILD_TESTS)
    add_executable(sim_core_tests tests/sim_core_tests.cpp)
    target_link_libraries(sim_core_tests PRIVATE SimCore::sim_core)
    target_compile_definitions(
        sim_core_tests
        PRIVATE SIM_CORE_SOURCE_DIR="${CMAKE_CURRENT_SOURCE_DIR}"
    )
    add_test(NAME sim_core_tests COMMAND sim_core_tests)
endif()
