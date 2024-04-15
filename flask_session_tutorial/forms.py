"""Sign-up & log-in forms."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignupForm(FlaskForm):
    """User Sign-up Form."""

    user_name = StringField("Name", validators=[DataRequired()])
    user_email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    user_password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    user_password_confirm = PasswordField(
        "Confirm Your Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    user_metadata_website = StringField("Website", validators=[Optional()])
    submit_button = SubmitField("Register")


class LoginForm(FlaskForm):
    """User Log-in Form for existing users."""

    user_email = StringField("Email", validators=[DataRequired(), Email(message="Enter a valid email.")])
    user_password = PasswordField("Password", validators=[DataRequired()])
    submit_button = SubmitField("Log In")
