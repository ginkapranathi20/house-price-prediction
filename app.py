

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter the house details to predict its price.")

@st.cache_resource
def load_model():
    return joblib.load("house_price_model (1).pkl")

try:
    model = load_model()

    bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1.0, value=2.0)
    sqft_living = st.number_input("Living Area (sqft)", min_value=100, value=1500)
    sqft_lot = st.number_input("Lot Area (sqft)", min_value=100, value=5000)
    floors = st.number_input("Floors", min_value=1.0, value=1.0)
    waterfront = st.selectbox("Waterfront", [0, 1])
    view = st.selectbox("View", [0, 1, 2, 3, 4])
    condition = st.selectbox("Condition", [1, 2, 3, 4, 5])
    sqft_above = st.number_input("Area Above Ground (sqft)", min_value=100, value=1500)
    sqft_basement = st.number_input("Basement Area (sqft)", min_value=0, value=0)
    yr_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000)
    yr_renovated = st.number_input("Year Renovated", min_value=0, max_value=2026, value=0)
    city = st.text_input("City", value="Seattle")
    statezip = st.text_input("State ZIP", value="WA 98101")
    country = st.text_input("Country", value="USA")

    if st.button("Predict House Price"):
        input_data = pd.DataFrame([{
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "sqft_living": sqft_living,
            "sqft_lot": sqft_lot,
            "floors": floors,
            "waterfront": waterfront,
            "view": view,
            "condition": condition,
            "sqft_above": sqft_above,
            "sqft_basement": sqft_basement,
            "yr_built": yr_built,
            "yr_renovated": yr_renovated,
            "city": city,
            "statezip": statezip,
            "country": country
        }])

        prediction = model.predict(input_data)
        st.success(f"Predicted House Price: ${prediction[0]:,.2f}")

except Exception as e:
    st.error(f"Error: {e}")
