from flask import Blueprint
from flask import render_template

from src.web.helpers.auth import login_required

config_blueprint = Blueprint("config", __name__, url_prefix="/configuracion")


@config_blueprint.get("/")
@login_required
def config_index():
    return render_template("config/index.html")
