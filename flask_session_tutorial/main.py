"""Routes for logged-in flask_session_tutorial."""
from flask import Blueprint, redirect, render_template, session, url_for
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
main = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@main.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged in Dashboard screen."""
    session["redis_test"] = "This is a session variable."
    return render_template(
        "dashboard.jinja2",
        title="Flask-Session Tutorial",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@main.route("/session", methods=["GET"])
@login_required
def session_view():
    """Display session variable value."""
    return render_template(
        "session.jinja2",
        title="Flask-Session Tutorial",
        template="dashboard-template",
        session_variable=str(session["redis_test"]),
    )


@main.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth.login"))
