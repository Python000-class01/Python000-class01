import lxml.etree,requests
from time import sleep
import csv

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
header = {}
header['user-agent'] = user_agent

def get_movie_info(url):
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    hrefs = selector.xpath('//*[@class="hd"]/a/@href')
    for href in hrefs:
        get_total_info(href)


def get_total_info(href):
    with open('movie.csv','a', newline='', encoding='utf-8-sig') as f:
        writer=csv.writer(f)
        response_to = requests.get(href, headers=header)
        selector_to = lxml.etree.HTML(response_to.text)
        name = selector_to.xpath('//*[@id="content"]/h1/span[1]/text()')
        grade = selector_to.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')
        sleep(2)
        total = selector_to.xpath('//*[@id="comments-section"]//h2/span/a/text()')
        content = selector_to.xpath('//*[@id="hot-comments"]//p/span/text()')
        writer.writerow([name,grade,total,content])


# 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

if __name__ == "__main__":
    for page in urls:
        get_movie_info(page)
        sleep(5)


