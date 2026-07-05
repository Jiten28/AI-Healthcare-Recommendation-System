from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.prediction_history import PredictionHistory
from app.ml.recommend import get_recommendation

home_bp = Blueprint("home", __name__)


# Landing Page
@home_bp.route("/")
def home():
    return render_template("landing/index.html")


# Medicine Page
@home_bp.route("/medicine")
@login_required
def medicine():

    latest = (
        PredictionHistory.query
        .filter_by(user_id=current_user.id)
        .order_by(PredictionHistory.created_at.desc())
        .first()
    )

    recommendation = None

    if latest:
        recommendation = get_recommendation(latest.disease)

    return render_template(
        "dashboard/medicine.html",
        recommendation=recommendation,
        latest=latest
    )


# Dashboard
@home_bp.route("/dashboard")
@login_required
def dashboard():

    predictions = (
        PredictionHistory.query
        .filter_by(user_id=current_user.id)
        .all()
    )

    total_predictions = len(predictions)

    latest_prediction = (
        predictions[-1]
        if predictions
        else None
    )

    return render_template(
        "dashboard/dashboard.html",
        total_predictions=total_predictions,
        latest_prediction=latest_prediction
    )


# Analytics
@home_bp.route("/analytics")
@login_required
def analytics():

    predictions = (
        PredictionHistory.query
        .filter_by(user_id=current_user.id)
        .all()
    )

    total_predictions = len(predictions)

    disease_count = {}

    for p in predictions:
        if p.disease:
            disease_count[p.disease] = (
                disease_count.get(p.disease, 0) + 1
            )

    most_predicted = None

    if disease_count:
        most_predicted = max(
            disease_count,
            key=disease_count.get
        )

    avg_confidence = 0

    if predictions:
        avg_confidence = round(
            sum(p.confidence for p in predictions)
            / total_predictions,
            2
        )

    return render_template(
        "dashboard/analytics.html",
        total_predictions=total_predictions,
        most_predicted=most_predicted,
        avg_confidence=avg_confidence,
        predictions=predictions
    )

# Doctor Page


@home_bp.route("/doctor")
def doctor():
    return render_template("dashboard/doctor.html")


# Admin Page
@home_bp.route("/admin")
def admin():
    return render_template("dashboard/admin.html")
