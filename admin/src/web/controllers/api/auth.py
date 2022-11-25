from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, unset_jwt_cookies, \
    get_jwt_identity

from src.core import models
from src.web.helpers.handlers import error_json

from src.core import auth

auth_api_blueprint = Blueprint("auth_api", __name__, url_prefix="/api/auth")


@auth_api_blueprint.post('/login_jwt')
def login_jwt():
    data = request.get_json()
    email = data['email']
    password = data['password']
    member = auth.verify_login_doc_num(email, password)

    if member:
        access_token = create_access_token(identity=member.id)
        response = jsonify()
        set_access_cookies(response, access_token)
        return response, 201
    else:
        return jsonify(message='Unauthorized'), 401


@auth_api_blueprint.get('/logout_jwt')
@jwt_required()
def logout_jwt():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200


@auth_api_blueprint.get('/user_jwt')
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    member = auth.get_member_by_id(current_user)
    response = jsonify({'full_name': f"{member.first_name} {member.last_name}"})
    return response, 200
