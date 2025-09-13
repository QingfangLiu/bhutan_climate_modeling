# 🌏 Bhutan Climate Modeling

This repository is part of two Omdena initiatives: the [Local Chapter Challenge](https://www.omdena.com/chapter-challenges/leveraging-ai-to-combat-climate-change-in-bhutan) and the [AI Innovation Project: Building ClimateSense AI](https://www.omdena.com/projects/building-climatesense-ai-climate-change-bhutan), both focused on leveraging AI to combat climate change in Bhutan.

Maintained by **Qingfang Liu**  

## 👥 Collaborators

Special thanks to the following team members for their collaboration:

- **Qingfang Liu** – Led end-to-end modeling workflow, including data pipeline, model development, evaluation, and presentation  
- **Tuhin Das** — Led prototype development; contributed to data analysis, EDA, and overall modeling workflow 
- **Pankaja Shankar** - Co-led prototype development; contributed to data preparation and analysis
- **Pavlo Kuts** - Led HydroSHEDS database download and analysis
- **Marlon Marín** — Assisted with data download
- [Name] – Role or main contribution  

> 📝 *If you're a team member and would like your contribution added or updated, feel free to open a PR or issue!*


## ✅ Project Goals  

1. **Advance scientific understanding of Bhutan’s climate and flood risks**  
   Analyze historical and projected meteorological and hydrological patterns to identify seasonal, regional, and long-term trends.  

2. **Develop reliable predictive and early warning systems**  
   Build and validate models to forecast riverine floods, flash floods, and glacial lake outburst floods (GLOFs) under current and future climate scenarios.  

3. **Strengthen decision-making and community resilience**  
   Design user-centered tools, dashboards, and communication strategies to support policymakers, disaster managers, and local communities.  


## 📄 Project Documentation

I created this workflow and presented it to the team to support understanding and communication:

- [docs/bhutan_flood_model_workflow.pdf](docs/bhutan_flood_model_workflow.pdf)  
  - Visual overview of the Bhutan flood risk prediction workflow  
  - Shows how ERA5 historical data and GraphCast forecasts are used to train and deploy an ML model  
  - Includes Q&A-style notes on model training, feature selection, proxy labels, and GraphCast usage  
  - Helps both technical and non-technical stakeholders understand the modeling strategy

📘 Looking for modeling FAQs? See [docs/README.md](docs/README.md) for answers to common questions about the ML approach, data, and forecast design.

At the project midpoint, I introduced new members to the core ML framework and progress to align the team:

- [docs/Bhutan_flood_risk_prediction_system_using_ML.pdf](docs/Bhutan_flood_risk_prediction_system_using_ML.pdf)  
  - Introduced the ML modeling workflow and explained the use of surface runoff as a proxy for flood risk  
  - Walked through how the models were developed, including data preparation, EDA, and feature engineering  
  - Showcased completed models: Random Forest, XGBoost, and Linear Regression → RF performed best  
  - Proposed next steps and modeling priorities to align efforts and support collaboration across the team

Later, I prepared and presented this mid-term report to Bhutan local climatologists to gather expert guidance and ensure our work benefits the community.

- [docs/Bhutan_flood_midterm_report_for_expert_consultation.pdf](docs/Bhutan_flood_midterm_report_for_expert_consultation.pdf)
  - Presented mid-term progress report to Bhutan local climatologists for domain expert guidance  
  - Explained current two lines of work and their status  
  - Summarized data sources used for weather forecasting  
  - Detailed ML workflow and predictive features under development  
  - Described three types of floods targeted and their spatial prediction levels  
  - Prepared and led Q&A discussions to gather expert feedback


## 💡Project Roadmap

### 1. Data Collection
**Goal:** Collect and organize relevant data from multiple sources, including meteorological, hydrological, and other geospatial features. We reviewed existing machine learning research to identify the features most critical for flood forecasting and gathered high-quality datasets from reliable sources specific to Bhutan.

#### Meteorological Data  
- **Primary Source:** ERA5 Hourly Reanalysis  
  - [ERA5 Single Levels - Copernicus Climate Data Store](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)  
- **Extracted Variables:**  
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

- **Region:** Bhutan bounding box (`lat: 26.5°N – 28.5°N`, `lon: 88.5°E – 92.0°E`)  
- **Temporal Coverage:** 1979 – present  
- **Additional Data:** Local meteorological station observations (RH, Tmax, Tmin, Rainfall) are available but not directly used in the modeling process.  


#### Hydrological Data  
- **Source:** [HydroSHEDS](https://www.hydrosheds.org/)  

**Extracted Variables:**  
- **DEM (Digital Elevation Model):** Represents elevation data, used to capture terrain shape and slope.  
- **ACC (Flow Accumulation):** Indicates the number of upstream cells draining into a given point, useful for identifying river networks.  

**Summary Statistics (per basin/watershed):**  
- `dem_min`, `dem_max`, `dem_mean`, `dem_std`, `dem_median`  
- `acc_min`, `acc_max`, `acc_mean`, `acc_std`, `acc_median`  

**Engineered Variables:**  
- **Relief:** Difference between maximum and minimum elevation within a basin, representing terrain ruggedness.  
- **elev_range_iqr_proxy:** Interquartile range of elevation values, used as a proxy for elevation variability.  
- **flow_density_proxy:** Ratio of accumulated flow paths to the total area, reflecting stream network density.  

**Purpose:** These engineered features were derived to better capture terrain and flow dynamics that may be more closely related to flood occurrence.  


#### Flood Historical Records

We also compiled flood event data from multiple public sources. With the help of ChatGPT agent, significant effort was made to manually review, deduplicate, and clean these records, resulting in a unified dataset of major flood events in Bhutan from 1979 to 2025.


####  Other Explored Data Sources

- GLOF event history 
- River discharge data

####  Data Sources to explore

- Earthquake data
- Other geospatial features: land cover, infrastructure exposure, imperviousness, etc


---

### 2. Exploratory Data Analysis (EDA) (Completed) 

**Goal:** Understand patterns, distributions, and anomalies in the processed climate and flood datasets

**Key Tasks:**
- Visualize temporal trends (e.g., rainfall, runoff, temperature) across years and seasons
- Compare variable distributions between flood and non-flood days
- Perform correlation analysis between climate variables and flood occurrences
- Identify extreme events using statistical thresholds


---

### 3. Forecast Data from ECMWF and GraphCast (Completed) 

**Goal:** Leverage existing weather forecast systems and products to  
1. Provide deployable, regionalized forecast products for Bhutan.  
2. Use these forecasts as input features for flood risk prediction.  

- **GraphCast (by DeepMind):** Provides 10-day, 6-hourly forecasts at 0.25° resolution. It is a state-of-the-art GNN-based global weather forecasting model trained on ERA5 reanalysis data. See the [GraphCast paper (Nature, 2023)](https://www.science.org/stoken/author-tokens/ST-1550/full) for details.  
- **GraphCast Global Forecast System (GraphCastGFS):** An experimental system set up by the National Centers for Environmental Prediction (NCEP) to produce medium-range global forecasts using GraphCast outputs. The dataset is openly available via the [NOAA AWS Registry](https://registry.opendata.aws/noaa-nws-graphcastgfs-pds/).  
- **ECMWF (European Centre for Medium-Range Weather Forecasts):** An independent intergovernmental organization that provides some of the most accurate global medium-range weather forecasts, including the ERA5 reanalysis dataset and high-resolution ensemble forecasts widely used in climate and hydrology research. More information is available on the [ECMWF forecasts portal](https://www.ecmwf.int/en/forecasts).  

---

### 4. Spatial Alignment (Completed)  

**Goal:** Align data from multiple sources across different spatial dimensions.  

Examples of spatial dimensions include:  
- **ERA5 historical meteorological data** and **weather forecasts** (both on gridded levels)  
- **Geospatial and hydrological data** (organized at watershed and basin levels)  
- **Early warning systems** (which need to operate at administrative levels)  

We leveraged a variety of shapefiles, mostly from the [Bhutan NSDI portal](https://nsdi.systems.gov.bt/data/Boundaries), and applied spatial interpolation and aggregation methods to align these spatial units. These aligned datasets are then used as inputs in ML and DL models.  



---

### 5. ML / DL Modeling (Ongoing)

**Goal:** Predict flood or extreme rainfall risk  

#### Feature Engineering
- Lagged variables (1, 3, 7, 14, 30 days)
- Rolling stats (3, 7, 14, 30 days)
- Temporal features: `dayofyear`, monsoon flag
- Spatial features: elevation, river and lake metrics 

#### Model Development
- Binary classification (e.g., extreme rainfall event)  
- Regression (e.g., total daily rainfall)
- **Algorithms:**
  - ML: XGBoost, RandomForest, Logistic Regression
  - DL: CNN-LSTM, Transformers

#### Evaluation
- Train/test split by time
- Metrics:
  - Classification: Accuracy, F1-score, Confusion Matrix
  - Regression: RMSE, MAE
- Cross-validation or time series split
- Visualizations: prediction vs actual plots

---



### 6. Deployment (Ongoing)
**Goal:** Build a usable predictive tool  

- Options:
  - Backend: Flask / FastAPI
  - Frontend: Streamlit
  - Daily scheduled inference
- Stretch goals:
  - Interactive dashboard (Plotly, Dash)
  - Risk alerts for high-probability days

---

## 📦 Hugging Face Dataset  

To make datasets easier to access and share, selected processed data are hosted on Hugging Face:  

**Dataset:** [qlk0610/bhutan-climate](https://huggingface.co/datasets/qlk0610/bhutan-climate)  

**Contents:**  
- `HydroSHEDS/` – Elevation (DEM) and flow accumulation (ACC) layers for Bhutan  
- `era5/` – ERA5 reanalysis data (subset and aligned extracts for Bhutan)  
- `README.md` – Dataset documentation  

**Notes:**  
- Full ERA5 and HydroSHEDS are too large to store on GitHub, so this Hugging Face dataset provides a lightweight mirror.  
- Use it to quickly download subsets for experimentation or teaching.    

**Example (Python):**  

```python
from datasets import load_dataset

# Load dataset metadata
ds = load_dataset("qlk0610/bhutan-climate")

# Explore contents
print(ds)
```

---


## 📁 Repository Structure

```
.
├─ code/                         # Python scripts & notebooks for downloading, cleaning, features, modeling
├─ deploy/                       # Docker/K8s/Prefect/Terraform configs for running in dev/prod
├─ docs/                         # Project documentation, diagrams, and notes
├─ data/                         # All datasets organized by WHAT they are
```

The repository is organized into three main pillars: **data**, **code**, and **deploy**.  

- The **`data/`** directory holds all datasets, arranged by *what they are*.  
  - Each dataset folder includes a `README.md` with source and schema details.  
  - Standard subfolders are `raw/` (untouched inputs) and `processed/` (cleaned or derived outputs).  
  - Large or local-only datasets are clearly marked.  

- The **`code/`** directory contains all scripts, notebooks, and modules, arranged by *what they do*.  
  - Each folder aligns with a dataset or analysis task, so it’s easy to trace inputs → transformations → models.  

- The **`deploy/`** directory is for infrastructure, containerization, and workflow automation.  
  - This part of the repository is **ongoing** and will be updated as deployment workflows mature.  

👉 **Rule of thumb:** look under `data/` to find the data itself, under `code/` to see how that data is used, and under `deploy/` for how analyses and models are run in production.  


```
data/
├─ basin_discharge/          # Basin discharge data (from local government)
│  └─ README.md
├─ boundaries/               # All boundary layers
│  ├─ basins/
│  ├─ 186_watershed/
│  ├─ world_boundaries_for_bhutan_map/
│  └─ README.md
├─ era5/                     # ERA5 climate data, local only due to size limit
│  ├─ era5_data_excel/
│  ├─ era5_data_grib_raw/
│  └─ era5_merged/           
├─ flood_data/               # Cleaned and merged historical flood records for Bhutan (1979–2025)
│  └─ README.md
├─ glof_data/                # GLOF-related datasets
├─ HydroSHEDS/               # HydroSHEDS products, local only due to size limit
├─ MET_data/                 # Meteorological station data (from local government)
│  ├─ raw/
│  ├─ processed_MET_data/    # cleaned outputs: region PKLs, summary.csv, region_coordinates.csv
│  └─ README.md
```

```
code/
├─ basin_discharge/              # basin shapefile inspection & conjunction with river discharge (to confirm)
├─ hydrosheds_stats/             # Derive stats like dem & acc from hydrosheds data on basin and watershed levels (to confirm)
├─ discharge/                    # analysis on river discharge data of each station (ongoing)
├─ earthquake/                   # Earthquake-related scripts (ongoing)
├─ ecmwf/                        # ECMWF forecast data handling (download, processing) (completed)
├─ era5_download/                # Scripts for downloading ERA5 reanalysis data (completed)
├─ era5_processing/              # Cleaning/transforming ERA5 into usable formats (completed)
├─ flood_analysis/               # Flood-related analytics (ongoing)
├─ geospatial/                   # Follow-up analysis on multiple geospatial features to prepare for ML modeling (ongoing)
├─ glof_data/                    # GLOF data inspection & analysis (completed)
├─ graphcast/                    # GraphCast forecast data handling (download, processing) (completed)
├─ met_data/                     # Meteorological station data inspection & light EDA (completed)
├─ modeling/                     # Machine learning / statistical models for prediction (ongoing)
└─ watershed/                    # Watershed shapefile inspection (to confirm)
```

