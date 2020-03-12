# Python 训练营 第一周作业 第一部分 20200304 00:36 @纪如军
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import re
import csv
import unicodedata

#通过输入网址返回BS对象
def get_url(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url,headers=header)
    bs_response=bs(response.text,'html.parser')
    return bs_response

#通过输入网址区配解析内容并按行写入CSV
def get_films(url):
    bs_info= get_url(url)
    for tags in bs_info.find_all('div',attrs={'class': 'info'}):
        comment_url = tags.find('a').get('href')
        film_name = tags.find('a').find('span').get_text()
        film_rating = tags.find('span',attrs={'class': 'rating_num'}).get_text()
        film_comment_num = tags.find(string=re.compile('评价')).replace('人评价','')
        film_comments = get_comments(comment_url)
        f = open('top25.csv',mode ='a' , encoding= 'utf-8')
        csv_writer = csv.writer(f, lineterminator='\n')
        csv_writer.writerow([film_name,film_rating,film_comment_num,film_comments])
        f.close()

#通过输入网址解析评论内容并优化后返回数组
def get_comments(url): 
    bscomment = get_url(url)
    comments = []
    sleep(10)
    for tags in bscomment.find_all('span',attrs={'class': 'short'}):
        comments.append(unicodedata.normalize('NFKC',tags.get_text()).replace('\n','').strip())
    return comments

#定义采集网址入口列表
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }' for page in range(10))

#程序主入口
if __name__ == '__main__':
    for url in urls:
        print(url)
        get_films(url)