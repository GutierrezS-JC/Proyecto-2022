from flask import Blueprint, request
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
