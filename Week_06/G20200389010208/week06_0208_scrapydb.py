import jieba
import jieba.analyse
import pprint
import pandas as pd
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random
import os
from os import path
from snownlp import SnowNLP
import pymysql
from sqlalchemy import create_engine

def read_csvfile():
    df = pd.read_csv('D:\Documents\Geek\Python\code/\/book_utf8.csv')
    df.columns = ['star', 'vote', 'shorts']
    star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
    }
    df['new_star'] = df['star'].map(star_to_number)
    return df

def get_shorts(df):
    return df['shorts'].to_string()

def word_cloud(df):
    comment = get_shorts(df)
    stop_words=r'10/day0402/extra_dict/stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)
    tfidf = jieba.analyse.extract_tags(comment, topK=10, withWeight=False)
    pprint.pprint(tfidf)
    text_string = ','.join(tfidf)

    dir = path.dirname(__file__)
    background_Image = np.array(Image.open(path.join(dir, 'background.jpg')))
    img_colors = ImageColorGenerator(background_Image)

    wc = WordCloud(
      width = 600,      #默认宽度
      height = 200,     #默认高度
      margin = 2,       #边缘
      ranks_only = None, 
      prefer_horizontal = 0.9,
      mask = background_Image,      #背景图形,如果想根据图片绘制，则需要设置    
      color_func = None,
      max_words = 200,  #显示最多的词汇量
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

    wc.generate_from_text(text_string)
    wc.recolor(color_func = img_colors)

    plt.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout()

    wc.to_file('book.png')
    plt.show()

def _sentiment(shorts):
    s = SnowNLP(shorts)
    return s.sentiments

if __name__ == "__main__":
    df = read_csvfile()
    word_cloud(df)
    df["sentiment"] = df.shorts.apply(_sentiment)
    engine = create_engine("mysql+pymysql://root:password@localhost:3306/scrapydb?charset=utf8", echo=True)
    df.to_sql(name = 'sentiments', con = engine, if_exists = 'append', index = False, index_label = False)
