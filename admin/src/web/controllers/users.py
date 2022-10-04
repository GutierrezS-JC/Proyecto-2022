from flask import Blueprint, redirect, url_for, request
from flask import render_template
from flask import session
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

    # for item in form:
    #     print(item)

    if form.validate_on_submit():
        roles = []
        # for rol in form.roles:
        #     print(rol)

        for item in form:
            print(item)
            print(item.data)

    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return render_template("users/index.html", form=form)
