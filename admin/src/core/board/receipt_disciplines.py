from datetime import datetime

from src.core.database import db


class ReceiptDisciplines(db.Model):
    __tablename__ = "receipt_disciplines"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    instructors = db.Column(db.String(255))
    days_hours = db.Column(db.String(100))
    monthly_fee = db.Column(db.Integer())

    receipt_id = db.Column(db.Integer, db.ForeignKey('receipts.id'))

    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.DateTime, default=datetime.now())
