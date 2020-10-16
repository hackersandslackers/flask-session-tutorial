"""Routes for logged-in flask_session_tutorial."""
from flask import Blueprint
from flask import current_app as app
from flask import redirect, render_template, session, url_for
from flask_login import current_user, login_required, logout_user

from .assets import compile_auth_assets

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Logged in Dashboard screen."""
    session['redis_test'] = 'This is a session variable.'
    return render_template(
        'dashboard.jinja2',
        title='Flask-Session Tutorial.',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!"
    )


@main_bp.route('/session', methods=['GET'])
@login_required
def session_view():
    """Display session variable value."""
    return render_template(
        'session.jinja2',
        title='Flask-Session Tutorial.',
        template='dashboard-template',
         session_variable=str(session['redis_test'])
    )

@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))
