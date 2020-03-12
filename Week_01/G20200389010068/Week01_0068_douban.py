import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd
# 豆瓣爬去数据
herf = []
names = []
grade = []
number=[]
numbers=[]
all=[]
review=[]
# def get_url_in(url):
#     ua = UserAgent()
#     user_agent = ua.random
#     header = {}
#     header['user-agent'] = user_agent
#     response = requests.get(url, headers=header)
#     bs_info = bs(response.text, 'html.parser')
#     for page in bs_info.find_all('span',attrs={'class':'short'})[0:5]:
#         review.append(page)
def _response_(url):
    ua = UserAgent()
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    user_agent =ua.random
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    return bs_info
def get_url(myurl):
    ua=UserAgent()
    # user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    user_agent = ua.random
    header={}
    header['user-agent'] = user_agent
    response=requests.get(myurl,headers=header)
    # print(response)
    bs_info=bs(response.text,'lxml')

    for tags in bs_info.find_all('div',attrs={'class': 'pl2'}):
        for tag in tags.find_all('a'):
            # 获取图书名字
            names.append(tag.get('title'))
            # 获取图书的链接
            herf.append(tag.get('href'))
            # 获取每一本书前5热评
            b=str(tag.get('href'))
            # _response_(tag.get('href'))
            re=requests.get(b+'comments/',headers=header).text
            bs_in=bs(re,'lxml')
            for revi in  bs_in.find_all('span',attrs={'class':'short'})[0:5]:
                review.append(str(revi.text))
            # numbe = list(str(i + 1) + ': ' + review[i] for i in range(len(review)))
            # numbers.append(numbe)
            # print(re)
            # sleep(1)
            # print(tag.get('title'))
            # print(tag.get('href'))
    # 获取每一本书的评分
    for pings in bs_info.find_all('span',attrs={'class': 'rating_nums'}):
        grade.append(pings.text)
        # print(pings.text)
    #     获取热评
    for nums in bs_info.find_all('span',attrs={'class':'pl'}):
        # 去掉括号以及空格
        num=str(nums.text).replace('(','').replace(')','').strip()
        # print(num)
        number.append(num)
    del(number[-1])
    # return numbers1







if __name__ =='__main__':
    url=list(f'https://book.douban.com/top250?start={25 * i}' for i in range(10))
    # url='https://book.douban.com/top250?'
    # get_url(url)
    for pa in url:
        get_url(pa)
        # print(f'page 的长度 ：{page}')
        sleep(1)
    # print(f'names 的长度 ：{len(names)}')
    # print(f'评价数量的长度 ：{len(grade)}')
    # print(f'评分的长度 ：{len(number)}')
    # print(len(herf))
    # print(review)
    # print(len(review))
    ALL=[names[i]+':'+grade[i] +'  '+number[i] for i in range(len(number))]
    # print(f'ALL : {ALL}')
    columns_name = ['douban']
    all = [str(ALL),str(review)]
    book = pd.DataFrame(columns=columns_name, data=all)
    book.to_csv('./book.csv', encoding='utf-8')


