from flask import render_template
from . import home
from app.models import *
from app import db

from pyecharts.charts import Pie

@home.route('/')
@home.route('/index')
def result():
        #shorts = T1.query.all()[0:10]
        #shorts = T1.query.order_by(T1.sentiment.desc())[:10]
        comments_data = CommmetsData.query.all()
        presented_data = comments_data[:20]
        return render_template('/home/result.html', comments_data=presented_data, sentiment_pie=sentiment_pie(comments_data))


def sentiment_pie(comments_data):
        
        postive_count = 0
        negative_count = 0
        for item in comments_data:
                if item.sentiment_score > 0.5:
                    postive_count += 1
                else:
                    negative_count += 1

        pie = Pie()
        pie.add("", [["positve", postive_count], ["negative", negative_count]]) 
        return pie.render_embed()       

        #print(comments_data[0].sentiment_score)
        #input("pause")
        #if comments_data.

'''
def sentiment_pie(comments_data):
    from pyecharts.charts import Bar
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    
    return bar.render_embed()
'''

