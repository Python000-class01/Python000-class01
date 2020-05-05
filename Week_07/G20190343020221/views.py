from . import homeBP
from app.models import *
from app import db

from flask import request, session, redirect, render_template, flash, url_for, jsonify
from flask_login import LoginManager, login_user, login_required

from random import randrange
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, WordCloud

import pandas as pd

from sqlalchemy import distinct, func
# from sqlalchemy.orm import load_only

from app.s1func.S1FUNC import *
from .weitoutiao_yiqing import *

@homeBP.route('/')
def index():
    return render_template('/index.html')

@homeBP.route('/index')
def dashboard():
    return render_template('/index.html')

@homeBP.route('/dashboard2')
def dashboard2():
    return render_template('/index2.html')

@homeBP.route('/dashboard3')
def dashboard3():
    return render_template('/index3.html')

@homeBP.route('/tables')
def tables():
    return render_template('/tables.html')

@homeBP.route('/tables_dynamic')
def tables_dynamic():
    return render_template('/tables_dynamic.html')

@homeBP.route('/echarts')
def echarts():
    return render_template('/echarts.html')

@homeBP.route('/ai', methods=('GET', 'POST'))
@login_required
def ai():
    page = 1
    pagesize = 10
    print('in to ai')
    if request.method == 'POST':
        print('in to post')
        import json
        data = json.loads(request.form['dataArray'])
        pageIndex = data["page"]
        pageSize = data["pagesize"]
        print(pageIndex, pageSize)

        pagination = News.query.paginate(page=pageIndex, per_page=pageSize)
        # cols = ['id', 'sentiment', 'event_time', 'collect_time']
        cols = ['id', 'event_time', 'collect_time']
        shorts = [{col: getattr(d, col) for col in cols} for d in pagination.items]
        result = dict()
        result['news'] = shorts
        result['pagination'] = {"totalCount": pagination.total}
        return jsonify(data=result)

    return render_template('/ai.html')

# 表格
@homeBP.route('/api/newstable', methods=('POST', 'GET'))
@login_required
def newstable():
    if request.method == 'GET':
        # page = int(request.args.get("page"))                 # 获取 get 参数
        # limit = int(request.args.get('limit'))
        # search_key = request.args.get('search_key')
        pass
    if request.method == 'POST':
        print('in to post')
        import json
        # data = json.loads(request.form['dataArray'])
        # page = data["page"]
        # limit = data["limit"]
        # search_key = data["search_key"]
        page = int(request.form['page'])
        limit = int(request.form['limit'])
        if 'search_key' in request.form:
            search_key = request.form['search_key']
        else:
            search_key = None
    response = get_news(page, limit, search_key)
    return jsonify(response)


# 柱状图
@homeBP.route("/barChart")
@login_required
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


# 饼图
@homeBP.route("/pieChart")
@login_required
def get_pie_chart():
    c = pie_base()
    return c.dump_options_with_quotes()


# 词云
@homeBP.route("/wordcloud")
@login_required
def get_wordcloud_chart():
    c = wordcloud_base()
    return c.dump_options_with_quotes()


from .forms import LoginForm
# 登录
@homeBP.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录
    """
    loginForm = LoginForm()

    if request.method == 'POST':
        print(loginForm.validate_on_submit())
        if loginForm.validate_on_submit():
            username = loginForm.username.data
            password = loginForm.password.data

            usr = User.query.filter(User.username == username).one_or_none()
            if usr and usr.verify_password(password):
                login_user(usr, loginForm.remeberme.data)
                return redirect(url_for("home.ai"))
            else:
                flash('登录失败')
                return redirect(url_for("home.login"))
        else:
            flash('未提交有效信息')
    return render_template('/login.html', form=loginForm)


# 登出
from  flask_login import  logout_user
@homeBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.login'))


# 注册
from .forms import RegisterForm
@homeBP.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()

    if request.method == 'POST':
        print(registerForm.validate_on_submit())

        if registerForm.validate_on_submit():
            username = registerForm.username.data
            password = registerForm.password.data
            reppassword = registerForm.reppassword.data
            user = User(username=username, password=password)
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                print('添加用户失败')
            else:
                print('添加用户成功')
            return redirect(url_for('home.login'))

        else:
            from flask import flash
            flash('注册失败')

    return render_template('/register.html', form=registerForm)
