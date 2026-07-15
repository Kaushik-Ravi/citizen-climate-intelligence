# Module Mapping

This document maps the chapter's three methodological modules to the reference scripts in this repository and to the companion implementation repositories.

## Integrated Framework

The framework is connected through a shared tree inventory layer. In the Pune case study, that layer is derived from the municipal tree census. In other settings, the smartphone measurement workflow can provide a pathway for creating or updating comparable tree records.

The same tree-derived attributes then move across the framework:

1. Tree location, species identity, height, DBH/GBH, and canopy diameter are represented as tree inventory records.
2. The analytics module converts those records into carbon, cooling, and archetype indicators.
3. The routing module aggregates tree-derived indicators to road segments for route scoring.

## Module 1: Democratized Measurement Toolkit

**Chapter role:** Generate or update tree-level inventory records using commodity smartphones and user-guided measurement workflows.

**Reference file in this repository:** `photogrammetry_model.py`

**Companion implementation repository:** <https://github.com/Kaushik-Ravi/tree-measurement-frontend>

**Conceptual outputs:**

- tree location;
- species identity, when available through census labels or species-identification services;
- tree height;
- canopy diameter;
- DBH/GBH or equivalent trunk measurement;
- image and calibration metadata where available.

**Reproducibility note:** In the Pune case study, the downstream analytics use the municipal tree census as the baseline inventory. Module 1 demonstrates how comparable records can be produced where such inventories are not available or require updating.

## Module 2: Analytics Engine and Dashboard

**Chapter role:** Convert tree inventory records and satellite observations into ecosystem-service analytics for planning.

**Reference file in this repository:** `analytics_engine.py`

**Companion implementation repository:** <https://github.com/Kaushik-Ravi/pune-tree-dashboard-sample>

**Conceptual outputs:**

- biomass-derived CO2 equivalent;
- localized cooling metrics;
- tree archetype classes;
- dashboard-ready layers for planning and simulation.

**Important methodological distinction:** NDVI is used to construct vegetated or non-vegetated comparison masks for thermal analysis. The focal tree locations are supplied by the tree inventory layer.

## Module 3: Eco-Routing Engine

**Chapter role:** Aggregate tree-derived attributes to street segments and evaluate routes using environmental utility.

**Reference file in this repository:** `routing_logic.py`

**Companion implementation repository:** <https://github.com/Kaushik-Ravi/Eco-Path>

**Conceptual outputs:**

- Static Environmental Quality (SEQ) score;
- Serenity Score for walking or recreational routing;
- route ranking using distance, emissions, and environmental reward terms;
- loop or turnaround route suggestions for recreational use cases.

## Why The Repositories Are Separate

The implementation repositories are intentionally kept separate because each module has different dependencies, deployment assumptions, and data requirements. The integration occurs through the data model and analytical flow, not through forcing all application code into a single monorepo.

The umbrella repository should therefore be cited as the reproducibility entry point, while the companion repositories should be cited where a specific deployed prototype or module implementation is reused.
