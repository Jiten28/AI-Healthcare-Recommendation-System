from flask import Flask
from config import Config


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object(Config)

    # Register Blueprints
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    return app
