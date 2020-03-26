import requests
import re
import time
import csv
from bs4 import BeautifulSoup as bs

url_list = [f'https://book.douban.com/top250?start={i*25}' for i in range (10)]
# url = 'https://book.douban.com/top250?start=0'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'

header = {}

header['user-agent'] = user_agent
flag = 0
for url in url_list:
    response = requests.get(url,headers=header)



    bs_info = bs(response.text,'html.parser')

    with open('book_info.csv','a',encoding='utf8') as bf:
        book_writer = csv.writer (bf)

        for books in bs_info.find_all('tr',attrs={'class':'item'}):
            atag = books.find('div',class_='pl2').find('a')
            b_response = requests.get(atag.get('href'),headers=header)
            bs_detail =bs(b_response.text,'html.parser')
            # 获取图书名字
            book_name = atag.get('title')
            # 获取评分
            ratag = books.find('div',class_='star clearfix').find('span', class_='rating_nums')
            book_rate = ratag.string
            # 获取评论条数
            comments = books.find('div',class_='star clearfix').find('span', class_='pl')
            book_comemts = re.sub(r'\s+','',comments.string)

            # print('以下是前5条热评')

            comment_list = [comment_detail for comment_detail in bs_detail.find_all('p',attrs={'class':'comment-content'})[:5]]
            comment_items = [item.find('span',class_='short').string for item in comment_list]
            book_writer.writerow([book_name,book_rate,book_comemts,comment_items[0],comment_items[1],comment_items[2],comment_items[3],comment_items[4]])
            flag +=1
            print('成功录入%d部书籍的信息！'%flag)
            