# 使用 MySQL 将一本图书的短评、评分、情感分析结果进行储存
# 使用 Flask 展示 MySQL 中的情感倾向最高的前十条，进行展示。

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import time
from snownlp import SnowNLP
import pandas as pd

class Douban(object):
    def __init__(self,bookid):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/79.0.3945.130 Safari/537.36'}
        self.bookid = bookid
        self.url = f'https://book.douban.com/subject/{self.bookid}/'
        self.comments = []

    # 获取书名和评分信息
    def get_bookinfo(self):
        res = requests.get(url=self.url, headers=self.headers)
        page = etree.HTML(res.content)
        book_name = page.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
        book_rating = page.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
        return book_name, book_rating

    # 获取评论链接
    def get_comments_url(self):
        comment_url = f'https://book.douban.com/subject/{self.bookid}/comments/hot'
        res = requests.get(url=comment_url, headers=self.headers)
        page = etree.HTML(res.content)
        all_comments = page.xpath('//*[@id="total-comments"]/text()')[0].split(' ')[1]
        # comment_page = 6
        comment_page = int(int(all_comments)/20 + 1)
        comment_urls = [f'https://book.douban.com/subject/{self.bookid}/comments/hot?p=' + str(i + 1) for i in
                        range(comment_page)]
        return comment_urls

    # 获取单个页面短评
    def get_comments(self,url):
        res = requests.get(url=url,headers=self.headers)
        print(f'正在下载：{url}')
        page = etree.HTML(res.text)
        comments = page.xpath('//*[@id="comments"]/ul/li//span[@class="short"]/text()')
        for comment in comments:
            self.comments.append(comment)
        # print(comments)
        time.sleep(3)
        return self.comments
        # print(comment_page)

    # 多线程爬取短评，分析情感，并且统计出情感倾向排名前十的评价
    def thread_comments(self):
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.get_comments, self.get_comments_url())
        book_name, book_rating = self.get_bookinfo()
        df = pd.DataFrame(columns=['book_name','book_rating','comment'])
        i = 0
        for comment in self.comments:
            # print(book_name,book_rating,comment)
            df.loc[i] = [book_name,book_rating,comment]
            i += 1
        def get_sentiment(text):
            s = SnowNLP(text)
            return s.sentiments
        df['sentiment'] = df['comment'].apply(get_sentiment)
        df = df.sort_values(by='sentiment', ascending=False)
        df2 = df.iloc[0:10]
        df.to_excel('result0415.xlsx')

ax = Douban('5299764')
ax.thread_comments()