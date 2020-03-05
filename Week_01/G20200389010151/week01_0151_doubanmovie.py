import time
import json
import re
import requests
import tqdm
import csv
from lxml import etree
from fake_useragent import UserAgent

CSV_FILE = '豆瓣电影500.csv'

headers = {
    'cache-control': 'no-cache',
    'User-Agent': UserAgent().random,
    'Connection': 'close'
    }

top500_urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))

csv_header = ['电影名', '评分', '短评数量', '热评1', '热评2', '热评3', '热评4', '热评5']


# 主函数
def main():
    print('获取全部电影链接...')
    # 全部电影链接
    movie_urls = get_all_movies(top500_urls)
    # 写入 csv 表头
    write_csv(CSV_FILE, csv_header, 'w')
    print('获取Top500电影信息...')
    # 分别获取每部电影的 url, 并写入 csv
    for movie_url in tqdm.tqdm(movie_urls):
        movie = get_current_movie_info(movie_url)
        # 将电影清洗并整理格式
        movie_info = data_clean(movie)
        # 写入 csv
        write_csv(CSV_FILE, movie_info, 'a')
        time.sleep(1)


# 获得每部电影的 url
def get_all_movies(top500_urls):
    all_movie_urls = []
    for single_page_url in tqdm.tqdm(top500_urls):
        response = requests.get(single_page_url, headers=headers)
        e_html = etree.HTML(response.text)
        movie_links = e_html.xpath('//div[@class="pic"]/a/@href')
        all_movie_urls.extend(movie_links)
        time.sleep(1)

    return all_movie_urls


# 获取指定电影信息
def get_current_movie_info(movie_url):
    response = requests.get(movie_url, headers=headers)
    e_html = etree.HTML(response.text)
    movie_name = e_html.xpath('//div[@id="content"]/h1/span[1]/text()')
    movie_score = e_html.xpath('//strong[@class="ll rating_num"]/text()')
    comments_count = e_html.xpath('//div[@id="comments-section"]/div[1]/h2/span/a/text()')
    comments = e_html.xpath('//div[@id="hot-comments"]/div/div/p/span[@class="short"]/text()')
    movie = {
        'name': movie_name[0],
        'score': movie_score[0],
        'comments_count': comments_count[0],
        'comments': comments
    }
    return movie


# 数据清洗
def data_clean(movie):
    # 把具体的短评数提取出来
    comments_num = re.findall('\d+', movie['comments_count'])
    # 将电影信息拼成行
    movie_info = [movie['name'], movie['score'], comments_num[0]]
    movie_info.extend(movie['comments'])
    return movie_info


# 将电影信息导入 csv
def write_csv(file, line, write_type):
    out = open(file, write_type, encoding='utf-8')
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(line)


if __name__ == '__main__':
    main()
