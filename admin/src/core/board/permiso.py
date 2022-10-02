from src.core.database import db


class Permiso(db.Model):
    __tablename__ = "permisos"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(255))
