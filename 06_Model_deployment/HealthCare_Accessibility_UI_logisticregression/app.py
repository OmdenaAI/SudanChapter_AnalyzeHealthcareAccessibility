import streamlit as st
import pickle
import numpy as np
import pandas as pd
from geopy.distance import geodesic
import pandas as pd
import plotly.express as px

import os

print("Current Working Directory:", os.getcwd())

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.pkl")

# Logistic Regression model load
with open(model_path, "rb") as f:
    model = pickle.load(f)

# hospital data load
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "hospital_data.csv")
hospital_data = pd.read_csv(data_path)

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
        print(f"An error occurred: {e}")
        return None


# Streamlit UI
st.title("HealthCare Accessibility Determination System")
st.write("By input your location, determine the possible accessibility to the nearest healthcare facility")

# user input
user_lat = st.number_input("Input your latitude", value=15.45, format="%.6f")
user_lon = st.number_input("Input your longitude", value=32.49, format="%.6f")
pop2024 = st.number_input("Input the population of your nearest city", value=1000000)

if st.button("Determine"):
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

    # Accessibility within 5km is accessible
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




    df = pd.DataFrame({
    "latitude": [user_lat, nearest_hospital["Latitude_h"]],
    "longitude": [user_lon, nearest_hospital["Longitude_h"]],
    "type": ["Your Location", "Healthcare Facility"]
    })

    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", 
                            color="type", zoom=10, mapbox_style="open-street-map",
                            color_discrete_map={"Your Location": "red", "Healthcare Facility": "blue"})
    
    # fig.update_layout(
    # mapbox=dict(
    #     center=go.layout.mapbox.Center(lat=user_lat, lon=user_lon),
    #     zoom=10
    # )
    # )



    st.plotly_chart(fig)
