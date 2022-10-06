from src.core.database import db
from src.core.board.permission import Permission
from src.core.board.rol import Rol
from src.core.board.config import Config


# def assign_user(issue, user):
#     issue.user = user
#     db.session.add(issue)
#     db.session.commit()
#
#     return issue
#
#
# def assign_labels(issue, labels):
#     issue.labels.extend(labels)
#     db.session.add(issue)
#     db.session.commit()
#
#     return issue

def get_rol_by_id(rol_id):
    return Rol.query.get(rol_id)


def create_rol(**kwargs):
    rol = Rol(**kwargs)
    db.session.add(rol)
    db.session.commit()

    return rol


def create_permission(**kwargs):
    permission = Permission(**kwargs)
    db.session.add(permission)
    db.session.commit()

    return permission


def assign_permissions(rol, permissions):
    rol.permissions.extend(permissions)
    db.session.add(rol)
    db.session.commit()

    return rol
