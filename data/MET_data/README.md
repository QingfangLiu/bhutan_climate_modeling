# Meteorological (MET) Data

This folder contains meteorological data used in the project.

## Source
The data is provided by the local government.

## Contents
- `MET_data.xlsx` : Raw meteorological data file (as received).
- `processed_MET_data/` : Cleaned and processed outputs derived from the raw dataset.
  - `region_coordinates.csv` : Coordinates for each weather station/region.
  - `summary.csv` : Processed summary statistics of the meteorological data.
  - `*.pkl` files : Cleaned and serialized datasets for each region.

### Regions included (processed into `.pkl` files)
- Bhur
- Chamkhar
- Deothang
- Gasa
- Kanglung_Tashigang
- Mongar
- Nganglam
- Paro
- Phuentsholing
- Simtokha
- Tangmachu_Lhuentse
- Tashiyangtse
- Trongsa
- Zhemgang

## Notes
- The `.pkl` files contain cleaned versions of the meteorological time series data for each region.
- The raw Excel file should remain unchanged for provenance.
- Any additional cleaning or transformation steps should be documented here or in accompanying scripts.
