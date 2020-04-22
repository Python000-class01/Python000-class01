from flask import render_template
from . import home
from dangdang_flask.app.models import *

@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def dashboard():
        return render_template('/home/index.html')

@home.route('/result')
def result():
        shorts = Comments.query.all()[0:10]
        return render_template('/home/result.html', shorts=shorts)