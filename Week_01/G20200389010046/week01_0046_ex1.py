import requests
from time import sleep
from lxml import etree
import pandas as pd
import json


def getcontent(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    headers = {}
    headers['user-agent'] = user_agent
    response = requests.get(url,headers=headers).text
    return response

def parsebooklist(htmltext):
    book_info = etree.HTML(htmltext)

    # xpath solution
    titles = book_info.xpath('//div[@class="pl2"]/a/@title')
    refs = book_info.xpath('//div[@class="pl2"]/a/@href')
    scores = book_info.xpath('//div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
    booklist = [{'title':title,'ref':ref,'score':score} for title,ref,score in  zip(titles,refs,scores)]
    return booklist

def parsebookdetails(bookbasicinfo):

    htmltext = getcontent(bookbasicinfo['ref'])
    book_detail = etree.HTML(htmltext)

    # xpath solution
    # wtm 豆瓣的前端写的实在是有点烂 

    auther = book_detail.xpath('//div[@id="info"]/span/span[text()=" 作者"]/following-sibling::*[1]/text()')
    # price = book_detail.xpath('//div[@id="info"]/span[text()="定价:"]/following-sibling::*[1]/text()')
    price = book_detail.xpath('//div[@id="info"]/text()[9]')
    comment = book_detail.xpath('//p[@class="comment-content"]/span[@class="short"]/text()')


    bookfullinfo = bookbasicinfo

    try:
        bookfullinfo['auther'] = auther[0]
        bookfullinfo['price'] = price[0]
        bookfullinfo['comment'] = comment[0:5]
    except:
        pass

    return bookfullinfo
 


if __name__ == '__main__':

    # get top 250 booklist
    booklist =[]
    for i in range(1):
        url = 'https://book.douban.com/top250?start='+str(i*25)
        mybookinfo = getcontent(url)
        booklist.extend(parsebooklist(mybookinfo))
        sleep(0.5)

    # get book details
    bookdetaillist = []
    for item in booklist:
        itemdetail = parsebookdetails(item)
        bookdetaillist.append(itemdetail)
        sleep(0.5)
        print('currnet book is 《%s》' % item['title'])
    result = pd.DataFrame(bookdetaillist)

    # save to csv
    result.to_csv('result.csv',encoding='utf-8')
