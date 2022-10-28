from flask import Blueprint, jsonify
from flask import make_response

from src.core import models

club_api_blueprint = Blueprint("club_api", __name__, url_prefix="/api/club")


@club_api_blueprint.get('/disciplines')
def get_disciplines_data():
    disciplines_data = models.get_all_disciplines()
    result = []
    for discipline in disciplines_data:
        result.append(models.club_discipline_json(discipline))

    response = make_response(jsonify(result), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@club_api_blueprint.get('/info')
def get_club_data():
    club_data = models.get_club_data()
    res_json = models.club_data_json(club_data[0], club_data[1])

    response = make_response(jsonify(res_json), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
