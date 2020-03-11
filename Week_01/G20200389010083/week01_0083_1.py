import re
import csv
import time
import requests
from time import sleep
from lxml import etree
from bs4 import BeautifulSoup as bs

def get_response(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    return response

def get_movie_info(url):
    response = get_response(url)
    html = etree.HTML(response.text)
    ol = html.xpath("//*[@id='content']/div/div[1]/ol")[0]
    lis = ol.xpath("./li")
    top250_lis = []
    for li in lis:
        spans = li.xpath(".//span")
        a_s = li.xpath(".//a")
        movie_name = spans[0].text
        movie_score = li.xpath(".//span[@class='rating_num']")[0].text
        movie_comment_num = re.findall("\d+", li.xpath(".//div[@class='star']//span")[3].text)[0]
        # movie_comment_num = re.sub("\D", "", movie_comment_num)
        movie_detail_url = a_s[0].attrib['href']
        movie_comment_lis = get_movie_detail_info(movie_detail_url)
        top250_lis.append((movie_name, movie_score, movie_comment_num, movie_comment_lis[0], movie_comment_lis[1],
             movie_comment_lis[2], movie_comment_lis[3], movie_comment_lis[4]))
        # print(f" movie_name: {movie_name} \n movie_score: {movie_score} \n movie_comment_num: {movie_comment_num} \n movie_detail_url: {movie_detail_url}")
        # print(f" movie_comment: {movie_comment_lis}")
    with open("movie.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(top250_lis)

def get_movie_detail_info(url):
    response = get_response(url)
    html = etree.HTML(response.text)
    elements = html.xpath("//*[@id='hot-comments']")[0]
    divs = elements.xpath(".//div[@class='comment-item']")
    lis = []
    for div in divs:
        movie_comment = div.xpath("div/p/span")[0].text
        lis.append(movie_comment)
    return lis

if __name__ == '__main__':
    with open("movie.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["电影名称", "评分", "短评数量", "短评_1", "短评_2",
             "短评_3", "短评_4", "短评_5"])
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10)) #
    i = 1
    for url in urls:
        print(f'**************************| {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} | {i} |****************************')
        get_movie_info(url)
        i += 1
        sleep(5)