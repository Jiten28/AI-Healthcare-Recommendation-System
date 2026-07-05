from flask import Blueprint, render_template
from flask_login import login_required

prediction_bp = Blueprint("prediction", __name__)


@prediction_bp.route("/prediction")
@login_required
def prediction():

    return render_template("dashboard/prediction.html")
