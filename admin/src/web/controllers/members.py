from flask import Blueprint
from flask import render_template

from src.web.helpers.auth import login_required

member_blueprint = Blueprint("members", __name__, url_prefix="/members")


@member_blueprint.get("/")
@login_required
def member_index():
    return render_template("members/index.html")
