"""Initialize app."""

from flask import Flask
from flask_assets import Environment
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
session = Session()
assets = Environment()


def create_app():
    """Construct the core flask_session_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    session.init_app(app)
    assets.init_app(app)

    with app.app_context():
        from . import auth, routes
        from .assets import compile_javascript, compile_stylesheets

        app.register_blueprint(routes.main_blueprint)
        app.register_blueprint(auth.auth_blueprint)

        # Create static asset bundles
        compile_stylesheets(assets)
        compile_javascript(assets)

        # Create Database Models
        db.create_all()

        return app
