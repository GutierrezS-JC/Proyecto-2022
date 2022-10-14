from flask import Blueprint
from flask import render_template

from core import board

from src.web.helpers.forms import ConfigForm
from src.web.helpers.auth import login_required

config_blueprint = Blueprint("config", __name__, url_prefix="/configuracion")


@config_blueprint.get("/")
@login_required
def config_index():
    config = board.get_configuration()
    form = ConfigForm()
    return render_template("config/index.html", config=config, form=form)
