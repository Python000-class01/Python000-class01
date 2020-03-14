import requests
import lxml.etree
import pandas as pd
import time

user_agent = 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'

header = {}

header['user-agent'] = user_agent


def get_movie_detail_page(movie_page):
    """
    获得豆瓣TOP250电影列表链接
    :param movie_page: 控制爬取豆瓣电影列表页数
    :return: movie_list
    """

    movie_page = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(movie_page))
    movie_detail_page = []
    for url in movie_page:
        # 请求豆瓣电影页面
        response = requests.get(url, headers=header)
        # xml化处理
        selector = lxml.etree.HTML(response.text)
        # 获取电影详情页链接
        link = selector.xpath('//div[@class="item"]//div[@class="info"]//a/@href')
        print(link)

        movie_detail_page.extend(link)

        time.sleep(10)

    return movie_detail_page


def get_movie_info(urls):
    """
    在豆瓣电影详情页获取电影名称、评分、短评数量和前5条热门短评信息
    :return:
    """
    name = []
    rating = []
    comment_num = []
    coment1 = []
    coment2 = []
    coment3 = []
    coment4 = []
    coment5 = []
    for url in urls:
        # 请求豆瓣电影页面
        response = requests.get(url, headers=header)
        # xml化处理
        selector = lxml.etree.HTML(response.text)
        # 获取电影名称
        new_name = selector.xpath('//span[@class="year"]/../span[1]/text()')
        name.append(new_name)
        # 获取评分
        new_rating = selector.xpath('//strong/text()')
        rating.append(new_rating)
        # 获取短评数量
        new_comment_num = selector.xpath('//a[@class="rating_people"]/span/text()')
        comment_num.append(new_comment_num)
        # 获取前5条热门短评信息
        comments = selector.xpath('//div[@class="comment"]//span[@class="short"]/text()')
        coment1.append(comments[0])
        coment2.append(comments[1])
        coment3.append(comments[2])
        coment4.append(comments[3])
        coment5.append(comments[4])

        # movie_info = [name, rating, comment_num] + comments
        time.sleep(10)

    movie_info = {}
    movie_info['电影名称'] = name
    movie_info['评分'] = rating
    movie_info['短评数量'] = comment_num
    movie_info['热评1'] = coment1
    movie_info['热评2'] = coment2
    movie_info['热评3'] = coment3
    movie_info['热评4'] = coment4
    movie_info['热评5'] = coment4

    return movie_info



# 爬取豆瓣TOP250电影
# movie_link = get_movie_detail_page(2)
movie_link = get_movie_detail_page(10)
# movie_info = get_movie_info(movie_link[0:2])
movie_info = get_movie_info(movie_link)
# 写入CSV
dbMovie_info = pd.DataFrame(movie_info)
dbMovie_info.to_csv('./dbMovie_top250.csv', encoding='gbk')