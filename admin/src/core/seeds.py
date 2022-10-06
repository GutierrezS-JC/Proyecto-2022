from datetime import datetime
from passlib.hash import sha256_crypt

from core import auth
from core import board


def run():
    password_hashed = sha256_crypt.encrypt("1234567aA")
    admin = auth.create_user(email="admin@gmail.com", username="Administrador", first_name="Root", last_name="Admin",
                             password=password_hashed, is_active=True, updated_at=datetime.now(),
                             inserted_at=datetime.now())

    rol_admin = board.create_rol(name="Admin")
    rol_operador = board.create_rol(name="Operador")

    auth.assign_roles(admin, [rol_admin, rol_operador])

    permission_member_index = board.create_permission(name="member_index")
    permission_member_new = board.create_permission(name="member_new")
    permission_member_destroy = board.create_permission(name="member_destroy")
    permission_member_update = board.create_permission(name="member_update")
    permission_member_show = board.create_permission(name="member_show")

    board.assign_permissions(rol_admin, [permission_member_index, permission_member_new, permission_member_destroy,
                                         permission_member_update, permission_member_show])

    board.assign_permissions(rol_operador, [permission_member_index, permission_member_new, permission_member_show,
                                            permission_member_update])

    configuration = board.create_configuration(elements_quantity=10, payment_enabled=True,
                                               contact_information="All your base are belong to us",
                                               payment_header="Ay no c", monthly_fee=2500, extra_charge=25)
