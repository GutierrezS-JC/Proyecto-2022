from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    config_db(app)


def config_db(app):
    @app.before_first_request
    def init_database():
        """ Primer Request  que se haga en la app e intervenga la BD crea todas las tablas mapeadas con el ORM """
        db.create_all()

    @app.teardown_request
    def close_session(exception=None):
        """ Se termina un request de Flask. Hace un close de la sesion de BD """
        db.session.remove()


def reset_db():
    print("Eliminando BD...")
    db.drop_all()
    print("Creando BD...")
    db.create_all()
    print("Okay Makey")