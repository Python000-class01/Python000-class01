import requests
import lxml.etree
from time import sleep
import csv

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
header = {}
header['user-agent'] = user_agent

def get_DoubanMovie_250(url):
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    mhref = selector.xpath('//*[@class="hd"]/a/@href')
    for href in mhref:
        get_DoubanMovie_all(href)


def get_DoubanMovie_all(href):
    with open('Doubanmovie.csv','a', newline='', encoding='utf-8-sig') as f:
        writer=csv.writer(f)
        response_all = requests.get(href, headers=header)
        selector_all = lxml.etree.HTML(response_all.text)
        name = selector_all.xpath('//*[@id="content"]/h1/span[1]/text()')
        grade = selector_all.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')
        sleep(2)
        total = selector_all.xpath('//*[@id="comments-section"]//h2/span/a/text()')
        content = selector_all.xpath('//*[@id="hot-comments"]//p/span/text()')
        writer.writerow([name,grade,total,content])


urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

if __name__ == "__main__":
    for page in urls:
        get_DoubanMovie_250(page)
        sleep(5)
