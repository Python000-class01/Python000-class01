# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup 
import pymysql
import threading
import queue
import time


class DBOperation:
    db_conn = pymysql.connect(host='localhost', db='python_train', user='python_train', passwd='python_train',port=3307)
    def __init__(self):        
        self.db_cursor = DBOperation.db_conn.cursor()
        
    def test_db_conn(self):
        cursor = self.db_cursor.execute('select version();')
        data = cursor.fetchone()
        print(data)
    def insert(self,sql, values):
        res = self.db_cursor.execute(sql, values)
        self.db_conn.commit()
        return res

    def insert_many(self, sql, values):
        res = self.db_cursor.executemany(sql, values)
        self.db_conn.commit()
        return res

    def select(self, sql, values=None):
        res = self.db_cursor.execute(sql, values)
        return self.db_cursor.fetchall()

        # data = cursor.fetchone()
    def close(self):
        self.db_conn.close()

class MovieDBO:
    
    def __init__(self):
        self.db_operation = DBOperation()
        

    def insert(self,movie):
        sql = "insert into douban_movie(movie_name,movie_link,movie_rating_level,movie_rating_num,movie_rating_persons) values(%s,%s,%s,%s,%s)"
        res = self.db_operation.insert(sql,(movie.movie_name,movie.movie_link,
        movie.movie_rating_level, movie.movie_rating_num, movie.movie_rating_persons))
        # print(res)
        # self.db_operation
    
    def insert_many(self,movies):
        res = DBOperation.db_operation.insert_many(sql, movies)
        self.db_conn.commit()
        return res

    def get_all(self):
        # print('test')
        res = self.db_operation.select('select * from douban_movie;')
        # print(res)
        return res

        

# movie entity map to db table 
class Movie:
    def __init__(self):
        
        self.movie_link = ''
        self.movie_name = ''
        self.movie_rating_level = 0
        self.movie_rating_num = 0
        self.movie_rating_persons = 0
    
    def __str__(self):
        return 'movie_name is:{0} movie_link is:{1}\n movie_level is:{2} movie_num is:{3}\nmovie_rating_persons:{4}'.format(self.movie_name, self.movie_link, self.movie_rating_level, self.movie_rating_num, self.movie_rating_persons)


class MovieCommentsDBO:
    def __init__(self):
        self.db_operation = DBOperation()
    def get_movie_comments(self, movie_id):
        comments = self.db_operation.select('select * from movie_comments where movie_id=%s'%(movie_id))
        return comments
    def insert(self, moviem_comments):
        sql = "insert into movie_comments(movie_id,movie_comment) values(%s,%s)"
        res = DBOperation.db_operation.insert(sql,(moviem_comments.movie_id, moviem_comments.comment))
        # print(res)
    def insert_many(self,list):
        # print('line 89:',list)
        sql = "insert into movie_comments(movie_id,movie_comment) values(%s,%s)"
        # comment_list = [ (c.movie_id, c.movie_comment) for c in list]
        res = self.db_operation.insert_many(sql, list)
        
        return res


# movie entity map to db table 
class MovieComments:
    def __init__(self):
        
        self.movie_id = 0
        self.comment = ''
    
    def __str__(self):
        return 'movie_id:{0}, comment:{1}'.format(self.movie_id, self.comment)
    # douban clawer . Currently, capture movie info
class DoubanClawler:
    # size: the amount of clawler thread
    def __init__(self,size=10):
        self.movieDBO = MovieDBO()
        self.movie_commentsDBO = MovieCommentsDBO()


        self.movie_urls = queue.Queue(100)
        self.movie_queue = queue.Queue(100)

        self.comment_urls = queue.Queue(100)
        self.comment_queue = queue.Queue(100)
        # thread group used to parse page
        self.threads = [ threading.Thread(target=self.douban_crawler) for _ in range(size)]
        self.semaphore = threading.Semaphore(1)
        # thread used to store data to mysql
        self.db_thread = threading.Thread(target=self.save_to_mysql)

        # thread used to generate urls
        self.url_thread = threading.Thread(target=self.generate_urls)
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        # self.init_urls()
    # get url , in fact you may generate url with a set of operations
    def generate_urls(self):
        for url in (f'https://movie.douban.com/top250?start={page * 25}' for page in range(2)):
            self.movie_urls.put(url)
            time.sleep(0.5)
            # print('generate url',url)
        
        # get movie url from db , waiting for db data
        
        self.semaphore.acquire()
        for movie in self.movieDBO.get_all():
            time.sleep(0.5)
            self.comment_urls.put((movie[0],movie[2]))
        self.semaphore.release()
        print('generate_urls thread is successfull!')

# parse page
    def douban_crawler(self):
        dowload = True
        while (dowload ):
            try:
                url = self.movie_urls.get(True, 1)
            except queue.Empty:
                dowload = False
                print('no movie url')
                continue

            response = requests.get(url, headers = self.headers)
            print(response)

            bs = BeautifulSoup(response.text)
            movies = bs.find_all('div', attrs={'class':'info'})
            for movie in movies:
                movie_headers = movie.find_all('div', attrs={'class':'hd'})
                movie_comments = movie.find_all('div', attrs={'class':'bd'})

                for i in range(len(movie_headers)):
                    movie = Movie()
                    movie_atag = movie_headers[i].a
                    movie.movie_link = movie_atag.get('href')
                    movie.movie_name = movie_atag.span.get_text()
                    movie_star = movie_comments[i].find('div')
                    movie_rating = movie_star.find_all('span')
                    movie.movie_rating_level = movie_rating[0]['class'][0]
                    movie.movie_rating_num = float(movie_rating[1].get_text())
                    movie.movie_rating_persons = int(re.search('\d*', movie_rating[3].get_text()).group())
                    # move_comments = self.get_comments(movie.movie_link)
                    self.movie_queue.put(movie)
        print('line 179:get movie info succussfully!',self.movie_queue.qsize())
                    
        dowload = True

        # self.semaphore_comments.acquire()
        while (dowload ):
            try:
                comment_url = self.comment_urls.get(True, 30)
                # print('line num 188:',comment_url)
                comments = self.get_comments(comment_url)
                # print('line190:',comments)
                self.comment_queue.put(comments)
                
            except queue.Empty:
                dowload = False
                continue
        print('douban_crawler thread is successfull!')
        
    # get movie top 5 comments
    def get_comments(self, comment_url):
        response = requests.get(comment_url[1],headers = self.headers)
        # print('line 184:',comment_url[1])
        bs = BeautifulSoup(response.text)
        comments = []
        movie_comments = bs.find_all('div', attrs={'class':'comment'})[0:5]
        # print('line 188:',len(movie_comments))
        tmp_comment = ''
        for comment in movie_comments:
            tmp_comment = comment.find_all('span', attrs={'class':'short'})
            # print('line 206:',tmp_comment[0].get_text())
            comments.append((comment_url[0], tmp_comment[0].get_text()[0:180]))
            
        return comments


    # save data to mysql
    def save_to_mysql(self):
        run = True
        # save movie info to mysql
        self.semaphore.acquire()
        time.sleep(10)
        print('line 221')
        while (run ):
            try:
                print('line 225:',self.movie_queue.qsize())
                movie = self.movie_queue.get(True, 1)
                self.movieDBO.insert(movie)
            except queue.Empty:
                print('movie_queue is empty!')
                run = False
                continue
        self.semaphore.release()
#  save comments to mysql
        run = True
        while (run ):
            try:
                # print('line 238:',self.comment_queue.qsize())
                comments = self.comment_queue.get(True, 10)
                self.movie_commentsDBO.insert_many(comments)
            except queue.Empty:
                print('comment_queue is empty!')
                run = False
                continue
        print('save_to_mysql thread is successful!')

                        
# start all thread then wait for running success
    def start(self):
        
        # start  download thread
        for thr in self.threads:
            thr.start()
        
        # start db thread
        self.db_thread.start()

        # start url thread
        self.url_thread.start()

        # waiting for all thread completed
        for thr in self.threads:
            thr.join()
        self.db_thread.join()
        self.url_thread.join()
        # close db conn
        self.movieDBO.db_operation.close()
        
    

if __name__ == "__main__":

    clawer = DoubanClawler(size=2)
    clawer.start()
    


