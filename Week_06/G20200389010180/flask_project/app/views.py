from app import app
from flask import render_template
#from . import home
from app.models import *
from app import db


@app.route('/')
def result():
    shorts = Douban.query.order_by(Douban.sentiment.desc()).all()[0:10]
    return render_template('/result.html', shorts=shorts)