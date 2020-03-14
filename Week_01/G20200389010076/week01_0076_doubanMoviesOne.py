import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


#获取user-agent
def get_header():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    return headers

#获取电影主页面的bs
def getBSInfo(page):
    start = str(page * 25)
    url = 'https://movie.douban.com/top250'
    headers = get_header()
    params = {'start': start}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code==200:
        bs_info = bs(response.text, 'lxml')
        return bs_info
    return None

#获取电影详细页面的bs
def getMoviesBSInfo(movies):
    movies_url = movies.find('a')['href']
    headers = get_header()
    movies_response = requests.get(movies_url, headers=headers)
    movies_bs= bs(movies_response.text, 'lxml')
    return movies_bs

#爬取电影详细页面信息
def forwardPage(page):
    #获取电影主页的bs
    bs_info=getBSInfo(page)
    if not bs_info:
        print('失败了')
        return

    #得到50部电影详细页面的url
    movies_list=bs_info.find_all('ol',class_='grid_view')[0].find_all('li')
    #分别用于存储电影名字，电影评分，电影评论条数，电影评价
    movies_name,movies_value,all_comment,all_short_comment=[],[],[],[]
    #遍历电影的url，进入电影详细页面获取所需要的信息
    for movies in movies_list:
        #获取电影详细页面的bs
        movies_bs=getMoviesBSInfo(movies)
        #获取电影名称
        movies_name.append(movies_bs.find('h1').find('span').string)
        #获取电影评分
        movies_value.append(movies_bs.find('strong',class_='rating_num').string)
        #获取短评数量
        short_number=movies_bs.find('div', class_='mod-hd').find('span',class_='pl').find('a').string
        #用正则表达式截取电影短评条数
        number=re.compile(r'\d+')
        mo=number.search(short_number)
        all_comment.append(mo.group())
        #前五条热门短评
        comment=movies_bs.find('div', attrs={'id': 'hot-comments'}).find_all('span', class_='short')
        short_comment=[]
        for i in range(0,5):
            short_comment.append(comment[i].string)
        all_short_comment.append(short_comment)

    #将爬取的50条电影的信息加入csv文件中
    datas={'moviesName': movies_name,'moviesRatings':movies_value,'moviesNumbers':all_comment,'moviesComment':all_short_comment}
    movies = pd.DataFrame(data=datas)
    movies.to_csv('./movies.csv', encoding='utf-8',mode='a',header=False,index=False)


if __name__ == '__main__':
    #共需要爬取的页
    all_page=10
    #给csv文件添加列名
    columns_name = ['moviesName', 'moviesRatings', 'moviesNumbers', 'moviesComment']
    movies = pd.DataFrame(columns=columns_name)
    movies.to_csv('./movies.csv', encoding='utf-8',index=False)
    #分别爬取每页的信息，每页25部电影，共250部电影
    for page in range(0,all_page):
        forwardPage(page)
