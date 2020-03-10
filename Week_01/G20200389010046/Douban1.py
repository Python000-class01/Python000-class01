import requests
# from bs4 import BeautifulSoup as bs
from time import sleep
from lxml import etree
import pandas as pd
import json


def getcontent(myurl):

    url  = myurl
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    headers = {}
    headers['user-agent'] = user_agent
    response = requests.get(url,headers=headers).text

    return response

def parsebooklist(htmltext):
    book_info = etree.HTML(htmltext)

    #bs4 solution
    # book_info = bs(book_response,'html.parser')
    # book_info  = etree.parse(etree.HTML(book_response))
    # book_info  = etree.parse(book_response,etree.HTMLParser())
    # content250 = bs_info.find_all('div',attrs={'class':'pl2'})

    # for tags in content250:
    # #获取a标签，href是属性，title属性是标题
    # a_tag = tags.contents[1]
    #     for atag in tags.find_all('a'):
    #     bookinfo.append({'href':atag.get('href'),'title':atag.get('title')})

    # xpath solution
    titles = book_info.xpath('//div[@class="pl2"]/a/@title')
    refs = book_info.xpath('//div[@class="pl2"]/a/@href')
    scores = book_info.xpath('//div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
    
    booklist = [{'title':title,'ref':ref,'score':score} for title,ref,score in  zip(titles,refs,scores)]

    print(len(booklist))

    return booklist

def parsebookdetails(html,bookbasic):

    bookfull = bookbasic

    htmltext = getcontent(html)
    book_detail = etree.HTML(htmltext)

    # xpath solution
    auther = book_detail.xpath('//div[@id="info"]/span[1]/a/text()')
    price = book_detail.xpath('//div[@id="info"]/text()[9]')
    # comment = book_detail.xpath('//div[@id="comment-list-wrapper"]/div[@id="comments"]/span[@class="short"]/text()')
    comment = book_detail.xpath('//p[@class="comment-content"]/span[@class="short"]/text()')

    # booklist = [{'title':title,'ref':ref,'score':score} for title,ref,score in  zip(titles,refs,scores)]
    print(type(auther))
    bookfull['auther'] = auther[0]
    bookfull['price'] = price[0]
    bookfull['comment'] = comment[0:3]

    return bookfull
 


if __name__ == '__main__':

    booknewlist =[]

    for i in range(2):
        url = 'https://book.douban.com/top250?start='+str(i*25)
        mybookinfo = getcontent(url)
        booknewlist.extend(parsebooklist(mybookinfo))
        sleep(1)

        pdbook = pd.DataFrame(booknewlist)

    print(pdbook)
    pdbook.to_csv('11.csv',encoding='utf-8')





# a = tuple(f'https://book.douban.com/top250?start={page*25}' for page in range(3))

