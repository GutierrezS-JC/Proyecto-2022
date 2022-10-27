from datetime import datetime

from src.core.database import db


class Fee(db.Model):
    __tablename__ = "fees"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    year = db.Column(db.String(20))
    month = db.Column(db.String(20))
    total = db.Column(db.Float)
    was_paid = db.Column(db.Boolean)
    was_expired = db.Column(db.Boolean)
    date_paid = db.Column(db.Date)

    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    member = db.relationship('Member', backref='members')
    receipt = db.relationship('Receipt', backref='fees', lazy=True, uselist=False)

    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.Date, default=datetime.now())
