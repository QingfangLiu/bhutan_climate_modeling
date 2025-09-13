# Modeling Folder

This folder contains two modeling approaches:

- **runoff_model/**  
  Early exploratory work that used ERA5 **surface runoff** as a proxy for floods.  
  Useful for reference, benchmarking, or quick prototypes.

- **riverine_flood_model/**  
  Main pipeline that models **river discharge** at basin level.  
  Contains a multi-stage workflow:
  - Stage A: Build grid-to-basin mapping  
  - Stage B: Align ERA5 data to basin-level time series  
  - Stage C: Build daily target variables (discharge)  
  - Stage D: Add static and dynamic predictors  
  - Stage E: Train ML models (e.g., XGB, RF, NN)  

