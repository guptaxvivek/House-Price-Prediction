import pickle
import streamlit as st
import numpy as np
import time

df = pickle.load(open("data.pkl",'rb'))
model = pickle.load(open("model.pkl",'rb'))

st.title("Bengaluru House Price Predictor")

st.image("house.png")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
with col1:
    location = st.selectbox("Location", df.location.unique())

with col2:
    bhk = st.selectbox("BHK",df.BHK.sort_values().unique())

with col3:
    bath = st.selectbox("Number of bathroom",df.bath.sort_values().unique())

with col4:
    area = st.number_input("Area(in sqft)")

if st.button("Predict Price"):
    bar = st.progress(0)
    for i in range(21):
        bar.progress(i * 5)
        time.sleep(0.1)
    values = np.array([location, area, bath, bhk]).reshape(1, 4)
    st.header("Price Should be ₹{:.2f}".format((model.predict(values)[0]) * 100000))
