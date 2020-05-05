import os
import glob
import  pandas as pd
path = r'/Users/huangzhijun/douban'
file = glob.glob(os.path.join(path, "*.csv"))

###   =======       将路径下的文件读取进来

dl = []
for f in file:
    dl.append(pd.read_csv(f))

###   =======       测试看看读取进来什么了
# for i in dl[:2]:
#     print(i)

###   =======       对爬取的短评内容进行清洗   ============
book = dl[0]
# print(book['book_name'][0])
# print(book['short_content'][1])
short_contents = book['short_content'].tolist()

###   =======        引用jieba分词，提取关键字   ============
import jieba.analyse
import pprint
class Key_Word(object):
    def __init__(self,content_list):
        self.text = content_list

    def keyWord(self,n):
        # stop_words =[ ]   ### 此处假装有stop_words吧..XDDD
        # jieba.analyse.set_stop_words(stop_words)
        tfidf = jieba.analyse.extract_tags(self.text,topK=n,withWeight=False)
        return tfidf
        # pprint.pprint(tfidf)


###   =======        绘制词云   ============
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random

# # 读取背景图片
# background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))
#
# # 提取背景图片颜色
# img_colors = ImageColorGenerator(background_Image)
# 根据图片色设置背景色
# wc.recolor(color_func = img_colors)


wc = WordCloud(
  width = 600,      #默认宽度
  height = 200,     #默认高度
  margin = 2,       #边缘
  ranks_only = None,
  prefer_horizontal = 0.9,
  mask = None,      #背景图形,如果想根据图片绘制，则需要设置
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


for i in range(2):
    book = dl[i]
    short_contents = book['short_content'].tolist()
    Text = Key_Word(str(short_contents))
    print(f'{book["book_name"][0]}',Text.keyWord(10))
    text = str(Text.keyWord(10))
    wc.generate_from_text(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

