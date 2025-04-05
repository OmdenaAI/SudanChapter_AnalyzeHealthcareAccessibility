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
from datetime import date, timedelta
from prophet import Prophet
from sklearn.linear_model import LogisticRegression
#from PIL import Image

st.cache_data.clear()

current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "assets", "omdena_logo.png")

# image_path = os.path.join(os.path.dirname(__file__), "omdena_logo.png")
# image = Image.open(image_path)

st.image(logo_path, width=200)


#malaria
#load the ndwi and ndvi data from the folder
def get_data():
    """ Get the NDVI AND NDWI VALUE INFORMATION AND INPUT IT INTO THE MODEL
    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = os.path.join(current_dir, 'ndvi_ndwi_values_2000_2023.csv')
    df = pd.read_csv(DATA_FILENAME)
    df = df.drop(columns= 'Unnamed: 0')
    one_hots = pd.get_dummies(df['GEO_NAME_SHORT'])
    final_df = pd.concat([df, one_hots], axis=1)
    return final_df

#create the dataframe from the csv file
df = get_data()

#train the model on the data with the hyperparameter tuned model specifications
def model(df):
    X = df[['ndvi_value','ndwi_value','month_x','Chad','Ethiopia','South Sudan','Sudan']]
    y = df['outbreak']
    classifier = LogisticRegression(solver='liblinear', max_iter=100, C=1, class_weight='balanced')
    res = classifier.fit(X , y)
    return res
model = model(df)


#malaria
#function for determining the ndvi and ndwi values based on a forecaster function
def forecaster(month, year, df):

    date = f'{int(year)}-{int(month)}-15'

    #select the date as 'ds' and values as 'y' for the prophet model to work 
    ndvi_df = df[['ds','ndvi_value']]
    ndvi_df = ndvi_df.rename(columns={'ndvi_value':'y'})
    ndwi_df = df[['ds','ndwi_value']]
    ndwi_df = ndwi_df.rename(columns={'ndwi_value':'y'})
    
    #create an instance of a prophet forecaster
    ndvi_fore = Prophet()
    ndvi_fore.fit(ndvi_df)
    ndvi_pred = ndvi_fore.predict(pd.DataFrame(data={'ds': date}, index=[0]))
    ndvi_pred.head()
    ndvi_val = ndvi_pred.loc[0, 'yhat']
    
    #now create an instance for the ndwi value
    ndwi_fore = Prophet()
    ndwi_fore.fit(ndwi_df)
    ndwi_pred = ndwi_fore.predict(pd.DataFrame(data={'ds': date}, index=[0]))
    ndwi_val = ndwi_pred.loc[0, 'yhat']
    return ndvi_val, ndwi_val



###Health care
model_path = os.path.join(current_dir, "model.pkl")
data_path = os.path.join(current_dir, "hospital_data.csv")
pop_path = os.path.join(current_dir, "population-by-cities-data.csv")

# Logistic Regression model load
with open(model_path, "rb") as f:
    model2 = pickle.load(f)

# hospital data load
hospital_data = pd.read_csv(data_path)

# Initialize the location to save the specific location when user clicks
if "user_lat" not in st.session_state:
    st.session_state.user_lat = None
    st.session_state.user_lon = None
# Initialize the status of session
if "map_data" not in st.session_state:
    st.session_state.map_data = folium.Map(location=[15.45, 32.49], zoom_start=6)  # default the center of Sudan
if "determined" not in st.session_state:
    st.session_state.determined = False  # Initialize
if "nearest_hospital" not in st.session_state:
    st.session_state.nearest_hospital = None
if "accessible" not in st.session_state:
    st.session_state.accessible = None
if "prob" not in st.session_state:
    st.session_state.prob = None

# Streamlit UI
st.title("Sudan Disease Prediction and HealthCare Accessibility Determination System")

###1page
###malaria outbreak probability
def malaria_page():
    st.title("Malaria Prediction")
    st.write("By input the month and the time of year, determine the probability of a malaria outbreak")
    
    # User input
    month = st.number_input("please provide the month of the year you are looking for (1-12)", min_value=1, max_value=12, step=1)
    year = st.number_input("please provide the year you are looking for", min_value=2000, max_value=2023, step=1)

    inputs = None
    if month and year:
        # preparation for prediction of malaria
        forecast = forecaster(month, year, df)  # forcast
        inputs = np.array([forecast[0], forecast[1], int(month), 0 ,0 ,0 ,1])
        inputs = inputs.reshape(1, -1)
        
        # result
        pred = model.predict(inputs)
        pred_proba = model.predict_proba(inputs)

        # message
        if pred == 0:
            st.write('The prediction is that there will not be a malaria outbreak')
        elif pred == 1:
            st.write('The prediction is that there will be a malaria outbreak')

        if pred_proba is not None:
            st.write(f'The probability of a malaria outbreak occurring is {pred_proba[0, 1]}')

    if st.button('Next Page: Healthcare Accessibility'):
        st.session_state.page = 'healthcare'



###2page
###healthcare accesibility 
def healthcare_page():      

    # Streamlit UI
    st.title("HealthCare Accessibility")
    st.write("Click your location on the map")

    # Show in the map in Streamlit
    st.write("### Nearest Healthcare Facility Map")    

    # show the map with `folium_static`
    location = st_folium(st.session_state.map_data, width=700, height=500, key="unique_map_key")

    # When click, save it to the session
    if location and "last_clicked" in location and location["last_clicked"]:
        lat, lon = location["last_clicked"]["lat"], location["last_clicked"]["lng"]
        st.session_state.user_lat, st.session_state.user_lon = lat, lon
        st.success(f"📍 Selected location: latitude {lat}, longitude {lon}")

    # backup as mannual input
    if st.session_state.user_lat is None or st.session_state.user_lon is None:
        st.warning("⚠️ Click your location on the map or input mannually")
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


    if st.button("Determine"):
        st.session_state.determined = True

        # if "map_data" not in st.session_state:
        #     st.session_state.map_data = None

        if st.session_state.map_data is not None:
            st.write("Map data is saved!")
        else:
            st.write("No map data saved.")

        
        # search the nearest hospitals
        st.session_state.nearest_hospital = find_nearest_hospital(user_lat, user_lon, hospital_data)

        # create the data for model input

        #if st.session_state.nearest_hospital is not None:
        input_data = np.array([
            user_lat,
            user_lon,
            pop2024,
            st.session_state.nearest_hospital["Latitude_h"],
            st.session_state.nearest_hospital["Longitude_h"],
            st.session_state.nearest_hospital["distance_km"],
            *st.session_state.nearest_hospital[["amenity_Referral Hospital", "amenity_Teaching Hospital",
                            "amenity_Type A Hospital", "amenity_Type B Hospital",
                            "amenity_Type C Hospital", "amenity_Type D Hospital",
                            "amenity_clinic", "amenity_dentist", "amenity_doctors",
                            "amenity_hospital", "amenity_pharmacy"]].values
        ]).reshape(1, -1)

        # prediction
        st.session_state.prob = model2.predict_proba(input_data)[:, 1]
        threshold = 0.71
        st.session_state.accessible = (st.session_state.nearest_hospital["distance_km"] <= 5) and (st.session_state.prob[0] > threshold)

    # show the result
    if st.session_state.determined and st.session_state.nearest_hospital is not None:
        amenity_columns = ["amenity_Referral Hospital", "amenity_Teaching Hospital",
                        "amenity_Type A Hospital", "amenity_Type B Hospital",
                        "amenity_Type C Hospital", "amenity_Type D Hospital",
                        "amenity_clinic", "amenity_dentist", "amenity_doctors",
                        "amenity_hospital", "amenity_pharmacy"]
        nearest_amenities = [col.replace("amenity_", "").replace("_", " ") for col in amenity_columns if st.session_state.nearest_hospital[col]]
        if nearest_amenities:
            st.write(f"**The nearest healthcare facility:** {', '.join(nearest_amenities)}")
        else:
            st.write("No healthcare facility found nearby.")
        st.write(f"**Distance:** {st.session_state.nearest_hospital['distance_km']:.2f} km")
        st.write(f"**Accessibility:** {'✅ YES' if st.session_state.accessible else '❌ NO'}(Possibility: {st.session_state.prob[0]:.2f})")


        # add markers on map
        st.session_state.map_data = folium.Map(location=[user_lat, user_lon], zoom_start=10)  # reset map
            # Make red as users location
        folium.Marker(
            location=[user_lat, user_lon], 
            popup="Your Location", 
            icon=folium.Icon(color="red")
        ).add_to(st.session_state.map_data)

        # Make blue as the nearest healthcare facility location
        folium.Marker(
            location=[st.session_state.nearest_hospital["Latitude_h"], st.session_state.nearest_hospital["Longitude_h"]],
            popup="Healthcare Facility",
            icon=folium.Icon(color="blue")
        ).add_to(st.session_state.map_data)

        
        if st.session_state.determined:
            st_folium(st.session_state.map_data, width=700, height=500, key="unique_map_key_after")

    if st.button('Previous Page: Malaria Prediction'):
        st.session_state.page = 'malaria'

# manage the page
if 'page' not in st.session_state:
    st.session_state.page = 'malaria'  # the page first come

# the current page
if st.session_state.page == 'malaria':
    malaria_page()
elif st.session_state.page == 'healthcare':
    healthcare_page()
