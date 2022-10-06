from datetime import datetime
from passlib.hash import sha256_crypt

from src.core import auth
from core import board


def run():

    password_hashed = sha256_crypt.encrypt("1234567aA")
    admin = auth.create_user(email="admin@gmail.com", username="Administrador", first_name="Root", last_name="Admin",
                             password=password_hashed, is_active=True, updated_at=datetime.now(),
                             inserted_at=datetime.now())

    rola_dmin = board.create_rol(name="Admin")
    rol_operador = board.create_rol(name="Operador")

    permission_member_index = board.create_permission(name="member_index")
    permission_member_new = board.create_permission(name="member_new")
    permission_member_destroy = board.create_permission(name="member_destroy")
    permission_member_update = board.create_permission(name="member_update")
    permission_member_show = board.create_permission(name="member_show")
