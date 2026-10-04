import pickle
import pandas as pd
import streamlit as st

model = pickle.load(open("model.pkl", "rb"))

st.title("Placement Package Predictor")
cgpa = st.number_input("Enter your CGPA: ", min_value=0.0, max_value=10.0, value=8.0, step=0.1)

if st.button("Predict"):
    pred = model.predict(pd.DataFrame({"cgpa":[cgpa]}))[0]
    st.success(f"Estimated package: {max(pred, 0):.2f} LPA")