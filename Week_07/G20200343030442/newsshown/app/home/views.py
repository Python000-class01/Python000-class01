from flask import render_template
from . import home
from app.models import *
from app import db

@home.route('/')
def index():
        return render_template('/home/index.html')

@home.route('/index')
def dashboard():
        return render_template('/home/index.html')


@home.route('/result')
def result():
        shorts = T1.query.all()
        return render_template('/home/result.html', shorts=shorts)

@home.route('/result')
def result2():
        zheng = T1.query.filter(score >0.5).count()
        rall = T1.query.filter().count()
        res = float(zheng / rall) 
        return render_template('/home/result.html', zheng=res)

@home.route('/result')
def result3():
        fu = T1.query.filter(score <=0.5).count()
        rall = T1.query.filter().count()
        res = float(fu / rall) 
        print(res)
        return render_template('/home/result.html', fu=res)


@home.route('/pieChart')
def pie_base(positive,negative) :
    c = (
        Pie()
        .add("舆情分析",[('positive',positive),('negative',negative)])
        .set_colors(["orange", "grey"])
        .set_global_opts(title_opts=opts.TitleOpts(title="舆情分析"))
        )
    return c

def get_pie_chart():
    negative_1 = T1.query.filter(T1.sentiment < 0.5).count()
    positive_1 = T1.query.filter(T1.sentiment>= 0.5).count()
    c = pie_base(positive_1,negative_1)
    return c.dump_options_with_quotes()


# 使用request登陆
from flask import request
@home.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        pass


@home.route('/buttons')
def buttons():
    return render_template('/home/buttons.html')

# 使用LoginForm登陆
from .forms import LoginForm
from flask import redirect, url_for
@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # 从db获取用户账号
            usr = 'admin'
            pwd = 'admin'

            if username == usr and password == pwd:
                return redirect(url_for("home.result"))
            else:
                return redirect(url_for("home.login"))
        else:
            return redirect(url_for("home.login"))
    return render_template('/home/login.html', form=form)




from flask import request, Response
# cookie
@home.route('/setcookie')
def setcookie():
    # 创建响应对象
    resp = Response('设置cookie')
    # 设置cookie保持1小时
    resp.set_cookie('name', 'wilson', max_age=3600)
    return resp

@home.route('/getcookie')
def getcookie():
    myname = request.cookies.get('name')
    return myname

@home.route('/delcookie')
def delcookie():
    resp = Response('删除cookie')
    resp.delete_cookie('name')
    return resp

# session
from flask import session
@home.route('/setsession')
def setsession():
    session['name'] = 'wilson'
    return 'session设置成功'

@home.route('/getsession')
def getsession():
    value = session.get('name')
    return f'session {value}'

@home.route('/delsession')
def delsession():
    session.pop('name')
    return 'session deleted'

