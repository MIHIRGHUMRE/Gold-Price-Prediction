import streamlit as st
import pickle
import numpy as np
import os

current_folder = os.path.dirname(__file__)

# Build the full path to the model
model_path = os.path.join(current_folder, 'gold_price_model.pkl')

# Load the saved model
model = pickle.load(open(model_path, 'rb'))

# App title
st.title("Gold Price Prediction App")

# Short description
st.write("Enter the financial indicators below to predict the Gold Price (GLD).")

# Input fields
spx = st.number_input("SPX (S&P 500 Index)", value=0.0)
uso = st.number_input("USO (Oil Price)", value=0.0)
slv = st.number_input("SLV (Silver Price)", value=0.0)
eur_usd = st.number_input("EUR/USD Exchange Rate", value=0.0)

# Predict button
if st.button("Predict Gold Price"):
    # Prepare the input data as a NumPy array
    input_data = np.array([[spx, uso, slv, eur_usd]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"Predicted Gold Price (GLD): ${prediction:.2f}")

