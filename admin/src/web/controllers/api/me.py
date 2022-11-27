import datetime
import os

from flask import Blueprint, jsonify, request, abort, url_for, current_app
from flask import make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.core import models
from src.web.helpers.handlers import error_json
from werkzeug.utils import secure_filename

# from admin.app import app
from core import auth

me_api_blueprint = Blueprint("me_api", __name__, url_prefix="/api/me")


@me_api_blueprint.get('/disciplines')
def get_disciplines_data():
    """Obtiene la lista de las disciplinas a las que está inscripto el usuario autentificado
     (Recibido por Authorization)"""

    member_req = request.headers.get('Authorization')
    searched_member = models.get_member_by_id(member_req)
    if searched_member:
        member_disciplines = models.get_members_disciplines(searched_member)
        result = []
        for member_discipline in member_disciplines:
            result.append(models.club_discipline_json(member_discipline))

        response = make_response(jsonify(result), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        res_abort = error_json("404 Not Found Error", "Usuario no encontrado")
        response = make_response(jsonify(res_abort), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


@me_api_blueprint.get('/payments')
def get_member_payments():
    """Obtiene la lista de pagos registrados (pagados) del usuario autentificado (Recibido por Authorization)"""

    member_req = request.headers.get('Authorization')
    searched_member = models.get_member_by_id(member_req)
    if searched_member:
        result = []
        for fee in searched_member.fees:
            if fee.was_paid:
                result.append(models.me_payment_json(fee.month, fee.receipt.total_amount))

        response = make_response(jsonify(result), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        res_abort = error_json("404 Not Found Error", "Usuario no encontrado")
        response = make_response(jsonify(res_abort), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


@me_api_blueprint.get('/payments/complete')
@jwt_required()
def get_member_payments_complete():
    """Obtiene la lista de pagos (completo) del usuario autentificado"""

    current_user = get_jwt_identity()
    member = auth.get_member_by_id(current_user)
    if member:
        paid = []
        not_paid = []
        for fee in member.fees:
            if fee.was_paid:
                paid.append(models.me_payment_new_json(fee.year, fee.month, fee.receipt.total_amount, fee.date_paid,
                                                       member.first_name, member.last_name))
            else:
                not_paid.append(models.me_payment_new_json(fee.year, fee.month, fee.total, fee.date_paid,
                                                           member.first_name, member.last_name))

        response = make_response(jsonify({'fees_paid': paid, 'fees_not_paid': not_paid}), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        res_abort = error_json("404 Not Found Error", "Usuario no encontrado")
        response = make_response(jsonify(res_abort), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


@me_api_blueprint.post('/payments')
@jwt_required()
def post_member_payments():
    """Registra un nuevo pago para el usuario autentificado (recibido por Authorization)"""

    current_user = get_jwt_identity()
    member_searched = auth.get_member_by_id(current_user)
    if member_searched:
        req_data = request.get_json()
        result_json = []

        result_fees = models.get_fees_not_paid_with_month_year(member_searched.id, req_data["month"],
                                                               req_data["year"])
        if result_fees:
            for fee in result_fees:
                result = models.register_fee_as_paid(fee)

                member_full_name = f"{member_searched.first_name} {member_searched.last_name}"
                month_description = models.format_month_description(int(fee.month), fee.year)
                total_amount_description = models.format_amount_description(result)

                new_receipt = models.create_receipt(member_full_name=member_full_name,
                                                    total_amount_description=total_amount_description,
                                                    total_amount=result, month_description=month_description,
                                                    fee_id=fee.id)

                archived_disciplines = models.create_receipt_disciplines(member_searched.disciplines, new_receipt.id)
                models.add_archived_disciplines_to_receipt(new_receipt, archived_disciplines)

                result_json.append(models.me_payment_json(fee.month, new_receipt.total_amount))
        response = make_response(jsonify(result_json), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        res_abort = error_json("404 Not Found Error", "Usuario no encontrado")
        response = make_response(jsonify(res_abort), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


@me_api_blueprint.post('/payments/file')
@jwt_required()
def post_member_payments_file():
    """Registra un nuevo pago FILE INPUT para el usuario autentificado (recibido por Authorization)"""
    file = request.files['file']
    current_user = get_jwt_identity()
    member_searched = auth.get_member_by_id(current_user)
    if member_searched:
        if request.files['file']:
            fee_paid = models.get_last_updated_fee(current_user)
            file.filename = f"Comprobante_{member_searched.doc_num}_{fee_paid.month}_{fee_paid.year}"
            # path = os.path.join(current_app.root_path, 'files')
            # print(os.path.join(current_app.root_path, 'files'))
            file.save(secure_filename(file.filename))

            response = make_response(jsonify({'status': 'Ok'}), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
    else:
        res_abort = error_json("404 Not Found Error", "Usuario no encontrado")
        response = make_response(jsonify(res_abort), 404)
        response.headers['Content-Type'] = 'application/json'
        return response
