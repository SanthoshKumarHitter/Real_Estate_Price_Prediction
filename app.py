import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load('model.pkl')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f9f9f9;
    }
    .title {
        color: #007BFF;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .input-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .input-label {
        font-size: 18px;
        margin-bottom: 10px;
        color: #333;
    }
    .button {
        background-color: #28a745;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        transition: background-color 0.3s;
        border: none;
    }
    .button:hover {
        background-color: #218838;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Real Estate Price Prediction</h1>", unsafe_allow_html=True)

st.write("Please enter the following details to predict the house price:")

# User inputs in columns
col1, col2 = st.columns(2)

with col1:
    distance_to_mrt = st.number_input('Distance to the nearest MRT station (meters)', min_value=0, step=1)

with col2:
    num_convenience_stores = st.number_input('Number of convenience stores', min_value=0, step=1)

# Realistic latitude and longitude ranges
latitude = st.slider('Latitude', min_value=24.5, max_value=25.5, value=25.0, step=0.0001)
longitude = st.slider('Longitude', min_value=121.0, max_value=122.0, value=121.5, step=0.0001)

if st.button('Predict Price', key="predict", help="Click to predict the house price"):
    if None not in [distance_to_mrt, num_convenience_stores, latitude, longitude]:
        features = pd.DataFrame([[distance_to_mrt, num_convenience_stores, latitude, longitude]], 
                                 columns=['Distance to the nearest MRT station', 
                                          'Number of convenience stores', 
                                          'Latitude', 
                                          'Longitude'])
        with st.spinner('Making prediction...'):
            prediction = model.predict(features)[0]
        st.success(f'Predicted House Price of Unit Area: **${prediction:.2f}**')
    else:
        st.warning('Please enter all values to get a prediction')
