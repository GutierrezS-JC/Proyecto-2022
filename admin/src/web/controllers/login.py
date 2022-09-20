from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

login_blueprint = Blueprint("login", __name__, url_prefix="/login")


@login_blueprint.get("/")
def login_index():
    if not session:
        return render_template("login/index.html")
    else:
        return redirect(url_for("home.home_index"))
