#作业1
import requests
import lxml.etree
from time import sleep
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {
    'user-agent':user_agent
}

urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10))

def get_info(myurl):
    response = requests.get(myurl,headers=header)
    selector = lxml.etree.HTML(response.text)
    name = selector.xpath('//div[@class="pl2"]/a/@title')
    score = selector.xpath('//div[@class="star clearfix"]//span[@class="rating_nums"]/text()')
    comment_nums = selector.xpath('//div[@class="star clearfix"]//span[@class="pl"]/text()')

    book = pd.DataFrame({
        'name':name,
        'score':score,
        'comment_nums':comment_nums
    })
    book.to_csv('./book.csv', mode='a', encoding='utf-8')

if __name__ == '__main__':
    for url in urls:
        get_info(url)
        sleep(5)




#作业2
import requests

url_1 = ' http://httpbin.org/get'
url_2 = 'http://httpbin.org/post'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
header = {
    'user-agent':user_agent
}

response_1 = requests.get(url_1, headers=header)
print (response_1.text)

response_2 = requests.post(url_2, headers=header)
print (response_2.json())
