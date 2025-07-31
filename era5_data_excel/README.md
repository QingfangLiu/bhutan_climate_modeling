### 📊 6-Hour ERA5 Weather Data (1979–2025)

This folder contains downsampled ERA5 weather variable data in Excel format. Each file corresponds to one variable and is saved in wide-format, with separate files for **1979–1999** and **2000–2025** to reduce file size and ease access. **All timestamps are in UTC time zone, not adjusted to Bhutan time.**

#### ✅ Key Details

- **⏱️ Time Resolution**:  
  Data is downsampled to **6-hour intervals** to match [GraphCast](https://github.com/google-deepmind/graphcast) prediction frequency.

- **📁 Format**:  
  Each Excel file contains **one sheet per year**, structured as:  
  - **Rows**: `(latitude, longitude)` grid points  
  - **Columns**: Timestamps at 6-hour steps

- **🗺️ Spatial Coverage**:  
  Grid points are limited to the **Bhutan region**, with bounding box:  
  `lat: 26.5°N to 28.5°N`, `lon: 88.5°E to 92.0°E`

- **📌 Variables Included**:
  - `total_precipitation`
  - `runoff`
  - `surface_runoff`
  - `sub_surface_runoff`
  - `snowmelt`
  - `snow_depth`
  - `soil_temperature_level_1`
  - `surface_solar_radiation_downwards`
  - `2m_temperature`
  - `2m_dewpoint_temperature`
  - `10m_u_component_of_wind`
  - `10m_v_component_of_wind`

- **📤 Source**:  
  Data was extracted from **ERA5 `.grib` files** and processed via an automated Python pipeline.  
  - **Temperature variables** (`2m_temperature`) were converted from **Kelvin to Celsius**.  
  - **All timestamps were rounded to the nearest 6-hour mark** (e.g., 01:00 → 00:00, 07:00 → 06:00) to ensure alignment across variables.  
  - Data was then saved in wide-format Excel files for easy access in modeling and visualization.
