from flask import Blueprint, redirect, url_for, request, flash
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
def discipline_index():
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

    form = DisciplineForm()
    edit_form = EditDisciplineForm()
    search_form = SearchDisciplineForm()
    search_form.is_active_search.data = status
    search_form.discipline_name.data = discipline

    return render_template("disciplines/index.html", form=form, edit_form=edit_form, search_form=search_form,
                           pagination=pagination)


@disciplines_blueprint.post("/cargar")
@login_required
def discipline_create():
    form = DisciplineForm()

    if form.validate_on_submit():

        board.create_discipline(
            name=form["name"].data,
            category=form["category"].data,
            instructors=form["instructors"].data,
            days_hours=form["days_hours"].data,
            monthly_fee=form["monthly_fee"].data,
            is_active=True if form["is_active"].data == "1" else False,
            is_deleted=False
        )
        flash("Disciplina creada exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    page = request.args.get('page', 1, type=int)
    discipline = request.args.get('disciplina', '')
    status = request.args.get('status', '0', type=str)

    return redirect(url_for("disciplines.discipline_index", page=page, discipline=discipline, status=status))
