from snownlp import SnowNLP
import requests
from bs4 import BeautifulSoup as bs
import csv
import matplotlib.pyplot as plt
import numpy as np
import pymysql


# 获取html内容
def get_content_html(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    html_contents = bs(response.text, 'html.parser')
    return html_contents


def parser_content(comments_html):

    courseinfos = []

    for comments in comments_html.find_all('li', attrs={'class': 'comment-item'}):
        nickname = comments.find('a').get('title')
        vote = comments.find('span', attrs={'class': 'vote-count'}).getText()
        content= comments.find('p', attrs={'class': 'comment-content'}).find('span').getText()
        courseinfos.append((nickname, vote, content))

    return courseinfos


def save_csv(courseInfo):

    with open('comments.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(courseInfo)


def save_json(courseInfo):
    import json
    with open('comments.json','w',encoding='utf-8') as f:
        for item in courseInfo:
            item = {
                'nickname':item[0],
                'vote': item[1],
                'content': item[2]
            }
            jsonitem = json.dumps(item, ensure_ascii=False, indent=4)
            f.write(jsonitem+'\n')


def create_snownlp():

    source = open("comments.csv", "r")
    line = source.readlines()
    sentimentslist = []
    
    for i in line:
        s = SnowNLP(i)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)

    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('book-comments')
    plt.show()


# 连接数据库
def connect_mysql():

    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123456' , db='test', charset="utf8")
        print("成功连接数据库！")
        return conn

    except Exception as e:
        print(f'ERROR：{e}')


def  closeMysql(conn):

    conn.close()
    print("关闭数据库！")


def insert_comments(conn, list):

    cursor = conn.cursor()
    sql = "insert into douban_book_comments(book_name,book_vote,content) values(%s,%s,%s)"
    try:
        cursor.executemany(sql, list)
        print("插入book_comments" + str(cursor.rowcount) + "条数据")
        conn.commit()
    except Exception as e:
        print("插入book_comments数据库错误=" + e)
        conn.rollback()


if __name__ == '__main__':

    url = 'https://book.douban.com/subject/1084336/comments/'
    html = get_content_html(url)
    courseInfos = parser_content(html)
    print(courseInfos)
    save_json(courseInfos)
    save_csv(courseInfos)
    create_snownlp()
    conn = connect_mysql()
    insert_comments(conn, courseInfos)
    closeMysql(conn)