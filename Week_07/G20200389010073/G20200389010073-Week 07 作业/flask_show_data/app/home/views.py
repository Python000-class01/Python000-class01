from flask import render_template, url_for, request, Response
from . import home
from app.models import *
from app import db
from app.models import T1
import copy
import time
import pprint


@home.route('/')
def index():
        # 查询数据库的评论数据
        shorts = T1.query.filter().order_by(T1.created_at.desc()).all()

        # 选取所有评论的采集时间created_at，并按日期统计的评论数
        list_time = []
        for short in shorts:
            list_time.append(short.created_at)
        time_set = sorted(list(set(list_time)))

        # 创建柱状图数据
        mb_data = []
        mb_data2 = {
            'y': 0,
            'x': 0
        }
        for time in time_set:
            num = list_time.count(time)
            mb_data2['y'] = num
            mb_data2['x'] = time
            mb_data.append(copy.deepcopy(mb_data2))

        mb = {
            'element': 'morris-bar-chart',
            'xkey': 'x',
            'ykeys': ['y'],
            'labels': ['采集评论数量'],
            'hideHover': 'auto',
            'resize': True,
            'data': mb_data
        }

        # 创建饼图数据
        as_count = len(T1.query.filter(T1.c_Sln_comment > 0.6).all())/len(T1.query.all())
        md_data = []
        md_data_as = {
            'label': '正向评论数',
            'value': as_count
        }
        md_data.append(md_data_as)
        ns_count = len(T1.query.filter(T1.c_Sln_comment < 0.6).all())/len(T1.query.all())
        md_data_ns = {
            'label': '负向评论数',
            'value': ns_count
        }
        md_data.append(md_data_ns)
        md = {
            'element': 'morris-donut-chart',
            'resize': True,
            'data': md_data
        }

        js_data = '$(function(){' + 'Morris.Bar(' + str(mb) + ');' + 'Morris.Donut(' + str(md) + ');' + '});'
        js_data = js_data.replace('True', 'true')

        # 写入图标数据
        with open('./app/static/js/morris-data.js', 'w', encoding='utf-8') as f:
            f.write(js_data)

        return render_template('/home/result.html', shorts=shorts)


@home.route('/index')
def dashboard():
        return url_for('index')


@home.route('/keyword', methods=['POST'])
def keyword():
        if request.method == 'POST':
            keywords = str(request.form.get('input_keyword'))
            shorts = T1.query.filter(T1.c_Comment.like(f'%{keywords}%')).all()
            title = f'包含关键词 \'{keywords}\' 的评论：'
            if shorts == []:
                return "未查到相关数据！"
            else:
                return render_template('/home/keyword.html', shorts=shorts, title=title)


@home.route('/date', methods=['POST'])
def date():
        if request.method == 'POST':
            startdate = str(request.form.get('startdate'))
            enddate = str(request.form.get('enddate'))
            starttime = ' 00:00:00'
            endtime = ' 23:59:59'
            print(startdate)
            print(enddate == '')

            if startdate != '' and enddate != '':
                if startdate == enddate:
                    start = int(time.mktime(time.strptime(startdate + starttime, "%Y-%m-%d %H:%M:%S")))
                    end = int(time.mktime(time.strptime(startdate + endtime, "%Y-%m-%d %H:%M:%S")))
                    shorts = T1.query.filter(T1.c_Time > start, T1.c_Time < end).all()
                    title = f'{startdate + starttime}-{endtime}的评论：'
                    return render_template('/home/date.html', shorts=shorts, title=title)
                elif startdate < enddate:
                    start = int(time.mktime(time.strptime(startdate + starttime, "%Y-%m-%d %H:%M:%S")))
                    end = int(time.mktime(time.strptime(enddate + endtime, "%Y-%m-%d %H:%M:%S")))
                    shorts = T1.query.filter(T1.c_Time > start, T1.c_Time < end).all()
                    title = f'{startdate + starttime}  -  {enddate + endtime}的评论：'
                    return render_template('/home/date.html', shorts=shorts, title=title)
                else:
                    return "截止日期必须比开始日期大，请重新选择正确的日期"
            elif startdate != '' and enddate == '':
                start = int(time.mktime(time.strptime(startdate + starttime, "%Y-%m-%d %H:%M:%S")))
                shorts = T1.query.filter(T1.c_Time > start).all()
                title = f'大于{startdate + starttime}的评论：'
                return render_template('/home/date.html', shorts=shorts, title=title)
            elif startdate == '' and enddate != '':
                end = int(time.mktime(time.strptime(enddate + endtime, "%Y-%m-%d %H:%M:%S")))
                shorts = T1.query.filter(T1.c_Time < end).all()
                title = f'小于{enddate + endtime}的评论：'
                return render_template('/home/date.html', shorts=shorts, title=title)
            else:
                return "日期选择错误，未查到相关数据！"