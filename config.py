import os


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "mediverse_secret_key"
    )

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "jwt_secret_key"
    )

    SQLALCHEMY_DATABASE_URI = "sqlite:///database/app.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
