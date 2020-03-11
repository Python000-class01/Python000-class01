# 作业一：
# 安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评
# 并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import re
import csv


# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评
def get_mv_info(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    movie_infos = []

    for tags in bs_info.find_all('div', attrs={'class': 'info'})[:2]:
        movie_info = []
        for hd_tags in tags.find_all('div', attrs={'class': 'hd'}):
            link_page_url = ''
            for a_tag in hd_tags.find_all('a'):
                sleep(5)
                link_page_url = a_tag.get('href')
                part_of_name = []
                for res in a_tag.find_all('span'):
                    part_of_name.append(res.get_text())
                    movie_name = ''.join(part_of_name)
                movie_info.append(movie_name)
            hot_comments = get_hot_comment(link_page_url)
            i = 0
            for comment in hot_comments:
                i = i+1
                movie_info.append(comment)
        for bd_tag in tags.find_all('div', attrs={'class': 'bd'}):
            for star_tag in bd_tag.find_all('div', attrs={'class': 'star'}):
                p = re.compile(r'<span>(.*?)人评价</span>', re.S)
                results = re.findall(p, str(star_tag))
                movie_info.append(results[0])
                for res1 in star_tag.find_all('span', attrs={'class': 'rating_num'}):
                    movie_info.append(res1.get_text())
                    print(movie_info)
        movie_infos.append(movie_info)

    print(movie_infos)
    return movie_infos


def get_hot_comment(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    results = []
    for comments in bs_info.find_all('div', attrs={'id': 'hot-comments'}):
        for comment in comments.find_all('p'):
            results.append(comment.text)
    return results[:5]


# 遍历豆瓣top250每一页
# urls = tuple(f'https://movie.douban.com/top250?start=0')
url_list = [f'https://movie.douban.com/top250?start=0']
# {page * 25}&filter=' for page in range(10))

# 通过name属性=main方法，主动调用get_my_url()方法，传入url
if __name__ == '__main__':

    csv_head = ['name', 'hot_comment1', 'hot_comment2', 'hot_comment3',
                'hot_comment4', 'hot_comment5', 'comment_num', 'rating_num',]
    csv_lines = []
    with open('douban_movie1.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f, delimiter=',', lineterminator='\n')
        f_csv.writerow(csv_head)
        for url in url_list:
            csv_lines = get_mv_info(url)
            f_csv.writerows(csv_lines)
