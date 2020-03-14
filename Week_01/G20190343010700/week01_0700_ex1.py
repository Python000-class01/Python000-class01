''' 
运用requests、beautifulsoup爬取豆瓣电影top250，获得电影名称、评分及前五条短评，以csv格式存储 

'''

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


##### ——————————————————     动态伪装header     ——————————————————————— 

ua = UserAgent()
header = {}
header['user-agent'] = ua.random


##### ——————————————    初始化列表，后续添加相应的信息   ———————————————————    

url_movie = []
name_movie = []
rating_movie = []
information_movie = []

##### ——————————————    获取影片的name,评星等级，链接地址      ——————————————————

def movie_infor(url):
    response = requests.get(url,headers = header)
    soup = bs(response.text,'html.parser')
    tag_name = soup.find_all("span","title")
    tag_rating = soup.find_all("span","rating_num")
    movie_name = [tag_name[i].string for i in range(len(tag_name))]
    movie_names = [name for name in movie_name if not ''.join(name.split()).startswith('/')]    ### 去掉同名的
    movie_rating = [tag_rating[i].string for i in range(len(tag_rating))]     ### 获得影片评级
    url_list= [href.get('href') for title_href in soup.find_all('div', class_='hd') for href in title_href.find_all('a') if href.get('href')] ### 获得影片链接
    return url_list,movie_names,movie_rating

##### ——————————————    获取影片的前五条热门评论      ———————————————————————

def movie_information(url_list):
    information = []
    for url in url_list:
        response = requests.get(str(url),headers = header)
        soup = bs(response.text,'html.parser')
        movie_information = soup.find_all("span","short")
        movie_getFiveInformation = [movie_information[i].string for i in range(len(movie_information)) if movie_information[i].string is not None]  
        information.append(movie_getFiveInformation[:6])  #### 这里有没有更有效的写法，更节省空间的写法
        time.sleep(1) #### 每个影片短评获取后休息1秒
    return information

#####  ——————————————    将信息及评论放置到列表中     ——————————————————

for i in range(11):
    url = 'https://movie.douban.com/top250?start=' + str(i)
    print(f'Now we obtain the information from url', {url})
    ### 调用函数，获取影片基础信息
    url_list, movie_names, movie_rating = movie_infor(url)
    ### 调用函数，获取每个影片的前五条短评
    information = movie_information(url_list)
    ### 将获取的信息加入相应的列表中
    url_movie.extend(url_list)
    name_movie.extend(movie_names)
    rating_movie.extend(movie_rating)
    information_movie.extend(information)
    print("finish")   


#####  ——————————————    将爬取的信息用dataframe形式存储，并写入csv中     ——————————————————

df = pd.DataFrame({'movie_name':name_movie,'rating':rating_movie,'url':url_movie,'information':information_movie})

df.to_csv('/Users/huangzhijun/Python_50days/movie_top250.csv',sep=',',encoding = 'utf-8')


##### 在teriminal 跟 vscode中可以运行，pycharm中运行遇到arrays 不等长问题， 解决如下：
###
# #df = pd.concat([pd.DataFrame(name_movie), pd.DataFrame(url_movie), pd.DataFrame(rating_movie), pd.DataFrame(information_movie)], axis=1)
# df.columns = ['name','url','rating','information']
# df.to_csv('/Users/huangzhijun/Python_50days/movie_top250.csv',sep=',',encoding = 'utf-8')

'''  思考：  
     1. 现有的编程方式感觉更像是面向过程编程的，如果要改写成面向对象过程的，应该怎么改写？ 
     2. 有没有更节省空间跟时间的方式？ ——  协程？？？
     3. 吐个槽：多掉坑，掉着掉着就能获得九阳真经了~~~~~~


’‘’

     