"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
session = Session()


def create_app():
    """Construct the core flask_session_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    session.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .assets import compile_static_assets

        app.register_blueprint(routes.main_blueprint)
        app.register_blueprint(auth.auth_blueprint)

        # Create static asset bundles
        compile_static_assets(app)

        # Create Database Models
        db.create_all()

        return app
