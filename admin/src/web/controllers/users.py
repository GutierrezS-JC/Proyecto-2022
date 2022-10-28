from passlib.hash import sha256_crypt
from flask import Blueprint, redirect, url_for, request, flash, jsonify
from flask import render_template

from core import auth
from core import board

from src.web.helpers import permissions

from src.web.helpers.forms import RegisterUserForm
from src.web.helpers.forms import EditUserForm
from src.web.helpers.forms import SearchUserForm
from src.web.helpers.auth import login_required

user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.get("/")
@login_required
def user_index():
    # Validar permisos
    permissions.validate_permissions('user_new')

    form = RegisterUserForm()
    return render_template("users/index.html", form=form)


@user_blueprint.route("/listado")
@login_required
def user_list_all():

    # Validar permisos
    permissions.validate_permissions('user_index')

    page = request.args.get('page', 1, type=int)
    per_page = board.get_configuration()

    email = request.args.get('email', '')
    status = request.args.get('status', '2', type=str)

    if email:
        if status == '2':
            pagination = auth.list_users_with_email(email, page, per_page=per_page.elements_quantity)
        else:
            pagination = auth.list_users_with_email_status(email, status, page, per_page=per_page.elements_quantity)
    else:
        if status == '2':
            pagination = auth.list_users_paginated(page, per_page=per_page.elements_quantity)
        else:
            pagination = auth.list_users_with_status(status, page, per_page=per_page.elements_quantity)

    form = EditUserForm()
    search_form = SearchUserForm()
    search_form.is_active_search.data = status
    search_form.email.data = email
    return render_template("users/listado.html", pagination=pagination, user_is_admin=auth.user_is_admin,
                           form=form, search_form=search_form)


@user_blueprint.route("/cambiar_rol/<username>")
@login_required
def user_change_status(username):

    permissions.validate_permissions('user_update')

    auth.user_set_status(username)
    page = request.args.get('page', 1, type=int)
    email = request.args.get('email', '')
    status = request.args.get('status', '', type=str)
    return redirect(url_for('users.user_list_all', page=page, email=email, status=status))


@user_blueprint.route("/eliminar_usuario/<user_id>")
@login_required
def user_delete(user_id):

    permissions.validate_permissions('user_destroy')

    auth.delete_user(user_id)
    page = request.args.get('page', 1, type=int)
    email = request.args.get('email', '')
    status = request.args.get('status', '2', type=str)

    return redirect(url_for('users.user_list_all', page=page, email=email, status=status))




@user_blueprint.post("/cargar")
@login_required
def user_create():

    permissions.validate_permissions('user_new')

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

            password = sha256_crypt.encrypt(form["password"].data)
            auth.create_user(
                email=form["email"].data,
                username=form["username"].data,
                first_name=form["first_name"].data,
                last_name=form["last_name"].data,
                password=password,
                is_active=True if form["status"].data == "1" else False,
                roles=roles
            )
            flash("Usuario creado exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return redirect(url_for("users.user_index"))


@user_blueprint.post("/editar_usuario")
@login_required
def user_edit():
    # Validar permisos
    permissions.validate_permissions('user_update')

    form = EditUserForm()
    form.roles.choices = [(rol.id, rol.name) for rol in board.get_roles()]

    page = request.args.get('page', 1, type=int)
    email = request.args.get('email', '')
    status = request.args.get('status', '0', type=str)

    if form.validate_on_submit():
        r_records = board.get_roles()
        accepted = []
        for rol in r_records:
            if rol.id in form.roles.data:
                accepted.append(rol)

        if not accepted:
            flash("Error. El usuario debe tener al menos un rol asignado", "danger")
            return redirect(url_for("users.user_list_all", page=page, email=email, status=status))

        user = auth.user_edit(user_id=form.user_id.data, first_name=form.first_name.data, last_name=form.last_name.data,
                              email=form.email.data, username=form.username.data, roles=accepted)
        flash("El usuario fue editado con exito", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return redirect(url_for('users.user_list_all', page=page, email=email, status=status))


@user_blueprint.route("/buscar_usuario", methods=["GET"])
@login_required
def user_search():
    # Validar permisos
    permissions.validate_permissions('user_index')

    page = request.args.get('page', 1, type=int)
    email = request.args.get('email', '')
    status = request.args.get('status', '')

    return redirect(url_for("users.user_list_all", page=page, email=email, status=status))


# APIs de user
@user_blueprint.route("/api/users/<user_id>")
@login_required
def get_user(user_id):
    user = auth.get_user_by_id(user_id)
    user_roles = []
    if user is None:
        return jsonify({'message': 'El usuario no existe'}), 404
    for rol in user.roles:
        user_roles.append(board.rol_json(rol))

    user_json = auth.user_json(user, user_roles)
    return jsonify({'user': user_json})
