#-*- coding:utf-8 -*-

import requests
import lxml.etree
from time import sleep
import pandas as pd
import numpy as np
from snownlp import SnowNLP
import pymysql

#抓取短评
def crawl(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    try:
        response = requests.get(url, headers=header, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f'抓取出错：{url}  原因：{e}')

    selector = lxml.etree.HTML(response.text)
    comments = selector.xpath('//div[@class="sub_ins"]//table')

    reviews_text = []
    for comment in comments:
        star = ''.join(comment.xpath('.//p[1]/span[@title]/@title'))
        shorts = comment.xpath('.//p[2]/text()')[0].strip()
        reviews_text.append([star, shorts])
    return reviews_text

#数据处理，标记情感分析
def data_process(data):
    columns = ['star','shorts']
    df = pd.DataFrame(columns=columns,data=data)
    star_to_number = {
                    '力荐' : 5,
                    '推荐' : 4,
                    '还行' : 3,
                    '较差' : 2,
                    '很差' : 1
                    }

    df['new_star'] = df['star'].map(star_to_number)
    df['shorts'] = df['shorts'].str.split(',',expand=True).replace('',np.nan)
    df = df.dropna()

    def _sentiment(text):
        s = SnowNLP(text)
        return s.sentiments

    df["sentiment"] = df.shorts.apply(_sentiment)
    return df

#访问Mysql数据库类
class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls
        self.run()

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                #result.append(cur.fetchone())
            cur.close()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f'Error info: {e}')
        conn.close()

#写入数据库
def save_to_mysql(data):
    dbInfo = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'root',
        'password' : 'rootroot',
        'db' : 'test'
    }

    create_table_sql = ["CREATE TABLE DoubanBook (new_star VARCHAR(10), shorts VARCHAR(2048), sentiment FLOAT)"]
    db = ConnDB(dbInfo, create_table_sql)

    sqls = []
    for index, row in data.iterrows() : 
        sqls.append(f'INSERT INTO DoubanBook (new_star,shorts,sentiment) VALUES ({row["new_star"]},"{row["shorts"]}",{row["sentiment"]})')

    db = ConnDB(dbInfo, sqls)
    return



if __name__=="__main__":
    urls = tuple(f'https://book.douban.com/subject/30414743/collections?start={page * 20}' for page in range(10))
    douban_book_review = []
    
    for url in urls:
        result = crawl(url)
        if result:
            douban_book_review += result
            sleep(3)

    #print(douban_book_review)
    pd_data = data_process(douban_book_review)
    print(pd_data['sentiment'].mean())
    save_to_mysql(pd_data)




        





