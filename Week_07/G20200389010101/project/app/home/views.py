from flask import render_template
from . import home
from app.models import *
from app import db
@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def dashboard():
        return render_template('/home/index.html')


@home.route('/result')
def result():
        shorts = MYTABLE.query.all()[0:100]
        return render_template('/home/result.html', shorts=shorts)