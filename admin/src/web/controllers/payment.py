from flask import Blueprint, request, url_for, redirect, flash
from flask import render_template

from core import board

from src.web.helpers.auth import login_required

from src.web.helpers import permissions

from src.web.helpers.forms import PaymentSearchForm

payment_blueprint = Blueprint("payment", __name__, url_prefix="/payment")


@payment_blueprint.get("/listado")
@login_required
def payment_index():
    # Validar permisos
    permissions.validate_permissions('payment_index')

    # Paginacion
    page = request.args.get('page', 1, type=int)
    per_page = board.get_configuration()

    input_search = request.args.get('input_search', '', type=str)

    if input_search == '' or input_search.isspace():
        pagination = board.list_payment_records(page=page, per_page=per_page.elements_quantity)
    else:
        # Por ahora last_name falta el otro
        pagination = board.list_payment_records_input(input_search, page=page, per_page=per_page.elements_quantity)
    search_form = PaymentSearchForm()
    search_form.input_search.data = input_search

    return render_template("payment/index.html", search_form=search_form, pagination=pagination)


@payment_blueprint.route("/registrar_pago_efectivo/<fee_id>")
@login_required
def payment_register_paid(fee_id):
    # Validar permisos
    permissions.validate_permissions('payment_update')
    fee = board.get_fee_by_id(fee_id)

    if not fee.was_paid:
        board.register_fee_as_paid(fee)
        flash('Se registro el pago de la cuota correctamente', 'success')
    else:
        flash('La cuota ya fue registrada como pagada', 'danger')
    page = request.args.get('page', 1, type=int)
    input_search = request.args.get('input_search', '', type=str)

    return redirect(url_for("payment.payment_index", page=page, input_search=input_search))
