# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup as bs
import time
import logging

logging.basicConfig(level=logging.INFO)


def doubanTop250(url):
    logging.info('开始doubanTop250方法')
    user_agent = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    header = {}
    movie_href = 'https://movie.douban.com/subject/1292052/'
    header['user-agent'] = user_agent
    try:
        response = requests.get(url, headers=header)
        time.sleep(1)
    except Exception as e:
        logging.error("请求地址报错 {error}".format(error=e))
        raise

    bs_info = bs(response.text, 'html.parser')
    movie_info_list = []
    logging.info('获取请求成功')
    for tag in bs_info.find_all('div', attrs={'class': 'info'}):
        movie_info = {}
        for hd in (tag.find_all('div', attrs={'class': 'hd'})):
            movie_info["title"] = hd.find('span', class_='title').text
            logging.info("当前采集影片 {}".format(movie_info["title"]))
            movie_href = hd.a['href']

        for bd in (tag.find_all('div', attrs={'class': 'bd'})):
            db_span = bd.find_all('span')
            movie_info["taring_num"] = db_span[1].text
            movie_info["review_num"] = db_span[3].text

        if movie_href:
            response = requests.get(movie_href, headers=header)
            bs_inner_info = bs(response.text, 'html.parser')
            short_list = []
            for tag_inner in bs_inner_info.find_all('div', attrs={'id': 'hot-comments'}):
                short_list = [i.find('span', class_='short').text for i in tag_inner.find_all('div', attrs={'class': 'comment-item'})]
            movie_info['short_list'] = short_list
        movie_info_list.append(movie_info)
    return movie_info_list


if __name__ == '__main__':
    import pandas as pd
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))
    columns = ['电影名称', '评分', '评论数', '评论1', '评论2', '评论3', '评论4', '评论5']
    page_len = 1
    for url in urls:
        logging.info("Page{}".format(page_len))
        movie_info_list = (doubanTop250(url))
        data = [[movie['title'], movie['taring_num'], movie['review_num'], movie['short_list'][0], movie['short_list'][1], movie['short_list'][2], movie['short_list'][3], movie['short_list'][4]] for movie in movie_info_list]
        movie_info = pd.DataFrame(data=data, columns=columns)
        if page_len == 1:
            movie_info.to_csv('./movie.csv', encoding='utf-8', mode='a', index=False)
        movie_info.to_csv('./movie.csv', encoding='utf-8', mode='a', index=False, header=None)
        page_len += 1
