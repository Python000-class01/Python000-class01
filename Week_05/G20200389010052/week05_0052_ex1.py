import numpy as np
import pandas as pd
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
from os import path
from PIL import Image


def word_segmentation():
    df = pd.read_csv('data.csv')
    jieba.enable_paddle()
    for line in df:
        keywrod = jieba.analyse.extract_tags(line, topK=10, withWeight=False)
        return keywrod


def word_cloud(words):
    # 获取当前路径
    dir = path.dirname(__file__)
    # 背景图片获取
    background_img = np.array(Image.open(path.join(dir, 'wordcloud.jpg')))
    # 抓取背景颜色
    img_colors = ImageColorGenerator(background_img)

    text_string = ','.join(words)
    wc = WordCloud(
        width=600,
        height=200,
        margin=2,
        ranks_only=None,
        prefer_horizontal=0.9,
        mask=background_img,  # 背景图形
        color_func=None,
        max_words=200,
        stopwords=None,
        random_state=None,
        background_color='#ffffff',
        font_step=1,
        mode='RGB',
        regexp=None,
        collocations=True,
        normalize_plurals=True,
        contour_width=0,
        colormap='viridis',
        contour_color='Blues',
        repeat=False,
        scale=2,
        min_font_size=10,
        max_font_size=200)
    wc.generate_from_text(text_string)
    wc.recolor(color_func=img_colors)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    wc.tofile('三体.png')


if __name__ == "__main__":
    keyword = word_segmentation()

    word_cloud(keyword)
