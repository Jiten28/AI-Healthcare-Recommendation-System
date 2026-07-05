from app import login_manager
from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    predictions = db.relationship(
        "PredictionHistory",
        backref="user",
        lazy=True
    )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
