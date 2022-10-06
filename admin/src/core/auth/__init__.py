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


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def user_is_admin(username):
    response = False
    user = get_user_by_username(username)
    for rol in user.roles:
        if rol.name == "Admin":
            response = True
    return response


def user_set_status(username):
    user = get_user_by_username(username)
    user.is_active = not user.is_active
    db.session.commit()

    return True
