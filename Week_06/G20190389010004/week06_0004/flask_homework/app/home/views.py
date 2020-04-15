from flask import render_template
from . import home
from app.models import Bookshort
# from app import db

@home.route('/')
def index():
    return render_template('/home/index.html')

@home.route('/index')
def dashboard():
    return render_template('/home/index.html')

@home.route('/result')
def result():
    shorts = Bookshort.query.order_by(Bookshort.sentiment.desc()).all()[0:10]
    return render_template('/home/result.html', shorts=shorts)