#conding=utf-8
__author__ = 'fangchao'

import requests
from  bs4 import BeautifulSoup as bs
import time
import csv

def crawler_url(top_number):
    '''
    通过传入的取TOP多少，计算出页码数量，暂不考虑小数情况，并取得所有排名电影的url
    :param top_number:
    :return:
    '''
    page_number = int(top_number / 25)
    movie_url = []
    for page_no in range(page_number):
        url = f'https://movie.douban.com/top250?start={page_no} * 25'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        header = {}
        header['user-agent'] = user_agent
        re = requests.get(url, headers=header, verify=False)
        bs_info = bs(re.text, 'html.parser')
        movie_info = bs_info.find_all('div', attrs={'class': 'hd'})
        for i in movie_info:
            for x in i.find_all('a'):
                movie_url.append(x.get('href'))
    return movie_url

def movie_info(number):
    '''
    根据电影url列表，逐个去爬取名称、评分、短评数、短评，并组成list，写入csv文件
    :param number:
    :return:
    '''
    file = open('data.csv', 'w', encoding='utf-8-sig',newline='')
    writer = csv.writer(file)
    writer.writerow(['电影名称','评分','短评数','短评1','短评2','短评3','短评4','短评5'])
    url_list = crawler_url(number)
    n = 1
    for url in url_list:
        # n = 1
        movie_data = []
        time.sleep(2)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        header = {}
        header['user-agent'] = user_agent
        re = requests.get(url, headers=header, verify=False)
        bs_info = bs(re.text, 'html.parser')
        movie_info = bs_info.find_all('div', attrs={'id': 'content'})
        for movie in movie_info:
            movie_name =  movie.find_all('span',attrs = {'property' : 'v:itemreviewed'})[0].get_text()
            movie_data.append(movie_name.split(' ')[0])
            movie_grade = movie.find_all('strong',attrs = {'class' : 'll rating_num'})[0].get_text()
            movie_data.append(movie_grade)
            dps = movie.find_all('div',attrs = {'class' : 'mod-hd'})[0].find_all('a',attrs = {'href' : f'{url}comments?status=P'})[0].get_text()
            movie_data.append(dps.split(' ')[1])
            for pjs in movie.find_all('div',attrs = {'id' : 'hot-comments'}):
                for pj in pjs.find_all('span',attrs = {'class' : 'short'}):
                    movie_data.append(pj.get_text())
                # print(movie_data)
        writer.writerow(movie_data)
        print(f'******************************************{n}')
        n = n + 1

    file.close()
    return 'game over'



if __name__ == '__main__':
    start_time = time.time()
    movie_info(250)
    stop_time = time.time()
    print(int(stop_time - start_time))
