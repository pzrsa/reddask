from flask import Flask, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os


from forms import RegistrationForm, LoginForm

app = Flask(__name__)
db = SQLAlchemy(app)


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

    return render_template('login.html', form=form)
