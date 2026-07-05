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

# Medicine Page


@home_bp.route("/medicine")
def medicine():
    return render_template("dashboard/medicine.html")

# Dashboard


@home_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard/dashboard.html")


# Analytics
@home_bp.route("/analytics")
def analytics():
    return render_template("dashboard/analytics.html")

# Doctor Page


@home_bp.route("/doctor")
def doctor():
    return render_template("dashboard/doctor.html")

# Admin Page


@home_bp.route("/admin")
def admin():
    return render_template("dashboard/admin.html")
