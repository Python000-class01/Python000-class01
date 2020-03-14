# !/bin/env python
# encoding=utf-8

import re
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import lxml.etree
import pandas as pd

mn = []  # 电影名称
mr = []  # 电影评分
mp = []  # 电影评价人数
mh = []  # 电影链接
mtp = []  # 电影短评
title_1 = []  # 评论1
title_2 = []  # 评论2
title_3 = []  # 评论3
title_4 = []  # 评论4
title_5 = []  # 评论5


def get_url_name(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    cookie = '''bid=ZNJjsDB1mu4; douban-fav-remind=1; __yadk_uid=EH2JTTZhVzZmeLKBWnLIsMyMuUKyCmlr; ll="108288"; push_noty_num=0; push_doumail_num=0; dbcl2="170609308:/CPcn6wSV8s"; ck=gCQ_; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1583642177%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1482876592.1570801355.1583329616.1583642177.4; __utmc=30149280; __utmz=30149280.1583642177.4.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt=1; __utmv=30149280.17060; douban-profile-remind=1; _pk_id.100001.8cb4=0032b1c289fde0dd.1570801350.3.1583642452.1570956509.; __gads=ID=356f8d35ed66b5f6:T=1583642453:S=ALNI_MbmKR7vLQRINc1rm5RCeVkIvGC60w; __utmb=30149280.8.10.1583642177'''
    cookie_dic = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
    response = requests.get(url, headers=header,cookies=cookie_dic)
    selector = lxml.etree.HTML(response.text)
    movie_tag = selector.xpath('//ol[@class="grid_view"]')
    # bs_info = bs(response.text,'html.parser')     #语法分析器,以html的方式进行分析
    for data in movie_tag:
        movie_name = data.xpath('//div[@class="hd"]//span[@class="title"][1]/text()')
        for mn_info in movie_name:
            mn.append(mn_info)
        movie_rating = data.xpath('//div[@class="bd"]//div[@class="star"]//span[@property="v:average"]/text()')
        # print(movie_rating)
        for mr_info in movie_rating:
            mr.append(mr_info)
        movie_pingjia = data.xpath('//div[@class="star"]//span[4]/text()')
        # print(movie_pingjia)
        for mp_info in movie_pingjia:
            mp.append(mp_info)
        movie_hrefs = data.xpath('li//div[@class="item"]/div[@class="pic"]/a/@href')
        for movie_href in movie_hrefs:
            mh.append(movie_href.strip().replace('\n',''))
            # print(mh)

            response_2 = requests.get(movie_href, headers=header,cookies=cookie_dic)
            selector_2 = lxml.etree.HTML(response_2.text)
            comments = selector_2.xpath('//*[@id="hot-comments"]')
            for topics in comments:
                # mtp.clear()
                topic = topics.xpath('div//div[@class="comment"]/p/span[@class="short"]/text()')

                # print(topic)
                # for aa in topic:
                mtp.append(tuple(topic))


urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

if __name__ == '__main__':
    for page in urls:
        print(page)
        get_url_name(page)
        sleep(10)

    dict_info ={}
    for i in range(len(mn)):

        title_1.append(mtp[i][0])
        title_2.append(mtp[i][1])
        title_3.append(mtp[i][2])
        title_4.append(mtp[i][3])
        title_5.append(mtp[i][4])

        dict_info = {
            '电影名称': mn,
            '电影评分': mr,
            '评价人数': mp,
            '电影链接': mh,
            '电影评价1': title_1,
            '电影评价2': title_2,
            '电影评价3': title_3,
            '电影评价4': title_4,
            '电影评价5': title_5
        }
    if dict_info:
        print(dict_info)
        book1 = pd.DataFrame(dict_info,
                             columns=['电影名称',
                                      '电影评分',
                                      '评价人数',
                                      '电影链接',
                                      '电影评价1',
                                      '电影评价2',
                                      '电影评价3',
                                      '电影评价4',
                                      '电影评价5'])
        book1.to_csv('./movie_info.csv', encoding='utf-8')









