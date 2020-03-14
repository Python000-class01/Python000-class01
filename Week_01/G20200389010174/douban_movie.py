import re
import requests
from bs4 import BeautifulSoup as bs
import csv

def get_content(urls):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
    response = requests.get(urls,headers={'User-Agent': user_agent})
    return  response.text

def parser_content(htmlContent):
    soup = bs(htmlContent, 'html.parser')
    bs_info = soup.find_all('div', attrs={'class': 'info'})
    for detail in bs_info:
        #获取电影名称
        movieName = detail.find('span', class_='title').get_text()

        #电影评分
        movieScore = detail.find('span', class_='rating_num').get_text()

        #评价人数
        movieCommentNum = detail.find(text=re.compile('\d+人评价'))
  	
        movieInfo.append((movieName, movieScore, movieCommentNum))

        
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}&filter=' for page in range(10))

from time import sleep

if __name__ =='__main__':

    #初始化列表
    movieInfo = []
    
    for page in urls: 
        content = get_content(page)
        parser_content(content)
        sleep(5)
    with open("douban_movie250" + ".csv", "w+", newline='', encoding='utf-8-sig') as f:
         writer = csv.writer(f)
         writer.writerow(['电影名', '评分', '评价数量','评论1','评论2','评论3','评论4','评论5'])
         for i in movieInfo:
             writer.writerow(i)
         print('csv写入完毕')
        
