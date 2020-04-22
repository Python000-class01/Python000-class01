from flask import render_template
from . import home
from app.models import SinaCommentSentiment
from app import session
from sqlalchemy import func, extract

@home.route('/')
def index():
    return render_template('/home/index.html')

@home.route('/index')
def dashboard():
    return render_template('/home/index.html')

@home.route('/result')
def result():
    comments = SinaCommentSentiment.query.all()    
    return render_template('/home/result.html', comments=comments)

@home.route('/show')
def show():
    # 分组统计
    query_result = session.query(extract('day', SinaCommentSentiment.time).label('day'), func.count('day')).group_by('day').all()
    showData = tupleListToDictList(query_result)
    sentiments = session.query(SinaCommentSentiment.sentiment).all()
    pn = process(sentiments)
    return render_template('/home/show.html', showData=showData, pn=pn)

@home.route('/search')
def search():
    # TODO
    return render_template('/home/search.html')

def tupleListToDictList(tupleList):
    names = 'day sum'.split()
    return [dict(zip(names, da)) for da in tupleList]

def process(tupleList):
    positive = 0
    negative = 0
    for num in tupleList:
        num0 = num[0]
        if num0 < 0.5:
            negative += 1
        else:
            positive += 1
    return [positive, negative]
