####################
# 根据豆瓣图书《活着》短评制作词云

import requests
import lxml.etree
import jieba
import jieba.analyse
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import random
from os import path



####################
# 获取短评


def get_book_comment_text(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    book_comment_data = selector.xpath(
        "//span[@class='short']/text()")
    return ''.join(book_comment_data)

####################
# 分词


def cut_words(string):
    stop_words = './stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)

    textrank = jieba.analyse.textrank(string,
                                      topK=10,
                                      withWeight=False)
    return textrank

####################
# 生成词云


def draw_wordcloud(text):
    text_string = ','.join(text)
    # 当前文件所在目录
    dir = path.dirname(__file__)
    # 读取背景图片
    background_Image = np.array(Image.open(path.join(dir, 'sp_background.jpg')))

    # 提取背景图片颜色
    img_colors = ImageColorGenerator(background_Image)

    # 生成词云
    wc = WordCloud(
        width=600,  # 默认宽度
        height=200,  # 默认高度
        margin=2,  # 边缘
        ranks_only=None,
        prefer_horizontal=0.9,
        mask=background_Image,  # 背景图形,如果想根据图片绘制，则需要设置
        color_func=None,
        max_words=200,  # 显示最多的词汇量
        stopwords=None,  # 停止词设置，修正词云图时需要设置
        random_state=None,
        background_color='#ffffff',  # 背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
        font_step=1,
        mode='RGB',
        regexp=None,
        collocations=True,
        normalize_plurals=True,
        contour_width=0,
        colormap='viridis',  # matplotlib色图，可以更改名称进而更改整体风格
        contour_color='Blues',
        repeat=False,
        scale=2,
        min_font_size=10,
        max_font_size=200)

    wc.generate_from_text(text_string)

    # 根据图片色设置背景色
    wc.recolor(color_func=img_colors)

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    # 存储图像
    wc.to_file('./book.png')


if __name__ == '__main__':
    url = "https://book.douban.com/subject/4913064/comments/"
    book_comment_text = get_book_comment_text(url)
    word_cloud_text = cut_words(book_comment_text)
    draw_wordcloud(word_cloud_text)