import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from time import sleep
from lxml import etree

def geturlcontentByHtml(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url,headers=header)
    bs_info = bs(response.text, 'html.parser')
    print(type(bs_info))
    for ctags in bs_info.find_all('div', attrs={'class':'pl2'}):
        for atag in ctags.find_all('a'):
            print(atag.get('href'))
            print(atag.get('title'))

def geturlcontentByXml(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url,headers=header)
    #print(response.text)
    selector = etree.HTML(response.text) # type(selector):lxml.etree._Element
    #bookTitles = selector.xpath('//*[@id="wrapper"]//div[@class="pl2"]//a/@title')
    film_review = selector.xpath('//div[@id = "wrapper"]//div[@class = "short-content"]/text()')
    print(film_review[4],'\n')
    data_review = np.zeros((5,2), dtype=np.str_) #还是不能转string，要tolist转成python的list
    data_review = data_review.tolist()
    di = 0
    for i in range(1,len(film_review),1):
        if di < 5:
           f = film_review[i].replace(' ', '').replace('\n', '').replace('\r', '')
           if f.endswith('\xa0('):
               print(i,f,'\n')
               data_review[di]=[di, f]
               di = di+1
    print(data_review)
    column = ['index', 'review']
    csv_text = pd.DataFrame(columns=column,data=data_review,dtype=np.str_)
    csv_text.to_csv('my_review.csv',encoding='utf_8')





# urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10))

if __name__ == '__main__':
    for page in range(1):
        #astring = 'https://book.douban.com/top250?start={ page * 25}'
        astring ='https://movie.douban.com/review/best/' # 影评
        # geturlcontentByHtml(astring)
        geturlcontentByXml(astring)
        sleep(2)
