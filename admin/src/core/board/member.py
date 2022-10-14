from datetime import datetime

from src.core.database import db


class Asociado(db.Model):
    __tablename__ = "asociados"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    doc_type = db.Column(db.String(100))
    doc_num = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    member_num = db.Column(db.String(100), unique=True)

    address = db.Column(db.String(100))
    is_active = db.Column(db.Boolean)
    phone_num = db.Column(db.String(30))
    email = db.Column(db.String(100))

    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.DateTime, default=datetime.now())  # fecha_alta
