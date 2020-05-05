from flask import render_template,request
from flask_nav.elements import Navbar,View
from io import BytesIO
from sqlalchemy import create_engine,text
import matplotlib.pyplot as plt
import time
import numpy as np
import pandas as pd
import base64

from .. import nav
from . import visitor
from ..models import Tencentcomm



nav.register_element('visitor_nav',Navbar(
    View('评论分析中心','.index'),
    View('主页','.index'),
    View('评论','.comment'),
    View('舆情分析','.analyze')
))


#主页
@visitor.route('/')
def index():
    return render_template('visitor/index.html')


#评论展示
@visitor.route('/comment',methods=['GET','POST'])
def comment():
    keywordtext = request.args.get("keywordtext", '', str)
    datetext=request.args.get('datetext','',str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)

    # SQL 条件
    base_sql = '1=1'
    keywordtext_sql = ' ' if keywordtext == '' else f' AND MATCH(`div_comment`) AGAINST("{keywordtext}" IN BOOLEAN MODE)'
    datetext_sql=''
    if datetext!='':
        start_time = datetext + ' 00:00:00'
        end_time = datetext + ' 23:59:59'
        start_time_array = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        start_time_stamp = int(time.mktime(start_time_array))
        end_time_array = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        end_time_stamp = int(time.mktime(end_time_array))
        datetext_sql=f" AND `time`>'{start_time_stamp}' AND `time`<'{end_time_stamp}'"
    else:
        datetext_sql=' '
    sql_text = base_sql + keywordtext_sql+datetext_sql

    # 查数据
    tencentcomm = Tencentcomm()
    res = tencentcomm.query.filter(text(sql_text)).order_by(text("id")).limit(limit).offset(offset).all()
    count = tencentcomm.query.filter(text(sql_text)).count()

    return render_template("visitor/comment.html", comms=res,datetext=datetext, keywordtext=keywordtext, offset=offset, limit=limit, count=count)


def get_data():
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')
    read_sql = 'SELECT * FROM tencentcomm'
    df = pd.read_sql(read_sql, con=engine)
    return df


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


#绘图
def painting():
    df=get_data()

    # 柱状图
    timeStamps = df['time'].tolist()
    dates = list(map(lambda timeStamp: time.strftime("%m/%d", time.localtime(int(timeStamp))), timeStamps))
    df['date'] = dates
    date_sort = df.groupby(by=['date']).size()
    date_dict = date_sort.to_dict()

    plt.figure(figsize=(6.5, 6.5))
    plt.title('近五日新闻评论数量')
    dates = list(date_dict.keys())
    nums = list(date_dict.values())
    if len(dates) > 5:
        dates = dates[-5:]
        nums = nums[-5:]
    plt.bar(dates, nums)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    # 将matplotlib图片转换为HTML
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims=imb.decode()
    zhu ="data:image/png;base64," + ims

    # 饼状图
    sort = df.groupby(by=['sort_sentiment']).size()
    unsa = f'不满意 {sort.loc["0"]}'
    mod = f'一般 {sort.loc["1"]}'
    sa = f'满意 {sort.loc["2"]}'
    con = [unsa, mod, sa]
    datas = [float(x.split(' ')[1]) for x in con]
    legends = [x.split(' ')[0] for x in con]

    plt.figure(figsize=(6.5, 6.5))
    wedges, texts, autotexts = plt.pie(datas, autopct=lambda data: func(data, datas), textprops=dict(color="w"))
    plt.legend(wedges, legends,title="新闻满意度",loc="center right",bbox_to_anchor=(1, 0, 0.5, 1))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.setp(autotexts, size=8, weight="bold")
    plt.title("新闻评论舆情分析")

    # figure 保存为二进制文件
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    # 将matplotlib图片转换为HTML
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims=imb.decode()
    bing ="data:image/png;base64," + ims

    return {'zhu':zhu,'bing':bing}


#评论分析
@visitor.route('/analyze',methods=['GET','POST'])
def analyze():
    imgs=painting()

    return render_template('/visitor/analyze.html',imgs=imgs)



