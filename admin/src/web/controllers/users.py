from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

from src.web.helpers.auth import login_required

user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.get("/")
@login_required
def user_index():
    return render_template("users/index.html")


@user_blueprint.get("/listado")
@login_required
def user_list_all():
    return render_template("users/listado.html")
