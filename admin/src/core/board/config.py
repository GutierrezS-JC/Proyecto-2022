from datetime import datetime

from src.core.database import db


class Config(db.Model):
    __tablename__ = "config"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    cantidad_elementos = db.Column(db.Integer)
    pago_habilitado = db.Column(db.Boolean)
    informacion_contacto = db.Column(db.Text)
    encabezado_pago = db.Column(db.String(255))
    cuota_mensual = db.Column(db.Float)
    recargo = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.DateTime, default=datetime.now())
