from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

from src.web.helpers.auth import login_required

disciplinas_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")


@disciplinas_blueprint.get("/")
@login_required
def disciplinas_index():
    return render_template("disciplinas/index.html")
