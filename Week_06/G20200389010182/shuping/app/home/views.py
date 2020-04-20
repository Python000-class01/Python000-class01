from flask import render_template
from . import home
from app.models import *
from app import db


@home.route('/')
def result():
        # shorts = T1.query.all()[0:2]

        # shorts = T1.query.order_by(T1.sentiment.desc())[0:10]
        shorts = T1.query.order_by(T1.sentiment.desc()).limit(10)
        print(shorts)
        return render_template('/home/result.html', shorts=shorts)