from flask import render_template, request
from . import home
from app.models import CommentSentiment
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
    comments = CommentSentiment.query.all()
    return render_template('/home/result.html', comments=comments)


@home.route('/show')
def show():
    query_result = session.query(CommentSentiment.date, func.count(CommentSentiment.mid)).group_by(
        CommentSentiment.date).order_by(CommentSentiment.date.asc()).all()
    show_data = tuple_list_to_dict_list(query_result)
    sentiments = session.query(CommentSentiment.sentiment).all()
    pn = process(sentiments)
    return render_template('/home/show.html', showData=show_data, pn=pn)


@home.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            keyword = form.keyword.data
            cut_keywords = jieba.cut_for_search(keyword)
            results = search_sql(cut_keywords)
            return render_template('/home/search.html', form=form, results=results)
        else:
            from flask import flash
            flash('关键词不能为空')
    return render_template('/home/search.html', form=form)


def tuple_list_to_dict_list(tuple_list):
    names = 'day sum'.split()
    return [dict(zip(names, da)) for da in tuple_list]


def process(tuple_list):
    positive = 0
    negative = 0
    for num in tuple_list:
        if num[0] < 0.5:
            negative += 1
        else:
            positive += 1
    return [{'label': 'positive', 'value': positive},
            {'label': 'negative', 'value': negative}]


def search_sql(keywords):
    rp = CommentSentiment.query.filter(
        or_(CommentSentiment.content.like("%" + keyword + "%") for keyword in keywords)
    ).all()
    return rp
