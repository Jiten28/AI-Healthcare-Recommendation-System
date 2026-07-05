from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "mediverse_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mediverse.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    # Blueprints
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.prediction import prediction_bp
    app.register_blueprint(prediction_bp)

    # Create tables
    with app.app_context():
        from app.models.user import User
        from app.models.prediction_history import PredictionHistory
        db.create_all()

    print(app.url_map)

    return app
