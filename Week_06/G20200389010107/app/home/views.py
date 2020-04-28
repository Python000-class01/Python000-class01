from flask import render_template
from . import home
from app.models import *
from app import db


@home.route('/')
@home.route('/index')
def result():
        #shorts = T1.query.all()[0:10]
        shorts = T1.query.order_by(T1.sentiment.desc())[:10]
        return render_template('/home/result.html', shorts=shorts)






