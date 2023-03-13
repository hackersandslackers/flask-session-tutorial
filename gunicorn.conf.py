"""Gunicorn configuration file."""
from os import path, environ

BASE_DIR = path.abspath(path.dirname(__file__))

wsgi_app = "wsgi:app"
reload = False
ca_certs = environ.get("SQLALCHEMY_CA_CERTS")
processes = 2
threads = 2
socket = "flask.sock"
proc_name = "flask_session_tutorial"
bind = f"unix:///{BASE_DIR}/flask.sock"
virtualenv = f"{BASE_DIR}/.venv"
env = environ.get("ENVIRONMENT")

if env == "development":
    reload = True
