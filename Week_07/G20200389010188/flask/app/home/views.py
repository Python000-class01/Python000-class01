from flask import Flask
from flask import redirect, url_for,render_template, request, render_template
from . import home
from app.models import *
from app import db
from app.home.forms import SearchForm

import jieba.analyse
import pandas as pd
from snownlp import SnowNLP
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import time

def _sentiment(text):
        s = SnowNLP(text)
        sentiment = '负向'

        if(s.sentiments > 0.8):
                sentiment = '正向'
        elif(s.sentiments > 0.5):
                sentiment = '中立'

        return sentiment

@home.route('/', methods=['GET', 'POST'])
def index():
        print(f'in index function, method is {request.method}')
        form = SearchForm()
        if request.method == 'POST':
                print(f'validate result is {form.validate_on_submit()} {form.name.data} {form.category.data}')
                if form.validate_on_submit():
                        name     = form.name.data
                        category = form.category.data
                        print(f'name={name}, category={category}')

                        return redirect(url_for('home.dashboard', name=name, category=category))
        return render_template('/home/index.html', form=form)

@home.route('/dashboard?name=<name>?category=<category>')
def dashboard(name, category):
        print(f'in dashboard url, name={name}, category={category}')

        """调用scrapy对指定的书或者电影进行爬虫（暂时还未实现）"""

        """读取数据库，将数据读取到Pandas中, 理应单独写函数，但暂时没时间做"""
        sql = f'select star, shorts from comments where name=\'{name}\' and category=\'{category}\''
        #records = T1.query.filter_by(name=name, category=category)
        df = pd.read_sql_query(sql, db.get_engine())
        comments = T1.query.all()[0:20]

        """数据清理"""
        #去重,缺失项删除
        df2 = df.drop_duplicates().dropna()

        star_to_number = {
                '力荐' : 5,
                '推荐' : 4,
                '还行' : 3,
                '较差' : 2,
                '很差' : 1
        }

        df2['new_star'] = df2['star'].map(star_to_number)

        #取出star列进行统计
        stars = df2.groupby('new_star')['new_star'].count().reset_index(name='count')
        stars2 = stars.sort_values (by = ['new_star'], ascending = False)
        number_to_star = {
                5 : '力荐',
                4 : '推荐',
                3 : '还行',
                2 : '较差',
                1 : '很差'
        }
        stars2['star'] = stars2['new_star'].map(number_to_star)
        print(f'测一哈3 {stars2}')


        #根据评分统计绘图
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
        plt.figure(figsize=(8,6), dpi=80)
        values=stars2['count']
        indexes=stars2['star']
        width = 0.35
        plt.bar(indexes, values, width, label="rainfall", color="#87CEFA") 
        plt.xlabel('评分')
        plt.ylabel('个数')
        plt.title('短评评分统计')
        plt.savefig(f'app/static/images/dptj_{name}.png')
        plt.close()       

        #取出shorts进行NLP统计
        #df3 = df2.copy()
        pl = df2.loc[:, ['shorts']]
        
        pl['sentiment'] = pl.shorts.apply(_sentiment)
        
        pl2 = pl.groupby('sentiment')['sentiment'].count().reset_index(name='count')
        print(f'看一哈 {pl2}')

        plt.figure(figsize=(8,6), dpi=80)
        labels = pl2['sentiment']
        counts = pl2['count']
        explode = (0,0.3,0)
        plt.pie(counts,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
        plt.title('短评情感统计')
        plt.savefig(f'app/static/images/qgtj_{name}.png')
        plt.close()


        #取出shorts列进行NLP分析，并统计正向(0.8~1)、中立(0.5~0.8)、负向(0~0.5)个数
        shorts = df2['shorts']
        
        stop_words = r'./stop_word.txt'

        jieba.enable_paddle()
        jieba.analyse.set_stop_words(stop_words)   
        #tfidf模式
        fc = jieba.analyse.extract_tags(" ".join(shorts), topK=100, withWeight=False)

        wc = WordCloud(
            width = 600,      #默认宽度
            height = 200,     #默认高度
            margin = 2,       #边缘
            ranks_only = None, 
            prefer_horizontal = 0.9,
            mask = None,      #背景图形,如果想根据图片绘制，则需要设置    
            color_func = None,
            max_words = 200,  #显示最多的词汇量
            stopwords = './stop_word.txt', #停止词设置，修正词云图时需要设置
            random_state = None,
            background_color = '#ffffff',#背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
            font_step = 1,
            mode = 'RGB',
            regexp = None,
            collocations = True,
            normalize_plurals = True,
            contour_width = 0,
            colormap = 'viridis',#matplotlib色图，可以更改名称进而更改整体风格
            contour_color = 'Blues',
            repeat = False,
            scale = 2,
            min_font_size = 10,
            max_font_size = 200)

        wc.generate_from_text(" ".join(fc))

        # 显示图像
        plt.imshow(wc, interpolation = 'bilinear')
        plt.axis('off')
        plt.tight_layout()
        # 存储图像
        wc.to_file('app/static/images/wc.png')

        #plt.savefig('/static/images/wc.png')      

        return render_template('/home/index2.html', wc_url = '/static/images/wc.png', title=name, 
                dptj_url = f'/static/images/dptj_{name}.png', qgtj_url = f'/static/images/qgtj_{name}.png', 
                comments=comments)


