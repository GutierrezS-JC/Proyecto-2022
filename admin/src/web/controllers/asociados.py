from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import session

from src.web.helpers.auth import login_required

asociado_blueprint = Blueprint("asociados", __name__, url_prefix="/asociados")


@asociado_blueprint.get("/")
@login_required
def asociado_index():
    return render_template("asociados/index.html")
