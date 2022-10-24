from flask import Blueprint, redirect, url_for, request, flash, jsonify
from flask import render_template
from flask import session

from src.web.helpers.auth import login_required
from src.web.helpers import permissions

from core import board
from src.web.helpers.forms import DisciplineForm
from src.web.helpers.forms import EditDisciplineForm
from src.web.helpers.forms import SearchDisciplineForm
from src.web.helpers.forms import SearchMemberForDisciplineForm

disciplines_blueprint = Blueprint("disciplines", __name__, url_prefix="/disciplines")


@disciplines_blueprint.get("/listado")
@login_required
def discipline_index():

    # Validar permisos
    permissions.validate_permissions('discipline_index')

    # Paginacion
    page = request.args.get('page', 1, type=int)
    per_page = board.get_configuration()

    discipline = request.args.get('disciplina', '')
    status = request.args.get('status', '2', type=str)

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
            pagination = board.list_disciplines_with_status(status, page, per_page=per_page.elements_quantity)

    search_member_form = SearchMemberForDisciplineForm()

    form = DisciplineForm()
    edit_form = EditDisciplineForm()
    search_form = SearchDisciplineForm()
    search_form.is_active_search.data = status
    search_form.discipline_name.data = discipline

    return render_template("disciplines/index.html", form=form, edit_form=edit_form, search_form=search_form,
                           search_member_form=search_member_form, pagination=pagination)


@disciplines_blueprint.post("/cargar")
@login_required
def discipline_create():
    # Validar permisos
    permissions.validate_permissions('discipline_new')

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


@disciplines_blueprint.route("/editar_socio")
@login_required
def discipline_edit():
    # Validar permisos
    permissions.validate_permissions('discipline_update')

    form = EditDisciplineForm()
    if form.validate_on_submit():
        member = board.discipline_edit(discipline_id=form.discipline_id_edit.data, name=form.name_edit.data,
                                       category=form.category_edit.data, instructors=form.instructors_edit.data,
                                       days_hours=form.days_hours_edit.data, monthly_fee=form.monthly_fee_edit.data,
                                       is_active=True if form["is_active_edit"].data == "1" else False)
        flash("Disciplina editada exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    page = request.args.get('page', 1, type=int)
    disciplina = request.args.get('apellido', '')
    status = request.args.get('status', '2', type=str)

    return redirect(url_for("disciplines.discipline_index", page=page, disciplina=disciplina, status=status))


@disciplines_blueprint.route("/agregar_socio_disciplina/<member_doc_num>/<discipline_id>")
@login_required
def discipline_add_member(member_doc_num, discipline_id):
    # Validar permisos
    permissions.validate_permissions('discipline_update')

    page = request.args.get('page', 1, type=int)
    disciplina = request.args.get('apellido', '')
    status = request.args.get('status', '2', type=str)

    member_searched = board.get_member_by_doc_num(member_doc_num)
    discipline_searched = board.get_discipline_by_id(discipline_id)

    if member_searched and discipline_searched:
        if not discipline_searched.is_active:
            flash("La disciplina no se encuentra habilitada", 'danger')
        elif board.does_discipline_includes_member(discipline_searched, member_searched):
            flash('El socio ya se encuentra registrado en la disciplina', 'warning')
        else:
            board.discipline_add_member(discipline_searched, member_searched)
            flash("El socio fue asignado en la disciplina correctamente", "success")
    else:
        flash('Por favor vuelva a intentarlo', 'danger')

    return redirect(url_for("disciplines.discipline_index", page=page, disciplina=disciplina, status=status))


# APIs de disciplina
@disciplines_blueprint.route("/api/discipline/<discipline_id>")
@login_required
def get_discipline(discipline_id):
    discipline = board.get_discipline_by_id(discipline_id)
    if discipline is None:
        return jsonify({'message': 'La disciplina no existe'}), 404

    discipline_json = board.discipline_json(discipline)
    return jsonify({'discipline': discipline_json})


@disciplines_blueprint.route("/api/members_discipline/<name>")
@login_required
def get_members_for_discipline(name):
    members = board.get_members_for_discipline(name)
    if members is None:
        return jsonify({'members_discipline': []})

    result = []
    for member in members:
        result.append(board.member_json(member))

    return jsonify({'members_discipline': result})
