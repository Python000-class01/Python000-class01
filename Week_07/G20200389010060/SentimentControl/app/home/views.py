from flask import render_template
from . import home
from ..models import *
from .form import SearchForm
from flask import redirect, url_for,render_template, request


# 获取采集数据的数量
def get_pick_cnt():
    try:
        cnts = []
        for cnt in PickCnt.query.all():
            cnts.append(cnt.pick_cnt)
        if len(cnts) > 6:
            cnts = cnts[-6:]
        cnts = list(reversed(cnts))
        while len(cnts) < 6:
            cnts.append(0)
        return cnts

    except Exception as e:
        print(e)
        return [0,0,0,0,0,0]

@home.route('/')
def index():
    return render_template('/home/index.html')

@home.route('/index')
def dashboard():
    return render_template('/home/index.html')


@home.route('/result')
def result():
    search_form = SearchForm()

    pos, neg = 0, 0
    for c in Comments.query.all():
        if c.positive:
            pos += 1
        else:
            neg += 1

    print(f'pos = {pos}, neg = {neg}')
    comments = [CommentItem(c.content, c.user_name, c.time_stamp, c.score, c.positive) for c in Comments.query.all()]
    comments.sort(key = lambda c : c.score, reverse=True)

    pick_cnts = get_pick_cnt()
    print(f'pick_cnts = {pick_cnts}')
    return render_template('/home/result.html', comments=comments[:10], search_keyword=None, search_form=search_form, positive=pos, negative=neg, cnt = pick_cnts)

@home.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            keyword = form.keyword.data
            print(f'keyword is {keyword}')

            comments = []
            pos, neg = 0, 0
            for c in Comments.query.all():
                if c.positive:
                    pos += 1
                else:
                    neg += 1

                keyword_set = set(c.keywords.split(','))
                if keyword in keyword_set:
                    comments.append(CommentItem(c.content, c.user_name, c.time_stamp, c.score, c.positive))

            print(f'pos = {pos}, neg = {neg}')
            comments.sort(key = lambda c : c.score, reverse=True)

            pick_cnts = get_pick_cnt()
            print(f'pick_cnts = {pick_cnts}')
            return render_template('/home/result.html', comments=comments[:10], search_keyword=keyword, search_form=form, positive=pos, negative=neg, cnt = pick_cnts)

    return redirect(url_for("index"))