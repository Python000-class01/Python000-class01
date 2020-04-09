# -*- coding: utf-8 -*-
import os
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import jieba.analyse
import jieba
from snownlp import  SnowNLP
from dbutil import MyDbUtil
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderMoviePipeline(object):
    def __init__(self):
        self.total_comment=None
    def get_keywords(self,text):
        # 基于TextRank算法进行关键词抽取   
        dir = path.dirname(__file__)       
        dict_dir=path.join(dir,'wc','user_dict.txt')
        print(dict_dir)
        jieba.load_userdict(dict_dir)
        jieba.analyse.set_idf_path(dict_dir)
        text_keywords = jieba.analyse.textrank(text,
        topK=40,                   # 权重最大的topK个关键词
        withWeight=False)
        text_keywordssss = jieba.analyse.textrank(text,
        topK=40,                   # 权重最大的topK个关键词
        withWeight=True)
        print(text_keywordssss)
        return text_keywords 
    def gen_image(self,text):
        # 当前文件所在目录
        dir = path.dirname(__file__)
        # 获取文本text
        text = self.get_keywords(text)
        dir_image = dir+ r'\wc\backgroud_image\kabigon.jpg'
        dir_fonts = dir+ r'\wc\fonts\simhei.ttf'
        # 读取背景图片
        background_Image = np.array(Image.open(dir_image))
        # 提取背景图片颜色
        img_colors = ImageColorGenerator(background_Image)
        # 生成词云
        wc = WordCloud(
        font_path=dir_fonts,
        width = 800,      
        #默认宽度
        height = 800,     #默认高度
        margin = 2,       #边缘
        ranks_only = None, 
        prefer_horizontal = 0.9,
        mask = background_Image,      #背景图形,如果想根据图片绘制，则需要设置    
        color_func = None,
        max_words = 40,  #显示最多的词汇量
        stopwords = None, #停止词设置，修正词云图时需要设置
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

        wc.generate_from_text(','.join(text))

        # 根据图片色设置背景色
        wc.recolor(color_func = img_colors)

        # 显示图像
        plt.imshow(wc, interpolation = 'bilinear')
        plt.axis('off')
        plt.tight_layout()
        # 存储图像
        # wc.to_file('love.png')

        plt.show()
    def process_item(self, item, spider):
        #item['movie_comment']
        self.gen_image(item['movie_comment'])
        return item
class SentimentsPipeline(object):
    def get_sentiments(self,text):
        s = SnowNLP (text)
        return s.sentiments
    def process_item(self, item, spider):
        #item['movie_comment']
        item['movie_trend']=self.get_sentiments(item['movie_comment'])
        return item

class SqlPipeline(object):
    dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'db' : 'db_test'
    }   
    def __init__(self,dbInfo):
        self.dbutils = MyDbUtil(dbInfo)
    def process_item(self, item, spider):
        #item['movie_comment']
        self.dbutils.insert("movie_data",[item,])
        return item

