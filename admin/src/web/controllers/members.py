from flask import Blueprint, flash, redirect, url_for
from flask import render_template

from core import board

from src.web.helpers.forms import MemberForm
from src.web.helpers.auth import login_required

member_blueprint = Blueprint("members", __name__, url_prefix="/members")


@member_blueprint.get("/")
@login_required
def member_index():
    form = MemberForm()
    members = board.list_members()
    return render_template("members/index.html", form=form, members=members)


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
