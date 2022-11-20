from flask import Flask

from .config import config

from .controllers.home import home_blueprint
from .controllers.login import login_blueprint
from src.web.controllers.users import user_blueprint
from src.web.controllers.config import config_blueprint
from src.web.controllers.members import member_blueprint
from .controllers.disciplines import disciplines_blueprint
from src.web.controllers.payment import payment_blueprint


from src.web.controllers.api.club import club_api_blueprint
from src.web.controllers.api.me import me_api_blueprint

from src.web.helpers import handlers
from src.web.helpers import auth
from web.helpers.permissions import has_permission

from src.core import database
from src.core import seeds

from flask_session import Session
from flask_cors import CORS


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    # CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"} })

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

    app.register_blueprint(member_blueprint)
    app.register_blueprint(disciplines_blueprint)

    app.register_blueprint(payment_blueprint)

    app.register_error_handler(401, handlers.unauthorized_error)
    app.register_error_handler(403, handlers.forbidden_error)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    # API
    app.register_blueprint(club_api_blueprint)
    app.register_blueprint(me_api_blueprint)

    # Global Jinja
    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)
    app.jinja_env.globals.update(has_permission=has_permission)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seeds")
    def seedsdb():
        seeds.run()

    return app
