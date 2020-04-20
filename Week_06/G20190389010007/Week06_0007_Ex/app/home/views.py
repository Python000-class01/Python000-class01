from flask import render_template
from . import home
from app.models import T1
from app import db
import json
@home.route('/')
def index():
    return render_template('/home/result.html')

@home.route('/index')
def dashboard():
    return render_template('/home/result.html')

@home.route('/data')
def dashboard123():
    dica = {'a':123,'b':2222}
    return json.dumps(dica)

@home.route('/result')
def result():
    shorts = T1.query.all()[0:10]
    return render_template('/home/result.html', shorts=shorts)