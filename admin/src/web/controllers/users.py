from flask import Blueprint, redirect, url_for, request, flash
from flask import render_template
from flask import session

from core import auth
from core import board

from src.web.helpers.forms import RegisterUserForm
from src.web.helpers.auth import login_required

user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.get("/")
@login_required
def user_index():
    form = RegisterUserForm()
    return render_template("users/index.html", form=form)


@user_blueprint.get("/listado")
@login_required
def user_list_all():
    users = auth.list_users()
    return render_template("users/listado.html", users=users, user_is_admin=auth.user_is_admin)


@user_blueprint.get("/cambiar_rol")
@login_required
def user_change_status(username):
    users = auth.list_users()
    auth.user_set_status(username)
    return render_template("users/listado.html", users=users, user_is_admin=auth.user_is_admin)


@user_blueprint.post("/cargar")
@login_required
def user_create():
    form = RegisterUserForm()

    if form.validate_on_submit():
        roles = []

        if auth.get_user_by_email(form["email"].data):
            flash("Error. El email ingresado ya se encuentra registrado", "danger")
        elif auth.get_user_by_username(form["username"].data):
            flash("Error. El nombre de usuario ya se encuentra registrado", "danger")
        else:
            for rol in form["roles"].data:
                rol_buscado = board.get_rol_by_id(rol)
                roles.append(rol_buscado)

            auth.create_user(
                email=form["email"].data,
                username=form["username"].data,
                first_name=form["first_name"].data,
                last_name=form["last_name"].data,
                password=form["password"].data,
                status=True if (form["status"].data == "1") else False,
                roles=roles
            )
            flash("Usuario creado exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return redirect(url_for("users.user_index"))
    # return render_template("users/index.html", form=form)
