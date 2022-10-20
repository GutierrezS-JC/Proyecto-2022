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


def update_configuration(elements_quantity, payment_enabled, contact_information, payment_header,
                         monthly_fee, extra_charge):
    config = Config.query.get(1)

    config.elements_quantity = elements_quantity
    config.payment_enabled = payment_enabled
    config.contact_information = contact_information
    config.payment_header = payment_header
    config.monthly_fee = monthly_fee
    config.extra_charge = extra_charge

    db.session.add(config)
    db.session.commit()
    return config


def get_configuration():
    config = Config.query.get(1)

    return config


# Members (Socios) methods
def list_members():
    return Member.query.order_by(Member.member_num).all()


def all_paginated(page=1, per_page=10):
    return Member.query.order_by(Member.member_num.asc()).paginate(page=page, per_page=per_page)


def list_members_with_last_name(last_name, page, per_page):
    return Member.query.filter(Member.last_name.like(f'%{last_name}%')).paginate(page=page, per_page=per_page)


def list_members_with_last_name_status(last_name, status, page, per_page):
    return Member.query.filter(Member.last_name.like(f'%{last_name}%'), Member.is_active == status).paginate(page=page, per_page=per_page)


def list_members_with_status(status, page, per_page):
    return Member.query.filter(Member.is_active == status).paginate(page=page, per_page=per_page)


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


def member_edit(member_id, first_name, last_name, genre, address, is_active, phone_num, email):
    member = get_member_by_id(member_id)

    member.first_name = first_name
    member.last_name = last_name
    member.genre = genre
    member.address = address
    member.is_active = is_active
    member.phone_num = phone_num
    member.email = email

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
