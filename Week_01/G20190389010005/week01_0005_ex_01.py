import threading
import time
import queue
import requests
from bs4 import BeautifulSoup as bs
import re
import csv


class ThreadCrawl(threading.Thread):
    def __init__(self, url_q, html_q):
        threading.Thread.__init__(self)
        print('爬取进程启动>>>')
        self.url_q = url_q
        self.html_q = html_q

    def run(self):
        while True:
            if not self.url_q.empty():
                items = self.url_q.get()
                html = get_html(items)
                self.html_q.put(html)
            else:
                time.sleep(1)
                break


class ThreadParse(threading.Thread):
    def __init__(self, html_q, data_save):
        threading.Thread.__init__(self)
        print('解析进程启动>>>')
        self.html_q = html_q
        self.data_save = data_save

    def run(self):
        while True:
            if not self.html_q.empty():
                html = self.html_q.get()
                parse(html, self.data_save)
            else:
                time.sleep(3)
                print('html为空')
                break


def get_html(url):
    response = requests.get(url=url, headers=headers)
    html_text = response.text
    bs_html = bs(html_text, 'html.parser')
    return bs_html


def parse(bs_html, data):
    print('解析了**')
    infos = bs_html.find_all('div', attrs={'class': 'info'})
    for info in infos:
        lst = []
        hd = info.contents[1]

        a_content = hd.find_all('a')[0]
        link = a_content['href']
        titles = a_content.strings
        title_str = ''.join(titles)
        title_str = re.sub('\n', '', title_str)
        lst.append(title_str)

        bd = info.contents[3]
        comment = bd.find('div', attrs={'class': 'star'})
        rating_num_tag = comment.find('span', attrs={'class': 'rating_num'})
        rating_num = rating_num_tag.string
        lst.append(rating_num)

        comment_num_tag = comment.find_all('span')[3]
        comment_num_str = comment_num_tag.string
        comment_num = re.sub('\D', '', comment_num_str)
        lst.append(comment_num)
        # 获取前五评论数
        movie_detail = requests.get(link, headers=headers)
        movie_detail_bs = bs(movie_detail.text, 'html.parser')

        comment_div = movie_detail_bs.find_all(name='div', attrs={'class': 'comment'})

        comments = []
        for comment in comment_div:
            short_full = comment.find(name='span', attrs={'class': 'hide-item full'})
            if short_full:
                comment_content = short_full.string
            else:
                short = comment.find(name='span', attrs={'class': 'short'})
                comment_content = short.string
            if comment_content:
                comments.append(comment_content)

        lst.append('||'.join(comments))
        data.append(lst)


def write_to_csv(data):
    with open('douban-movie.csv', 'a', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(['title', 'rating-number', 'comment-number', 'comments'])
        f_csv.writerows(data)


if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    headers = {
        "User-Agent": user_agent
    }

    url_queue = queue.Queue()
    content_q = queue.Queue()
    result = list()

    urls = [url_queue.put(f'https://movie.douban.com/top250?start={page * 25}') for page in range(10)]

    t1 = [ThreadCrawl(url_queue, content_q) for _ in range(url_queue.qsize())]
    t2 = [ThreadParse(content_q, result) for _ in range(url_queue.qsize())]

    for t in t1:
        t.start()
    time.sleep(2)

    for t in t2:
        t.start()

    for t in t1:
        t.join()

    for t in t2:
        t.join()

    write_to_csv(result)

