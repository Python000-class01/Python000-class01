import requests
from bs4 import BeautifulSoup as bs
import time
import jieba.analyse
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random

def get_url(url):
    global short
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent':user_agent}
    response = requests.get(url,headers=header)
    soup = bs(response.text, 'html.parser')
    comments = soup.find_all('div', attrs={'class':'comment'} )      
    for comment in comments:
        short += comment.find('span', attrs={'class':'short'}).text + ' \n'

urls = tuple(f'https://book.douban.com/subject/34433981/comments/hot?p={page}' for page in range(1,10))
short = ''

if __name__ == '__main__':
    for page in urls:
        get_url(page)
        time.sleep(1)
    #print(short)
    stop_words=r'day0402/extra_dict/stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)
    # 基于TF-IDF算法进行关键词抽取
    tfidf = jieba.analyse.extract_tags(short,
    topK=10,                   # 权重最大的topK个关键词
    withWeight=False) 
    #print(tfidf)
    text_string = ','.join(tfidf)
    # 生成词云
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

    wc.generate(text_string)


    # 显示图像
    plt.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout()
    # 存储图像
    wc.to_file('book.png')

    plt.show()