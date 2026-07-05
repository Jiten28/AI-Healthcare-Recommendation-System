from flask import abort
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.user import User
from app.models.prediction_history import PredictionHistory
from app.ml.recommend import get_recommendation
from app import db

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

    disease_count = {}

    for p in predictions:
        if p.disease:
            disease_count[p.disease] = (
                disease_count.get(p.disease, 0) + 1
            )

    chart_labels = list(disease_count.keys())
    chart_values = list(disease_count.values())

    return render_template(
        "dashboard/dashboard.html",
        total_predictions=total_predictions,
        latest_prediction=latest_prediction,
        chart_labels=chart_labels,
        chart_values=chart_values
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
@login_required
def admin():

    if not current_user.is_admin:
        abort(403)

    total_users = User.query.count()
    total_predictions = PredictionHistory.query.count()

    total_diseases = (
        db.session.query(
            PredictionHistory.disease
        ).distinct().count()
    )

    recent_predictions = (
        PredictionHistory.query
        .order_by(PredictionHistory.created_at.desc())
        .limit(10)
        .all()
    )

    return render_template(
        "dashboard/admin.html",
        total_users=total_users,
        total_predictions=total_predictions,
        total_diseases=total_diseases,
        recent_predictions=recent_predictions
    )
