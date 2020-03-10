from abc import abstractmethod

import requests
import re
from bs4 import BeautifulSoup as bs
from time import sleep
from typing import List
from typing import Tuple
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor
import threading
import pandas as pd



# 电影信息
class MovieInfo:
    def __init__(self, name, score, comments_num, top5_comments):
        self.name = name

        try:
            self.score = float(score)
        except Exception as e:
            self.score = 0
            print(f'score string invalid {score} {e}')

        try:
            self.comments_num = int(comments_num)
        except Exception as e:
            self.comments_num = 0
            print(f'comments_num string invalied {comments_num} {e}')

        self.top5_comments = top5_comments

    def __str__(self):
        info = f'BookInfo:\n\rmovie name:{self.name}\n\rscore:{self.score}\n\rshort comments number:{self.comments_num}\r\ntop5 comments:\n'
        for c in self.top5_comments:
            info += str(c)
        return info

# 短评信息
class ShortComment:
    def __init__(self, publisher, publish_time, content):
        self.publisher = publisher
        self.publish_time = publish_time
        self.content = content

    def __str__(self):
        return f'short comment:\n\tpublisher:{self.publisher}\n\tpublish time:{self.publish_time}\n\tcontnet:{self.content}\n'

class Spider:
    def __init__(self, urls):
        self.urls = urls

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def saveCSV(self, file_name):
        pass


class DoubanMovieSpider(Spider):
    def __init__(self, urls, max_movie_num = 250, max_thread_num = 5):
        super().__init__(urls)
        self.movie_info = []
        self.thread_pool = ThreadPoolExecutor(max_thread_num)
        self.movie_info_lock = threading.RLock()
        self.max_movie_num = max_movie_num

    def work(self):
        return self.getAllMovieInfo()

    def saveCSV(self, file_name):
        df = pd.DataFrame(columns=['movie_name', 'movie_score', 'comments_num',
                                      'comment1_publisher', 'comment1_time', 'comment1_content',
                                      'comment2_publisher', 'comment2_time', 'comment2_content',
                                      'comment3_publisher', 'comment3_time', 'comment3_content',
                                      'comment4_publisher', 'comment4_time', 'comment4_content',
                                      'comment5_publisher', 'comment5_time', 'comment5_content',
                                      ])

        for movie in self.movie_info:
            print(f'append {movie.name}')
            df.loc[df.shape[0]] = {'movie_name': movie.name,
                        'movie_score': movie.score,
                        'comments_num': movie.comments_num,
                        'comment1_publisher': movie.top5_comments[0].publisher,
                        'comment1_time': movie.top5_comments[0].publish_time,
                        'comment1_content': movie.top5_comments[0].content,
                        'comment2_publisher': movie.top5_comments[1].publisher,
                        'comment2_time': movie.top5_comments[1].publish_time,
                        'comment2_content': movie.top5_comments[1].content,
                        'comment3_publisher': movie.top5_comments[2].publisher,
                        'comment3_time': movie.top5_comments[2].publish_time,
                        'comment3_content': movie.top5_comments[2].content,
                        'comment4_publisher': movie.top5_comments[3].publisher,
                        'comment4_time': movie.top5_comments[3].publish_time,
                        'comment4_content': movie.top5_comments[3].content,
                        'comment5_publisher': movie.top5_comments[4].publisher,
                        'comment5_time': movie.top5_comments[4].publish_time,
                        'comment5_content': movie.top5_comments[4].content,
                        }

        df.to_csv(file_name, encoding='utf-8')
        print(df)


    def workerThreadFunc(self, movie_name, movie_score, comment_url):
        print(f'thread {threading.current_thread().getName()} is getting info of movie {movie_name}')
        comments = self.getTop5Commnet(comment_url)

        with self.movie_info_lock:
            if len(self.movie_info) < self.max_movie_num:
                self.movie_info.append(MovieInfo(str(movie_name), str(movie_score), str(comments[0]), comments[1]))

    # 获取所有页面所有书信息
    def getAllMovieInfo(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        header = {}
        header['user-agent'] = user_agent

        submit_cnt = 0
        futures = []
        for myurl in self.urls:
            sleep(3)
            with self.movie_info_lock:
                if len(self.movie_info) >= self.max_movie_num:
                    break

            response = requests.get(myurl, headers=header)

            print(f'get response length = {len(response.text)}')

            bs_info = bs(response.text, 'html.parser')
            for tags in bs_info.find_all('div', attrs={'class': 'info'}):
                names = []
                score = 0.0
                for atag in tags.find_all('a', ):
                    detail_url = atag.get('href')
                    for span_tag in atag.find_all('span', attrs={'class': 'title'}):
                        if len(span_tag.contents) > 0:
                            names.append(span_tag.contents[0])

                for span_tag in tags.find_all('span', attrs={'class': 'rating_num'}):
                    if len(span_tag.contents) > 0:
                        score = span_tag.contents[0]

                futures.append(self.thread_pool.submit(self.workerThreadFunc, str(names[0]), str(score), detail_url))
                submit_cnt += 1

                if submit_cnt >= self.max_movie_num:
                    break

        # 等待所有提交线程结束
        for f in futures:
            f.result()

        return deepcopy(self.movie_info)


    def getTop5Commnet(self, url) -> Tuple[int, List[ShortComment]]:
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        header = {}
        header['user-agent'] = user_agent

        comment_num = 0

        response = requests.get(url, headers=header)
        #print(f'get response length = {len(response.text)}')

        bs_info = bs(response.text, 'html.parser')
        for tags in bs_info.find_all('div', attrs={'id': 'comments-section'}):
            for span_tag in tags.find_all('span', attrs={'class': 'pl'}):
                for atag in span_tag.find_all('a', ):
                    if len(atag.contents) > 0:
                        comment_num = atag.contents[0]

            match_obj = re.match(r'^\D*([0-9]+)\D*$', comment_num)
            if match_obj:
                comment_num = int(match_obj.group(1))

        top5 = []
        for tags in bs_info.find_all('div', attrs={'id': 'hot-comments', 'class': 'tab'}):
            comment_cnt = 0

            for comment_tag in tags.find_all('div', attrs={'class': 'comment-item'}):
                publisher, publish_time, comment_content = '', '', ''

                for comment_info_tag in comment_tag.find_all('span', attrs={'class': 'comment-info'}):
                    for atag in comment_info_tag.find_all('a', ):
                        if len(atag.contents) > 0:
                            publisher = atag.contents[0]

                    for time_tag in comment_info_tag.find_all('span', attrs={'class': 'comment-time'}):
                        publish_time = time_tag.get('title')

                for content_tag in comment_tag.find_all('span', attrs={'class', 'short'}):
                    if len(content_tag.contents) > 0:
                        comment_content = content_tag.contents[0]

                top5.append(ShortComment(str(publisher), str(publish_time), str(comment_content)))

                comment_cnt += 1
                if comment_cnt >= 5:
                    break

            while len(top5) < 5:
                top5.append(ShortComment('unknown', 'unknown', 'unknown'))

        return (comment_num, top5)



if __name__ == '__main__':
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(20))
    spider = DoubanMovieSpider(urls, max_movie_num=250)
    all_movie_info = spider.work()

    for movie in all_movie_info:
        print('\n-----------------------------------------')
        print(movie)
        print('-----------------------------------------')

    spider.saveCSV('douban_top250_movie_info.csv')
