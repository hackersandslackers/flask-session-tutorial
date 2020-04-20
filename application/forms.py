"""Create form logic."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignupForm(FlaskForm):
    """User Signup Form."""
    name = StringField('Name',
                       validators=[DataRequired()])
    email = StringField('Email',
                        validators=[Length(min=6, message=('Enter a valid email address.')),
                                    Email(message=('Enter a valid email address.')),
                                    DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, message=('Select a stronger password.')),
                                         EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Your Password',)
    website = StringField('Website',
                          validators=[Optional()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Login Form."""
    email = StringField('Email', validators=[DataRequired(),
                                             Email('Enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
