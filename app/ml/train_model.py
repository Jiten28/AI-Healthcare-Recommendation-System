import os
import json
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATASET = os.path.join(BASE_DIR, "dataset", "disease", "Training.csv")

MODEL_DIR = os.path.dirname(__file__)


df = pd.read_csv(DATASET)

X = df.drop("prognosis", axis=1)

y = df["prognosis"]

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X, y_encoded)

joblib.dump(
    model,
    os.path.join(MODEL_DIR, "disease_model.pkl")
)

joblib.dump(
    label_encoder,
    os.path.join(MODEL_DIR, "label_encoder.pkl")
)

with open(
    os.path.join(MODEL_DIR, "symptoms.json"),
    "w"
) as f:

    json.dump(list(X.columns), f, indent=4)

print("Training Completed Successfully!")
