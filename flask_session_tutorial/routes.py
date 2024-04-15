"""Routes for logged-in flask_session_tutorial."""

from flask import Blueprint, Response, redirect, render_template, session, url_for
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
main_blueprint = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@main_blueprint.route("/dashboard", methods=["GET"])
@login_required
def dashboard() -> Response:
    """
    Logged in Dashboard screen.

    :returns: Response
    """
    session["redis_test"] = "This is a session variable."
    return render_template(
        "dashboard.jinja2",
        title="Flask-Session Tutorial",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@main_blueprint.route("/session", methods=["GET"])
@login_required
def session_view() -> Response:
    """
    Display session variable value.

    :returns: Response
    """
    return render_template(
        "session.jinja2",
        title="Flask-Session Tutorial",
        template="dashboard-template",
        session_variable=str(session["redis_test"]),
    )


@main_blueprint.route("/logout")
@login_required
def logout() -> Response:
    """
    User log-out logic.

    :returns: Response
    """
    logout_user()
    return redirect(url_for("auth.login"))
