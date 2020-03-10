import csv
import requests
from time import sleep
from lxml import etree
from bs4 import BeautifulSoup as bs

def get_movie_info(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    html = etree.HTML(response.text)
    ul = html.xpath("//ol[@class='grid_view']")[0]
    lis = ul.xpath("./li")
    with open("movie.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["电影名称", "评分", "短评数量", "短评_1", "短评_2",
             "短评_3", "短评_4", "短评_5"])
        for li in lis:
            spans = li.xpath(".//span")
            a_s = li.xpath(".//a")
            movie_name = spans[0].text
            movie_score = li.xpath(".//span[@class='rating_num']")[0].text
            movie_comment_num = spans[len(spans) - 2].text#.replace('人评价','')
            movie_detail_url = a_s[0].attrib['href']
            movie_comment_lis = get_movie_detail_info(movie_detail_url)
            print(f" movie_name: {movie_name} \n movie_score: {movie_score} \n movie_comment_num: {movie_comment_num} \n movie_detail_url: {movie_detail_url}")
            # print(f" movie_comment: {movie_comment_lis}")
            writer = csv.writer(csvfile)
            writer.writerow([movie_name, movie_score, movie_comment_num, movie_comment_lis[0], movie_comment_lis[1],
             movie_comment_lis[2], movie_comment_lis[3], movie_comment_lis[4]])
            print('*********************************************************')

def get_movie_detail_info(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    html = etree.HTML(response.text)
    elements = html.xpath("//div[@id='hot-comments']")[0]
    divs = elements.xpath(".//div[@class='comment-item']")
    lis = []
    for div in divs:
        movie_comment = div.xpath(".//span[@class='short']")[0].text
        lis.append(movie_comment)
    return lis

if __name__ == '__main__':
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10)) #
    for url in urls:
        get_movie_info(url)
        sleep(5)