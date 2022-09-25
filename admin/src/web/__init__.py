from flask import Flask

from .config import config
from .controllers.home import home_blueprint
from .controllers.login import login_blueprint
from .controllers.issues import issue_blueprint

from src.web.helpers import handlers
from ..core import database


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    database.init_app(app)

    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(issue_blueprint)

    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()
    return app

