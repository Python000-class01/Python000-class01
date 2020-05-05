# 安装并使用 requests、bs4 库；
# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评；
# 并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
import lxml

def get_url(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a',):

            # 获取单条详细页面
            url = atag.get('href')

            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            header = {}
            header['user-agent'] = user_agent
            response = requests.get(url, headers=header)

            # xml化处理
            selector = lxml.etree.HTML(response.text)

            # 电影名称
            name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
            print(f'名称: {name}')

            # 评分
            score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')
            print(f'评分：{score}')

            # 短评数
            comments_num = selector.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()')
            print(f'短评数:{comments_num}')

            # 热评前五
            top5_1 = selector.xpath('//*[@id="hot-comments"]/div[1]/div/p/span/text()')
            print(f'热评1:{top5_1}')

            top5_2 = selector.xpath('//*[@id="hot-comments"]/div[2]/div/p/span/text()')
            print(f'热评2:{top5_2}')

            top5_3 = selector.xpath('//*[@id="hot-comments"]/div[3]/div/p/span/text()')
            print(f'热评3:{top5_3}')

            top5_4 = selector.xpath('//*[@id="hot-comments"]/div[4]/div/p/span/text()')
            print(f'热评4:{top5_4}')

            top5_5 = selector.xpath('//*[@id="hot-comments"]/div[5]/div/p/span/text()')
            print(f'热评5:{top5_5}')

            # 制作表格
            my_list = [name, score, comments_num, top5_1, top5_2, top5_3, top5_4, top5_5]
            columns_name = ['one']

            import pandas as pd
            movie1 = pd.DataFrame(columns=columns_name, data=my_list)
            movie1.to_csv('./movie1.csv', encoding='utf_8_sig')


# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

# 控制请求和程序入口
from time import sleep

for page in urls:
    get_url(page)
    sleep(5)




