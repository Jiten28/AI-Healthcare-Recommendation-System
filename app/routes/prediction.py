from flask import (
    Blueprint,
    render_template,
    request,
    flash
)
from flask_login import login_required
import json
import os
from app.ml.recommend import get_recommendation
from flask_login import current_user
from app import db
from app.models.prediction_history import PredictionHistory

from app.ml.predict import predict_disease

prediction_bp = Blueprint("prediction", __name__)

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "ml")

with open(os.path.join(MODEL_DIR, "symptoms.json")) as f:
    all_symptoms = json.load(f)


@prediction_bp.route("/prediction", methods=["GET", "POST"])
@login_required
def prediction():

    print("Prediction Route Called", flush=True)

    result = None

    if request.method == "POST":

        selected_symptoms = request.form.getlist("symptoms")

        # Validate input
        if not selected_symptoms:

            flash(
                "Please select at least one symptom before predicting.",
                "warning"
            )

            return render_template(
                "dashboard/prediction.html",
                result=None,
                symptoms=all_symptoms
            )

        disease, confidence = predict_disease(selected_symptoms)

        recommendation = get_recommendation(disease)
        history = PredictionHistory(
            user_id=current_user.id,
            disease=disease,
            confidence=confidence,
            symptoms=", ".join(selected_symptoms)
        )

        db.session.add(history)
        db.session.commit()
        print(recommendation)
        result = {
            "disease": disease,
            "confidence": confidence,
            "recommendation": recommendation
        }

    print("Length:", len(all_symptoms))
    print("First 10:", all_symptoms[:10], flush=True)

    return render_template(
        "dashboard/prediction.html",
        result=result,
        symptoms=all_symptoms
    )
