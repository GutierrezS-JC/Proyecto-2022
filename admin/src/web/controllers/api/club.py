import datetime

from flask import Blueprint, jsonify
from flask import make_response

from src.core import models

club_api_blueprint = Blueprint("club_api", __name__, url_prefix="/api/club")


# Aux sort
def sort_func(e):
    return len(e['details'])


# Aux disciplines by group
def parse_disciplines_group_by_name():
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
    return result


@club_api_blueprint.get('/disciplines')
def get_disciplines_data():
    """ Obtiene todas las disciplinas que se realizan en el club"""

    result = parse_disciplines_group_by_name()
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


@club_api_blueprint.get('/charts/members/disciplines/genre')
def get_members_with_disciplines_by_genre():
    """ Obtiene la participación en disciplinas con la cantidad de inscriptos por
        género (historico). Usamos el endpoint previamente creado (obtencion de disciplinas) para iterar
        por las disciplinas ya obtenidas"""

    result = []

    disciplines_data = []
    for discipline in parse_disciplines_group_by_name():
        disciplines_data.append(discipline['name'])

    for discipline in disciplines_data:
        query_result = models.get_members_with_disciplines_by_genre(discipline)
        obj = {
            'nombre_disciplina': discipline,
            'cant_inscriptos_hombres': query_result[0],
            'cant_inscriptos_mujeres': query_result[1],
            'cant_inscriptos_otros': query_result[2]
        }

        result.append(obj)

    response = make_response(jsonify(result), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@club_api_blueprint.get('/charts/members/disciplines/current_year')
def get_members_already_in_disciplines():
    """ Cantidad de personas inscriptas en una disciplina registrada el año actual.
        A diferencia del endpoint de abajo, este evalua unicamente aquellos socios que
        tienen una disciplina asociada"""

    current_year = datetime.date(datetime.date.today().year, 1, 1)
    next_year_limit = current_year.replace(current_year.year + 1, 1, 1)
    query_result = models.get_members_already_in_disciplines(current_year, next_year_limit)

    result = {
        'cant_male': query_result[0],
        'cant_female': query_result[1],
        'cant_others': query_result[2]
    }

    response = make_response(jsonify(result), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@club_api_blueprint.get('/charts/members/year/genre_alternative')
def get_members_by_year_total_and_genre_alternative():
    """ Obtiene la informacion relacionada al club con respecto a la
        cantidad de asociados registrados por cada año (en un rango 5 años hastaa fecha actual).
        Total y separado por genero """

    result = []
    for x in range(3):
        fecha_inicio = datetime.date((datetime.date.today().year - 5), 1, 1)
        fecha_sig = fecha_inicio.replace(fecha_inicio.year + 1, 1, 1)
        fecha_fin = datetime.date.today()
        arreglo_obj = []
        genre = x + 1

        while fecha_inicio < fecha_fin:
            members_years_genre = models.get_members_by_year_total_and_genre_alternative(fecha_inicio, fecha_sig, genre)
            arreglo_obj.append(members_years_genre[0])
            fecha_inicio = fecha_inicio.replace(fecha_inicio.year + 1, 1, 1)
            fecha_sig = fecha_sig.replace(fecha_inicio.year + 1, 1, 1)

        result.append(arreglo_obj)

    response = make_response(jsonify(result), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


# Metodo aux para las fechas usadas en las metricas
@club_api_blueprint.get('/charts/members/years_in_range')
def get_years_in_range():
    """ Obtiene los años contenidos dentro de un rango a partir de una fecha de inicio dada """

    fecha_inicio = datetime.date((datetime.date.today().year - 5), 1, 1)
    fecha_sig = fecha_inicio.replace(fecha_inicio.year + 1, 1, 1)
    fecha_fin = datetime.date.today()
    result = []

    while fecha_inicio < fecha_fin:
        result.append(fecha_inicio.year)
        fecha_inicio = fecha_inicio.replace(fecha_inicio.year + 1, 1, 1)
        fecha_sig = fecha_sig.replace(fecha_inicio.year + 1, 1, 1)

    response = make_response(jsonify(result), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@club_api_blueprint.get('/charts/members/year/genre')
def get_members_by_year_total_and_genre():
    """ Obtiene la informacion relacionada al club con respecto a la
        cantidad de asociados registrados por cada año (en un rango 5 años hastaa fecha actual).
        Total y separado por genero """

    fecha_inicio = datetime.date((datetime.date.today().year - 5), 1, 1)
    fecha_sig = fecha_inicio.replace(fecha_inicio.year + 1, 1, 1)
    fecha_fin = datetime.date.today()
    result = []
    while fecha_inicio < fecha_fin:
        members_years_genre = models.get_members_by_year_total_and_genre(fecha_inicio, fecha_sig)
        obj = {
            'year': fecha_inicio.year,
            'total': members_years_genre[0],
            'cant_men': members_years_genre[1],
            'cant_women': members_years_genre[2],
            'cant_another': members_years_genre[3]
        }
        result.append(obj)
        fecha_inicio = fecha_inicio.replace(fecha_inicio.year + 1, 1, 1)
        fecha_sig = fecha_sig.replace(fecha_inicio.year + 1, 1, 1)

    response = make_response(jsonify(result), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
