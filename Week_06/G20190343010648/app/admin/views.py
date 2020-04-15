from flask import render_template
from . import admin
from app.models import *
from app import db

@home.route('/result')
def result():
        shorts = T1.query.all()[0:10]
        return render_template('/result.html', shorts=shorts)