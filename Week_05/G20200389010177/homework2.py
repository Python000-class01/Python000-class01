# 使用 snowNLP 预测豆瓣中任意一本书评或影评的评论是正向还是负向，并将评论内容和评分使用 PyMySQL 存入 MySQL 数据库
from bs4 import BeautifulSoup
import requests
import snownlp
import re
import time
import csv

class Douban(object):

    def __init__(self, bookid):
        self.bookid = bookid
        self.comments = []
        self.headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

    def get_bookinfo(self):
        url = f'https://book.douban.com/subject/{self.bookid}/'
        res = requests.get(url, headers=self.headers).text
        soup = BeautifulSoup(res,'html.parser')
        name = soup.select('span[property="v:itemreviewed"]')[0].get_text()
        rating = soup.select('strong[class="ll rating_num"]')[0].get_text()
        return name, rating


    def get_bookcomments(self,page=1):
        url = f'https://book.douban.com/subject/{self.bookid}/comments/hot?p={1}'
        res = requests.get(url,headers=self.headers).text
        _comment_number = BeautifulSoup(res,'html.parser').select('#total-comments')[0].get_text()
        comment_pages = int(re.findall(r"\d+",_comment_number)[0])//20+1
        # 待完善，页面范围需要设定为comment_pages（目前是10页），多线程完成此部分代码
        for page in range(2):
            url = f'https://book.douban.com/subject/{self.bookid}/comments/hot?p={page+1}'
            res = requests.get(url, headers=self.headers).text
            soup = BeautifulSoup(res,'html.parser').select('div[id="comment-list-wrapper"]')[0]
            comments =[comment.get_text() for comment in soup.select('span[class="short"]')]
            # print(comments)
            # time.sleep(5)
            self.comments.extend(comments)
        return self.comments



    def nlp(self):
        name, rating = self.get_bookinfo()
        comments = self.get_bookcomments()
        with open('douban_nlp.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(['name','rating','comment','sentiment'])
            for comment in comments:
                sentiments = snownlp.SnowNLP(comment).sentiments
                data=[name,rating,comment,sentiments]
                writer.writerow(data)

if __name__ == '__main__':
    Douban('1007305').nlp()
