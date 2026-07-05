from flask import Blueprint, render_template
from app.forms.auth_forms import RegisterForm, LoginForm

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    return render_template(
        "auth/register.html",
        form=form
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    return render_template(
        "auth/login.html",
        form=form
    )
