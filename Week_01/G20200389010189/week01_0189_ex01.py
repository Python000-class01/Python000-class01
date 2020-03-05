# 抓取豆瓣top250电影数据
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import random
import csv

# 抓取链接

def getMovieUrl(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {}
    headers['user-agent'] = user_agent
    url_list = []
    for num in range(0, 250, 25):
        final_url = url + str(num)

        response = requests.get(final_url, headers=headers)
        sleep(random.random())
        bs_info = bs(response.text, 'html.parser')
        for tags in bs_info.find_all('div', attrs={'class':'hd'}):
            for atag in tags.find_all("a", ):
                url_list.append(atag.get('href'))
    return url_list

# 抓取页面详细信息

def getDetailData(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {}
    headers['user-agent'] = user_agent
    response = requests.get(url, headers=headers)
    sleep(random.random())
    bs_info = bs(response.text, 'html.parser')

    data_list = []

    name = bs_info.find('span', attrs={'property':'v:itemreviewed'}).get_text()
    rating_num = bs_info.find('strong', attrs={'class':'ll rating_num'}).get_text()
    # comment_num = bs_info.find_all('h2', )[5].find('span', attrs={'class': 'pl'}).find('a', ).get_text().replace('全部', '').replace(' ', '').replace('条', '')
    comment = bs_info.find_all('div', attrs={'class': 'comment'})
    comment_num = bs_info.find('div', attrs={'class': 'mod-hd'}).find('h2',).find('span', attrs={'class': 'pl'}).find('a', ).get_text().replace('全部', '').replace(' ', '').replace('条', '')
    for com in comment:
        data_list.append([name, rating_num,  comment_num, com.find('span', attrs={'class': 'short'}).get_text().replace('\n', '')])

    return data_list

# 将数据写进CSV

def writeData(data_list):
    f = open('./movie_data1.csv', 'a+', encoding='UTF-8')
    csv_writer = csv.writer(f)
    for data in data_list:
        csv_writer.writerow(data)

if __name__  ==  '__main__':
    url = 'https://movie.douban.com/top250?start='
    url_list = getMovieUrl(url)
    f = open('./movie_data1.csv', 'a', encoding='UTF-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['电影名称', '评分', '短评数量', '前 5 条热门短评'])
    f.close()
    for a in url_list:
        print(a)
        data_list = getDetailData(a)
        writeData(data_list)