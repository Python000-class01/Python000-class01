# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import jieba.analyse
import pprint
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random
import re

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

import pandas as pd
from snownlp import SnowNLP

def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

Base = declarative_base()
class Comment(Base):
    #表名
    __tablename__="comments"
    #字段 属性
    id       = Column(Integer, primary_key=True)
    star     = Column(String(3))
    shorts   = Column(String(1500))
    name     = Column(String(50))
    category = Column(String(3))


class DoubanPipeline(object):

    def __init__(self, sql_url):
        self.sql_url = sql_url


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sql_url = crawler.settings.get('MYSQL_URI')
        )


    def open_spider(self, spider):
        engine = create_engine(
            self.sql_url,
            echo=True)
        self.engine = engine



    def process_item(self, item, spider):
        shorts   = item['shorts']
        star     = item['star']
        name     = item['name']
        category = item['category']
         
        #将Comment/star保存到数据库里
        DBSession = sessionmaker(bind = self.engine)
        session = DBSession()
        new_data = Comment(shorts=shorts, star=star, name=name, category=category)
        session.add(new_data)
        session.commit()
        session.close()

        return item


    def close_spider(self, spider):
        """先关闭数据库连接"""
        self.engine.dispose()

        """SnowNLP对所有的短评进行情感分析，并将结果存如文件"""
        #df = pd.read_csv('./test1.txt', encoding='gb18030', names=['star','comment'])
        #df['sentiment'] = df.comment.apply(_sentiment)
        #mean = df.sentiment.mean()
        #with open('./wxcdndyz_rate.txt', 'w') as f:
        #    f.write(str(mean))

        '''
        """爬虫结束后将评论结果转化为词云显示"""
        stop_words = r'./stop_word.txt'
        with open('./wxcdndyz.txt', 'r') as f:
            text = f.read()


        jieba.enable_paddle()
        jieba.analyse.set_stop_words(stop_words)
        #tfidf模式
        fc = jieba.analyse.extract_tags(text, topK=100, withWeight=False)          
        #textRank模式
        #fc = jieba.analyse.textrank(text, topK=100, withWeight=False) 

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
        wc.to_file('wxcdndyz.png')

        plt.show()
        '''
        



