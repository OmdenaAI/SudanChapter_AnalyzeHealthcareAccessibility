import streamlit as st
import pickle
import numpy as np
import pandas as pd
from geopy.distance import geodesic
import pandas as pd
import plotly.express as px
from datetime import date, timedelta
from prophet import Prophet
import numpy as np
from sklearn.linear_model import LogisticRegression

import os


print("Current Working Directory:", os.getcwd())

current_dir = os.path.dirname(os.path.abspath(__file__))

#load the ndwi and ndvi data from the folder
def get_data():
    """ Get the NDVI AND NDWI VALUE INFORMATION AND INPUT IT INTO THE MODEL
    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = os.path.join(current_dir, 'ndvi_ndwi_values_2000_2023_gen.csv')
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



model_path = os.path.join(current_dir, "model.pkl")

# Logistic Regression model load
with open(model_path, "rb") as f:
    model = pickle.load(f)

# hospital data load
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



# Streamlit UI
st.title("HealthCare Accessibility Determination System")
st.write("By input your location and the time of year, determine the probability of a malaria outbreak and possible accessibility to the nearest healthcare facility")



# user input
#month and year for malaria probability

month = st.number_input('please provide the month of the year you are looking for (1-12)')
year = st.number_input('please provide the year you are looking for')

#lat, long, and pop for healthcare accesibility model

user_lat = st.number_input("Input your latitude", value=15.45, format="%.6f")
user_lon = st.number_input("Input your longitude", value=32.49, format="%.6f")
pop2024 = st.number_input("Input the population of your nearest city", value=1000000)



###malaria outbreak probability
inputs = None

if month and year:
    #generate ndvi and ndwi values based on time of year
    forecast = forecaster(month, year, df)
    #prepare the inputs for the model
    inputs = np.array([forecast[0], forecast[1], int(month), 0 ,0 ,0 ,1])
    
    inputs = inputs.reshape(1,-1)
    #predicte the probability of malaria outbreak
    pred = model.predict(inputs)
    pred_proba = model.predict_proba(inputs)

    #verbally declare the prediction value's interpretation
    #verbally declare the probablity of the prediction
    
    if pred == 0:
        
        st.write('the prediction is that there will not be a malaria outbreak')

    elif pred == 1:
        
        st.write('the prediction is that there will be a malaria outbreak')


    if pred_proba is not None:

        st.write(f'the probability of a malaria outbreak occuring is {pred_proba[0,1]}')



###healthcare accesibility 
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
