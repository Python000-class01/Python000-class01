# -*- encoding=utf-8 -*-
# @File: week01_0108_ex.py.py
# @Author：wsr
# @Date ：2020/3/5 15:24

import requests
from bs4 import BeautifulSoup as bs
import xlwt
import re
import json

# 获取豆瓣电影列表页面信息
def get_douban_movie_html(doban_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    header = {'user-agent': user_agent};
    response = requests.get(doban_url, headers=header)
    html_contents = bs(response.text, 'html.parser')
    return html_contents

# 获取豆瓣电影详情评论
def get_doban_movie_comment(detail_url) :
    comments_top5 = []
    detail_content = get_douban_movie_html(detail_url)
    for detail in detail_content.find_all('div', attrs={'id': 'hot-comments'}):
        comments = detail.find_all('span', attrs={'class': 'short'})
        i = 0;
        for comment in comments:
            if i < 5:
                comments_top5.append(comment.getText() + '\n')
            else:
                break
            i += 1;
    return comments_top5

def get_douban_movie_list_contents(myurl):
    bs_movie_infos = get_douban_movie_html(myurl)
    movie_names = []
    movie_urls = []
    movie_rating_scores = []
    movie_people_totals = []
    movie_comments = []

    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    for info in bs_movie_infos.find_all('div', attrs={'class': 'info'}) :
        movie_name = info.find('span', class_='title').get_text()
        movie_url = info.find('a').get('href')
        movie_rating_score = float(info.find('span', class_='rating_num').get_text())
        movie_people_total = info.find('div', class_="star").find_all('span')[3].contents[0]
        movie_people_total = re.sub("人评价", '', movie_people_total, 0)

        movie_names.append(movie_name.strip())
        movie_urls.append(movie_url.strip())
        movie_rating_scores.append(movie_rating_score)
        movie_people_totals.append(movie_people_total.strip())
        comment = get_doban_movie_comment(movie_url)
        movie_comment = json.dumps(comment, ensure_ascii=False)
        movie_comments.append(movie_comment.strip())

    return movie_names, movie_urls, movie_rating_scores, movie_people_totals, movie_comments


def main(page, workbook, ws, file_name):
    names, urls, rating_scores, totals,comments = get_douban_movie_list_contents(page)

    #生成第一列
    for i in range(0,len(names)):
        ws.write(i+1,0,names[i])
        ws.write(i + 1, 1, rating_scores[i])
        ws.write(i + 1, 2, totals[i])
        ws.write(i + 1, 3, urls[i])
        ws.write(i + 1, 4, comments[i])

    workbook.save(file_name)

from time import sleep
if __name__ == '__main__':
    file_name = 'douban_movie_datas.xlsx';
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 新建一个表
    ws = workbook.add_sheet('movies', cell_overwrite_ok=True)

    # 设置表头
    titles = [u'名称', u'评分', u'评论人数', u'地址', u'评论']
    for i in range(0, len(titles)):
        ws.write(0, i, titles[i])

    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(5));
    for url in urls:
        main(url, workbook, ws, file_name)
        sleep(5)