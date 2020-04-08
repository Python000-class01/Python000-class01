#region 作业要求
# 作业一：
# 使用 jieba 对豆瓣中任意一本书评或影评提前 top10 关键词，并绘制词云。
#endregion

import jieba
import pprint
import jieba.analyse

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread

import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

import os
import threading
import time
# jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持

strings_comment = []


def Get_Urls():
    return [
        f'https://book.douban.com/subject/30416923/collections?start={i*20}'
        for i in range(0, 10)
    ]


class Url_comments(object):
    def __init__(self, urls):
        self.urls = urls
        self.urlsResponse = []
        self.comments = []

    def Get_response(self, oneurl):
        time.sleep(1)
        #region cookie伪造
        jar = requests.cookies.RequestsCookieJar()
        jar.set('bid', 'ehjk9OLdwha', domain='.douban.com', path='/')
        jar.set('11', '25678', domain='.douban.com', path='/')
        #endregion
        useragent = UserAgent()
        response = requests.get(oneurl,
                                headers={'user-agent': useragent.random},
                                cookies=jar)
        self.urlsResponse.append(response.text)
        th1 = threading.Thread(target=self.save_responses_csv())
        th1.start()

    def Get_comments(self):
        for oneurl in self.urls:
            th = threading.Thread(target=self.Get_response(oneurl))
            th.start()

    def analyse_comments(self):
        for str_response in self.urlsResponse:
            bs_info = bs(str_response, 'lxml')
            bs_info = bs_info.find('div', attrs={'class': 'sub_ins'})
            for bs_item in bs_info.find_all(
                    'p', attrs={'style': "word-break: break-all;"}):
                str = bs_item.text.replace('\n', '')
                str = str.replace('  ', '')
                if not str == '':
                    strings_comment.append(str)
                    self.comments.append(str)
                    th2 = threading.Thread(target=self.save_comments_csv())
                    th2.start()

    def save_responses_csv(self):
        with open('save_responses.csv', 'a', encoding='utf-8') as file_1:
            for oneresponse in self.urlsResponse:
                file_1.write(f'{oneresponse}\n')

    def save_comments_csv(self):
        while len(self.comments) > 0:
            with open('save_comments.csv', 'a', encoding='utf-8') as file_2:
                onecomment = self.comments.pop()
                file_2.write(f'{onecomment}\n')


class Extract_tags(object):
    """ 提取关键词 类 """
    def __init__(self, List_str):
        self.List_string_Input = List_str

    def Get_tags(self):
        """ 提取关键词 """
        # 停止词
        stopwords = r'stopwords.txt'
        jieba.analyse.set_stop_words(stopwords)

        list_words = ['老唐', '本书']
        for word in list_words:
            jieba.suggest_freq(word, True)  # 调整词频
            jieba.add_word(word)  # 动态添加词典

        # for string in strings:
        #     result = jieba.cut(self.string_Input, use_paddle=True, HMM=False)  # paddle模式
        #     print('Default Mode:' + '/'.join(list(result)))

        string_str = ','.join(self.List_string_Input)
        # 提取关键词
        words = jieba.analyse.extract_tags(string_str,
                                           topK=10,
                                           withWeight=False)
        pprint.pprint(words)

        return ','.join(words)


class Create_wordcloud(object):
    """ 生成词云 类 """
    def __init__(self, str):
        self.string_Input = str

    def Get_word(self):
        """ 生成词云 """
        wc = WordCloud(
            width=600,  # 默认宽度
            height=200,  # 默认高度
            margin=2,  # 边缘
            ranks_only=None,
            prefer_horizontal=0.9,
            mask=None,  # 背景图形,如果想根据图片绘制，则需要设置  
            color_func=None,
            max_words=200,  # 显示最多词汇个数
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

        wc.generate_from_text(self.string_Input)

        # 显示图像
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        # 存储图像
        wc.to_file('book.png')
        plt.show()


if __name__ == '__main__':

    G_comment = Url_comments(Get_Urls())
    G_comment.Get_comments()
    G_comment.analyse_comments()

    extag = Extract_tags(strings_comment)
    C_wordcloud = Create_wordcloud(extag.Get_tags())
    C_wordcloud.Get_word()