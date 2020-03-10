import requests
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

    # xpath solution
    titles = book_info.xpath('//div[@class="pl2"]/a/@title')
    refs = book_info.xpath('//div[@class="pl2"]/a/@href')
    scores = book_info.xpath('//div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
    
    booklist = [{'title':title,'ref':ref,'score':score} for title,ref,score in  zip(titles,refs,scores)]

    return booklist

def parsebookdetails(html,bookbasic):

    bookfull = bookbasic

    htmltext = getcontent(html)
    book_detail = etree.HTML(htmltext)

    # xpath solution

    auther = book_detail.xpath('//div[@id="info"]/span[1]/a/text()')
    price = book_detail.xpath('//div[@id="info"]/text()[9]')
    comment = book_detail.xpath('//p[@class="comment-content"]/span[@class="short"]/text()')


    # booklist = [{'title':title,'ref':ref,'score':score} for title,ref,score in  zip(titles,refs,scores)]

    try:
        bookfull['auther'] = auther[0]
        bookfull['price'] = price[0]
        bookfull['comment'] = comment[0:5]
    except:
        pass

    return bookfull
 


if __name__ == '__main__':

    booknewlist =[]

    for i in range(1):
        url = 'https://book.douban.com/top250?start='+str(i*25)
        mybookinfo = getcontent(url)
        booknewlist.extend(parsebooklist(mybookinfo))
        sleep(0.5)
    pdbook = pd.DataFrame(booknewlist)


    bookdetail = []
    for item in booknewlist:
        oneurl = item['ref']
        print(item)
        onedetail = parsebookdetails(oneurl,item)
        bookdetail.append(onedetail)
        sleep(0.5)
        print('currnet book is %s' % item['title'])
    pddetail = pd.DataFrame(bookdetail)

    pddetail.to_csv('22.csv',encoding='utf-8')





# a = tuple(f'https://book.douban.com/top250?start={page*25}' for page in range(3))

