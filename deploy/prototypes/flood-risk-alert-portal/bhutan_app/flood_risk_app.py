import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
import pydeck as pdk
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error
import os

# Constants
BASE_DIR = os.path.dirname(__file__)  # Path to Bhutan_App folder
DATA_PATH = os.path.join(BASE_DIR, "data", "bhutan_runoff_hourly_data.csv")

MODEL_DIR = os.path.join(BASE_DIR, "model")

# Page configuration
st.set_page_config(layout="wide")

st.markdown("""
    <div style="background-color:white; padding: 10px 5px 5px 5px; border-bottom: 2px solid #e6e6e6;">
        <h1 style="text-align: left; font-size: 60px; color: black; font-style: Calibri;">
            འབྲུག་ཆུ་རུད་ཀྱི་རྐྱེན་ངན་ཉེན་བརྡའི་དྲ་ངོས།<br>
            <span style="font-size: 30px;">Bhutan Flood Disaster Alert Portal</span>
        </h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @keyframes blink-text {
            0% { opacity: 1; }
            50% { opacity: 0; }
            100% { opacity: 1; }
        }
        span.blink {
            animation: blink-text 1s infinite;
            color: white;
            font-weight: bold;
        }
    </style>
    <div style="background-color: #2a6aad; border-radius: 6px 6px 0 0; padding: 5px 15px; margin: 5px 0 0 0; color: white;">
        <div style="font-size: 18px; font-weight: bold; animation: blink-text 1.2s infinite;">
            LIVE:
        </div>
    </div>

    <div style="background-color: #ffcccc; border-left: 5px solid red; padding: 10px; margin: 0 0 10px 0; overflow: hidden; border-radius: 0 0 6px 6px;">
        <div style="
            display: inline-block;
            white-space: nowrap;
            animation: scroll-left 15s linear infinite;
            font-weight: bold;
            color: red;
            font-size: 18px;
        ">
            🚨 High Flood Risk | Paro | 24 Jul 2025 ------- Stay alert and follow evacuation protocols. 🚨
        </div>
    </div>

    <style>
        @keyframes scroll-left {
            0% {
                transform: translateX(100%);
            }
            100% {
                transform: translateX(-100%);
            }
        }
    </style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    # Navigation section
    st.header("Navigation")
    st.markdown("- 📘 [Guide](#)")
    st.markdown("- 🧠 [GitHub Repo](https://github.com/name_123)")  # Replace with actual link
    st.markdown("---")

    # Social media icons vertically
    st.markdown("""
        <div style="margin-top: 20px; margin-bottom: 20px;">
            <a href="https://facebook.com" target="_blank" style="display: block; margin-bottom: 10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="25"> Facebook
            </a>
            <a href="https://twitter.com" target="_blank" style="display: block; margin-bottom: 10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" width="25"> X (Twitter)
            </a>
            <a href="https://youtube.com" target="_blank" style="display: block; margin-bottom: 10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="25"> YouTube
            </a>
            <a href="https://instagram.com" target="_blank" style="display: block; margin-bottom: 10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="25"> Instagram
            </a>
        </div>
    """, unsafe_allow_html=True)

    # Add a small vertical spacer before the footer
    st.markdown("<div style='height:0px;'></div>", unsafe_allow_html=True)

    # Footer text
    st.markdown("""
        <div style="font-weight: bold; font-size: 16px;">
            🇧🇹 Powered by Omdena Bhutan
        </div>
                <div style="font-size: 14px; margin-top:10px; line-height:1.4; text-align: left; color: #e6e6e6;">
            This portal is developed as part of Bhutan's Disaster Management initiative, 
            aiming to provide real-time flood alerts, risk forecasts, and safety information 
            to keep citizens informed and prepared during emergencies.
        </div>
        <div style="margin-top:10px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Flag_of_Bhutan.svg" 
                 alt="Bhutan Flag" width="120">
        </div>
                
        <div style="font-size: 14px; margin-top:10px; line-height:1.4; text-align: left; color: #e6e6e6;">
                Version 1.0
        </div>
                
        <div style="font-size: 14px; margin-top:10px; line-height:1.4; text-align: left; color: #e6e6e6;">
                Last Updated On: 24 July 2025
        </div>
    """, unsafe_allow_html=True)

# ---------- 💅 Custom CSS ----------
# ---------- Complete CSS (Adjusted for Small Shift) ----------
st.markdown("""
    <style>
    /* Remove black top bar */
    [data-testid="stHeader"] {
        background-color: white !important;
        height: 0px !important;
    }

    /* App background and font */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .main {
        background-color: white !important;
        color: black !important;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #2a6aad !important;
    }

    /* Sidebar content */
    [data-testid="stSidebar"] * {
        color: white !important;
        font-weight: bold !important;
        text-decoration: none !important;
    }

    /* Tab bar (horizontal strip behind tab names) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #2a6aad !important;
        padding: 12px 30px !important;
        border-radius: 0px;
        width: 100% !important;
        display: flex;
        justify-content: flex-start;
    }

    /* Tab labels */
    .stTabs [data-baseweb="tab"] {
        color: white !important;
        font-weight: bold !important;
        font-size: 24px !important;
        padding: 12px 24px !important;
        border-radius: 6px !important;
    }

    /* Highlight selected tab */
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid white !important;
    }

    /* Remove link underlines */
    a {
        text-decoration: none !important;
    }
    a:hover {
        text-decoration: none !important;
    }

    /* ----------- MOVE CONTENT SLIGHTLY UP ----------- */
    .main .block-container {
        padding-top: 0rem !important;
        margin-top: -0.3rem !important;
    }
    section[data-testid="stSidebar"] ~ section div.block-container {
        padding-top: 0rem !important;
        margin-top: -0.3rem !important;
    }
    div[data-testid="stTabs"] {
        margin-top: -0.1rem !important;
    }
    </style>
""", unsafe_allow_html=True)


# ---------- Load Data ----------
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['DateTime'] = pd.to_datetime(df['DateTime'], dayfirst=True, errors='coerce')
    df['Year'] = df['DateTime'].dt.year
    df['Month'] = df['DateTime'].dt.month
    df['Day'] = df['DateTime'].dt.day
    df['Hour'] = df['DateTime'].dt.hour
    return df

df = load_data()

# ---------- 🔵 Tab Container with Tabs inside ----------
tab_dashboard, tab_dos, tab_volunteers, tab_phone = st.tabs([
    "📊 Dashboard ", "✅ Dos and Don’ts ", "🧑‍🤝‍🧑 Volunteers ", "📞 Emergency Contacts "
])


# ---------- 📊 Dashboard ----------
with tab_dashboard:
    st.markdown("<h2 style='font-size:28px; color:black;'>📍 Forecast & Risk Map of Bhutan</h2>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color:#f5f5f5; padding:10px; border-radius:6px; border: 1px solid #ddd; margin-bottom:10px; font-size:16px; line-height:1.5;">  
            This dashboard provides real-time flood risk forecasts, interactive maps, and 10-day surface runoff predictions for major cities in Bhutan.  
            Stay informed, stay safe. 🇧🇹
        </div>
    """, unsafe_allow_html=True)

    # --- City List ---
    available_models = [f for f in os.listdir(MODEL_DIR) if f.endswith('.pkl')]
    cities = sorted([f.replace("model_", "").replace(".pkl", "") for f in available_models])

    # Dropdown for city selection
    selected_city = st.selectbox("Select a City for Forecast", cities)

    # Load the model for selected city
    model_path = os.path.join(MODEL_DIR, f"model_{selected_city}.pkl")
    model = joblib.load(model_path)

    # Forecast for 2026 - 10 days
    future_dates = pd.date_range(start="2026-01-01", periods=10, freq="D")
    city_df_full = df[df['City'] == selected_city].copy()
    last_row = city_df_full.iloc[-1]

    forecast_features = pd.DataFrame({
        "Temperature": [last_row['Temperature']] * 10,
        "Precipitation": [last_row['Precipitation']] * 10,
        "Month": future_dates.month,
        "Day": future_dates.day,
        "Hour": [12] * 10
    })

    forecast_values = model.predict(forecast_features)
    forecast_df = pd.DataFrame({"Date": future_dates, "Forecast_Runoff": forecast_values})

    # City coordinates
    city_coordinates = {
        "Thimphu": (27.4728, 89.6390),
        "Paro": (27.4305, 89.4167),
        "Punakha": (27.5916, 89.8775),
        "Phuntsholing": (26.8601, 89.3893),
        "Trongsa": (27.5023, 90.5085),
        "Wangdue Phodrang": (27.4333, 89.9167),
        "Trashigang": (27.3311, 91.5523),
        "Mongar": (27.2747, 91.2400),
        "Samdrup Jongkhar": (26.8000, 91.5000),
        "Gasa": (27.9045, 89.7266)
    }

    city_coords = pd.DataFrame(
        [(c, *city_coordinates.get(c, (27.5, 90.5))) for c in cities],
        columns=["City", "Latitude", "Longitude"]
    )

    # Assign color: Blue for selected city, Red for others
    city_coords["Color"] = city_coords["City"].apply(
        lambda x: [0, 0, 255, 200] if x == selected_city else [200, 30, 0, 160]
    )

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🗺️ Map of Forecast Locations")
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=27.5,
                longitude=90.5,
                zoom=6.5,
            ),
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=city_coords,
                    get_position='[Longitude, Latitude]',
                    get_color='Color',
                    get_radius=8000,
                    pickable=True
                )
            ],
            tooltip={"text": "{City}"}
        ))

    with col2:
        st.subheader(f"📈 10-Day Forecasted Surface Runoff in {selected_city} (2026)")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(forecast_df['Date'], forecast_df['Forecast_Runoff'], marker='o', color='blue', label='Forecast')
        ax.set_title(f"10-Day Forecast (2026) - {selected_city}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Runoff")
        ax.legend()
        ax.tick_params(axis='x', rotation=90)
        st.pyplot(fig)


# ---------- ✅ Dos and Don’ts ----------
with tab_dos:
    st.title("✅ Flood Safety Guidelines")
    st.subheader("Dos")
    st.markdown("""
    - ✅ Move to higher ground  
    - ✅ Keep emergency kit ready  
    - ✅ Disconnect electrical appliances  
    - ✅ Stay updated with alerts  
    - ✅ Assist vulnerable individuals  
    """)
    st.subheader("Don'ts")
    st.markdown("""
    - ❌ Don’t drive through flooded roads  
    - ❌ Avoid touching wet electrical devices  
    - ❌ Don’t ignore evacuation orders  
    - ❌ Don’t drink untreated water  
    """)

# ---------- 🧑‍🤝‍🧑 Volunteers ----------
with tab_volunteers:
    st.title("🧑‍🤝‍🧑 Volunteer Directory")

    # Volunteer Data
    volunteer_df = pd.DataFrame({
        "Name": ["Sonam Dorji", "Karma Choden", "Tashi Wangdi"],
        "Region": ["Thimphu", "Punakha", "Paro"],
        "Phone": ["+975-17XXXXXX", "+975-16XXXXXX", "+975-18XXXXXX"]
    })

    # Convert DataFrame to HTML with custom class
    st.markdown(
        volunteer_df.to_html(index=False, classes="black-table"),
        unsafe_allow_html=True
    )

    # Custom CSS for black text and table styling
    st.markdown("""
        <style>
        .black-table {
            color: black !important;
            font-size: 16px;
            border-collapse: collapse;
            width: 100%;
        }
        .black-table th, .black-table td {
            border: 1px solid #ddd;
            text-align: left;
            padding: 8px;
        }
        .black-table th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)


# ---------- 📞 Emergency Contacts ----------
with tab_phone:
    st.title("📞 Emergency Contact Numbers")
    st.markdown("""
    - 📞 **Disaster Management**: 999  
    - 🚑 **Ambulance**: 112  
    - 🔥 **Fire Brigade**: 110  
    - 🚓 **Police**: 113  
    - ❤️ **Red Cross Bhutan**: 1717  
    """)
