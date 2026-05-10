import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("dataset/symptoms_dataset.csv")

# Features and target
X = df.drop("disease", axis=1)
y = df["disease"]

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Page configuration
st.set_page_config(page_title="SymptoCare AI")

# Title
st.title("🩺 SymptoCare AI")
st.subheader("AI-Powered Health Symptom Checker")

# Description
st.write(
    "Select the symptoms below to predict the possible disease."
)

# Symptom selection
fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")
vomiting = st.checkbox("Vomiting")
body_pain = st.checkbox("Body Pain")

# Prediction button
if st.button("Predict Disease"):

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

    prediction = model.predict(symptoms)[0]

    st.success(f"Predicted Disease: {prediction}")

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

    st.info(
        f"Recommended Precaution: {precautions.get(prediction)}"
    )

    st.warning(
        "⚠ Educational project only. Not professional medical advice."
    )
