from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "mediverse_secret_key"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mediverse.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    with app.app_context():
        from app.models.user import User
        db.create_all()

    return app
