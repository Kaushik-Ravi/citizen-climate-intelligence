# Zenodo Release Workflow

This repository is intended to be the DOI-bearing reproducibility entry point for the chapter. The companion application repositories are linked from this repository but are not vendored into it.

## Recommended Scope

Archive the umbrella repository first:

`Kaushik-Ravi/citizen-climate-intelligence`

This record should represent the integrated framework and point to the companion repositories:

- `tree-measurement-frontend`
- `pune-tree-dashboard-sample`
- `Eco-Path`

The companion repositories can receive their own Zenodo records later if they are cleaned, versioned, and ready to be cited as standalone software components.

## Before Creating A Release

1. Confirm the repository contains no secrets, `.env` files, local datasets, model weights, or generated builds.
2. Add or confirm a license. Recommended options:
   - MIT License for permissive research software reuse.
   - Apache-2.0 if patent language is desired.
   - CC-BY-4.0 only for documentation/data, not software code.
3. Confirm `CITATION.cff` is present at the repository root.
4. Confirm `README.md`, `MODULES.md`, and `REPRODUCIBILITY.md` accurately describe the limits of the release.
5. Do not add `.zenodo.json` unless Zenodo-specific metadata are required. If both `.zenodo.json` and `CITATION.cff` are present, Zenodo uses `.zenodo.json` and ignores `CITATION.cff` for GitHub release archiving.

## GitHub Release Steps

After the documentation is committed and pushed:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Then create a GitHub release from the tag:

- Title: `Citizen Centered Climate Intelligence v0.1.0`
- Release notes:

```text
Initial public reproducibility release for the chapter "Citizen Centered Climate Intelligence: Operationalizing Open Tree Data for Urban Cooling and Eco-Routing in Indian Cities".

This release provides the umbrella framework documentation, reference scripts, module mapping, and reproducibility notes. Companion application repositories are linked but not vendored into this repository.
```

## Zenodo Steps

1. Log in to Zenodo.
2. Connect GitHub to Zenodo if it is not already connected.
3. In the Zenodo GitHub integration page, enable `Kaushik-Ravi/citizen-climate-intelligence`.
4. Create or re-process the GitHub release.
5. Wait for Zenodo to archive the release.
6. Open the Zenodo record and copy:
   - version DOI for the exact release;
   - concept DOI for the software project across versions.

Use the **version DOI** in the chapter if the chapter refers to a fixed archived state. Use the **concept DOI** if you want the citation to point to the evolving software project.

## Suggested Chapter Wording

Use a short transparency sentence in the Methodology or Data/Code Availability section:

> The reference implementation and module-level repository map for the framework are archived on Zenodo and available through the project repository (Ravi & Brück, 2026).

After Zenodo mints the DOI, cite the software record in the references:

```text
Ravi, K., & Brück, A. (2026). Citizen Centered Climate Intelligence (Version 0.1.0) [Computer software]. Zenodo. https://doi.org/[insert Zenodo DOI]
```

If the publication style prefers repository access rather than software citation:

```text
The source-code skeleton and companion repository map are available in the archived project repository: https://doi.org/[insert Zenodo DOI].
```

## Companion Repository Citation

Only cite the companion repositories separately if a specific result, interface, or deployed app depends directly on that repository. Otherwise, cite the umbrella Zenodo record and use `MODULES.md` to point readers to the module implementations.
