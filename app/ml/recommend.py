import pandas as pd
import os
import ast

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

description_df = pd.read_csv(os.path.join(DATA_DIR, "description.csv"))
medicine_df = pd.read_csv(os.path.join(DATA_DIR, "medications.csv"))
diet_df = pd.read_csv(os.path.join(DATA_DIR, "diets.csv"))
precaution_df = pd.read_csv(os.path.join(DATA_DIR, "precautions_df.csv"))
workout_df = pd.read_csv(os.path.join(DATA_DIR, "workout_df.csv"))

# optional
doctor_df = None
doctor_path = os.path.join(DATA_DIR, "doctors.csv")

if os.path.exists(doctor_path):
    doctor_df = pd.read_csv(doctor_path)


def get_recommendation(disease):

    recommendation = {}

    print("Predicted Disease:", disease)

    # ================= Description =================

    desc = description_df[
        description_df["Disease"] == disease
    ]

    recommendation["description"] = (
        desc.iloc[0]["Description"]
        if not desc.empty
        else "No description available."
    )

    # ================= Medicines =================

    meds = medicine_df[
        medicine_df["Disease"] == disease
    ]

    if not meds.empty:
        recommendation["medicines"] = ast.literal_eval(
            meds.iloc[0]["Medication"]
        )
    else:
        recommendation["medicines"] = []

    # ================= Diet =================

    diet = diet_df[
        diet_df["Disease"] == disease
    ]

    if not diet.empty:
        recommendation["diet"] = ast.literal_eval(
            diet.iloc[0]["Diet"]
        )
    else:
        recommendation["diet"] = []

    # ================= Precautions =================

    precaution = precaution_df[
        precaution_df["Disease"] == disease
    ]

    if not precaution.empty:

        row = precaution.iloc[0]

        recommendation["precautions"] = [
            row["Precaution_1"],
            row["Precaution_2"],
            row["Precaution_3"],
            row["Precaution_4"]
        ]

        recommendation["precautions"] = [
            x for x in recommendation["precautions"]
            if pd.notna(x)
        ]

    else:
        recommendation["precautions"] = []

    # ================= Workout =================

    workout = workout_df[
        workout_df["disease"] == disease
    ]

    recommendation["workout"] = (
        workout["workout"].tolist()
        if not workout.empty
        else []
    )

    # ================= Doctor =================

    doctor_map = {
        "Allergy": "Allergist",
        "Fungal infection": "Dermatologist",
        "GERD": "Gastroenterologist",
        "Diabetes": "Endocrinologist",
        "Hypertension": "Cardiologist",
        "Migraine": "Neurologist",
        "Bronchial Asthma": "Pulmonologist",
        "AIDS": "Infectious Disease Specialist",
        "Drug Reaction": "General Physician",
        "Gastroenteritis": "Gastroenterologist"
    }

    recommendation["doctor"] = doctor_map.get(
        disease,
        "General Physician"
    )

    return recommendation
