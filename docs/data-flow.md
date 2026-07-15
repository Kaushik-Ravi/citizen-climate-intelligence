# Integrated Data Flow

The framework connects citizen science, municipal open data, remote sensing, and routing through a shared tree inventory layer.

## 1. Tree Inventory Layer

The tree inventory layer contains geolocated tree records. In the Pune case study, this layer is supplied by the municipal tree census. In contexts without a sufficiently current inventory, the citizen measurement toolkit provides a pathway for creating compatible records.

Typical fields include:

- location;
- species identity;
- tree height;
- DBH/GBH or comparable trunk measurement;
- canopy diameter;
- measurement or calibration metadata.

## 2. Ecosystem-Service Analytics

The analytics module uses the tree inventory layer to estimate tree-level and aggregate ecosystem-service indicators.

Examples include:

- biomass-derived CO2 equivalent;
- localized cooling metrics based on satellite-derived land surface temperature;
- species-specific tree archetypes based on height, girth/DBH/GBH, and canopy diameter;
- planning-oriented simulation layers.

For cooling analysis, the tree inventory layer identifies the focal tree locations. NDVI is used to construct comparison masks, especially non-vegetated pixels inside the local buffer.

## 3. Street-Segment Aggregation

Tree attributes are spatially joined to nearby road segments. The chapter prototype uses a road-segment buffer to aggregate canopy, biomass-derived CO2 equivalent, and species richness.

These attributes are normalized and combined into route-relevant environmental scores:

- Static Environmental Quality (SEQ), used for vehicular or carbon-aware routing;
- Serenity Score, used for walking or recreational route suggestions.

## 4. Planning and Routing Outputs

The final layer converts environmental analytics into decision-support outputs:

- planning dashboards;
- planting or reforestation simulations;
- route comparison;
- environmental routing recommendations;
- recreational loop or turnaround suggestions.

## Why This Is A Framework

The modules are not independent applications placed side by side. They are connected by a common data model and a shared analytical sequence:

```text
tree inventory -> ecosystem-service analytics -> planning/routing intervention
```

This is the operational meaning of the chapter's closed feedback loop. Citizens and municipal data systems generate or maintain tree records; the analytics engine converts those records into environmental intelligence; and the resulting outputs return to planners, researchers, and citizens as usable decision support.
