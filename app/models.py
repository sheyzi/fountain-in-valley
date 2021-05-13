from enum import unique

from sqlalchemy.orm import backref
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

    transactions = db.relationship('Transaction', backref='user', lazy=True)

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"


import enum
from datetime import datetime
class StatusEnum(enum.Enum):
    approved = 'Approved'
    decline = 'Decline'
    pending = 'Pending'

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, nullable=False)
    status = db.Column(
        db.Enum(StatusEnum),
        default = StatusEnum.pending,
        nullable = False
    )
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.details}"