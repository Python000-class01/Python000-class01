import requests
import re
import csv
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


def get_movie_info(url, csv_writer):
    response = get_response(url)
    root = etree.HTML(response.content)
    movie_items = root.xpath('//ol/li//div[@class="item"]')
    for item in movie_items:
        title = item.xpath(
            './div[@class="info"]/div[@class="hd"]//span[@class="title"]/text()')[0]
        rating = item.xpath(
            './div[@class="info"]/div[@class="bd"]//span[@class="rating_num"]/text()')[0]
        detail_url = item.xpath(
            './div[@class="info"]/div[@class="hd"]//a/@href')[0]
        #print(title, rating, detail_url, flush=True)
        comment_info = get_comment_info(detail_url, 5)
        sleep(1)
        result_list = [title, rating] + comment_info
        print(result_list, flush=True)
        csv_writer.writerow(result_list)


def get_comment_info(url, count):
    response = get_response(url)
    root = etree.HTML(response.content)
    comment_count_text = root.xpath(
        '//*[@id="comments-section"]/div[1]/h2/span/a/text()')[0]
    comment_count = re.findall(r"\d+", comment_count_text)[0]
    #print(f"comment count: {comment_count}")

    comments = root.xpath(
        '//*[@id="hot-comments"]//div/p/span[@class="short"]/text()')[:5]

    #print(comments, flush=True)
    return [comment_count] + comments


if __name__ == "__main__":
    urls = tuple(
        f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))

    result_file = open("douban_movie_top_250_info.txt",
                       "w", newline='', encoding='utf-8')
    wr = csv.writer(result_file, delimiter=',')
    for url in urls:
        get_movie_info(url, wr)
        sleep(5)

    result_file.close()
    print("done.")
