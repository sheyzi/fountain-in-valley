from enum import unique
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80))
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    account_number = db.Column(db.String(10), unique=True, nullable=False)
    account_balance = db.Column(db.Float, unique=True, nullable=False, default=0.00)
    password = db.Column(db.String(100), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} "