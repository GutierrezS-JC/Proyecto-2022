from flask import Blueprint, redirect, url_for, flash, jsonify, request, abort
from flask import make_response

from core import board


me_api_blueprint = Blueprint("me_api", __name__, url_prefix="/api/me")


@me_api_blueprint.get('/disciplines')
def get_disciplines_data():
    member_req = request.headers.get('Authorization')
    searched_member = board.get_member_by_id(member_req)
    if searched_member:
        member_disciplines = board.get_members_disciplines(searched_member)
        result = []
        for member_discipline in member_disciplines:
            result.append(board.club_discipline_json(member_discipline))

        response = make_response(jsonify(result), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        abort(404)
