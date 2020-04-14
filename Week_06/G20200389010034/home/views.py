from flask import render_template
from . import home
from douban.app.models import *

@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def dashboard():
        return render_template('/home/index.html')


@home.route('/result')
def result():
    comments = [CommentItem(c.item_id, c.comment, c.score, c.sentiments) for c in Comments.query.all()]
    comments.sort(key=lambda c : c.score, reverse=True)
    return render_template('/home/result.html', comments=comments[:10]) 
