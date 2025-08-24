# 🌏 Bhutan Climate Modeling

This repository is part of two Omdena initiatives: the [Local Chapter Challenge](https://www.omdena.com/chapter-challenges/leveraging-ai-to-combat-climate-change-in-bhutan) and the [AI Innovation Project: Building ClimateSense AI](https://www.omdena.com/projects/building-climatesense-ai-climate-change-bhutan), both focused on leveraging AI to combat climate change in Bhutan.

Maintained by **Qingfang Liu**  

## 👥 Collaborators

Special thanks to the following team members for their collaboration:

- **Qingfang Liu** – Led end-to-end modeling workflow, including data pipeline, model development, evaluation, and presentation  
- **Tuhin Das** — Led prototype development; contributed to data analysis, EDA, and overall modeling workflow 
- **Pankaja Shankar** - Co-led prototype development; contributed to data preparation and analysis
- **Marlon Marín** — Assisted with data download
- [Name] – Role or main contribution  

> 📝 *If you're a team member and would like your contribution added or updated, feel free to open a PR or issue!*

## ✅ Project Goals

- Understand historical meteorological trends and seasonal/regional patterns  
- Build and validate predictive models to forecast floods and extreme weather events such as glacial lake outburst floods (GLOFs)  
- Support downstream applications like risk maps and early-warning systems

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
**Goal:** Fetch and organize relevant data from multiple sources  

#### ERA5 Hourly Reanalysis (Main Source)

[ERA5 Single Levels - Copernicus Climate Data Store](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)

- **Variables:**  
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
- **Region:** Bhutan bounding box (`lat: 26.5°N to 28.5°N`, `lon: 88.5°E to 92.0°E`)
- **Temporal range:** 1979 to latest date
- **Tools:** `cdsapi`, structured folder organization (by variable/year)

#### Flood Historical Records

We also compiled flood event data from multiple public sources. With the help of ChatGPT agent, significant effort was made to manually review, deduplicate, and clean these records, resulting in a unified dataset of major flood events in Bhutan from 1979 to 2025.


####  Other Explored Data Sources
- Local meteorological data from weather stations (RH, Tmax, Tmin, Rainfall)
- GLOF event history 


####  Data Sources to explore
- River discharge or lake level data
- Earthquake data
- DEM/topographic data (elevation, slope)
- Land cover and infrastructure exposure


---

### 2. Exploratory Data Analysis (EDA) (Ongoing) 

**Goal:** Understand patterns, distributions, and anomalies in the processed climate and flood datasets

**Key Tasks:**
- Visualize temporal trends (e.g., rainfall, runoff, temperature) across years and seasons
- Compare variable distributions between flood and non-flood days
- Perform correlation analysis between climate variables and flood occurrences
- Identify extreme events using statistical thresholds



---

### 3. ML / DL Modeling (Ongoing)
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

### 4. Forecast Data from ECMWF and GraphCast (Completed) 

**Goal:** Leverage existing weather forecast systems and products to  
1. Provide deployable, regionalized forecast products for Bhutan.  
2. Use these forecasts as input features for flood risk prediction.  

- **GraphCast (by DeepMind):** Provides 10-day, 6-hourly forecasts at 0.25° resolution. It is a state-of-the-art GNN-based global weather forecasting model trained on ERA5 reanalysis data. See the [GraphCast paper (Nature, 2023)](https://www.science.org/stoken/author-tokens/ST-1550/full) for details.  
- **GraphCast Global Forecast System (GraphCastGFS):** An experimental system set up by the National Centers for Environmental Prediction (NCEP) to produce medium-range global forecasts using GraphCast outputs. The dataset is openly available via the [NOAA AWS Registry](https://registry.opendata.aws/noaa-nws-graphcastgfs-pds/).  
- **ECMWF (European Centre for Medium-Range Weather Forecasts):** An independent intergovernmental organization that provides some of the most accurate global medium-range weather forecasts, including the ERA5 reanalysis dataset and high-resolution ensemble forecasts widely used in climate and hydrology research. More information is available on the [ECMWF forecasts portal](https://www.ecmwf.int/en/forecasts).  

---

### 5. Spatial Alignment (Ongoing)  

**Goal:** Align data from multiple sources across different spatial dimensions.  

Examples of spatial dimensions include:  
- **ERA5 historical meteorological data** and **weather forecasts** (both on gridded levels)  
- **Geospatial and hydrological data** (organized at watershed and basin levels)  
- **Early warning systems** (which need to operate at administrative levels)  

We leveraged a variety of shapefiles, mostly from the [Bhutan NSDI portal](https://nsdi.systems.gov.bt/data/Boundaries), and applied spatial interpolation and aggregation methods to align these spatial units. These aligned datasets are then used as inputs in ML and DL models.  


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

## 📁 Repository Structure

```
.
├─ code/                         # Python scripts & notebooks for downloading, cleaning, features, modeling
├─ deploy/                       # Docker/K8s/Prefect/Terraform configs for running in dev/prod
├─ docs/                         # Project documentation, diagrams, and notes
├─ data/                         # All datasets organized by WHAT they are (each has raw/processed/README)
│  ├─ basin_discharge/           # Basin discharge data (from local government)
│  │  └─ README.md
│  ├─ boundaries/                # All boundary layers
│  │  ├─ basins/
│  │  ├─ 186_watershed/
│  │  └─ world_boundaries_for_bhutan_map/
│  ├─ era5/                      # ERA5 climate data
│  │  ├─ era5_data_excel/
│  │  ├─ era5_data_grib_raw/     
│  │  └─ era5_merged
│  ├─ flood_data/                # Cleaned and merged historical flood records for Bhutan (1979–2025), with source tracking and standardized formatting
│  │  └─ README.md
│  ├─ glof_data/                 # GLOF-related datasets
│  ├─ HydroSHEDS/                # HydroSHEDS products
│  └─ MET_data/                  # Meteorological station data (local government)
│     ├─ raw/
│     ├─ processed_MET_data/     # cleaned outputs: region PKLs, summary.csv, region_coordinates.csv
│     └─ README.md
```
