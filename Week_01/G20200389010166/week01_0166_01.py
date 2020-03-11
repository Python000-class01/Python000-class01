import requests
import lxml.etree
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    my_list = []
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a',):
            # 获取所有链接
            sub_urls = atag.get('href')
            #print(sub_urls)
            response_sub = requests.get(sub_urls, headers=header)
            selector = lxml.etree.HTML(response_sub.text)
            #info = selector.xpath('//h1/span[1]/text()')
            movie_name = selector.xpath('//h1/span[1]/text()')
            movie_star = selector.xpath('//strong[1]/text()')
            movie_hotnum = selector.xpath('//div[@id="comments-section"]/div/h2/span/a[1]/text()')
            movie_short = selector.xpath('//div[@id="hot-comments"]/div/div/p/span/text()')
            #print(movie_name,movie_star,movie_hotnum,movie_short)
            info_list = [str(movie_name),str(movie_star),str(movie_hotnum),str(movie_short)]
            my_list.append(info_list)
    #print(my_list)
    colums_name = ['电影名称', '评分', '短评数量', '热门短评']
    movie_list = pd.DataFrame(columns = colums_name, data = my_list, index = list(range(250)))
    movie_list.to_csv('./movie_list.csv',encoding = 'UTF-8')
    #,encoding='gbk'

urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))


from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(7)