from src.core.database import db


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
