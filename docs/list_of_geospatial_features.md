# Geospatial Features for Flood Modeling in Bhutan

This document summarizes the geospatial features relevant for flood modeling (flash floods, riverine floods, and GLOFs), 
based on DEM-derived analysis and external datasets.

---

## 🌄 DEM-derived Features (from HydroSHEDS DEM and terrain processing)

- Elevation  
- Slope  
- Curvature indices  
- Valley depth  
- Flow accumulation (ACC)  
- Height Above Nearest Drainage (HAND)  
- Topographic Wetness Index (TWI) *(= slope + ACC)*  
- Stream Power Index (SPI) *(= slope + ACC)*  
- Terrain position / relative topographic indices  

---

## 🌊 Hydrography / Water Proximity (DEM + hydrography)

- Distance to rivers/streams  
- River/stream density  
- Distance to coast *(irrelevant for Bhutan, landlocked)*  

---

## 🟩 Land Surface & Environmental Features (external datasets)

- Land use / Land cover (LULC)  
- Impervious surface fraction (built-up areas)  
- Vegetation cover / NDVI  
- Soil type  
- Lithology (geological formations)  
- Land surface roughness (e.g. Manning’s coefficient)  
- Saturated hydraulic conductivity  

---

## 🚧 Human / Infrastructure Context

- Road segments (for road flood risk modeling)  
- Administrative boundaries / census tracts  

---

# 📌 Priority External Datasets for Bhutan

To complement the DEM-derived features, the following non-DEM datasets are most valuable for Bhutan flood modeling:

### 🌍 Top Priority
1. **Land Use / Land Cover (LULC)**  
   - Distinguishes urban/impervious vs. forested vs. agricultural areas.  
   - Crucial for flash flood susceptibility and runoff estimation.  
   - Source: ESA WorldCover (10 m), Copernicus, Landsat.  

2. **Soil type & hydraulic properties**  
   - Controls infiltration/retention, key for flash and riverine floods.  
   - Source: SoilGrids (250 m global), FAO HWSD.  

3. **Lithology / geology**  
   - Important for slope stability, landslide-induced floods, and GLOF modeling.  
   - Source: Global Lithological Map (GLiM), regional geological surveys.  

### ⚡ Secondary Priority
4. **Impervious surface fraction**  
   - Refines urban flood modeling, complements LULC.  
   - Especially relevant in urban centers (Thimphu, Phuentsholing).  
   - Source: Global Human Settlement Layer (GHSL), OSM.  

---

# ✅ Summary

- **DEM-derived features**: already achievable with HydroSHEDS + your watershed pipeline.  
- **Hydrography**: distance to rivers, river density — feasible with your current flow accumulation and river network.  
- **External features**: prioritize LULC, soils, and lithology; add imperviousness later for urban detail.  

Together, these form the core geospatial feature set for building flash flood, riverine flood, and GLOF models in Bhutan.

