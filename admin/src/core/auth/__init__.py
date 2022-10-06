import json
from passlib.hash import sha256_crypt
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


def assign_roles(user, roles):
    user.roles.extend(roles)
    db.session.add(user)
    db.session.commit()

    return user


def find_user_by_email_and_pass(email, password):
    return User.query.filter_by(email=email, password=password).first()


def verify_login(email, password):
    response = User.query.filter_by(email=email).first()
    if response:
        if sha256_crypt.verify(password, response.password):
            return response

    return None


def get_initials(email):
    user = User.query.filter_by(email=email).all()
    return user.first_name[0] + user.last_name[0]


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


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


# APIs
def user_json(user):
    return {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_active': user.is_active
    }
