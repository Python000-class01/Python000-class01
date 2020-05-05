from flask import render_template,url_for,redirect
from . import home
from app.models import BilibiliComment,T1,Sentiment
from app import db
import json
import datetime
@home.route('/')
def index():
    return redirect(url_for('home.comment'))

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

@home.route('/comment')
def comment():
    shorts = BilibiliComment.query.all()[0:10]
    for short in shorts:
        short.comment_date = datetime.datetime.utcfromtimestamp(short.comment_date).strftime("%Y-%m-%d %H:%M:%S")
    return render_template('/home/result.html', shorts=shorts)