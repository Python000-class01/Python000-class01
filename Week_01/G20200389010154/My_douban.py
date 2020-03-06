import requests
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
    print(response.text)
    selector = etree.HTML(response.text) # type(selector):lxml.etree._Element
    print(selector.xpath('//*[@id="wrapper"]//div[@class="pl2"]//a/@title'))




# urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10))

if __name__ == '__main__':
    for page in range(1):
        astring = 'https://book.douban.com/top250?start={ page * 25}'
        # geturlcontentByHtml(astring)
        geturlcontentByXml(astring)
        sleep(2)
