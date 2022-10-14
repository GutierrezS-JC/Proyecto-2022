from src.core.database import db
from src.core.board.permission import Permission
from src.core.board.rol import Rol
from src.core.board.config import Config
from src.core.board.member import Member

# def assign_user(issue, user):
#     issue.user = user
#     db.session.add(issue)
#     db.session.commit()
#
#     return issue


# Rol methods
def get_rol_by_id(rol_id):
    return Rol.query.get(rol_id)


def get_roles():
    return Rol.query.all()


def create_rol(**kwargs):
    rol = Rol(**kwargs)
    db.session.add(rol)
    db.session.commit()

    return rol


def assign_permissions(rol, permissions):
    rol.permissions.extend(permissions)
    db.session.add(rol)
    db.session.commit()

    return rol


# Permission methods
def create_permission(**kwargs):
    permission = Permission(**kwargs)
    db.session.add(permission)
    db.session.commit()

    return permission


# Configuration methods
def create_configuration(**kwargs):
    config = Config(**kwargs)
    db.session.add(config)
    db.session.commit()

    return config


def update_configuration(**kwargs):
    config = Config.query.get(1)
    for key, value in kwargs:
        setattr(config, key, value)


def get_configuration():
    config = Config.query.get(1)

    return config


# Members (Socios) methods
def list_members():
    return Member.query.all()


# APIs
def rol_json(rol):
    return {
        'id': rol.id,
        'name': rol.name
    }
