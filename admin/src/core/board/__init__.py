from src.core.database import db
from src.core.board.permission import Permission
from src.core.board.rol import Rol
from src.core.board.config import Config
from src.core.board.member import Member
from src.core.board.disciplines import Discipline
from src.core.board.fee import Fee


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
def all_paginated(page=1, per_page=10):
    return Member.query.order_by(Member.member_num.asc()).paginate(page=page, per_page=per_page, error_out=False)


def list_members_with_last_name(last_name, page, per_page):
    return Member.query.filter(Member.last_name.ilike(f'%{last_name}%')).paginate(page=page, per_page=per_page,
                                                                                  error_out=False)


def list_members_with_last_name_status(last_name, status, page, per_page):
    return Member.query.filter(Member.last_name.ilike(f'%{last_name}%'), Member.is_active == status) \
        .paginate(page=page, per_page=per_page, error_out=False)


def list_members_with_status(status, page, per_page):
    return Member.query.filter(Member.is_active == status).paginate(page=page, per_page=per_page, error_out=False)


def get_member_by_email(email):
    return Member.query.filter_by(email=email).first()


def get_member_by_doc_num(doc_num):
    return Member.query.filter_by(doc_num=doc_num).first()


def get_last_member_num():
    return db.engine.execute("SELECT coalesce(member_num, '0') as member_num FROM members"
                             " WHERE id IN (SELECT MAX(id) FROM members)").first()


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


# Member Files
def get_list_members_with_last_name(last_name):
    return Member.query.filter(Member.last_name.ilike(f'%{last_name}%'))


def get_list_members_with_last_name_status(last_name, status):
    return Member.query.filter(Member.last_name.ilike(f'%{last_name}%'), Member.is_active == status)


def get_all_members():
    return Member.query.order_by(Member.member_num).all()


def get_list_members_with_status(status):
    return Member.query.filter(Member.is_active == status)


# Discipline methods
def create_discipline(**kwargs):
    discipline = Discipline(**kwargs)
    db.session.add(discipline)
    db.session.commit()

    return discipline


def discipline_edit(discipline_id, name, category, instructors, days_hours, monthly_fee, is_active):
    discipline = get_discipline_by_id(discipline_id)

    discipline.name = name
    discipline.category = category
    discipline.instructors = instructors
    discipline.days_hours = days_hours
    discipline.monthly_fee = monthly_fee
    discipline.is_active = is_active

    db.session.add(discipline)
    db.session.commit()

    return discipline


def list_disciplines_with_name(discipline, page, per_page):
    return Discipline.query.filter(Discipline.name.ilike(f'%{discipline}%')).paginate(page=page, per_page=per_page,
                                                                                      error_out=False)


def list_disciplines_with_name_status(discipline, status, page, per_page):
    return Discipline.query.filter(Discipline.name.ilike(f'%{discipline}%'), Discipline.is_active == status) \
        .paginate(page=page, per_page=per_page, error_out=False)


def list_disciplines_paginated(page, per_page):
    return Discipline.query.order_by(Discipline.id.asc()).paginate(page=page, per_page=per_page, error_out=False)


def list_disciplines_with_status(status, page, per_page):
    return Discipline.query.filter(Discipline.is_active == status).paginate(page=page, per_page=per_page,
                                                                            error_out=False)


def get_discipline_by_id(discipline_id):
    return Discipline.query.filter_by(id=discipline_id).first()


def get_members_for_discipline(name):
    return Member.query.filter(Member.first_name.ilike(f'%{name}%')).limit(10).all()


def discipline_add_member(discipline, member):
    res = discipline.members.append(member)
    db.session.commit()
    return res


def does_discipline_includes_member(discipline, member):
    return member in discipline.members


# Payment (Fee) methods
def list_payment_records(page, per_page):
    return Fee.query.order_by(Fee.id.desc()).paginate(page=page, per_page=per_page, error_out=False)


def list_payment_records_input(input_search, page, per_page):
    return Member.query.filter(Member.last_name.ilike(f'%{input_search}%')).paginate(page=page, per_page=per_page,
                                                                                     error_out=False)


# CLUB
def get_all_disciplines():
    return Discipline.query.all()


def get_club_data():
    return Config.query.with_entities(Config.email, Config.phone).first()


# ME (Member API)
def get_members_disciplines(searched_member):
    return searched_member.disciplines


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
        'email': member.email,
        'doc_num': member.doc_num
    }


def discipline_json(discipline):
    return {
        'id': discipline.id,
        'name': discipline.name,
        'category': discipline.category,
        'instructors': discipline.instructors,
        'days_hours': discipline.days_hours,
        'monthly_fee': discipline.monthly_fee,
        'is_active': discipline.is_active
    }


def club_data_json(email, phone):
    return {
        'email': email,
        'phone': phone
    }


def club_discipline_json(discipline):
    return {
        'name': discipline.name,
        'days_hours': discipline.days_hours,
        'teachers': discipline.instructors
    }
