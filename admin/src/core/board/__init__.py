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


def get_member_by_email(email):
    return Member.query.filter_by(email=email).first()


def get_member_by_doc_num(doc_num):
    return Member.query.filter_by(doc_num=doc_num).first()


def get_last_member_num():
    return db.engine.execute("SELECT * FROM members WHERE id IN (SELECT MAX(id) FROM members)").first()


def get_member_by_id(member_id):
    return Member.query.filter_by(id=member_id).first()


def create_member(**kwargs):
    member = Member(**kwargs)
    db.session.add(member)
    db.session.commit()

    return member


# APIs
def rol_json(rol):
    return {
        'id': rol.id,
        'name': rol.name
    }


def member_json(member):
    print(member.is_active)
    return {
        'id': member.id,
        'first_name': member.first_name,
        'last_name': member.last_name,
        'genre': member.genre,
        'address': member.address,
        'is_active': member.is_active,
        'phone_num': member.phone_num,
        'email': member.email
    }
