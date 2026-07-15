# Reproducibility Notes

## Scope

This repository provides reference implementations for the methodological logic described in the chapter. It is designed for transparency and review, not for direct production deployment.

The companion repositories contain fuller prototype applications, but they may require environment variables, external APIs, geospatial data, or deployment-specific configuration.

## Pune Case Study Data Flow

The Pune demonstration uses the municipal tree census as the baseline tree inventory layer. This inventory supplies tree locations and structural attributes for the downstream analytics.

The smartphone measurement module should be interpreted as a pathway for producing comparable inventory records in contexts where municipal inventories are absent, incomplete, or outdated. It is not presented as the source of the Pune case-study inventory.

## What Is Included

This repository includes:

- compact reference scripts for photogrammetry, environmental scoring, and route scoring;
- a module-to-repository map;
- documentation of the integrated data flow;
- citation metadata.

## What Is Not Included

This repository does not include:

- raw municipal datasets;
- private API keys or local `.env` files;
- large model weights;
- generated application builds;
- node or Python virtual environments;
- certified emissions factors or official forestry inventory tools.

## Key Assumptions

### Tree Inventory

Tree locations and attributes are assumed to be available through either municipal tree census records or a compatible citizen-measurement workflow.

### Cooling Metrics

The focal tree pixel is identified from the tree inventory layer. NDVI-derived masks are used to define local comparison pixels, especially non-vegetated background pixels, for percentile-based thermal metrics.

### Routing Scores

Road-segment scores are based on tree-derived canopy, biomass-derived CO2 equivalent, and species richness. These are proxies for environmental quality and do not exhaust all relevant route-experience variables. Direct shade, noise, sidewalk quality, slope, safety, and real-time thermal comfort are future extensions where validated layers are available.

## Limitations

- The complete citizen-measurement-to-updated-routing loop has not yet been validated as a continuous operational workflow with end users.
- The reference scripts are simplified and intended to communicate method logic.
- The case study is a proof-of-concept demonstration rather than a certified planning decision system.
- Users should inspect companion repositories for data dependencies and deployment assumptions before reuse.

## Recommended Archival Workflow

1. Clean each companion repository of secrets, generated artifacts, and local-only files.
2. Create a tagged release for each companion repository.
3. Create a tagged release for this umbrella repository.
4. Archive the releases on Zenodo.
5. Cite the umbrella repository for the integrated framework and module repositories for specific software components.
