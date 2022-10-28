import datetime

import pdfkit
from flask import Blueprint, request, url_for, redirect, flash, make_response
from flask import render_template

from src.core import models

from src.web.helpers.auth import login_required

from src.web.helpers import permissions

from src.web.helpers.forms import PaymentSearchForm

payment_blueprint = Blueprint("payment", __name__, url_prefix="/payment")


@payment_blueprint.get("/listado")
@login_required
def payment_index():
    permissions.validate_permissions('payment_index')

    page = request.args.get('page', 1, type=int)
    per_page = models.get_configuration()

    input_search = request.args.get('input_search', '', type=str)

    if input_search == '' or input_search.isspace():
        pagination = models.list_payment_records(page=page, per_page=per_page.elements_quantity)
    else:
        pagination = models.list_payment_records_input(input_search, page=page, per_page=per_page.elements_quantity)
    search_form = PaymentSearchForm()
    search_form.input_search.data = input_search
    current_date = datetime.date.today()
    return render_template("payment/index.html", search_form=search_form, pagination=pagination,
                           current_date=current_date)


@payment_blueprint.route("/registrar_pago_efectivo/<fee_id>")
@login_required
def payment_register_paid(fee_id):
    permissions.validate_permissions('payment_update')

    fee = models.get_fee_by_id(fee_id)
    config_extra = models.get_configuration().extra_charge

    if not fee.was_paid:
        result = models.register_fee_as_paid(fee)

        # Creamos el comprobante para su posterior descarga
        member_searched = models.get_member_by_id(fee.member_id)

        member_full_name = f"{member_searched.first_name} {member_searched.last_name}"
        month_description = models.format_month_description(int(fee.month), fee.year)
        total_amount_description = models.format_amount_description(result)

        new_receipt = models.create_receipt(member_full_name=member_full_name,
                                            total_amount_description=total_amount_description,
                                            total_amount=result, month_description=month_description, fee_id=fee.id)

        archived_disciplines = models.create_receipt_disciplines(member_searched.disciplines, new_receipt.id)
        models.add_archived_disciplines_to_receipt(new_receipt, archived_disciplines)

        flash(f'Se registro el pago de la cuota con un recargo del {config_extra}% (Total: {result})', 'success')
    else:
        flash('La cuota ya fue registrada como pagada', 'danger')
    page = request.args.get('page', 1, type=int)
    input_search = request.args.get('input_search', '', type=str)

    return redirect(url_for("payment.payment_index", page=page, input_search=input_search))


# PDF
@payment_blueprint.route('download/comprobante/pdf/<fee_id>')
@login_required
def download_receipt_pdf(fee_id):
    permissions.validate_permissions('payment_show')

    fecha = datetime.date.today().strftime('%d-%m-%Y')
    file_name = f"Comprobante_cuota_{fecha}.pdf"

    fee_searched = models.get_fee_by_id(fee_id)

    receipt = fee_searched.receipt

    config = models.get_configuration()
    due_date = f"{fee_searched.year}-{fee_searched.month}"

    rendered = render_template('pdf/receipt.html', receipt=receipt, config=config, due_date=due_date,
                               was_expired=fee_searched.was_expired)
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename={file_name}'

    return response
