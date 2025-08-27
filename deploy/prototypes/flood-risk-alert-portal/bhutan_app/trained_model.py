import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

data_path = 'data/bhutan_runoff_hourly_data.csv'
df = pd.read_csv(data_path)
df['DateTime'] = pd.to_datetime(df['DateTime'], dayfirst=True, errors='coerce')
df['Year'] = df['DateTime'].dt.year
df['Month'] = df['DateTime'].dt.month
df['Day'] = df['DateTime'].dt.day
df['Hour'] = df['DateTime'].dt.hour

# Required columns
required_cols = {'City', 'Temperature', 'Precipitation', 'Surface_Runoff', 'DateTime'}
if not required_cols.issubset(df.columns):
    raise ValueError(f"Missing required columns: {required_cols - set(df.columns)}")

# Create output directory
os.makedirs('model', exist_ok=True)
metrics = []

#Train per city
for city in df['City'].unique():
    print(f"\nTraining model for city: {city}")

    city_df = df[df['City'] == city].copy()
    
    features = ['Temperature', 'Precipitation', 'Month', 'Day', 'Hour']
    target = 'Surface_Runoff'

    # Drop missing data
    city_df.dropna(subset=features + [target], inplace=True)

    train_df = city_df[city_df['Year'] < 2025]
    valid_df = city_df[city_df['Year'] == 2025]

    if train_df.empty or valid_df.empty:
        print(f"Skipping {city}: Insufficient training/validation data.")
        continue

    X_train = train_df[features]
    y_train = train_df[target]
    X_valid = valid_df[features]
    y_valid = valid_df[target]

    # Skip if validation has NaNs
    if X_valid.isnull().values.any() or y_valid.isnull().values.any():
        print(f"Skipping {city}: Validation set contains NaNs.")
        continue

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_valid)
    rmse = np.sqrt(mean_squared_error(y_valid, y_pred))
    r2 = r2_score(y_valid, y_pred)

    print(f"{city} - RMSE: {rmse:.2f} | R²: {r2:.3f}")
    metrics.append({'City': city, 'RMSE': rmse, 'R2': r2})

    joblib.dump(model, f"model/model_{city}.pkl", compress=3)
