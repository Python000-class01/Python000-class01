import requests
from bs4 import BeautifulSoup as bs
import csv
from time import sleep


def get_html(url):
    """
    获取请求页面的html
    :param href_url:
    :return:
    """
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/78.0.3904.108 Safari/537.36 "
    header = {'user-agent': user_agent}
    try:
        response = requests.get(url, headers=header)
        return response.text
    except Exception as e:
        print(e)


def get_href(href_url):
    """
    获取电影的超链接
    :param href_url:
    :return:
    """
    href_list = []
    html = get_html(href_url)
    bs_info = bs(html, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        href_list.append(tags.a.get('href'))
    return href_list


def get_movie_info(movie_url):
    """
    获取电影的具体信息
    :param movie_url:
    :return:
    """
    movie = []
    html = get_html(movie_url)
    bs_info = bs(html, 'html.parser')

    name = bs_info.find_all('span', attrs={'property': 'v:itemreviewed'})[0].string
    movie.append(name)
    rating = bs_info.find_all('strong', attrs={'class': 'll rating_num'})[0].string
    movie.append(rating)
    comment = bs_info.find_all('div', attrs={'id': 'comments-section'})[0]
    cmt_num = comment.find_all('span', attrs={'class': 'pl'})[0].a.string
    movie.append(cmt_num)
    short_cmt = comment.find_all('span', attrs={'class': 'short'})
    short_list = []
    for short in short_cmt:
        short_list.append(short.string)
    movie.append('\n'.join(short_list))

    return movie


def save2csv(row):
    """
    保存数据至CSV文件中
    :param row:
    :return:
    """
    with open('movies_info.csv', 'a', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(row)


if __name__ == "__main__":
    urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }' for page in range(10))
    for url in urls:
        for href in get_href(url):
            fin_movie = get_movie_info(href)
            print(fin_movie)
            save2csv(fin_movie)
            sleep(5)
