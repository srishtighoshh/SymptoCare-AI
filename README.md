# 🩺 SymptoCare AI

## Overview

SymptoCare AI is a Machine Learning-based health symptom checker that predicts possible diseases using symptoms selected by the user.


## Live Application

[Click Here to Open SymptoCare AI](https://symptocare-ai-ynyv3u2tetfzv4bmwrspfc.streamlit.app/)


## Features

- Disease prediction using Machine Learning
- Symptom-based analysis
- Precaution recommendations
- Interactive user interface
- Fast prediction system


## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- scikit-learn
- Google Colab
- GitHub


## Project Structure

```text
SymptoCare-AI/
│
├── dataset/
│   └── symptoms_dataset.csv
│
├── project_report/
│   └── Project Report.pdf
│
├── screenshots/
│   ├── dataset.png
│   ├── accuracy.png
│   ├── prediction.png
│   └── live app.png
│
├── app.py
├── requirements.txt
└── README.md
```


## How to Run the Project

### Install Required Libraries

Open terminal and run:

```bash
pip install -r requirements.txt
```

### Run the Application

Run the following command:

```bash
streamlit run app.py
```

### Open in Browser

After running the command, the application will open automatically.

If it does not open automatically, open:

```text
http://localhost:8501
```

## Machine Learning Model

The project uses a Random Forest Classifier trained on symptom data to provide preliminary disease predictions and precaution suggestions.

## Disclaimer

This project is developed for educational purposes only and should not be considered professional medical advice.
