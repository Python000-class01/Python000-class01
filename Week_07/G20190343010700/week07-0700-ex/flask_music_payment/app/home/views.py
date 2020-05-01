from flask import Flask
from  flask import render_template
from . import home
from app.models import *
from app import db
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Bar
import datetime 



def bar_base(time_date,num_list):
    c = (
        Bar()
        .add_xaxis(time_date)
        .add_yaxis("评论数", num_list)
        .set_colors(["orange"])
        .set_global_opts(title_opts=opts.TitleOpts(title="每日评论数量"))
    )
    return c


def pie_base(positive,negative) :
    c = (
        Pie()
        .add("舆情分析",[('positive',positive),('negative',negative)])
        .set_colors(["orange", "grey"])
        .set_global_opts(title_opts=opts.TitleOpts(title="舆情分析"))
        )
    return c

###   ============   首页展示10条最新的评论 ================
@home.route('/')
def index():   
    shorts = T1.query.order_by(T1.time.desc()).limit(10)
    return render_template('/home/index.html', shorts=shorts)


###   ============   制作舆情饼图 ================
'''
正面舆情 sentiment >= 0.5
负面舆情 sentiment <  0.5
'''
@home.route('/pieChart')
def get_pie_chart():
    negative_1 = T1.query.filter(T1.sentiment < 0.5).count()
    positive_1 = T1.query.filter(T1.sentiment>= 0.5).count()
    c = pie_base(positive_1,negative_1)
    return c.dump_options_with_quotes()

###   ============   每日采集评论统计图 ================

@home.route('/barChart')
def get_bar_chart():
    firstDay = datetime.date(2020,4,15)
    lastDay= datetime.date.today()
    delta = lastDay - firstDay
    date = []
    for i in range(delta.days+1):
        date.append(firstDay + datetime.timedelta(days = i))
    num_list = []
    for day in date:
        num_list.append(T1.query.filter(T1.time == day).count())
    time_list = date
    bar = bar_base(time_list,num_list)
    return bar.dump_options_with_quotes()


