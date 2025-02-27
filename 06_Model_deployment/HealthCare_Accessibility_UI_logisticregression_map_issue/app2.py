import pickle
import numpy as np
import pandas as pd
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
#import requests
import os
import streamlit as st
import folium
from streamlit_folium import st_folium
#import urllib.parse

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.pkl")
data_path = os.path.join(current_dir, "hospital_data.csv")
pop_path = os.path.join(current_dir, "population-by-cities-data.csv")
# Logistic Regression model load
with open(model_path, "rb") as f:
    model = pickle.load(f)

# hospital data load
hospital_data = pd.read_csv(data_path)


# Initialize the location to save the specific location when user clicks
if "user_lat" not in st.session_state:
    st.session_state.user_lat = None
    st.session_state.user_lon = None

# Streamlit UI
st.title("HealthCare Accessibility Determination System")
st.write("Click your location on the map")

# center of Sudan
default_location = [15.45, 32.49]  # default location. around the center of Sudan

# make a map
m = folium.Map(location=default_location, zoom_start=6)

# Show in the map in Streamlit
st.write("### Nearest Healthcare Facility Map")    

# show the map with `folium_static`
location = st_folium(m, width=700, height=500)

# When click, save it to the session
if location and "last_clicked" in location and location["last_clicked"]:
    lat, lon = location["last_clicked"]["lat"], location["last_clicked"]["lng"]
    st.session_state.user_lat, st.session_state.user_lon = lat, lon
    st.success(f"📍 Selected location: latitude {lat}, longitude {lon}")

# backup as mannual input
if st.session_state.user_lat is None or st.session_state.user_lon is None:
    st.warning("⚠️ Click your location on the map or input mannualy")
    user_lat = st.number_input("Input your latitude", value=15.45, format="%.6f")
    user_lon = st.number_input("Input your longitude", value=32.49, format="%.6f")
else:
    user_lat = st.session_state.user_lat
    user_lon = st.session_state.user_lon

# function for searching the nearest healthcare facility
def find_nearest_hospital(user_lat, user_lon, hospital_data):

    # check if the data is empty
    if hospital_data.empty:
        raise ValueError("Error: Hospital data is empty.")
    
    try:
        # copy the hospital_data
        hospital_data_copy = hospital_data.copy()

        # calculate the distance
        hospital_data_copy["distance_km"] = hospital_data_copy.apply(
            lambda row: geodesic((user_lat, user_lon), (row["Latitude_h"], row["Longitude_h"])).km, axis=1
        )

        # get the nearest hospital
        nearest_hospital = hospital_data_copy.loc[hospital_data_copy["distance_km"].idxmin()]
        return nearest_hospital

    except Exception as e:
        st.write(f"An error occurred: {e}")
        return None





def get_nearest_city(user_lat, user_lon):
    """
    Based on the lat and lon that the user input, get the nearest city from the CSV file
    """
    min_distance = float("inf")
    nearest_city = "Unknown"

    city_data = pd.read_csv(pop_path)

    for _, row in city_data.iterrows():
        city_lat, city_lon = row["latitude"], row["longitude"]
        distance = geodesic((user_lat, user_lon), (city_lat, city_lon)).kilometers

        if distance < min_distance:
            min_distance = distance
            nearest_city = row["city"]

    return nearest_city


def get_city_population(city):
    """
    get the city population from the assigned city in the CSV file
    """
    city_data = pd.read_csv(pop_path)
    population = city_data.loc[city_data["city"] == city, "pop2024"]
    return int(population.values[0]) if not population.empty else "Unknown"


# get the nearest city
nearest_city = get_nearest_city(user_lat, user_lon)
st.write(f"Nearest city: {nearest_city}")

# population of the city
population = get_city_population(nearest_city)
pop2024 = population
st.write(f"Population: {population}")


# セッション状態の初期化
if "map_data" not in st.session_state:
    st.session_state.map_data = None  # 地図の初期値
if "determined" not in st.session_state:
    st.session_state.determined = False  # 初期化   


if st.button("Determine"):
    st.session_state.determined = True

    if "map_data" not in st.session_state:
        st.session_state.map_data = None

    if st.session_state.map_data is not None:
        st.write("Map data is saved!")
    else:
        st.write("No map data saved.")

    
    # search the nearest hospitals
    nearest_hospital = find_nearest_hospital(user_lat, user_lon, hospital_data)

    # create the data for model input
    input_data = np.array([
        user_lat,
        user_lon,
        pop2024,
        nearest_hospital["Latitude_h"],
        nearest_hospital["Longitude_h"],
        nearest_hospital["distance_km"],
        *nearest_hospital[["amenity_Referral Hospital", "amenity_Teaching Hospital",
                           "amenity_Type A Hospital", "amenity_Type B Hospital",
                           "amenity_Type C Hospital", "amenity_Type D Hospital",
                           "amenity_clinic", "amenity_dentist", "amenity_doctors",
                           "amenity_hospital", "amenity_pharmacy"]].values
    ]).reshape(1, -1)

    # prediction
    prob = model.predict_proba(input_data)[:, 1]  # get the probability for prediction
    threshold = 0.71  # Logistic Regression threshold

    # Accessibility within 5km and threshold 0.71 is accessible
    accessible = (nearest_hospital["distance_km"] <= 5) and (prob[0] > threshold)

    # result
    amenity_columns = ["amenity_Referral Hospital", "amenity_Teaching Hospital",
                   "amenity_Type A Hospital", "amenity_Type B Hospital",
                   "amenity_Type C Hospital", "amenity_Type D Hospital",
                   "amenity_clinic", "amenity_dentist", "amenity_doctors",
                   "amenity_hospital", "amenity_pharmacy"]

    # Extract only the variable with `True` 
    nearest_amenities = [col.replace("amenity_", "").replace("_", " ") for col in amenity_columns if nearest_hospital[col]]

    # Streamlit
    if nearest_amenities:
        st.write(f"**The nearest healthcare facility:** {', '.join(nearest_amenities)}")
    else:
        st.write("No healthcare facility found nearby.")

    st.write(f"**Distance:** {nearest_hospital['distance_km']:.2f} km")
    st.write(f"**Accessbility:** {'✅ YES' if accessible else '❌ NO'}(Possibility: {prob[0]:.2f})")




    # make a Folium map. the setting location is the user's location
    # 地図データがすでにある場合はそれを利用
    if st.session_state.map_data is None:
        m = folium.Map(location=[user_lat, user_lon], zoom_start=10)
        folium.Marker([user_lat, user_lon], popup="Khartoum").add_to(m)
    #st.session_state.map_data = m  # save the map data

        # Make red as users location
        folium.Marker(
            location=[user_lat, user_lon], 
            popup="Your Location", 
            icon=folium.Icon(color="red")
        ).add_to(m)

        # Make blue as the nearest healthcare facility location
        folium.Marker(
            location=[nearest_hospital["Latitude_h"], nearest_hospital["Longitude_h"]],
            popup="Healthcare Facility",
            icon=folium.Icon(color="blue")
        ).add_to(m)

        # Streamlitに地図を表示
        st.session_state.map_data = m  # 地図のデータを保存
    # map_display = st_folium(m, width=700, height=500)  # 地図を表示
    # if st.session_state.determined:
    #     st.write("Results are displayed here!")

    # セッションに保存された地図を表示
    if st.session_state.determined and st.session_state.map_data:
        st_folium(st.session_state.map_data, width=700, height=500)