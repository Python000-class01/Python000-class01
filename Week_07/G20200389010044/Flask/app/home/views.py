from flask import render_template
from . import home
from app.models import *
from app import db
@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def homepage():
        return render_template('/home/index.html')

@home.route('/dashboard')
def dashboard():
        return render_template('/home/dashboard.html')

@home.route('/result')
def result():
        shorts = T1.query.all()
        return render_template('/home/result.html', shorts=shorts)

@home.route('/histogram')
def histogram():
        shorts = T1.query.all()
        return render_template('/home/histogram.html', shorts=shorts)
        
@home.route('/pie')
def pie():
        shorts = T1.query.all()
        return render_template('/home/pie.html', shorts=shorts)