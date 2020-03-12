# 这是一个测试类
from time import sleep
import requests as req
from bs4 import BeautifulSoup as bs
import csv

def get_url_name(myurl, csv_writer):

   #设置header
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    # 请求页面
    response = req.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')
    # 循环抓取页面元素
    for tags in bs_info.find_all('div', class_='item'):
        list1 = []
        infoTag = tags.find_next('div', class_='info')
        #print("详情链接",infoTag.find_next('a').get('href'))
        #list1.append(infoTag.find_next('a').get('href'))
        info_href = infoTag.find_next('a').get('href')
        list1.append(info_href)
        #print(info_href)
        list1.append(get_Info(info_href))
        sleep(5)
        #print('标题',infoTag.find_next('span', class_='title').get_text())
        list1.append(infoTag.find_next('span', class_='title').get_text())
        #print('评分',infoTag.find_next('span', class_='rating_num').get_text())
        list1.append(infoTag.find_next(
            'span', class_='rating_num').get_text())
        ftags = infoTag.find('div', class_='star').find_all('span')
        #print('短评数量',ftags[-1].get_text()[0:-3])
        list1.append(ftags[-1].get_text()[0:-3])
        #print(list1)
        # 写行
        csv_writer.writerow(list1)
   

def get_Info(info_url):
    #设置header
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = req.get(info_url, headers=header)
    #print(response)
    bs_info = bs(response.text, 'html.parser')
    list1 = ''
    for tags in bs_info.find_all('div', class_='comment-item',limit=5):
        infotag = tags.find_next('span', class_='comment-info')
        list1 = list1 + infotag.find_next('span', class_='short').get_text()
    return list1
        



urls = tuple(
    f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))

if __name__ == '__main__':
    try:
        f = open('site.csv', 'w', encoding='utf_8_sig', newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["链接","标题","评分","短评数量"])
        for page in urls:
            get_url_name(page,csv_writer)
            sleep(5)
    finally:
        if f:
            f.close()
