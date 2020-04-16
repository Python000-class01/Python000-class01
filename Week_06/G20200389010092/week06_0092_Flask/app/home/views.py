from flask import render_template
from . import home
from app.models import *
from app import db
# @home.route('/')
# def index():
#         return render_template('/home/index.html')

# @home.route('/index')
# def dashboard():
#         return render_template('/home/index.html')


@home.route('/')
def result():
        shorts = T1.query.order_by(T1.sentiment.desc()).all()[0:10]
        return render_template('/home/result.html', shorts=shorts)