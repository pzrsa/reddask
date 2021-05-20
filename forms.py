from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, email_validator


class RegistrationForm(FlaskForm):
    """
    Allows users to register a new account. Each instance is a part of form and is a required field.
    """
    username = StringField('username', validators=[
                           DataRequired(), Length(min=2, max=12)])

    email = StringField('email', validators=[DataRequired(), Email()])

    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('register')
