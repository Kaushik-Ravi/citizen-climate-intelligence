# Citizen Centered Climate Intelligence

Reference implementation and companion repository map for the chapter:

**Ravi, K., & Brück, A. (forthcoming). Citizen Centered Climate Intelligence: Operationalizing Open Tree Data for Urban Cooling and Eco-Routing in Indian Cities. In _Data, Cities and Citizens: How open data revolutionizes urban and transport planning_.**

## Purpose

This repository provides the reproducibility entry point for the chapter's integrated framework. It contains compact reference scripts that express the core methodological logic and links to the companion application repositories used to prototype the three modules.

The framework should be read as a data-to-decision pipeline:

1. A tree inventory layer supplies tree locations and structural attributes.
2. Those records are converted into ecosystem-service analytics, including biomass-derived CO2 equivalent, localized cooling metrics, and tree archetypes.
3. Tree-derived attributes are aggregated to street segments for planning and environmental routing.

In the Pune case study, the baseline tree inventory layer comes from the Pune municipal tree census. The smartphone measurement module demonstrates how comparable inventory records could be generated or updated in contexts where municipal inventories are absent, incomplete, or outdated.

## Repository Contents

| File | Role in chapter |
|---|---|
| `photogrammetry_model.py` | Reference logic for smartphone-based photogrammetric tree measurement. |
| `analytics_engine.py` | Reference logic for road-segment environmental scoring using tree attributes. |
| `routing_logic.py` | Reference logic for route scoring with environmental utility. |
| `MODULES.md` | Mapping between chapter modules and companion implementation repositories. |
| `REPRODUCIBILITY.md` | Scope, assumptions, and reproducibility notes for the case study. |
| `ZENODO.md` | Release and DOI workflow for archiving the umbrella repository. |
| `docs/data-flow.md` | Data-flow explanation for the integrated framework. |
| `CITATION.cff` | Citation metadata for software citation tools. |

## Companion Repositories

The full prototype is distributed across companion repositories rather than vendored or merged into this repository. This keeps each module's dependencies, deployment choices, and limitations explicit while preserving the umbrella repository as the citation and reproducibility entry point.

| Chapter module | Companion repository | Purpose |
|---|---|---|
| Module 1: Democratized Measurement Toolkit | <https://github.com/Kaushik-Ravi/tree-measurement-frontend> | Smartphone-facing tree measurement frontend and field workflow. |
| Module 2: Analytics Dashboard | <https://github.com/Kaushik-Ravi/pune-tree-dashboard-sample> | Pune tree analytics dashboard and planning-oriented visualization workflow. |
| Module 3: Eco-Routing Engine | <https://github.com/Kaushik-Ravi/Eco-Path> | Environmental routing prototype using tree-derived road-segment scores. |

See `MODULES.md` for a more detailed mapping.

## Installation

The reference scripts require Python 3.9+.

```bash
pip install -r requirements.txt
```

The scripts are intentionally compact reference implementations. Inspect them as method sketches, or run them after checking local dependencies and imports:

```bash
python photogrammetry_model.py
python analytics_engine.py
python routing_logic.py
```

## Reproducibility Scope

This repository is not a production deployment and does not include raw municipal datasets, private API credentials, model weights, local environment files, or generated build artifacts.

The scripts are intended to make the chapter's methodological logic transparent. The companion repositories contain fuller application prototypes, but should be reviewed for deployment-specific configuration before reuse.

## Important Notes

- The Pune case study uses the municipal tree census as the baseline inventory layer.
- Citizen measurement is presented as a pathway for generating or updating comparable inventory records where official data are missing or stale.
- The code is proof-of-concept research software, not certified planning, forestry, or emissions-inventory software.
- Large model weights and secrets must not be committed to this repository.

## Citation

If you use this repository or the companion prototypes, please cite the chapter and this software repository. Citation metadata are provided in `CITATION.cff`.
