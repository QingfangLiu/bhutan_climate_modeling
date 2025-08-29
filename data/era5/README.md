# ERA5 Climate Data for Bhutan (1979–2025)

This folder contains ERA5 reanalysis data for Bhutan spanning **1979–2025**.  
The data has been processed in multiple stages for use in climate modeling and flood risk prediction.

---

## 📂 Folder Structure

- **`era5_data_grib_raw/`**  
  Raw ERA5 files in **`.grib`** format, downloaded from the [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/).  
  Each file corresponds to a specific **year** and **variable** over the Bhutan region.

- **`era5_data_excel/`**  
  ERA5 data converted from `.grib` to **Excel (.xlsx)** format.  
  - Data downsampled to **6-hour intervals** (to align with GraphCast predictions).  
  - Each Excel file contains one sheet per year.  
  - Grid points cover Bhutan (`lat: 26.5°N – 28.5°N`, `lon: 88.5°E – 92.0°E`).  
  - Temperature converted from **Kelvin → Celsius**.  
  - Timestamps rounded to the nearest 6-hour mark.

- **`era5_merged/`**  
  Final combined dataset stored as **Parquet** for efficient analysis.  
  - Produced using the notebook `merge_era5_1979_2025.ipynb`.  
  - The notebook:
    - Reads each Excel file and reshapes to long format (`latitude`, `longitude`, `datetime`).  
    - Converts time from **UTC → Asia/Thimphu** (Bhutan local time) while keeping a strict 6-hour cadence (00, 06, 12, 18).  
    - Merges all variables on (`latitude`, `longitude`, `datetime`).  
    - Saves the result as `merged_era5_6hour_1979_2025.parquet`.

---

## ⏱️ Time Resolution
- Original data: **Hourly**  
- Processed data: **6-hourly** (00:00, 06:00, 12:00, 18:00, Bhutan time)

---

## 📌 Variables Included
- `total_precipitation`
- `runoff`
- `surface_runoff`
- `sub_surface_runoff`
- `snowmelt`
- `snow_depth`
- `soil_temperature_level_1`
- `surface_solar_radiation_downwards`
- `2m_temperature` (in °C)
- `2m_dewpoint_temperature`
- `10m_u_component_of_wind`
- `10m_v_component_of_wind`
- `potential_evaporation`

---

## ⚙️ Processing Pipeline
1. **Download** ERA5 `.grib` files via CDS API.  
2. **Convert** `.grib` → `.xlsx` (6-hour, per variable & year).  
3. **Merge** Excel files across variables and years with `merge_era5_1979_2025.ipynb`.  
4. **Export** unified dataset to `.parquet`.

---

## 📤 Usage
- Use the `.grib` files if you need **raw ERA5 reanalysis**.  
- Use the `.xlsx` files for **variable-specific** analysis or inspection.  
- Use the `.parquet` file for **efficient large-scale modeling** in Python (e.g., with `pandas` or `pyarrow`).  

---

✍️ Maintainer: **Qingfang Liu**
