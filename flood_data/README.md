# Bhutan Flood Dataset Cleaning Summary

**Finalized:** 2025-07-30

This document summarizes the steps taken to process and clean the flood dataset compiled from multiple sources related to historical and recent flood events in Bhutan.

---

## 🧭 Data Sources and Aggregation
- Combined information from:
  - `Major_Flash_Flood_Events_Bhutan_CLEANED.csv`
  - `Extreme_Events_2016_2025_updated.xlsx` (multiple tabs)
  - `Compendium of Extreme Events vol2.pdf`
- Merged all records into one unified dataset, aligning column structure and content.

---

## 🧹 Cleaning and Filtering
- Removed records with:
  - Missing or vague dates (e.g. only year-level entries)
  - No spatial detail or vague regional mentions
  - No mention of "flood" in event type
  - Pre-1979 entries
- Cleaned up inconsistent date formats, converting to `YYYY-MM-DD`
- Dropped empty or redundant columns like:
  - `EventID`, `Hospitals`, `Education_Centers`, `Num_Events`, `Houses_Damaged`

---

## 🗺️ Geocoding and Location
- Filled in missing `Latitude` and `Longitude` using:
  - District and location names
  - External geographic lookup (online + internal reference)
- Split entries listing multiple districts into individual rows for accurate mapping
- Retained both `District` and `Location` columns for detail

---

## 🔁 De-duplication
- Identified and dropped duplicate entries where both `Date` and coordinates matched
- Retained only one instance for each identical event

---

## 📑 Column Refinement
- Reordered columns to prioritize key metadata:
  - `Date`, `District`, `Location`, `Latitude`, `Longitude`, `Flood_Type`
- Merged `Description` and `Comments` into a single field
- Labeled `Source` with numeric codes (1, 2, 3…) and documented them

---

## 📆 Final Output
- Total events: **113 unique flood records**
- Date range: **1979–2025**

---

This dataset provides a curated, structured foundation for flood risk analysis, event frequency modeling, and disaster preparedness work in Bhutan.

