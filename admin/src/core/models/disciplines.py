from datetime import datetime

from src.core.database import db

discipline_members = db.Table(
    "discipline_members",
    db.Column("discipline_id", db.Integer, db.ForeignKey("disciplines.id"), primary_key=True),
    db.Column("member_id", db.Integer, db.ForeignKey("members.id"), primary_key=True),
)


class Discipline(db.Model):
    __tablename__ = "disciplines"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    instructors = db.Column(db.String(255))
    days_hours = db.Column(db.String(100))
    monthly_fee = db.Column(db.Integer())
    is_active = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean, default=False)

    members = db.relationship("Member", secondary=discipline_members, backref="disciplines")
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    inserted_at = db.Column(db.DateTime, default=datetime.now())
