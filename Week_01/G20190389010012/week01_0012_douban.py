#!/usr/local/bin/python3
"""
爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中
"""
import csv
import time
import random
import requests
from bs4 import BeautifulSoup

user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/80.0.3987.132 Safari/537.36",
    "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14379",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like "
    "Gecko) Chrome/51.0.2704.79 Safari/537.36",
    "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1113) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Mobile Safari/537.36 Edge/14.14379",
]


class DoubanSpider(object):
    """
    豆瓣电影TOP250爬虫
    """

    def __init__(self, user_agents):
        """
        init
        """
        self.headers = {
            "user-agent": random.choice(user_agents),
        }
        self.movie_top_url = "https://movie.douban.com/top250?start=%s&filter="

    def get_top_movie(self):
        """
        获取豆瓣电影top250名称、评分、和短评数量
        :return: list
        """

        url_tuple = tuple(self.movie_top_url % i * 25 for i in range(10))
        movie_list = []
        for url in url_tuple:
            response = requests.get(url, headers=self.headers)
            html_info = BeautifulSoup(response.text, 'lxml')
            for movie in html_info.find_all(name="div", attrs={"class": "info"}):
                movie_url = movie.find("a")["href"]
                movie_name = movie.find("span", {"class": "title"}).text
                movie_rating = movie.find("span", {"class": "rating_num"}).text
                movie_comments = movie.find_all("span")[-2].text[0:-3]
                comments = self.get_hot_comments(movie_url)
                movie_list.append([movie_name, movie_rating, movie_comments, comments])
            time.sleep(1)
        return movie_list

    def get_hot_comments(self, url):
        """
        获取电影短评
        :return:
        """
        hot_comments = []
        response = requests.get(url, headers=self.headers)
        html_info = BeautifulSoup(response.text, 'lxml')
        for info in html_info.find_all(name="div", attrs={"class": "comment"}):
            hot_comments.append(info.find("p").find("span").text)
        return ",".join(hot_comments)

    @staticmethod
    def save_csv(movie_list):
        """
        保存top250电影数据到csv
        :param list movie_list: 电影评分列表
        """
        with open("douban_movies.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(movie_list)

    def run(self):
        """
        启动
        """
        self.save_csv(self.get_top_movie())


if __name__ == '__main__':
    douban_spider = DoubanSpider(user_agents)
    douban_spider.run()
