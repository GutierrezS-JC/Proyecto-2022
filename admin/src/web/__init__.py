from flask import Flask

from .config import config

from .controllers.home import home_blueprint
from .controllers.login import login_blueprint
from src.web.controllers.users import user_blueprint
from src.web.controllers.config import config_blueprint
from src.web.controllers.asociados import asociado_blueprint
from .controllers.disciplinas import disciplinas_blueprint

from src.web.helpers import handlers
from src.web.helpers import auth

from src.core import database
from src.core import seeds


from flask_session import Session


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    # Load config
    app.config.from_object(config[env])

    # Config session backend
    Session(app)

    # Init database
    database.init_app(app)

    # Register blueprints and handlers
    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(config_blueprint)

    app.register_blueprint(asociado_blueprint)
    app.register_blueprint(disciplinas_blueprint)

    app.register_error_handler(401, handlers.unauthorized_error)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    # Global Jinja
    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seeds")
    def seedsdb():
        seeds.run()

    return app
