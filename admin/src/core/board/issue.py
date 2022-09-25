from datetime import datetime

from ..database import db


class Issue(db.Model):

    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(50))
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    status = db.Column(db.String(50))
    updated_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now()
    )
    inserted_at = db.Column(db.DateTime, default=datetime.now())
