import os
import json
import joblib
import numpy as np

MODEL_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(MODEL_DIR, "disease_model.pkl"))
label_encoder = joblib.load(os.path.join(MODEL_DIR, "label_encoder.pkl"))

with open(os.path.join(MODEL_DIR, "symptoms.json"), "r") as f:
    symptoms = json.load(f)


def predict_disease(selected_symptoms):

    input_data = np.zeros(len(symptoms))

    for symptom in selected_symptoms:
        if symptom in symptoms:
            index = symptoms.index(symptom)
            input_data[index] = 1

    prediction = model.predict([input_data])[0]
    disease = label_encoder.inverse_transform([prediction])[0]
    confidence = round(
        max(model.predict_proba([input_data])[0]) * 100,
        2
    )

    return disease, confidence
