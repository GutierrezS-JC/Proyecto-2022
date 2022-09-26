from flask import Blueprint
from flask import render_template

config_blueprint = Blueprint("config", __name__, url_prefix="/configuracion")


@config_blueprint.get("/")
def config_index():
    return render_template("config/index.html")
