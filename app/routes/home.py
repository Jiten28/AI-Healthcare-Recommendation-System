from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)
# Landing Page


@home_bp.route("/")
def home():
    return render_template("landing/index.html")


# Prediction Page
@home_bp.route("/prediction")
def prediction():
    return render_template("dashboard/prediction.html")


# Dashboard
@home_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard/dashboard.html")


# Analytics
@home_bp.route("/analytics")
def analytics():
    return render_template("dashboard/analytics.html")
