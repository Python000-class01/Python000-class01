# 安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
import lxml.etree
from time import sleep
import csv
import os

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/80.0.3987.116 Safari/537.36 '
header = {'user-agent': user_agent}
i = 0
j = 0
file = 'movie_top250_from_douban.csv'

if os.path.exists(file):
    print('file exist')
    os.remove(file)
else:
    print('file not exist')

urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))
try:
    with open(file, 'a', newline='', encoding='utf-8-sig') as f:

        for url in urls:
            print('***** 第%s页执行中 *****' % (i + 1))
            i += 1
            resp_movie_list = requests.get(url, headers=header)
            selector = lxml.etree.HTML(resp_movie_list.text)
            link_list = selector.xpath('//*[@class="hd"]/a/@href')
            for link in link_list:
                print('*** 第%s条执行中 ***' % (j + 1))
                j += 1
                writer = csv.writer(f)
                resp_movie = requests.get(link, headers=header)
                selector_to = lxml.etree.HTML(resp_movie.text)
                name = selector_to.xpath('//*[@id="content"]/h1/span[1]/text()')
                grade = selector_to.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')
                total = selector_to.xpath('//*[@id="comments-section"]//h2/span/a/text()')
                content = selector_to.xpath('//*[@id="hot-comments"]//p/span/text()')
                writer.writerow([name, grade, total, content])

                sleep(2)
except Exception as e:
    print(e)
finally:
    f.close()

print('终于爬完了！！！')
