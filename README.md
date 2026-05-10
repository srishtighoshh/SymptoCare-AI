# 🩺 SymptoCare AI

## Overview

SymptoCare AI is a Machine Learning-based health symptom checker that predicts possible diseases based on symptoms selected by the user.

The project uses a Random Forest Classifier trained on symptom data to provide preliminary disease predictions and precaution suggestions.

## Live Application

[Click Here to Open SymptoCare AI](https://symptocare-ai-ynyv3u2tetfzv4bmwrspfc.streamlit.app/)

## Features

- Disease prediction using Machine Learning
- Symptom-based analysis
- Precaution recommendations
- User-friendly interface
- Fast prediction system

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- scikit-learn
- Joblib

## Project Structure

```text
SymptoCare-AI/
│
├── dataset/
│   └── symptoms_dataset.csv
│
├── model/
│   └── disease_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

## How to Run the Project

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

## Machine Learning Model

The project uses:

- Random Forest Classifier

for disease prediction based on symptoms entered by the user.

## Disclaimer

This project is developed for educational purposes only and should not be considered professional medical advice.
