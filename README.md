
# 🌏 Bhutan Climate Modeling

This repository is part of [Omdena's local chapter challenge](https://www.omdena.com/chapter-challenges/leveraging-ai-to-combat-climate-change-in-bhutan), focused on leveraging AI to combat climate change in Bhutan.

## 👥 Collaborators

Special thanks to the following team members for their collaboration:

- **Qingfang Liu** – Lead end-to-end modeling workflow, data pipeline, model development and evaluation, and presentation  
- **Tuhin Das** — Led prototype development; contributed to data analysis, EDA, and overall modeling workflow 
- **Marlon Marín** — Assisted with data download  
- [Name 1] – Role or main contribution  


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


At the midpoint of the project, as new members joined, I presented the core ML modeling framework and current progress to guide team alignment:

- [docs/Bhutan_flood_risk_prediction_system_using_ML.pdf](docs/Bhutan_flood_risk_prediction_system_using_ML.pdf)  
  - Introduced the ML modeling workflow and explained the use of surface runoff as a proxy for flood risk  
  - Walked through how the models were developed, including data preparation, EDA, and feature engineering  
  - Showcased completed models: Random Forest, XGBoost, and Linear Regression → RF performed best  
  - Proposed next steps and modeling priorities to align efforts and support collaboration across the team


## 💡Project Roadmap

### 1. Data Collection
**Goal:** Fetch and organize relevant data from multiple sources  

#### ERA5 Hourly Reanalysis (Main Source)

[ERA5 Single Levels - Copernicus Climate Data Store](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)

- **Variables:**  
  - `Total_precipitation`  
  - `2m_temperature`  
  - `2m_dewpoint_temperature`  
  - `10m_u_component_of_wind`  
  - `10m_v_component_of_wind`  
  - `surface_solar_radiation_downwards`  
  - `potential_evaporation`  
  - `snow_depth`  
  - `Snowmelt`  
  - `Soil temperature level 1`  
  - `Relative_humidity`
- **Region:** Bhutan bounding box
- **Temporal range:** 1979 to latest year
- **Tools:** `cdsapi`, structured folder organization (by variable/year)

####  Other Explored Data Sources
- Local MET data (RH, Tmax, Tmin, Rainfall)
- GLOF/flood event history 
- River discharge or lake level data (if available)
- DEM/topographic data (elevation, slope)
- Land cover and infrastructure exposure


---

### 2. Data Preprocessing & Daily Aggregation
**Goal:** Convert hourly data into daily metrics  

- **Daily aggregations:**
  - Sum: `Total_precipitation`, `Snowmelt`
  - Mean: `2m_temperature`, `2m_dewpoint_temperature`, `RH`
  - Max/min: computed for `Tmax`/`Tmin` from hourly temps
- Use `xarray`/`pandas` to resample

---

### 3. ML / DL Modeling (Ongoing)
**Goal:** Predict flood or extreme rainfall risk  

#### 🧩 Feature Engineering
- Lagged variables (1, 3, 7, 14, 30 days)
- Rolling stats (3, 7, 14, 30 days)
- Temporal features: `dayofyear`, monsoon flag
- (Optional) Spatial features: elevation, river and lake metrics 

#### 🧠 Model Development
- Binary classification (e.g., extreme rainfall event)  
- Regression (e.g., total daily rainfall)
- **Algorithms:**
  - ML: XGBoost, RandomForest, Logistic Regression
  - DL: CNN-LSTM, Transformers
  - (Optional): GNN for spatiotemporal modeling across regions

#### ✅ Evaluation
- Train/test split by time
- Metrics:
  - Classification: Accuracy, F1-score, Confusion Matrix
  - Regression: RMSE, MAE
- Cross-validation or time series split
- Visualizations: prediction vs actual plots

---

### 4. Deployment (Next step)
**Goal:** Build a usable predictive tool  

- Options:
  - Backend: Flask / FastAPI
  - Frontend: Streamlit / Gradio interface
  - Daily scheduled inference
- Stretch goals:
  - Interactive dashboard (Plotly, Dash)
  - Risk alerts for high-probability days

---

## 📁 Repository Structure

- `code/` – Python scripts and notebooks for data downloading, processing and analysis  
- `data/` – Mixed meteorological datasets, including raw and auxiliary data sources  
- `docs/` – Flood prediction ML workflow documentation  
- `era5_data_excel/` – ERA5 climate variables downsampled to 6-hour intervals and saved in Excel format  
- `era5_data_grib_raw/` – Raw ERA5 climate data in GRIB format, organized by variable and year  
- `processed_MET_data/` – Cleaned and standardized meteorological data from each weather station
- `world_boundaries_for_bhutan_map/` – Shapefiles and boundary data used for Bhutan mapping  
- `README.md` – Project overview and usage instructions  
- `.gitignore` – Specifies intentionally untracked files to ignore


