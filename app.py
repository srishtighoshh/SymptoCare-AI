import streamlit as st
import pandas as pd
import joblib

# Load trained ML model
model = joblib.load("model/disease_model.pkl")

# Page configuration
st.set_page_config(page_title="SymptoCare AI")

# Title
st.title("🩺 SymptoCare AI")
st.subheader("AI-Powered Health Symptom Checker")

# Description
st.write(
    "Select the symptoms below to predict the possible disease using Machine Learning."
)

# Symptom inputs
fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")
vomiting = st.checkbox("Vomiting")
body_pain = st.checkbox("Body Pain")

# Predict button
if st.button("Predict Disease"):

    # Create input dataframe
    symptoms = pd.DataFrame([[
        int(fever),
        int(cough),
        int(headache),
        int(fatigue),
        int(vomiting),
        int(body_pain)
    ]], columns=[
        "fever",
        "cough",
        "headache",
        "fatigue",
        "vomiting",
        "body_pain"
    ])

    # Make prediction
    prediction = model.predict(symptoms)[0]

    # Display prediction
    st.success(f"Predicted Disease: {prediction}")

    # Precaution dictionary
    precautions = {
        "Flu": "Drink plenty of fluids and take proper rest.",
        "Dengue": "Consult a doctor immediately and stay hydrated.",
        "Cold": "Take rest and consume vitamin C.",
        "Typhoid": "Avoid outside food and consult a physician.",
        "COVID-19": "Isolate yourself and seek medical advice.",
        "Migraine": "Reduce stress and rest in a quiet environment.",
        "Malaria": "Get a blood test and seek treatment quickly.",
        "Allergy": "Avoid allergens and take proper medication.",
        "Pneumonia": "Seek medical attention immediately.",
        "Stress": "Practice relaxation and stress management."
    }

    # Show precaution
    st.info(f"Recommended Precaution: {precautions.get(prediction)}")

    # Warning message
    st.warning(
        "⚠ This project is developed for educational purposes only and should not be considered professional medical advice."
    )
