from flask import Blueprint, redirect, url_for, request
from flask import render_template
from flask import session

from core import auth

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
    return render_template("users/listado.html")


@user_blueprint.post("/cargar")
@login_required
def user_create():
    form = RegisterUserForm()

    if form.validate_on_submit():
        roles = []

        print(form["status"].data)
        print(form["roles"].data)
        auth.create_user(
            email=form["email"].data,
            username=form["username"].data,
            first_name=form["first_name"].data,
            last_name=form["last_name"].data,
            password=form["password"].data,
            status=True if form["status"].data == 1 else False,
            roles=roles
        )
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return render_template("users/index.html", form=form)
