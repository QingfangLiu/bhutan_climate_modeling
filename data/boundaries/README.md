# Boundaries Data

This folder contains boundary datasets used in the project. These boundaries define
administrative areas, basins, and watersheds relevant to the study region.

## Source
- Provided by local government and publicly available geospatial data sources.

## Structure
- `186_watershed/` : Watershed boundary dataset (186 delineations).
- `basins/` : Major basin boundary dataset.
- `world_boundaries_for_bhutan_map/` : Administrative boundaries for Bhutan.

### Processed

The `processed/` directory contains derived datasets at basin and watershed levels. 

- **From HydroSHEDS DEM (summary stats, CSV):**
  - `basin_dem_acc_stats.csv`
  - `watershed_dem_acc_stats.csv`

- **From shapefiles (CSV exports of geometry statistics):**
  - `basin_shape_stats.csv`
  - `watershed_shape_stats.csv`

- **River discharge features:**
  - `basin_discharge_features.csv` — includes information related to river discharge data.


## Notes
- Original (raw) datasets should not be modified.
- Any cleaning, reprojection, or consolidation should be saved in a `processed/` subfolder inside each dataset folder.

