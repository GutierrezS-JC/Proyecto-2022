from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

user_blueprint = Blueprint("users", __name__, url_prefix="/users")


@user_blueprint.get("/")
def user_index():
    return render_template("users/index.html")
