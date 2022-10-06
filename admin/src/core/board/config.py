from datetime import datetime

from src.core.database import db


class Config(db.Model):
    __tablename__ = "config"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    elements_quantity = db.Column(db.Integer)
    payment_enabled = db.Column(db.Boolean)
    contact_information = db.Column(db.Text)
    payment_header = db.Column(db.String(255))
    monthly_fee = db.Column(db.Float)
    extra_charge = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.DateTime, default=datetime.now())
