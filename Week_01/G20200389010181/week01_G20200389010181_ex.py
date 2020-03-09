"""
1. 安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
并以 UTF-8 字符集保存到 csv 格式的文件中。

2. 使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，对 http://httpbin.org/post 进行 POST 方式请求，
并将请求结果转换为 JSON 格式（转换 JSON
的库和方式不限）。
"""

import requests
from bs4 import BeautifulSoup as bS
import json

# 请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}

file = '/Users/bai/Downloads/top250_movies.csv'


# 作业1
def home_work1():
    ids = list_all_ids()
    for m_id in ids:
        try:
            print(f'get movie_id:{m_id}')
            one_str = get_one_movie_csv(m_id)
        except AttributeError:
            print(f'error id: {m_id}, continue')
            # 出错时写入错误id
            err_id = f'id:{m_id} 抓去出错，跳过 \n'
            write_one(err_id)
            continue
        write_one(one_str)


# 作业2
def to_json_test():
    get_url = ' http://httpbin.org/get'
    post_url = 'http://httpbin.org/post'

    get_response = requests.get(get_url)
    get_json = get_response.json()
    print(f'get json 方式一 response 自带函数:{get_json}')

    post_response = requests.post(post_url)
    print(f'post json 方式二 json库 str to json:{json.loads(post_response.text)}')


def write_one(content):
    with open(file, 'a') as f:
        f.write(content)


# 获取top250全部电影id
def list_all_ids():
    all_ids = []
    crawl_end = False
    start = 0
    while not crawl_end:
        sub_ids = list_sub_ids(start)
        print(f'param start = {start}')
        if not sub_ids:
            crawl_end = True
        else:
            start += len(sub_ids)
            all_ids += sub_ids

    return all_ids


def list_sub_ids(start):
    url = 'https://movie.douban.com/top250'
    params = {"start": start}

    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200

    soup = bS(response.text, 'html.parser')
    items = soup.find_all('div', 'item')
    return list(map(get_id_from_item, items))


def get_id_from_item(item):
    href_tag = item.find('a')
    href = href_tag['href']
    end = href.rfind('/')
    start = href.rfind('/', 0, end)
    return href[start + 1: end]


# 电影名称、评分、短评数量和前 5 条热门短评
def get_one_movie_dict(m_id):
    movie_soup = get_soup(m_id)
    m_dict = {'name': get_name(movie_soup), 'score': get_score(movie_soup),
              'comment_count': get_comment_count(movie_soup), 'comments': get_5comment_list(movie_soup)}
    return m_dict


def get_one_movie_csv(m_id):
    movie_soup = get_soup(m_id)
    name = get_name(movie_soup)
    score = get_score(movie_soup)
    comment_count = get_comment_count(movie_soup)
    comments = get_5comment_list(movie_soup)
    comments_str = ",".join(comments)

    return f'{name},{score},{comment_count},{comments},{comments_str} \n'


def get_soup(m_id):
    url = f'https://movie.douban.com/subject/{m_id}/'
    response = requests.get(url, headers=headers)
    return bS(response.text, 'html.parser')


def get_name(html_soup):
    return html_soup.find('h1').find('span').text


def get_score(html_soup):
    return html_soup.find('strong', 'll rating_num').text


def get_comment_count(html_soup):
    score = html_soup.find_all('h2')[5].find('a').text
    start = score.find(' ')
    end = score.find(' ', start + 1)
    return score[start + 1: end]


def get_5comment_list(html_soup):
    comments = html_soup.find_all('div', 'comment')
    return list(map(get_comment_str, comments))


def get_comment_str(comment_soup):
    return comment_soup.find('p').find('span').text


# def to_csv_str(json):


if __name__ == '__main__':
    to_json_test()
