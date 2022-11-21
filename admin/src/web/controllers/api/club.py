from flask import Blueprint, jsonify
from flask import make_response

from src.core import models

club_api_blueprint = Blueprint("club_api", __name__, url_prefix="/api/club")


# Aux sort
def sort_func(e):
    return len(e['details'])


@club_api_blueprint.get('/disciplines')
def get_disciplines_data():
    """ Obtiene todas las disciplinas que se realizan en el club"""

    disciplines_data = models.get_all_disciplines_group()
    result = []
    details = []
    index = 0
    actual = None
    ant = None

    if len(disciplines_data) > 1:
        actual = disciplines_data[0].name
        ant = disciplines_data[0].name

    while index < len(disciplines_data):
        actual = disciplines_data[index].name

        if actual != ant:
            result.append(models.club_discipline_group_json(ant, details))
            details = []

        obj = {
            'category': disciplines_data[index].category,
            'days_hours': disciplines_data[index].days_hours,
            'id': disciplines_data[index].id,
            'monthly_fee': disciplines_data[index].monthly_fee,
            'teachers': disciplines_data[index].instructors
        }

        details.append(obj)
        ant = actual
        index += 1

    result.append(models.club_discipline_group_json(ant, details))
    # for discipline in disciplines_data:
    #     print(discipline.name)
    #     result.append(models.club_discipline_json(discipline))

    result.sort(reverse=True, key=sort_func)
    response = make_response(jsonify(result), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@club_api_blueprint.get('/info')
def get_club_data():
    """ Obtiene la informacion relacionada al club con respecto al telefono y email """

    club_data = models.get_club_data()
    res_json = models.club_data_json(club_data[0], club_data[1])

    response = make_response(jsonify(res_json), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
