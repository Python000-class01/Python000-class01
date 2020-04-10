import requests
from bs4 import BeautifulSoup as bs
import pymysql
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from snownlp import SnowNLP


# 请求豆瓣
def request_douban(url):
    user_agent = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    header = {}
    header['user-agent'] = user_agent
    try:
        response = requests.get(url, headers=header)
        time.sleep(1)
    except Exception as e:
        raise

    return response


def next_page(url):
    response = request_douban(url)
    bs_info = bs(response.text, 'html.parser')
    total_comments = bs_info.find('span', attrs={'id': 'total-comments'})
    total_num = int(total_comments.text.split()[1])
    total_page_comments = bs_info.find_all('li', attrs={'class': 'comment-item'})
    comment_num = len(total_page_comments)
    page_list = [url+"hot?p={}".format(i) for i in range(1, int(total_num/comment_num)+1)]
    return page_list


def get_all_comments(url):
    movie_comment_list = []
    response = request_douban(url)
    bs_info = bs(response.text, 'html.parser')
    for comments in bs_info.find_all('div', attrs={'class': 'comment-list hot'}):
        for comment in comments.find_all('p', attrs={'class': 'comment-content'}):
            movie_comment_list.append(comment.find('span').text)
    return movie_comment_list


def reviews_snow_nlp(review_text):
    snp = SnowNLP(review_text)
    return snp.sentiments


dbInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'db': 'geektime'
}


class ConnDB(object):
    def __init__(self):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def run(self, sql, val):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        cur = conn.cursor()
        try:
            print(sql, val)
            cur.executemany(sql, val)
            conn.commit()
        except:
            conn.rollback()
            raise
        conn.close()


def sql_generator():
    return "INSERT INTO book_comments (col_comment, col_sentiments) VALUES (%s,%s)"



def exec_step():
    page_url_list = (next_page(url="https://book.douban.com/subject/5406559/comments/"))  # 加缪 - 鼠疫 全部评论
    for page_url in page_url_list:
        comment_list = get_all_comments(page_url)
        sql_val = tuple((str(reviews_snow_nlp(comment)), comment) for comment in comment_list)
        db_object = ConnDB()
        db_object.run(sql=sql_generator(), val=sql_val)
        break # 第一页循环跳出


if __name__ == '__main__':
    exec_step()

