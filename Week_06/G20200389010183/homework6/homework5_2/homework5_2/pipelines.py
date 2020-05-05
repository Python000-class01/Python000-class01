# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from lxml import etree
import jieba.analyse
import pprint
import re
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from snownlp import SnowNLP

Base = declarative_base()


class Homework52Pipeline(object):
    def open_spider(self, spider):
        self.article = open('newsCrawl/comments/comments2.txt', 'w')

    def close_spider(self, spider):
        self.article.close()
        # with open('newsCrawl/comments/comments2.txt', 'r') as f:
        #     text = f.read()
        #     tfidf = jieba.analyse.extract_tags(text, topK=10, withWeight=False)
        #     pprint.pprint(tfidf)
        #     print(','.join(tfidf))
        #     self.gene_word_cloud(','.join(tfidf))

    @staticmethod
    def gene_word_cloud(text):
        font = "/System/Library/fonts/PingFang.ttc"
        wc = WordCloud(
            width=600,  # 默认宽度
            height=200,  # 默认高度
            margin=2,  # 边缘
            ranks_only=None,
            prefer_horizontal=0.9,
            mask=None,  # 背景图形,如果想根据图片绘制，则需要设置
            color_func=None,
            max_words=200,  # 显示最多的词汇量
            stopwords=None,  # 停止词设置，修正词云图时需要设置
            random_state=None,
            background_color='#ffffff',  # 背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
            font_step=1,
            font_path=font,
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

        wc.generate_from_text(text)

        # 存储图像
        wc.to_file('饥饿站台top10关键词2.png')

    def process_item(self, items, spider):
        # print("=" * 20)
        for item in items['comments']:
            comment_html = item['comment']
            # print(comment_str)
            # comment_div = etree.XML(comment_str)
            # comment = comment_div.xpath('/div/div/div')
            # print("=" * 20)
            # print(comment)
            # for text in comment:
            #     print("*" * 20)
            #     print(text)
            # txt = nltk.clean_html(comment_html)
            # soup = BeautifulSoup(comment_html)
            # txt = soup.get_text()
            # txt = re.sub(r"[\n\t\s]*", "", txt)
            item['comment'] = comment_html
            self.article.write(comment_html)
        return items


class SaveToDbPipeline(object):
    star_to_number = {
        '5': '力荐',
        '4': '推荐',
        '3': '还行',
        '2': '较差',
        '1': '很差'
    }

    def open_spider(self, spider):
        engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4", echo=True)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, items, spider):
        for item in items['comments']:
            s2 = SnowNLP(item['comment'])
            sent = s2.sentiments
            sentStr = str(int(sent))
            print(sent)
            print("=" * 50)
            # old _data = CommentDO.query.filter_by(id=item['id']).first
            new_data = CommentDO(id=item['id'], rank=item['rank'], comment=item['comment'], sentiments=sent)
            old_data = self.session.query(CommentDO).filter_by(id=item['id']).first()
            if not old_data:
                self.session.add(new_data)
            self.session.commit()


class CommentDO(Base):
    # 表名
    __tablename__ = "jezt_comment_short"
    # 字段，属性
    id = Column(Integer, primary_key=True)
    comment = Column(String(65535))
    rank = Column(Integer)
    sentiments = Column(String(20))
