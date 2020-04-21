from app.models import *
from app import db
from sqlalchemy import distinct, func

from pyecharts.charts import Bar, Pie, WordCloud
from pyecharts import options as opts

import json, time
import pandas as pd

def get_news(page, limit) -> dict:

    pagination = (
        db
        .session
        .query(News.content_id, News.desc, News.event_time, News.collect_time, Sentiments.sentiment)
        .join(Sentiments, News.content_id==Sentiments.content_id)
        .order_by(News.event_time.desc())
        .paginate(page=page, per_page=limit, error_out=False)
    )

    cols = ['content_id', 'desc', 'sentiment', 'event_time', 'collect_time']
    data = [{col: getattr(d, col) for col in cols} for d in pagination.items]

    df = pd.DataFrame(data)
    df['采集时间'] = (
        df['collect_time']
        .apply(lambda x:
            time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(float(x)))
            )
    )
    df.drop(['collect_time'], inplace=True, axis=1)
    df['发布时间'] = (
        df['event_time']
        .apply(lambda x:
            time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(float(x)))
            )
    )
    df.drop(['event_time'], inplace=True, axis=1)
    response = dict()
    response['data'] = df.to_dict(orient='records')     # 直接赋值data即可，这里 df 是用来处理时间戳转换
    response['limt'] = limit
    response['total'] = pagination.total
    return response

# 柱状图
def bar_base() -> Bar:
    """柱状图"""
    import datetime
    data = (
        db.session
        .query(News.event_date, func.count(News.event_date))
        .group_by(News.event_date)
        .all()
    )
    xaxis = [ i[0] for i in data]
    yaxis = [ i[1] for i in data]
    c = (
        Bar()
        # .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_xaxis(xaxis)
        .add_yaxis('采集数量(条)', yaxis, color='#26B99A')
        # .add_yaxis('采集数量(条)', yaxis, temstyle_opts=opts.ItemStyleOpts(color='red'))
        # .add_yaxis("商家A", [randrange(0, 100) for _ in range(len(xaxis))])
        # .add_yaxis("商家B", [randrange(0, 100) for _ in range(len(xaxis))])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


# 饼图
def pie_base() -> Pie:
    """饼图"""
    zheng = db.session.query(Sentiments).filter(Sentiments.sentiment > 0.5).count()
    fan = db.session.query(Sentiments).filter(Sentiments.sentiment <= 0.5).count()

    c = (
        Pie()
        .add("", [['正向', zheng], ['负向', fan]])
        .set_colors(["#E74C3C", "#3498DB"])
        # .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-情感分析"))
        # .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
    return c

# 词云
def wordcloud_base() -> WordCloud:
    """词云"""
    data = (
        User.query
        .with_entities(News.desc)
        .order_by(News.event_time.desc())
        .limit(100)
        .all()
    )
    text = ''.join([i[0] for i in data])

    import jieba.analyse
    tfidf = jieba.analyse.extract_tags(
        text,
        topK=200,                   # 权重最大的topK个关键词
        withWeight=True
        )

    c = (
        WordCloud()
        .add(series_name="热点分析", data_pair=tfidf, word_size_range=[6, 66])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c
