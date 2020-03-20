import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import lxml
import pandas as pd
import os

def save2csv(csv_file, columns_name, attrs):
    df = pd.DataFrame(columns=columns_name, data=attrs, index=[0])
    if os.path.exists(csv_file):
        df.to_csv(csv_file, encoding='utf-8', header=False, mode='a', index=False)
    else:
        df.to_csv(csv_file, encoding='utf-8', mode='a', index=False)

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    columns_name = [
        'title', 'rating', 'comment_count', 'comment_top5'
    ]
    csv_file="douban_movie250.csv"

    response = requests.get(myurl, headers=header)
    #print(myurl.split("=")[1])
    with open(f"page{myurl.split('=')[1]}.html", 'w',encoding='utf-8') as f:
        f.write(response.text)
    '''
    爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
    并以 UTF-8 字符集保存到 csv 格式的文件中。
    '''
    bs_info = bs(response.text, 'html.parser')


    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        movie_name = ''
        movie_href = ''
        for atag in tags.find_all('a'):
            # 获取所有链接
            print(atag.get('href'))
            movie_href=atag.get('href')
            # 获取图书名字
        movie_average=bs_info.find('span',attrs={'property':"v:average"})
        print(f'评分：{movie_average.text}')

        for item in atag.find_all('span'):
            movie_name+=item.text
        print(movie_name)

        response_movie = requests.get(movie_href, headers=header)
        print(response_movie)
        bs_movie_info = bs(response_movie.text, 'lxml')
        movie_people=bs_movie_info.find('span',attrs={'property':"v:votes"})
        print(f'评分人数：{movie_people.text}')
        pinglunst=bs_movie_info.find('div',attrs={'id':"hot-comments"})
        pingluns = pinglunst.findAll('span', attrs={'class': "short"})
        comment_top5=''
        for tmp in pingluns:
            print(tmp.text)
            comment_top5 = comment_top5 + tmp.text + ';'
        movie_dict = {'title': movie_name, 'rating': movie_average.text, 'comment_count': movie_people.text, 'comment_top5': comment_top5}
        save2csv(csv_file, columns_name, movie_dict)
        break# 测试中



urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}&filter=' for page in range(1))






## 单独执行 python 文件的一般入口
if __name__ == '__main__':
    for url in urls:
        get_url_name(url)
        sleep(5)
