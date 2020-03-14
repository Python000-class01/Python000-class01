import pandas as pd
import requests
import time
from bs4 import BeautifulSoup as bs

url_name = "https://movie.douban.com/top250"
movie_list = [[], [], [], []]


def get_url_name():
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    header = {'user-agent': user_agent}
    response = requests.get(url_name, headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for a_tags in tags.find_all('a', ):
            time.sleep(2)
            get_movie_info(a_tags.get('href'))


def get_movie_info(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')

    # 短评数量
    movie_list[0].append(
        bs_info.find('div', {'class': 'mod-hd'}).find('span', {'class': 'pl'}).find('a', ).get_text()[3:-2])

    # 前5条短评的内容
    movie_short_com = ''
    for span_tags in bs_info.find_all('div', {'class': 'comment'}):
        for tags in span_tags.find_all('span', {'class': 'short'}):
            movie_short_com = movie_short_com + '\n' + tags.get_text()

    movie_list[1].append(movie_short_com)

    # 电影名称
    movie_list[2].append(bs_info.find('span', {'property': 'v:itemreviewed'}).get_text())

    # 评分
    movie_list[3].append(bs_info.find('strong', {'class': 'll rating_num'}).get_text())


def save_as_csv():
    dateframe = pd.DataFrame({'短评数量': movie_list[0], '前5条短评内容': movie_list[1], '电影名称': movie_list[2],
                              '评分': movie_list[3]})
    dateframe.to_csv('homework1.csv', index=False, sep=',')


if __name__ == '__main__':
    get_url_name()
    save_as_csv()
