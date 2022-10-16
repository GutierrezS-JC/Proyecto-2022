from flask import Blueprint, flash, redirect, url_for, jsonify
from flask import render_template

from core import board

from src.web.helpers.forms import MemberForm
from src.web.helpers.forms import EditMemberForm
from src.web.helpers.auth import login_required

member_blueprint = Blueprint("members", __name__, url_prefix="/members")


@member_blueprint.get("/")
@login_required
def member_index():
    form = MemberForm()
    edit_form = EditMemberForm()
    members = board.list_members()
    return render_template("members/index.html", form=form, members=members, edit_form=edit_form)


@member_blueprint.post("/cargar")
@login_required
def member_create():
    form = MemberForm()

    if form.validate_on_submit():

        # Verificammos data opcional
        if form["email"].data:
            if form.email.data.isspace():
                flash("Por favor, ingresa una direccion de email valida")
                return redirect(url_for("members.member_index"))
            if board.get_member_by_email(form["email"].data):
                flash("Error. El email ingresado ya se encuentra registrado", "danger")
                return redirect(url_for("members.member_index"))
        if form.phone_num.data:
            if form.phone_num.data.isspace():
                flash("Por favor, ingresa un numero de telefono valido", "danger")
                return redirect(url_for("members.member_index"))

        if board.get_member_by_doc_num(form["doc_num"].data):
            flash("Error. El numero de documento ya se encuentra registrado", "danger")
        else:
            member_num_db = board.get_last_member_num()
            board.create_member(
                first_name=form["first_name"].data,
                last_name=form["last_name"].data,
                doc_type=form["doc_type"].data,
                doc_num=form["doc_num"].data,
                genre=form["genre"].data,
                member_num=member_num_db['id'] + 1,
                address=form["address"].data,
                is_active=True if form["is_active"].data == "1" else False,
                phone_num=form["phone_num"].data if form["phone_num"].data else None,
                email=form["email"].data if form["email"].data else None,
            )
            flash("Socio creado exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return redirect(url_for("members.member_index"))


@member_blueprint.post("/editar_socio")
@login_required
def member_edit():
    form = EditMemberForm()

    if form.validate_on_submit():
        member = board.member_edit(member_id=form.member_id_edit.data, first_name=form.first_name_edit.data,
                                   last_name=form.last_name_edit.data, genre=form.genre_edit.data,
                                   address=form.address_edit.data,
                                   is_active=True if form["is_active_edit"].data == "1" else False,
                                   phone_num=form.phone_num_edit.data, email=form.email_edit.data)
        flash("Socio editado exitosamente", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return redirect(url_for("members.member_index"))


# APIs de user
@member_blueprint.route("/api/member/<member_id>")
@login_required
def get_user(member_id):
    member = board.get_member_by_id(member_id)

    if member is None:
        return jsonify({'message': 'El socio no existe'}), 404

    member_json = board.member_json(member)
    return jsonify({'member': member_json})