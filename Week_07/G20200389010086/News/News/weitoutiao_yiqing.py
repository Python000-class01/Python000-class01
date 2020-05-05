# -*- coding: utf-8 -*-
from app.models import *
from app import db
from sqlalchemy import distinct, func, or_

from pyecharts.charts import Bar, Pie, WordCloud
from pyecharts import options as opts

import json, time
import pandas as pd

def get_news(page, limit, search_key) -> dict:
    """分页方式获取新闻纪录
    :page: int
    :limit: int
    """
    db.session.commit()
    if search_key:
        rule = f'%{search_key}%'
        pagination = (
            db.session
            .query(News.content_id, News.ndesc, News.event_time, News.collect_time, Sentiments.sentiment)
            .outerjoin(Sentiments)
            .order_by(News.event_time.desc())
            .filter(News.ndesc.like(rule))     # 多列搜索是用 or_ 实现的
            .paginate(page=page, per_page=limit, error_out=False)
        )
    else:
        pagination = (
            db.session
            .query(News.content_id, News.ndesc, News.event_time, News.collect_time, Sentiments.sentiment)
            .outerjoin(Sentiments)  # 有 relationship 定义时简写
            # .outerjoin(Sentiments, News.content_id==Sentiments.content_id)    #无relationship 定义时
            .order_by(News.event_time.desc())
            .paginate(page=page, per_page=limit, error_out=False)
        )

    response = dict()

    cols = ['content_id', 'ndesc', 'sentiment', 'event_time', 'collect_time']
    data = [{col: getattr(d, col) for col in cols} for d in pagination.items]
    df = pd.DataFrame(data)

    if df.empty:
        response['data'] = None
    else:
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
        response['data'] = df.to_dict(orient='records')

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
        .add_xaxis(xaxis)
        .add_yaxis('采集数量(条)', yaxis, color='#26B99A')
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
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-情感分析"))
        )
    return c

# 词云
def wordcloud_base() -> WordCloud:
    """词云"""
    from sqlalchemy.orm import load_only
    data = (
        db.session.query(News.ndesc)
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