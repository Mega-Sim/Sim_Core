# Sim_Core — Applied Materials Sharing Build

This branch provides an English-only presentation layer for sharing and demonstrating the current Sim_Core desktop workbench to Applied Materials.

## Branch

`feature/applied-materials-english`

The branch is based on the latest `main` branch and keeps the existing simulation, conversion, routing, analysis, and AutoMod export logic unchanged. The English layer is applied after the existing feature patches are installed.

## Current Demonstration Scope

### Native Desktop Workbench

- Native Qt/PySide6 desktop application
- No web browser is required for the workbench UI
- Integrated workspace for model inputs, CAD conversion, flow analysis, and deterministic simulation

### CAD / Rail Layout Processing

- Load DXF or Rail layout data
- Convert layout geometry into a directed graph representation
- Visualize large layouts with optimized graph rendering
- Zoom, pan, select graph edges, and reverse selected edge directions
- Save the converted Graph JSON

### Layout Static Analysis

- Select either Random FromTo or Actual FromTo analysis mode
- Generate random station-to-station demand for layout-only analysis
- Load an actual FromTo CSV and use its transport volumes directly
- Route demand through directed shortest paths
- Visualize edge traffic with a green-to-red heatmap
- Preserve the original Actual FromTo CSV and save a separate analysis snapshot

### AutoMod Model Export

- Convert the current CAD/Rail graph into an AutoMod `model.arc` structure
- Generate `pm.asy` linked to the converted graph data

### Core Analysis and Simulation

- Validate Facility and Scenario inputs
- Run flow analysis through the Sim_Core executable when available
- Review edge flow, reachable routes, merge pressure, and station capacity metrics
- Run deterministic discrete-event simulation and review run manifest information

## English Presentation Layer

The branch adds `desktop/english_ui_patch.py`, which translates the user-facing presentation layer without changing the underlying modeling or analysis behavior.

The translated surface includes:

- Navigation and page titles
- Input cards and CAD conversion controls
- Random / Actual FromTo controls
- Layout static-analysis status messages
- Heatmap dialog labels and metrics
- Graph toolbar and direction-reversal controls
- File dialogs and message boxes
- AutoMod conversion controls and status messages
- Core analysis and simulation controls

## Entry Point

The desktop entry point remains:

```text
desktop/app.py
```

The English presentation layer is enabled only on this sharing branch through:

```python
install_applied_english_ui(base)
```

This design keeps the mainline implementation intact while providing a clean English-facing demonstration build for external review.
