"""Compile static asset bundles."""
from flask import Flask
from flask_assets import Bundle, Environment


def compile_stylesheet_assets(app: Flask):
    """
    Generate stylesheets for thr application.

    :param Flask app: Parent application to generate styles for.
    """
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    stylesheet_bundle_account = Bundle(
        "src/less/account.less",
        filters="less,cssmin",
        output="dist/css/account.css",
        extra={"rel": "stylesheet/less"},
    )
    stylesheet_bundle_dashboard = Bundle(
        "src/less/dashboard.less",
        filters="less,cssmin",
        output="dist/css/dashboard.css",
        extra={"rel": "stylesheet/less"},
    )
    # Register assets
    assets.register("styles_account", stylesheet_bundle_account)
    assets.register("styles_dashboard", stylesheet_bundle_dashboard)
    # Build assets in development mode
    if app.config.get("ENVIRONMENT") != "production":
        stylesheet_bundle_account.build(force=True)
        stylesheet_bundle_dashboard.build(force=True)


def compile_javascript_assets(app: Flask):
    """
    Generate static assets for main views.

    :param Flask app: Parent Flask application to generate Javascript bundles for.
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


def compile_static_assets(app: Flask):
    """
    Compile all asset bundles.

    :param Flask app: Parent Flask application to generate asset bundles for.
    """
    compile_stylesheet_assets(app)
    compile_javascript_assets(app)
