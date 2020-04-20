from  flask import render_template
from . import home
from app.models import *
from app import db

@home.route('/')
def index():
    shorts = T1.query.order_by(T1.sentiment.desc()).limit(20)
    return render_template('/home/index.html', shorts=shorts)
    # return render_template('/home/index.html')

# @home.route('/')
# def dashboard():
#     return render_template('/home/index.html')

@home.route('/result')
def result():
        shorts = T1.query.order_by(T1.sentiment).limit(10)
        return render_template('/home/result.html', shorts=shorts)