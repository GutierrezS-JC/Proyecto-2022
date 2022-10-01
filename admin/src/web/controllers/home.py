from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

from src.web.helpers import auth
from src.web.helpers.auth import login_required


home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.get("/")
@login_required
def home_index():
    return render_template("home.html")
