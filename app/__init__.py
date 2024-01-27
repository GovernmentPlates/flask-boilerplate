from flask import Flask, abort
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .modules.util.config import eval_bool_env_var

db = SQLAlchemy()
login = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)
    login.login_view = "auth.login"

    from app.main import main as main

    app.register_blueprint(main)

    from app.auth import auth as auth

    app.register_blueprint(auth)

    from app import errors

    app.register_blueprint(errors.error)

    @app.before_request
    def maintenance_mode():
        # If maintenance mode is enabled, return a 503
        if eval_bool_env_var(app.config["MAINTENANCE_MODE"]):
            abort(503)

    return app
