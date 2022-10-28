from flask import session, abort

from src.core import auth


def user_is_active(user_email):
    return auth.is_active(user_email)


def validate_permissions(permission):
    if not user_is_active(session.get("user")):
        abort(403)
    if not permission.isspace() and not has_permission(permission):
        abort(403)
    return True


def has_permission(permission):
    return auth.does_user_has_permission(session.get("user"), permission)


def is_admin():
    if not auth.user_is_admin(session.get("user")):
        abort(403)
    return True
