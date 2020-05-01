from flask import render_template,request
from . import home
from app.models import *
from app import db
import numpy
import json
import logging

@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def dashboard():
        return render_template('/home/index.html')


@home.route('/result')
def result():
        keyword = request.args.get("keyword") or ""
        input_time_from = request.args.get('input_time_from') or ""
        input_time_to = request.args.get('input_time_to') or ""
        comment_time_from = request.args.get('comment_time_from') or ""
        comment_time_to = request.args.get('comment_time_to') or ""

        news_filter = []
        if keyword != "":
                news_filter.append(NewsModel.keywords.like("%" + keyword + "%"))
        if input_time_from != "":
                news_filter.append(NewsModel.input_time >= input_time_from)
        if input_time_to != "":
                news_filter.append(NewsModel.input_time <= input_time_to)
        if comment_time_from != "":
                news_filter.append(NewsModel.time >= comment_time_from)
        if comment_time_to != "":
                news_filter.append(NewsModel.time <= comment_time_to)
        #查询
        comments = NewsModel.query.filter(*news_filter).all()
        
        return render_template('/home/result.html', 
                comments=comments, 
                keyword=keyword, 
                input_time_from=input_time_from, 
                input_time_to=input_time_to, 
                comment_time_from=comment_time_from, 
                comment_time_to=comment_time_to)

@home.route('/charts')
def charts():
        sql = 'SELECT substring(time, 1, 10) as date, COUNT(*) as sum FROM `news` GROUP BY substring(time, 1, 10);'
        date_comment_count = db.session.execute(sql)
        date = []
        sum = []
        for x in date_comment_count:
                date.append(x['date'])
                sum.append(x['sum'])

        comments_total = NewsModel.query.count()
        positive_comment = NewsModel.query.filter(NewsModel.sentiments.__gt__(0.5)).count()
        negative_comment = comments_total - positive_comment
        pnn = []
        pnn.append(positive_comment)
        pnn.append(negative_comment)

        return render_template('/home/charts.html', date=json.dumps(date), sum=json.dumps(sum), pnn=pnn)

        