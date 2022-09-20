from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.get("/")
def home_index():
    if session:
        return render_template("home.html")
    else:
        return redirect(url_for("login.login_index"))
