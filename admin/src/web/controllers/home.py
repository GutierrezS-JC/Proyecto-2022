from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.get("/")
def home_index():
    return render_template("home.html")

