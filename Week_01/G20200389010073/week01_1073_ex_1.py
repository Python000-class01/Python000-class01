import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
from time import sleep
import threading
from fake_useragent import UserAgent


class Thread_onePage(threading.Thread):
    def __init__(self, thread_ID, thread_Name):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
        self.thread_Name = thread_Name

    def run(self):
        # 获取锁，用于线程同步
        threadLock_onePage.acquire()
        print("开始线程：" + self.thread_Name)
        thread_get_AllPage_info()
        print("退出线程：" + self.thread_Name)
        # 释放锁，开启下一个线程
        threadLock_onePage.release()


class Thread_oneMovie(threading.Thread):
    def __init__(self, thread_ID, thread_Name):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
        self.thread_Name = thread_Name

    def run(self):
        # 获取锁，用于线程同步
        threadLock_oneMovie.acquire()
        print("开始线程：" + self.thread_Name)
        thread_get_oneMovie_info(self.thread_Name)
        print("退出线程：" + self.thread_Name)
        # 释放锁，开启下一个线程
        threadLock_oneMovie.release()


#region 方法
def thread_get_AllPage_info():
    int_page = 0
    for page in urls:
        get_url_name(page)
        int_page += 1
        print(f'>>> 第 {int_page} 页 完成 >>>')
        sleep(1)


def thread_get_oneMovie_info(str_thread_name):
    int_movies_num = 0
    while True:
        if len(dict_onemovies_urls) > 0:
            List_name_url = dict_onemovies_urls.popitem()
            get_onepage_information(List_name_url[0], List_name_url[1],
                                    int_movies_num + 1)
            int_movies_num += 1
            print(
                f'完成 {int_movies_num} 个电影的详细信息搜索，剩余未搜索个数为：{len(dict_onemovies_urls)}...'
            )
            continue
        elif len(dict_onemovies_urls) == 0:
            break
        else:
            sleep(0.01)
            continue
    print(
        f'完成 {int_movies_num} 个电影的详细信息搜索，剩余未搜索个数为：{len(dict_onemovies_urls)}...'
    )


def get_url_name(myurl):
    """ 获取网页信息 """
    #region 记录开始时间
    time_start = datetime.now()
    print(f'开始时间：{time_start}')
    #endregion
    #region cookie伪造
    jar = requests.cookies.RequestsCookieJar()
    jar.set('bid', 'ehjk9OLdwha', domain='.douban.com', path='/')
    jar.set('11', '25678', domain='.douban.com', path='/')
    #endregion
    useragent = UserAgent()
    response = requests.get(myurl,
                            headers={'user-agent': useragent.random},
                            cookies=jar)

    bs_info = bs(response.text, 'html.parser')

    # bs_item：循环每一行信息
    for bs_item in bs_info.find_all('div', attrs={'class': 'info'}):

        #region 1.循环开头：获取链接、获取名字
        # tag_hd：循环开头
        tag_hd = bs_item.find('div', attrs={'class': 'hd'})
        btag = tag_hd.find('a', )
        # 获取所有链接
        str_movie_url = btag.get('href')

        # 获取电影名称
        str_movie_Name = btag.find_all('span', attrs={'class':
                                                      'title'})[0].string

        dict_onemovies_urls[str_movie_Name] = str_movie_url  # 保存进urls列表
        #endregion

        #region 2.循环内容：
        tag_rating = bs_item.find('div', attrs={'class': 'star'})
        # 获取评分
        str_movie_rating_num = tag_rating.find('span',
                                               attrs={
                                                   'class': 'rating_num'
                                               }).string

        #endregion

        #region 2.5 显示信息：
        print(
            f'电影名称：{str_movie_Name}\r\n电影评分：{str_movie_rating_num}\r\n电影网址：{str_movie_url}\r\n'
        )
        #endregion

        #region 3.写入csv文件：
        str_info = f'{str_movie_Name},{str_movie_url},{str_movie_rating_num}'
        writefile_csv(str_info)
        #endregion

    #region 记录用时
    time_end = datetime.now()
    time_Using = float((time_end - time_start).total_seconds())
    print(f'结束时间：{time_end}')
    print(f'用时s：{time_Using}')
    #endregion


def get_onepage_information(str_moviename, str_url, int_movie_num):
    """ 获取单个网页具体信息 """
    #region 记录开始时间
    time_start = datetime.now()
    print(f'开始时间：{time_start}')
    #endregion
    dict_Movie_Info_One = {}
    useragent = UserAgent()
    response = requests.get(str_url, headers={'user-agent': useragent.random})

    bs_info = bs(response.text, 'html.parser')

    #tag_h1 = bs_info.find('h1', )
    tag_body = bs_info.find('div', attrs={'class': 'grid-16-8 clearfix'})

    # 3.1 找到电影名字 str_name
    # str_name = tag_h1.find_next('span', attrs={
    #     'property': "v:itemreviewed"
    # }).text
    str_name = str_moviename
    print(str_name)
    dict_Movie_Info_One['str_name'] = str_name

    # 3.2 找到电影评分 str_ratingnum
    tag_rating = tag_body.find_next('div',
                                    attrs={'class': 'rating_self clearfix'})
    tag_ratingnum = tag_rating.find_next('strong',
                                         attrs={'class': 'll rating_num'})
    str_ratingnum = tag_ratingnum.text
    print(str_ratingnum)
    dict_Movie_Info_One['str_ratingnum'] = str_ratingnum

    # 3.3 找到短评数量 str_rating_people_num
    tag_comment = tag_body.find_next('div', attrs={'id': 'comments-section'})
    tag_rating_people_num = tag_comment.find_next('div',
                                                  attrs={'class': 'mod-hd'})
    tag_rating_people_num = tag_rating_people_num.find_next('h2', )
    tag_rating_people_num = tag_rating_people_num.find_next('a', )
    str_rating_people_num = tag_rating_people_num.text
    print(str_rating_people_num)
    dict_Movie_Info_One['str_rating_people_num'] = str_rating_people_num

    # 3.4 找到前5条热门短评 list_onemovies_comments
    tag_comment_hd = tag_comment.find_next('div',
                                           attrs={
                                               'id': 'hot-comments',
                                               'class': 'tab'
                                           })
    list_onemovies_comments = [0 for i in range(5)]
    int_num = 1
    for tag_one_comment in tag_comment_hd.find_all(
            'div', attrs={'class': 'comment-item'}):
        str_one_comment = tag_one_comment.find_next('span',
                                                    attrs={
                                                        'class': 'short'
                                                    }).text
        list_onemovies_comments[int_num - 1] = str_one_comment
        print(f'第{int_num}条评论：{str_one_comment}\n')
        int_num += 1
    dict_Movie_Info_One['list_onemovies_comments'] = list_onemovies_comments

    dict_Movies_Info_All[int_movie_num] = dict_Movie_Info_One

    str_log = '{str_name},{str_ratingnum},{str_rating_people_num},{str_url},{comment1},{comment2},{comment3},{comment4},{comment5}'.format(
        str_name=dict_Movie_Info_One['str_name'],
        str_ratingnum=dict_Movie_Info_One['str_ratingnum'],
        str_rating_people_num=dict_Movie_Info_One['str_rating_people_num'],
        str_url=str_url,
        comment1=dict_Movie_Info_One['list_onemovies_comments'][0],
        comment2=dict_Movie_Info_One['list_onemovies_comments'][1],
        comment3=dict_Movie_Info_One['list_onemovies_comments'][2],
        comment4=dict_Movie_Info_One['list_onemovies_comments'][3],
        comment5=dict_Movie_Info_One['list_onemovies_comments'][4])

    str_log = str_log.replace('\r', '')
    str_log = str_log.replace('\n', '')
    writefile_AllMovies_csv(str_log + '\n')

    #region 记录用时
    time_end = datetime.now()
    time_Using = float((time_end - time_start).total_seconds())
    print(f'结束时间：{time_end}')
    print(f'用时s：{time_Using}')
    #endregion


def writefile_csv(str_info):
    """ 写入csv文件记录信息 """
    with open(
            'homework1_Informations_of_Top250_movies.csv',
            'a',
            # encoding='utf-8'
    ) as file_1:
        file_1.write(f'{str_info}\n')


def writefile_AllMovies_csv(str_info):
    """ 写入csv文件记录信息 """
    with open('Informations_of_Top250_movies.csv', 'a',
              encoding='utf-8') as file_1:
        file_1.write(f'{str_info}\n')


import os


def checkanRemove_oldfile(
    str_fileName='homework1_Informations_of_Top250_movies.csv'):
    """ 删除旧文件，建立新文件的列标题 """
    if os.path.isfile(str_fileName):
        os.remove(str_fileName)
    with open(
            str_fileName,
            'w',
            #encoding='utf-8'
    ) as file_header:
        file_header.write('电影名字,电影网址,电影评分\n')


def checkanRemove_oldfile_allmovies(
    str_fileName='Informations_of_Top250_movies.csv'):
    """ 删除旧文件，建立新文件的列标题 """
    if os.path.isfile(str_fileName):
        os.remove(str_fileName)
    with open(
            str_fileName,
            'w',
            #encoding='utf-8'
    ) as file_header:
        file_header.write(
            '电影名字,电影评分,短评数量,电影网址,第1条短评,第2条短评,第3条短评,第4条短评,第5条短评\n')


def confirm_PageNum(int_pagenum=1):
    """ 确认爬取几页信息，1页有25项 """
    if int_pagenum < 1:
        int_pagenum = 1
    return tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter='
                 for page in range(int_pagenum))


#endregion

#region 变量
# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter='
             for page in range(1))

# 存放电影信息的字典
dict_Movies_Info_All = {}
dict_Movie_Info_One = {}

# 暂时存放url的字典   电影名称-电影网址
dict_onemovies_urls = {}


threadLock_onePage = threading.Lock()
threadLock_oneMovie = threading.Lock()
#endregion

if __name__ == '__main__':  # 如果不是别人调用，就运行

    #region 记录开始时间
    time_start = datetime.now()
    #endregion
    urls = confirm_PageNum(10)
    checkanRemove_oldfile('homework1_Informations_of_Top250_movies.csv')
    checkanRemove_oldfile_allmovies('Informations_of_Top250_movies.csv')
    print('>>> 爬取开始 >>>')

    threads = []
    threads_one_movie = []

    # 创建新线程
    th_onePage = Thread_onePage(1, f"th_onePage")
    th_oneMovie = Thread_oneMovie(2, f"th_oneMovie")
    # 开启新线程
    th_onePage.start()
    sleep(2)
    th_oneMovie.start()
    # 添加线程到线程列表
    threads.append(th_onePage)
    threads.append(th_oneMovie)
    # 等待所有线程完成
    for t in threads:
        t.join()
    print('>>> 爬取完成 >>>')
    #region 记录用时
    time_end = datetime.now()
    time_Using = float((time_end - time_start).total_seconds())
    print(f'总用时s：{time_Using}')
    #endregion
