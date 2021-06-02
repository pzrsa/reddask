from flask import flash, redirect, render_template, url_for
from flask_login import login_user

from reddask import app
from reddask.models import User
from reddask.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f"welcome {form.username.data}, your account was successfully created")
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash(f"login successful!")
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check the email and password.', 'danger')

    return render_template('login.html', form=form)
