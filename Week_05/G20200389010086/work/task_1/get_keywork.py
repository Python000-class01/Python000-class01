import requests
import lxml.etree
from time import sleep
import csv

HEADER = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36 '
}


def get_db_url(url):
    response = requests.get(url, headers=HEADER)
    selector = lxml.etree.HTML(response.text)
    contents = selector.xpath('//*[@class="comment-content"]/span/text()')
    for i in range(len(contents)):
        writer(contents[i])


def writer(contents):
    with open(f'./contents.text', 'a+') as f:
        f.writelines(contents + '\n')


if __name__ == '__main__':
    #  f-string是格式化字符串的新语法。f-string用大括号 {} 表示被替换字段，其中直接填入替换内容
    URLS = tuple(f'https://book.douban.com/subject/33379779/comments/hot?p={page + 1}' for page in range(160))
    for url in URLS:
        get_db_url(url)
        sleep(5)
