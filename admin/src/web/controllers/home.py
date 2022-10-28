from flask import Blueprint
from flask import render_template

from src.web.helpers.auth import login_required


home_blueprint = Blueprint("home", __name__, url_prefix="/home")


@home_blueprint.get("/")
@login_required
def home_index():
    return render_template("home.html")
