import streamlit as st
import json
import time
import pandas as pd
from twilio.rest import Client
import pydeck as pdk
st.set_page_config(layout="wide", page_title="Disaster Monitoring Dashboard")
RESULT_FILE = "results.json"
LOCATIONS_FILE = "locations.json"
LOG_FILE = "alert_log.txt"
ACCOUNT_SID = "AC128b24534dd716a966739668c2a61ab5"
AUTH_TOKEN = "9d045755b02e306141ab208056049f3d"
FROM_NUMBER = "+18149956570"
TO_NUMBER = "+916382640762"
client = Client(ACCOUNT_SID, AUTH_TOKEN)
if "alert_sent" not in st.session_state:
    st.session_state.alert_sent = False
def send_sms(msg):
    try:
        client.messages.create(body=msg, from_=FROM_NUMBER, to=TO_NUMBER)
    except:
        pass
def load_result():
    try:
        with open(RESULT_FILE) as f:
            return json.load(f)
    except:
        return None
def load_locations():
    try:
        with open(LOCATIONS_FILE) as f:
            return json.load(f)
    except:
        return {}
def log_disaster(entry):
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")
def extract_disaster_from_filename(image_name):
    name = image_name.lower()
    if "pre_disaster" in name:
        return None
    base = name.split("_")[0]
    parts = base.split("-")
    if parts[0] in ["hurricane", "social", "socialfire", "social_fire"]:
        return parts[0].replace("_", " ").capitalize()
    if len(parts) > 1:
        return parts[1].capitalize()
    return "Unknown"
st.title("🌍 AI Disaster Monitoring Dashboard")
main = st.empty()
while True:
    data = load_result()
    locations = load_locations()
    with main.container():
        if data and data["detected"]:
            image_name = data["image"]
            disaster = extract_disaster_from_filename(image_name)
            if disaster is None:
                st.success("🟢 Pre-disaster image detected — No disaster")
                st.session_state.alert_sent = False
            else:
                confidence = data["confidence"]
                source = data["source"]
                st.markdown(
                    f"""
                    <h1>🌪 <b>{disaster}</b></h1>
                    <h3>Confidence: {confidence}%</h3>
                    <p><b>Source:</b> {source}</p>
                    """,
                    unsafe_allow_html=True
                )
                if not st.session_state.alert_sent:
                    send_sms(
                        f"🚨 ALERT\nDisaster: {disaster}\nConfidence: {confidence}%\nSource: {source}"
                    )
                    log_disaster(f"{disaster},{confidence},{source},{image_name}")
                    st.session_state.alert_sent = True
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("📊 Confidence Level")
                    chart_df = pd.DataFrame(
                        {"Metric": ["Confidence"], "Value": [confidence]}
                    )
                    st.bar_chart(chart_df.set_index("Metric"))
                # ============================
                # ✅ SATELLITE MAP (FREE ESRI)
                # ============================
                with col2:
                    st.subheader("📍 Disaster Location")
                    place = image_name.split("-")[0].lower()
                    if place in locations:
                        lat, lon = locations[place]
                        map_deck = pdk.Deck(
                            initial_view_state=pdk.ViewState(
                                latitude=float(lat),
                                longitude=float(lon),
                                zoom=5,
                                pitch=0,
                            ),
                            layers=[
                                pdk.Layer(
                                    "TileLayer",
                                    data="https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                                    tile_size=100,
                                ),
                                pdk.Layer(
                                    "ScatterplotLayer",
                                    data=[{"lat": float(lat), "lon": float(lon)}],
                                    get_position="[lon, lat]",
                                    get_radius=15000,
                                    get_fill_color=[0, 255, 255],
                                    pickable=True,
                                ),
                            ],
                        )
                        st.pydeck_chart(map_deck)
                    else:
                        st.warning("Location not found in locations.json")
                # ============================
                # ✅ SATELLITE MAP (FREE ESRI)
                # ============================

        else:
            st.success("✅ No disaster detected")
            st.session_state.alert_sent = False

    time.sleep(3)
