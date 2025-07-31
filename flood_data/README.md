# Bhutan Flood Dataset Cleaning Summary

**Finalized:** 2025-07-30  
**Author:** Qingfang Liu

This document summarizes the steps taken to process and clean the flood dataset compiled from multiple sources related to historical and recent flood events in Bhutan.

---

## 🧭 Data Sources and Aggregation

Combined information from:

| Code | Original Source                             |
|------|---------------------------------------------|
| 1    | Major_Flash_Flood_Events_Bhutan_CLEANED     |
| 2    | Tuhin_Flood_Data_1                          |
| 3    | Qingfang_Flood_Data_1                       |
| 4    | Compendium_extreme_events_vol2              |

All records were merged into one unified dataset, aligning column structures and content.

---

## 🧹 Cleaning and Filtering

- Removed records with:
  - Missing or vague dates (e.g., only year-level entries)
  - No spatial detail or vague regional mentions
  - No mention of "flood" in event type
  - Pre-1979 entries
- Standardized all date formats to `YYYY-MM-DD`
- Dropped empty or redundant columns:
  - `EventID`, `Hospitals`, `Education_Centers`, `Num_Events`, `Houses_Damaged`

---

## 🗺️ Geocoding and Location

- Filled missing `Latitude` and `Longitude` using:
  - District and location names
  - Online geographic lookup
- For records listing multiple districts:
  - Split into individual rows
  - Assigned coordinates accordingly
- Retained both `District` and `Location` columns

---

## 🔁 De-duplication

- Identified and removed duplicate entries based on `Date` + coordinates
- Retained only one record per unique event

---

## 📑 Column Refinement

- Kept only key columns:
  - From `Date` to `Source`, plus `Gewog` and `River_Basin`
- Reordered columns to prioritize:
  - `Date`, `District`, `Location`, `Latitude`, `Longitude`, `Flood_Type`
- Merged `Description` and `Comments`
- Re-labeled `Source` as numeric codes (1–4), explained above

---

## 📆 Final Output

- Total events: **113 unique flood records**
- Date range: **1979–2025**

---

This curated dataset supports flood modeling, climate resilience planning, and emergency preparedness analysis in Bhutan.
