import requests
import time
from bs4 import BeautifulSoup as bs
from lxml import etree
import re
import csv
import random


def get_url(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    return response


def get_top_books(url):
    """ 获取每页的top书籍数据：url和书籍名称 """
    per_page_books = []
    response = get_url(url)
    bs_info = bs(response.text, 'html.parser')
    book_title_link_list = bs_info.find_all('div', attrs={'class': 'pl2'})
    for tags in book_title_link_list:
        for a_tags in tags.find_all('a',):
            per_page_books.append((a_tags.get('href'), a_tags.get('title')))
    return per_page_books


def get_book_subject(book):
    """ 获取每本书籍的评分、短评数量、top5热评数据 """
    response = get_url(book[0]).content
    # 使用xpath获取指定元素
    selector = etree.HTML(response)
    # 评分
    rating_num = selector.xpath('//div/strong[@class="ll rating_num "]/text()')[0].strip()
    # 短评数量
    comments_num_string = selector.xpath('//div[@class="mod-hd"]/h2/span/a/text()')
    comments_num = re.findall(r'\d+', comments_num_string[0])[0]
    # top5评论
    top5_comments = selector.xpath('//div[@class="comment"]/p/span[@class="short"]/text()')[:5]
    comment_list = [comment.strip('\r\n') for comment in top5_comments]
    per_book_info = (book[1], rating_num, comments_num) + tuple(comment_list)
    print(list(per_book_info))
    return per_book_info


def save_utf8_csv(info_list):
    """ 将获得的数据通过'utf-8'格式保存在csv文件中 """
    headers = ['book_name', 'rating_num', 'comments_number', 'top_comment_01', 'top_comment_02', 'top_comment_03', 'top_comment_04', 'top_comment_05']
    # 'utf-8-sig'格式保存，excel打开后中文不会出现乱码的问题
    with open('./book_top_250.csv', 'a+', encoding='utf-8-sig') as file:
        file_csv = csv.writer(file)
        file_csv.writerow(headers)
        file_csv.writerows(info_list)
        print("该次写入完成！")


if __name__ == '__main__':
    urls = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(10))
    for url_ in urls:
        per_page_book = get_top_books(url_)
        per_page_book_info = []
        for per_book in per_page_book:
            per_nook_info = get_book_subject(per_book)
            per_page_book_info.append(per_nook_info)
            # 每次请求限制在1-6s之间
            time.sleep(random.randint(1, 6))
        save_utf8_csv(per_page_book_info)
        time.sleep(6)
