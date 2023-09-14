"""App configuration."""
from os import environ, path, system

import redis
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")

    # Flask Config
    FLASK_APP = "main.py"
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")

    # Flask-Session
    REDIS_URI = environ.get("REDIS_URI")
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url(REDIS_URI)

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Flask-Assets (Optional)
    LESS_BIN = system("which lessc")
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")
