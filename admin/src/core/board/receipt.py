from datetime import datetime

from src.core.database import db


class Receipt(db.Model):
    __tablename__ = "receipts"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    member_full_name = db.Column(db.String(255))
    total_amount = db.Column(db.Float)
    total_amount_description = db.Column(db.String(255))
    month_description = db.Column(db.String(255))

    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'), nullable=False)

    disciplines = db.relationship('ReceiptDisciplines', backref='receipts')

    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.Date, default=datetime.now())
