from datetime import datetime

from flask import Blueprint, flash, redirect, url_for, jsonify, request, Response, make_response
from flask import render_template

import io
import csv
import pdfkit
from passlib.handlers.sha2_crypt import sha256_crypt

from src.core import models

from src.web.helpers import permissions
from src.web.helpers.forms import MemberForm
from src.web.helpers.forms import EditMemberForm
from src.web.helpers.auth import login_required

from src.web.helpers.forms import SearchMemberForm

member_blueprint = Blueprint("members", __name__, url_prefix="/members")


@member_blueprint.get("/listado")
@login_required
def member_index():
    """Metodo encargado de devolver el template de la vista principal del modulo de socios (members)"""

    permissions.validate_permissions('member_index')

    page = request.args.get('page', 1, type=int)
    per_page = models.get_configuration()

    last_name = request.args.get('apellido', '')
    status = request.args.get('status', '', type=str)

    if last_name:
        if status == '2':
            pagination = models.list_members_with_last_name(last_name, page, per_page=per_page.elements_quantity)
        else:
            pagination = models.list_members_with_last_name_status(last_name, status, page,
                                                                   per_page=per_page.elements_quantity)
    else:
        if status == '2':
            pagination = models.all_paginated(page, per_page=per_page.elements_quantity)
        else:
            pagination = models.list_members_with_status(status, page, per_page=per_page.elements_quantity)

    form = MemberForm()
    edit_form = EditMemberForm()
    search_form = SearchMemberForm()
    search_form.last_name.data = last_name
    search_form.is_active_search.data = status

    return render_template("members/index.html", form=form, edit_form=edit_form, search_form=search_form,
                           pagination=pagination)


@member_blueprint.post("/cargar")
@login_required
def member_create():
    """Metodo encargado de la creacion de un socio"""

    permissions.validate_permissions('member_new')

    form = MemberForm()
    if form.validate_on_submit():

        if form["email"].data:
            if form.email.data.isspace():
                flash("Por favor, ingresa una direccion de email valida")
                return redirect(url_for("members.member_index"))
            if models.get_member_by_email(form["email"].data):
                flash("Error. El email ingresado ya se encuentra registrado", "danger")
                return redirect(url_for("members.member_index"))
        if form.phone_num.data:
            if form.phone_num.data.isspace():
                flash("Por favor, ingresa un numero de telefono valido", "danger")
                return redirect(url_for("members.member_index"))

        if models.get_member_by_doc_num(form["doc_num"].data):
            flash("Error. El numero de documento ya se encuentra registrado", "danger")
        else:
            member_num_db = models.get_last_member_num()

            password = sha256_crypt.encrypt("123socio321")
            member_reg = 1 if member_num_db is None else (int(member_num_db.member_num) + 1)
            models.create_member(
                first_name=form["first_name"].data,
                last_name=form["last_name"].data,
                doc_type=form["doc_type"].data,
                doc_num=form["doc_num"].data,
                genre=form["genre"].data,
                member_num=member_reg,
                address=form["address"].data,
                is_active=True if form["is_active"].data == "1" else False,
                phone_num=form["phone_num"].data if form["phone_num"].data else None,
                email=form["email"].data if form["email"].data else None,
                password=password
            )
            flash("Socio creado exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    page = request.args.get('page', 1, type=int)
    apellido = request.args.get('apellido', '')
    status = request.args.get('status', '0', type=str)

    return redirect(url_for("members.member_index", page=page, apellido=apellido, status=status))


@member_blueprint.post("/editar_socio")
@login_required
def member_edit():
    """Metodo encargado de la edicion de un socio"""

    permissions.validate_permissions('member_update')

    form = EditMemberForm()
    if form.validate_on_submit():
        member = models.member_edit(member_id=form.member_id_edit.data, first_name=form.first_name_edit.data,
                                    last_name=form.last_name_edit.data, genre=form.genre_edit.data,
                                    address=form.address_edit.data,
                                    is_active=True if form["is_active_edit"].data == "1" else False,
                                    phone_num=form["phone_num_edit"].data if form["phone_num_edit"].data else None,
                                    email=form["email_edit"].data if form["email_edit"].data else None)
        flash("Socio editado exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    page = request.args.get('page', 1, type=int)
    apellido = request.args.get('apellido', '')
    status = request.args.get('status', '0', type=str)

    return redirect(url_for("members.member_index", page=page, apellido=apellido, status=status))


# CSV
@member_blueprint.route('download/report/csv')
@login_required
def download_report_csv():
    """Metodo encargado de generar un archivo CSV con la informacion de los socios
    de acuerdo a un criterio de busqueda dado por si incluye o no el apellido
    y un estado (todos - actvio - inactivo)"""

    permissions.validate_permissions('member_index')

    last_name = request.args.get('apellido', '')
    status = request.args.get('status', '', type=str)

    name_file = f"ListadoSocios_{datetime.today().strftime('%d-%m-%Y')}.csv"

    output = io.StringIO()
    writer = csv.writer(output)

    line = ['Id socio', 'Nombre', 'Apellido', 'Nro documento', 'Genero', 'Direccion', 'Email']
    writer.writerow(line)

    if last_name:
        if status == '2':
            result = models.get_list_members_with_last_name(last_name)
        else:
            result = models.get_list_members_with_last_name_status(last_name, status)
    else:
        if status == '2':
            result = models.get_all_members()
        else:
            result = models.get_list_members_with_status(status)

    for row in result:
        if row.genre == 1:
            row.genre = 'M'
        elif row.genre == 2:
            row.genre = 'F'
        else:
            row.genre = 'X'
        line = [str(row.member_num), row.first_name, row.last_name, row.doc_num, str(row.genre), row.address, row.email]
        writer.writerow(line)
    output.seek(0)
    return Response(output, mimetype="text/csv", headers={'Content-Disposition': f'attachment; filename={name_file}'})


# PDF
@member_blueprint.route('download/report/pdf')
@login_required
def download_report_pdf():
    """Metodo encargado de generar un archivo PDF con la informacion de los socios
    de acuerdo a un criterio de busqueda dado por si incluye o no el apellido
    y un estado (todos - actvio - inactivo)"""

    permissions.validate_permissions('member_index')

    last_name = request.args.get('apellido', '')
    status = request.args.get('status', '', type=str)

    if last_name:
        if status == '2':
            result = models.get_list_members_with_last_name(last_name)
        else:
            result = models.get_list_members_with_last_name_status(last_name, status)
    else:
        if status == '2':
            result = models.get_all_members()
        else:
            result = models.get_list_members_with_status(status)

    fecha = datetime.today().strftime('%d-%m-%Y')
    file_name = f"Listado_Socios_{fecha}.pdf"

    rendered = render_template('pdf/index.html', list=result)
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename={file_name}'

    return response


# APIs de members (socios)
@member_blueprint.route("/api/member/<member_id>")
@login_required
def get_user(member_id):
    """Retorna json con informacion de socios que sera de utilidad
    para la consulta desde la vista, en particular fue pensado para la edicion"""

    member = models.get_member_by_id(member_id)
    if member is None:
        return jsonify({'message': 'El socio no existe'}), 404

    member_json = models.member_json(member)
    return jsonify({'member': member_json})
