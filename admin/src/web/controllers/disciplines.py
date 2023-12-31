from flask import Blueprint, redirect, url_for, request, flash, jsonify
from flask import render_template

from src.web.helpers.auth import login_required
from src.web.helpers import permissions

from src.core import models
from src.web.helpers.forms import DisciplineForm
from src.web.helpers.forms import EditDisciplineForm
from src.web.helpers.forms import SearchDisciplineForm
from src.web.helpers.forms import SearchMemberForDisciplineForm

disciplines_blueprint = Blueprint("disciplines", __name__, url_prefix="/disciplines")


@disciplines_blueprint.get("/listado")
@login_required
def discipline_index():
    """Metodo encargado de devolver el template de la vista principal del modulo de disciplinas"""

    permissions.validate_permissions('discipline_index')

    page = request.args.get('page', 1, type=int)
    per_page = models.get_configuration()
    discipline = request.args.get('disciplina', '')
    status = request.args.get('status', '2', type=str)

    if discipline:
        if status == '2':
            pagination = models.list_disciplines_with_name(discipline, page, per_page=per_page.elements_quantity)
        else:
            pagination = models.list_disciplines_with_name_status(discipline, status, page,
                                                                  per_page=per_page.elements_quantity)
    else:
        if status == '2':
            pagination = models.list_disciplines_paginated(page, per_page=per_page.elements_quantity)
        else:
            pagination = models.list_disciplines_with_status(status, page, per_page=per_page.elements_quantity)

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
    """Metodo encargado de la creacion de una disciplina"""

    permissions.validate_permissions('discipline_new')

    form = DisciplineForm()

    if form.validate_on_submit():

        models.create_discipline(
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


@disciplines_blueprint.post("/editar_disciplina")
@login_required
def discipline_edit():
    """Metodo encargado de la edicion de una disciplina"""

    permissions.validate_permissions('discipline_update')

    form = EditDisciplineForm()
    if form.validate_on_submit():
        old_discipline_value = int(models.get_discipline_by_id(form.discipline_id_edit.data).monthly_fee)
        discipline = models.discipline_edit(discipline_id=form.discipline_id_edit.data, name=form.name_edit.data,
                                            category=form.category_edit.data, instructors=form.instructors_edit.data,
                                            days_hours=form.days_hours_edit.data,
                                            monthly_fee=form.monthly_fee_edit.data,
                                            is_active=True if form["is_active_edit"].data == "1" else False)
        if old_discipline_value != int(discipline.monthly_fee):
            models.update_payments_after_current_month(discipline, old_discipline_value)

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
    """Metodo encargado de agregar un socio no moroso en una disciplina.
    Ademas, en caso de realizar exitosamente la asignacion anterior, se generan
    las cuotas a partir del mes siguiente al actual.
    """

    permissions.validate_permissions('discipline_update')

    page = request.args.get('page', 1, type=int)
    disciplina = request.args.get('apellido', '')
    status = request.args.get('status', '2', type=str)

    member_searched = models.get_member_by_doc_num(member_doc_num)
    discipline_searched = models.get_discipline_by_id(discipline_id)

    if member_searched and discipline_searched:
        if not discipline_searched.is_active:
            flash("La disciplina no se encuentra habilitada", 'danger')
        elif models.does_discipline_includes_member(discipline_searched, member_searched):
            flash('El socio ya se encuentra registrado en la disciplina', 'warning')
        elif models.member_is_currently_defaulted(member_searched):
            flash("El socio es moroso. Debe regularizar la situacion", 'danger')
        else:
            models.discipline_add_member(discipline_searched, member_searched)
            models.generate_payments(member_searched, discipline_searched)
            flash("El socio fue asignado en la disciplina correctamente", "success")
    else:
        flash('Por favor vuelva a intentarlo', 'danger')

    return redirect(url_for("disciplines.discipline_index", page=page, disciplina=disciplina, status=status))


# APIs de disciplina
@disciplines_blueprint.route("/api/discipline/<discipline_id>")
@login_required
def get_discipline(discipline_id):
    """Retorna json con informacion de disciplinas que sera de utilidad
    para la consulta desde la vista, en particular fue pensado para la edicion"""

    discipline = models.get_discipline_by_id(discipline_id)
    if discipline is None:
        return jsonify({'message': 'La disciplina no existe'}), 404

    discipline_json = models.discipline_json(discipline)
    return jsonify({'discipline': discipline_json})


@disciplines_blueprint.route("/api/members_discipline/<name>")
@login_required
def get_members_for_discipline(name):
    """Retorna json con informacion de los socios (members) que coinciden con
    el parametro <name> correspondiente a un string a buscar en el sistema.
    Esta pensado para utilizarse desde la vista mostrando el resultado
    de una busqueda de socios para agregarlos en una disciplina"""
    members = models.get_members_for_discipline(name)
    if members is None:
        return jsonify({'members_discipline': []})

    result = []
    for member in members:
        result.append(models.member_json(member))

    return jsonify({'members_discipline': result})
