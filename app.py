from flask import Flask, render_template
import os

from forms import RegistrationForm

app = Flask(__name__)

# CSRF protection secret key stored in environment variable
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# creates the website routes, make sure to provide the arguments needed for the template


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def register():

    form = RegistrationForm()

    return render_template('register.html', form=form)
