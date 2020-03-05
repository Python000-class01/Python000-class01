import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from time import sleep


def get_response(url):
    user_agent = user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header["user-agent"] = user_agent
    response = requests.get(url, headers=header)
    # print(response)
    return response


def get_movie_info(url):

    response = get_response(url)
    root = etree.HTML(response.content)
    movies = root.xpath('//ol/li//div[@class="hd"]')
    for movie in movies:
        title = movie.xpath('./a/span[@class="title"]/text()')[0]
        detail_url = movie.xpath('./a/@href')[0]
        print(title, detail_url, flush=True)
        get_hot_comments(detail_url, 5)
        sleep(1)


def get_hot_comments(url, count):
    response = get_response(url)
    root = etree.HTML(response.content)
    comments = root.xpath(
        '//*[@id="hot-comments"]//div/p/span[@class="short"]/text()')[:5]

    print(comments, flush=True)


if __name__ == "__main__":
    urls = tuple(
        f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))

    for url in urls:
        get_movie_info(url)
        sleep(5)
