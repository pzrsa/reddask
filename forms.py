from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, email_validator


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(), Length(min=2, max=12)])

    email = StringField('email', validators=[DataRequired(), Email()])

    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('register')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])

    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('register')
