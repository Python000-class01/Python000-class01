import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from lxml import etree
import time


#模拟浏览器，设置请求头
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"

header = {}
header["user-agent"] = user_agent


def get_detail_link ():
    '''获取豆瓣电影详情页面,共250个
    url: 指豆瓣电影主页，https://movie.douban.com/top250?start=0
    '''

    detail_link = []

    for page in range(10):

        url = f'https://movie.douban.com/top250?start={page*25}'
        #发送请求
        response = requests.get(url,headers = header)

        #用lxml解析网页
        selector = etree.HTML(response.text)

        #提取详情网址
        items = selector.xpath('//div[@class="item"]//div[@class="info"]//a/@href')

        detail_link += items
        time.sleep(10)

    return detail_link


def get_movie_info ( ):
    '''
    利用xpath获取电影名称/评分/短评数量/前5条热评
    :return: 影名称/评分/短评数量/热门短评1，2，3，4，5
    '''
    url_list = get_detail_link()

    data = []
    #便利250个网址
    for url in url_list:

        #将每个电影的名称/评分/短评数量/5个热门短评存入 列表变量 item
        item = []

        #发送get请求
        response = requests.get(url,headers = header)

        #解析网页
        selector = etree.HTML(response.text)

    #提取名字/评分/评论数
        name = selector.xpath('//div[@id = "content"]/h1/span[@property="v:itemreviewed"]/text()')
        rating = selector.xpath('//div[@id = "content"]//div[@class="rating_self clearfix"]/strong/text()')
        comment_num = selector.xpath('//div[@id = "content"]//div[@class="rating_sum"]//span[@property="v:votes"]/text()')
        comments = selector.xpath('//div[@class="comment"]//span[@class="short"]/text()')
        comment_five = comments[0:5]

        #将name/rating/comment_num/comments以单个元素的形式传入 item
        item += name
        item += rating
        item += comment_num
        item += comment_five

        #最后将每部电影的信息以list传入data
        data.append(item)

        #暂停7s再进行下次爬取，防止被封号
        time.sleep(10)

    # print(data)

    return data





def main ():
    """
    将数据写入csv文件
    :return: None
    """
    data = get_movie_info()
    colunms = ["名称","评分","短评数量","热评1","热评2","热评3","热评4","热评5"]

    # 将数组转化为Dataframe格式
    df_data = pd.DataFrame(data=data,columns=colunms)

    df_data.to_csv("./movie_top250v2.csv",encoding="utf-8-sig")



if __name__ == "__main__":
    main()