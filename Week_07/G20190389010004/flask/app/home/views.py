from flask import render_template, request
from . import home
from app.models import SinaCommentSentiment
from app import session
from sqlalchemy import func, extract, or_
import json

from forms import SearchForm
import jieba

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
    # 分组统计（每日采集数据）
    # query_result = session.query(extract('day', SinaCommentSentiment.time).label('day'), func.count(SinaCommentSentiment.mid)).group_by('day').all()
    query_result = session.query(SinaCommentSentiment.date, func.count(SinaCommentSentiment.mid)).group_by(SinaCommentSentiment.date).order_by(SinaCommentSentiment.date.asc()).all()
    showData = tupleListToDictList(query_result)
    # 情感分析
    sentiments = session.query(SinaCommentSentiment.sentiment).all()
    pn = process(sentiments)
    return render_template('/home/show.html', showData=showData, pn=pn)

@home.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            keyword = form.keyword.data
            # 对关键词分词
            cut_keywords = jieba.cut_for_search(keyword)
            results = search_sql(cut_keywords)
            return render_template('/home/search.html', form = form, results=results)
        else:
            from flask import flash
            flash('关键词不能为空')
    return render_template('/home/search.html', form = form)


def tupleListToDictList(tupleList):
    names = 'day sum'.split()
    return [dict(zip(names, da)) for da in tupleList]

def process(tupleList):
    positive = 0
    negative = 0
    for num in tupleList:
        if num[0] < 0.5:
            negative += 1
        else:
            positive += 1
    return [{'label': 'positive', 'value': positive},
            {'label': 'negative', 'value': negative}]


def search_sql(keywords):
    result = SinaCommentSentiment.query.filter(
        or_(SinaCommentSentiment.content.like("%" + keyword + "%") for keyword in keywords)
        ).all()
    return result
