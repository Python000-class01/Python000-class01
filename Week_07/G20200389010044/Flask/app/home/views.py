from flask import render_template
from flask import Response
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from . import home
from app.models import *
from app import db
import json
import pandas
import datetime


@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def homepage():
        return render_template('/home/index.html')

@home.route('/dashboard')
def dashboard():
        return render_template('/home/dashboard.html')

class MyForm(Form):
    user = StringField('keyword', validators=[DataRequired()])

@home.route('/result', methods=('GET', 'POST'))
def result():
        form = MyForm(csrf_enabled = False)
        if form.validate_on_submit():
                # if form.user.data == 'admin':
                keyword =  form.data['keyword']
                shorts = T1.query.filter(T1.content.like('%'+keyword+'%'))
                return render_template('/home/result.html', shorts=shorts, form = form)
        else:
                shorts = T1.query.all()
                return render_template('/home/result.html', shorts=shorts, form = form)
                

@home.route('/histogram')
def histogram():
        res = {'data':[]}
        for timedelta in range(7):
                date = ( datetime.date.today() - datetime.timedelta(days = timedelta) ).strftime("%Y-%m-%d") 
                query = T1.query.filter(T1.pub_time == date).all()
                res['data'].append({'date':date, 'val':len(query)})
        return render_template('/home/histogram.html', data = res )

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@home.route('/echarts')
def echarts():
        res = {'data':[]}
        for timedelta in range(6, -1, -1):
                date = ( datetime.date.today() - datetime.timedelta(days = timedelta) ).strftime("%Y-%m-%d") 
                query = T1.query.filter(T1.pub_time.like(date+"%")).all()
                res['data'].append({'date':date, 'val':len(query)})
        content = json.dumps(res)
        resp = Response_headers(content)
        return resp



@home.route('/pie')
def pie():
        shorts = T1.query.all()
        pos = len(T1.query.filter(T1.sentiment >= 0.5).all())
        neg = len(shorts) - pos
        return render_template('/home/pie.html', pos = pos, neg = neg)