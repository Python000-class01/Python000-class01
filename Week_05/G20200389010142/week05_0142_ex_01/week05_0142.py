import requests
import lxml.etree

import jieba
import jieba.analyse

import os
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread

def download_data(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    header = {'user-agent' : user_agent}

    response = requests.get(url, headers = header)
    movie_info = lxml.etree.HTML(response.text)

    # 单页所有短评
    comments = movie_info.xpath('//span[@class="short"]/text()')
    for comment in comments:
        comment_list.append(comment)


def jieba_info(comments):
    stop_words= path.dirname(__file__)+'/stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)

    tfidf = jieba.analyse.extract_tags(comments,
                                        topK=50,                   # 权重最大的topK个关键词
                                        withWeight=False)         # 返回每个关键字的权重值
    # print(tfidf)
    text = ','.join(tfidf)

    return text


def wordcloud_plot(text):
    # # 当前文件所在目录
    dir = path.dirname(__file__)
    # print(dir)
    background_Image = np.array(Image.open(path.join(dir, 'qq.jpg')))
    img_colors = ImageColorGenerator(background_Image)

    # 生成词云
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

    wc.generate_from_text(text)

    # 根据图片色设置背景色
    wc.recolor(color_func = img_colors)

    # 显示图像
    plt.imshow(wc, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout()
    # 存储图像
    wc.to_file(dir+'\\love.png')

    plt.show()


pages = tuple(f'https://book.douban.com/subject/6913343/comments/hot?p={page}' for page in range(58))
from time import sleep

if __name__ == "__main__":
    comment_list = []
    for page in pages:
        download_data(page)
        sleep(2)
    comments = ''.join(comment_list)

    with open(path.dirname(__file__)+'/text.txt', 'w', encoding='utf-8') as f:
        f.write(comments)

    text = jieba_info(comments)
    wordcloud_plot(text)



