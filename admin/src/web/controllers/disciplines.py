from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

from src.web.helpers.auth import login_required

disciplines_blueprint = Blueprint("disciplines", __name__, url_prefix="/disciplinas")


@disciplines_blueprint.get("/")
@login_required
def disciplines_index():
    return render_template("disciplines/index.html")
