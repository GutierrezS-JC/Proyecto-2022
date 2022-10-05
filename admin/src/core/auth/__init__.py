import json

from src.core.database import db
from src.core.auth.user import User


def list_users():
    return User.query.all()


def create_user(**kwargs):
    user = User(**kwargs)
    print(user.roles)
    db.session.add(user)
    db.session.commit()

    return user


def find_user_by_email_and_pass(email, password):
    return User.query.filter_by(email=email, password=password).first()


def get_initials(email):
    user = User.query.filter_by(email=email).all()
    return user.first_name[0] + user.last_name[0]
