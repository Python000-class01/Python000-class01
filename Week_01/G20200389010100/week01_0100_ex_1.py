import time
import logging
import re

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


class Request:
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    session = requests.Session()
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.session.headers = self.header

    def get(self, *args, **kwargs):
        return self.session.get(*args, headers=self.header, **kwargs)

    def post(self, *args, **kwargs):
        return self.session.post(*args, **kwargs)


class Crawler:
    req = Request()

    @staticmethod
    def index_url(start: int = 0) -> str:
        return f'https://movie.douban.com/top250?start={start}'

    def login(self):
        login_url = 'https://accounts.douban.com/j/mobile/login/basic'
        form_data = {
            'ck': '',
            'name': '',
            'password': '',
            'remember': 'false',
            'ticket': ''
        }

        response = self.req.post(login_url, data=form_data)

    def index(self):
        movie_info_list = list()
        for x in range(0, 250, 25):
            url = self.index_url(x)
            rp = self.req.get(url)
            while rp.status_code != 200:
                rp = self.req.get(url)
                time.sleep(1)

            text = bs(rp.text, 'lxml')
            try:
                for movie in text.body.find('ol', class_='grid_view').find_all('li'):
                    movie_div = movie.find(name='div', attrs={'class': 'hd'})
                    movie_url = movie_div.contents[1].attrs['href']
                    movie_name = movie_div.contents[1].find('span').string
                    grace_div = movie.find(name='div', attrs={'class': 'star'})
                    grace = grace_div.find('span', attrs={'class': 'rating_num'}).string
                    comments_number, hot_comments = self.movie(movie_url)

                    movie_info = {
                        'movie_name': movie_name,
                        'grace': grace,
                        'comments_number': comments_number,
                        'hot_comments': hot_comments
                    }

                    movie_info_list.append(movie_info)
                    print(movie_info)
                    print(len(movie_info_list))
                    time.sleep(5)
            except Exception as err:
                logging.warning(err)
            # break
        self.save(movie_info_list)

    @staticmethod
    def save(data):
        df = pd.DataFrame(data=data)
        df.to_csv('./data.csv')

    def movie(self, url):

        rp = self.req.get(url)
        while rp.status_code != 200:
            rp = self.req.get(url)
            time.sleep(1)

        text = bs(rp.text, 'lxml')
        hot_comments = list()
        comments_number = 0
        try:
            comments_section = text.find(id='comments-section').extract()
            comments_text = comments_section.find('span', attrs={'class': 'pl'}).find('a').string
            comments_number = re.match('\S*\s(\d*)\s\S*', comments_text).group(1)

            hot_comments_section = comments_section.find(id='hot-comments')
            for hot_comment_section in hot_comments_section.find_all('div', class_='comment-item')[:5]:
                hot_comment = hot_comment_section.find('span', class_='short').string
                hot_comments.append(hot_comment)
        except Exception as err:
            logging.warning(err)

        return comments_number, hot_comments

    def run(self):
        self.login()
        self.index()


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
