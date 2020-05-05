"""
作业一：
使用 jieba 对豆瓣中任意一本书评或影评提前 top10 关键词，并绘制词云。

爬取《Python深度学习》的书评top10关键词，并绘制词云。豆瓣链接为：
https://book.douban.com/subject/30293801/
"""

import jieba.analyse
import requests
from lxml import etree
import numpy as np
from wordcloud import WordCloud
from matplotlib import pyplot as plt


class BookReview(object):

    def __init__(self, id, **kwargs):
        self.id = id
        self.comments = []
        # self.top = kwargs['top']
        # self.bg = kwargs['bg']

    def getComments(self, page=1):
        url = f'https://book.douban.com/subject/{self.id}/comments/hot?p={page}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        resp = requests.get(url, headers=headers).text
        html = etree.HTML(resp)
        if page == 1:
            count = html.xpath('/html/body/div[3]/div[1]/div/div[1]/div/div[1]/span/text()')
            if len(count) > 0:
                count = int(count[0].split(' ')[1])
            pages = count / 20 if count % 20 == 0 else int(count / 20) + 1
            for i in range(2, pages+1):
                self.getComments(i)
        comments = html.xpath('/html/body/div[3]/div[1]/div/div[1]/div/div[2]/div/ul/li/div[2]/p/span/text()')
        self.comments += list(map(lambda comment: comment.replace('\n', ''), comments))

    def getKeywords(self):
        keywords = []
        results = jieba.analyse.extract_tags('\n'.join(self.comments), topK=10, withWeight=True)
        print(results)
        for result in results:
            keywords.append(result)
        def takeSecond(elem):
            return elem[1]
        keywords.sort(key=takeSecond, reverse=True)
        keywords = list(map(lambda word: word[0], keywords))
        return keywords

    def genWordCloud(self):
        self.getComments()
        keywords = self.getKeywords()
        print(keywords)
        text_string = ','.join(keywords)
        ch_font = '/System/Library/Fonts/PingFang.ttc'
        wc = WordCloud(
            width=600,
            height=200,
            margin=2,
            ranks_only=None,
            prefer_horizontal=0.9,
            mask=None,
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
            max_font_size=150,
            font_path=ch_font)
        wc.generate_from_text(text_string)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        wc.to_file('top10.png')
        plt.show()


if __name__ == '__main__':
    review = BookReview('30293801')
    review.genWordCloud()
