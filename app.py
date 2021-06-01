from flask import Flask, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import login_user
from werkzeug.security import check_password_hash
from models import User
import os


from forms import RegistrationForm, LoginForm

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt()


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


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
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f"login successful!")
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check the email and password.', 'danger')

    return render_template('login.html', form=form)
