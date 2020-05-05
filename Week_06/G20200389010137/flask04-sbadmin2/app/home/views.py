from . import home
from app.models import get_db, query_db
# from app import db
import json

from flask import request, session, redirect, render_template, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash


@home.route('/')
def index():
        return render_template('/index.html')

@home.route('/index')
def dashboard():
        return render_template('/index.html')


@home.route('/douban', methods=('GET', 'POST'))
def result():
    db = get_db()
    # page = 1
    # pagesize = 10
    # if request.method == 'POST':
    #     data = request.form['dataArray']
    #     print(data)
    #     page = data['page']
    #     pagesize = data['pagesize']
    # # shorts = query_db('SELECT id, n_star, short, sentiment FROM douban').paginate(page=page,per_page=pagesize)
    shorts = query_db('SELECT id, n_star, short, sentiment FROM douban')
    return render_template('/douban.html', shorts=shorts)


# 登录
@home.route('/login', methods=('GET', 'POST'))
def login():
    """通过将用户id添加到会话来登录注册用户。"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
            ).fetchone()        # 查询数据保存在变量中

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):   # 哈希 提交的密码 并比较哈希值
            error = 'Incorrect password.'

        # session 是一个 dict ，它用于储存横跨请求的值。当验证 成功后，用户的 id 被储存于一个新的会话中。会话数据被储存到一个 向浏览器发送的 cookie 中，在后继请求中，浏览器会返回它。 Flask 会安全对数据进行 签名 以防数据被篡改。
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('/login.html')