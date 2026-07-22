include(FetchContent)

find_package(nlohmann_json 3.11.3 CONFIG QUIET)

if(NOT TARGET nlohmann_json::nlohmann_json)
    set(JSON_BuildTests OFF CACHE INTERNAL "")
    set(JSON_Install OFF CACHE INTERNAL "")
    FetchContent_Declare(
        nlohmann_json
        GIT_REPOSITORY https://github.com/nlohmann/json.git
        GIT_TAG 9cca280a4d0ccf0c08f47a99aa71d1b0e52f8d03
        GIT_PROGRESS TRUE
    )
    FetchContent_MakeAvailable(nlohmann_json)
endif()
