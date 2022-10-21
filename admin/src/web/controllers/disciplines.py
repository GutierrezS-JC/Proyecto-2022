from flask import Blueprint, redirect, url_for, request
from flask import render_template
from flask import session

from src.web.helpers.auth import login_required

from core import board
from src.web.helpers.forms import DisciplineForm
from src.web.helpers.forms import EditDisciplineForm
from src.web.helpers.forms import SearchDisciplineForm

disciplines_blueprint = Blueprint("disciplines", __name__, url_prefix="/disciplinas")


@disciplines_blueprint.get("/listado")
@login_required
def disciplines_index():
    # Paginacion
    page = request.args.get('page', 1, type=int)
    per_page = board.get_configuration()

    discipline = request.args.get('disciplina', '')
    status = request.args.get('status', '', type=str)

    if discipline:
        if status == '2':
            pagination = board.list_disciplines_with_name(discipline, page, per_page=per_page.elements_quantity)
        else:
            pagination = board.list_disciplines_with_name_status(discipline, status, page,
                                                                 per_page=per_page.elements_quantity)
    else:
        if status == '2':
            pagination = board.list_disciplines_paginated(page, per_page=per_page.elements_quantity)
        else:
            pagination = board.list_us_with_status(status, page, per_page=per_page.elements_quantity)

    form = DisciplineForm
    edit_form = EditDisciplineForm()
    search_form = SearchDisciplineForm()
    search_form.is_active_search.data = status
    search_form.discipline_name.data = discipline

    return render_template("disciplines/index.html", form=form, edit_form=edit_form, search_form=search_form,
                           pagination=pagination)
