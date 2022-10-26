import json
from passlib.hash import sha256_crypt
from src.core.database import db
from src.core.auth.user import User


def all_paginated(page=1, per_page=10):
    return User.query.order_by(User.id.asc()).paginate(page=page, per_page=per_page, error_out=False)


def list_users():
    return User.query.all()


def list_users_paginated(page, per_page):
    return all_paginated(page, per_page)


def list_users_with_email(email, page, per_page):
    return User.query.filter(User.email.ilike(f'%{email}%')).paginate(page=page, per_page=per_page, error_out=False)


def list_users_with_email_status(email, status, page, per_page):
    return User.query.filter(User.email.ilike(f'%{email}%'), User.is_active == status)\
        .paginate(page=page, per_page=per_page, error_out=False)


def list_users_with_status(status, page, per_page):
    return User.query.filter(User.is_active == status).paginate(page=page, per_page=per_page, error_out=False)


def create_user(**kwargs):
    user = User(**kwargs)
    print(user.roles)
    db.session.add(user)
    db.session.commit()

    return user


def user_edit(user_id, first_name, last_name, email, username, roles):
    user = get_user_by_id(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.username = username
    user.roles = roles

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


def user_is_admin(email):
    response = False
    user = get_user_by_email(email)
    for rol in user.roles:
        if rol.name == "Admin":
            response = True
    return response


def user_set_status(username):
    user = get_user_by_username(username)
    user.is_active = not user.is_active
    db.session.commit()

    return True


def does_user_has_permission(user, in_permission):
    user = get_user_by_email(user)
    response = False
    for rol in user.roles:
        for permission in rol.permissions:
            if permission.name == in_permission:
                response = True
    return response


def is_active(user):
    return get_user_by_email(user).is_active


# APIs
def user_json(user, user_roles):
    return {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_active': user.is_active,
        'roles': user_roles
    }
