from datetime import datetime

from src.core.database import db


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    doc_type = db.Column(db.Integer())
    doc_num = db.Column(db.String(100), unique=True)
    genre = db.Column(db.Integer())  # Integer?
    member_num = db.Column(db.String(100), unique=True)

    address = db.Column(db.String(100))
    is_active = db.Column(db.Boolean)
    phone_num = db.Column(db.String(30))
    email = db.Column(db.String(100))
    is_deleted = db.Column(db.Boolean, default=False)

    fees = db.relationship('Fee', backref='members')

    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.DateTime, default=datetime.now())
