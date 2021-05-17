from flask import Flask, render_template
import os

from forms import MyForm

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def register():

    form = MyForm()

    return render_template('register.html', form=form)
