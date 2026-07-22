# Third-party dependencies

## JSON for Modern C++

- Project: `nlohmann/json`
- Pinned revision: `9cca280a4d0ccf0c08f47a99aa71d1b0e52f8d03` (`v3.11.3`)
- License: MIT
- Source: <https://github.com/nlohmann/json>

The dependency is resolved by CMake and is not copied into this repository.

## ezdxf

- Project: `ezdxf`
- Supported range: `>=1.4,<2`
- License: MIT
- Source: <https://github.com/mozman/ezdxf>

The native desktop package uses ezdxf to read DXF modelspace LINE and ARC
entities. PyInstaller bundles the installed package into the Windows artifact.
