"""Compile static asset bundles."""

from flask import current_app as app
from flask_assets import Bundle, Environment


def compile_stylesheets(assets: Environment) -> Environment:
    """
    Generate CSS from .LESS source.

    :param Flask app: Top-level Flask application.
    """
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    account_stylesheet_bundle = Bundle(
        "src/less/account.less",
        filters="less,cssmin",
        output="dist/css/account.css",
        extra={"rel": "stylesheet/less"},
    )
    dashboard_stylesheet_bundle = Bundle(
        "src/less/dashboard.less",
        filters="less,cssmin",
        output="dist/css/dashboard.css",
        extra={"rel": "stylesheet/less"},
    )
    # Register assets
    assets.register("styles_account", account_stylesheet_bundle)
    assets.register("styles_dashboard", dashboard_stylesheet_bundle)
    # Build assets in development mode
    if app.config.get("ENVIRONMENT") != "production":
        account_stylesheet_bundle.build(force=True)
        dashboard_stylesheet_bundle.build(force=True)
    return assets


def compile_javascript(assets: Environment) -> Environment:
    """
    Bundle and minimize Javascript source files.

    :param Flask app: Top-level Flask application.
    """
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # JavaScript Bundle
    js_bundle = Bundle("src/js/main.js", filters="jsmin", output="dist/js/main.min.js")
    # Register assets
    assets.register("js_all", js_bundle)
    # Build assets in development mode
    if app.config.get("ENVIRONMENT") != "production":
        js_bundle.build(force=True)
    return assets
