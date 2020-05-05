import requests
import lxml.etree
import sys
import io
import codecs

def setup_io():
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    # sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)


def getpages(url):
    '''
    requests.get()请求url指向的豆瓣短评页面
    1. 获取短评总数
    2. 生成页面数 = 短评总数 // 20 if 短评总数 % 20 == 0 else 短评总数 // 20 + 1
    3. 列表推导式生成各个页面的url 
    4. 将urls作为结果返回
    '''
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    headers = {"user-agent":user_agent}
    response = requests.get(url, headers = headers)
    content = response.text
    selector = lxml.etree.HTML(content)
    total = selector.xpath('//span[@id="total-comments"]/text()')[0]

    totalNum = ""
    for i in total:
        if i.isnumeric():
            totalNum += i
    totalNum = int(totalNum)
    pageNum = totalNum // 20 if totalNum % 20 == 0 else totalNum // 20 + 1
    urls = [url + f"hot?p={i}" for i in range(1, pageNum + 1)]
    return urls


def getcomments(commentsurl):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    headers = {"user-agent":user_agent}
    urls = getpages(commentsurl)
    stars = []
    comments = []
    for url in urls[:2]:
        response = requests.get(url, headers = headers)
        content = response.text
        selector = lxml.etree.HTML(content)
        comments += selector.xpath('//span[@class="short"]/text()')
        stars += selector.xpath('//span[@class="comment-info"]/span[1]/@title')
    return comments

if __name__ == '__main__':
    setup_io()
    url = "https://book.douban.com/subject/10554308/comments/"
    comments = getcomments(url)
    


