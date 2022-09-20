from flask import Blueprint
from flask import render_template

# noinspection PyUnresolvedReferences
from src.core import board

issue_blueprint = Blueprint("issues", __name__, url_prefix="/consultas")


@issue_blueprint.get("/")
def issue_index():
    issues = board.list_issues()
    return render_template("issues/index.html", issues=issues)
