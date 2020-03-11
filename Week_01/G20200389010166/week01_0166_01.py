import requests
import lxml.etree
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(myurl, headers=header)
    selector = lxml.etree.HTML(response.text)
    sub_urls = selector.xpath('//div[@class="hd"]/a/@href')
    for sub_url in sub_urls:
        sub_list.append(sub_url)

def get_info(mylist):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
    header = {}
    header['user-agent'] = user_agent
    response_sub = requests.get(mylist, headers=header)
    selector = lxml.etree.HTML(response_sub.text)
    #info = selector.xpath('//h1/span[1]/text()')
    movie_name = selector.xpath('//h1/span[1]/text()')
    movie_star = selector.xpath('//strong[1]/text()')
    movie_hotnum = selector.xpath('//div[@id="comments-section"]/div/h2/span/a[1]/text()')
    movie_short = selector.xpath('//div[@id="hot-comments"]/div/div/p/span/text()')
    #print(movie_name,movie_star,movie_hotnum,movie_short)
    info_list = [str(movie_name),str(movie_star),str(movie_hotnum),str(movie_short)]
    my_list.append(info_list)

def list_to_csv(my_list):
    colums_name = ['电影名称', '评分', '短评数量', '热门短评']
    movie_list = pd.DataFrame(columns = colums_name, data = my_list, index = list(range(250)))
    movie_list.to_csv('./movie_list.csv', encoding='UTF-8')

sub_list = []
my_list = []
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))


from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(6)
    print(sub_list)
    for sub_url in sub_list:
        get_info(sub_url)
    print(my_list)
    list_to_csv(my_list)


