"""Routes for user authentication."""

from typing import Optional

from flask import Blueprint, Response, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user

from flask_session_tutorial import login_manager
from flask_session_tutorial.forms import LoginForm, SignupForm
from flask_session_tutorial.models import User, db

# Blueprint Configuration
auth_blueprint = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup() -> Response:
    """
    View for new users to sign up with new accounts.

    GET: Serve sign-up page.
    POST: Validate form, create account, redirect user to dashboard.

    :response: Response
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.user_email.data).first()
        if existing_user is None:
            user = User(name=form.name.data, email=form.user_email.data, website=form.website.data)
            user.set_password(form.user_password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for("main.dashboard"))
        flash("A user already exists with that email address.")
    return render_template(
        "signup.jinja2",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )


@auth_blueprint.route("/", methods=["GET", "POST"])
def login() -> Response:
    """
    Log-in page for registered users.

    GET: Serve Log-in page.
    POST: Validate form and redirect user to dashboard.

    :returns: Response
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))  # Bypass if user is logged in
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.user_email.data).first()  # Validate Login Attempt
        if user and user.check_password(password=form.user_password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.dashboard"))
        flash("Invalid username/password combination")
        return redirect(url_for("auth.login"))
    return render_template(
        "login.jinja2",
        form=form,
        title="Log In",
        template="login-page",
        body="Log in with your User account.",
    )


@login_manager.user_loader
def load_user(user_id: int) -> Optional[User]:
    """
    Check if user is logged-in upon page load.

    :param int user_id: Primary user ID to load from database, if exists.

    :returns: Optional[User]
    """
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized() -> Response:
    """
    Redirect unauthorized users to Login page.

    :returns: Response
    """
    flash("You must be logged in to view that page.")
    return redirect(url_for("auth.login"))
