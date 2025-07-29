import cdsapi
import os
import time

def download_era5_hourly_variable(variable_name,
                                   years,
                                   base_data_dir='../../era5_data_grib_raw', 
                                   area=[28.5, 88.5, 26.5, 92.0]):
    """
    Download hourly ERA5 data for a single variable over Bhutan for specified years.
    Saves to ../era5_data_grib_raw/<variable_name>/ from current script location.

    Parameters:
    - variable_name: str, name of the ERA5 variable (e.g., '2m_temperature')
    - years: list of str or int, e.g., ['2020', '2021']
    - base_data_dir: str, path to main data directory (default: '../era5_data')
    - area: list [N, W, S, E], bounding box for Bhutan
    """
    c = cdsapi.Client()

    output_dir = os.path.join(base_data_dir, variable_name)
    os.makedirs(output_dir, exist_ok=True)

    months = [f"{m:02d}" for m in range(1, 13)]
    days = [f"{d:02d}" for d in range(1, 32)]
    hours = [f"{h:02d}:00" for h in range(24)]

    total_start = time.time()

    for year in years:
        year = str(year)
        output_file = os.path.join(output_dir, f"{variable_name}_{year}.grib")

        if os.path.exists(output_file):
            print(f"✅ Already exists: {output_file}")
            continue

        print(f"\n⬇️ Downloading {variable_name} for {year}...")
        year_start = time.time()

        try:
            c.retrieve(
                'reanalysis-era5-single-levels',
                {
                    'product_type': 'reanalysis',
                    'format': 'grib',
                    'variable': [variable_name],
                    'year': year,
                    'month': months,
                    'day': days,
                    'time': hours,
                    'area': area,
                },
                output_file
            )
            print(f"✅ Finished {year} in {time.time() - year_start:.2f} seconds")
        except Exception as e:
            print(f"❌ Failed for {year}: {e}")

    total_end = time.time()
    print(f"\n⏱️ Total time for {variable_name}: {total_end - total_start:.2f} seconds")
