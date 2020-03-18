import requests
from bs4 import BeautifulSoup as bs
import re
from time import sleep
import csv


def get_movie_list():
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
     }
    movies = []
    for i in range(1,10):
        url = f'https://movie.douban.com/top250?stat={i*25}'
        response = requests.get(url,headers=headers,timeout=10)

        movie_list = bs(response.text,'html.parser')

        for movie in movie_list.find_all('div',attrs={'class':'info'}):
            movie_header = movie.find_all('div',attrs={'class':'hd'})
            movie_scores = movie.find_all('div',attrs={'class':'bd'})

            for i in range(len(movie_header)):
                movie_atag = movie_header[i].a
                #评论链接
                movie_href = movie_atag.get('href')
                #电影名称
                movie_title = movie_atag.span.get_text()
                movie_star = movie_scores[i].find('div')
                movie_score = movie_star.find_all('span')
                #获取电影评分
                movie_rate = movie_score[1].get_text()
                #评论人数，正则匹配第一个数字类型
                movie_rate_num = int(re.search(r'\d*',movie_score[3].get_text()).group())

                ##获取电影影评
                movie_comment_url = '{}comments?status=P'.format(movie_href)#评论链接
                comment_res = requests.get(movie_comment_url, headers=headers, timeout=10)
                comment_xml = bs(comment_res.text,'html.parser')
                comments = comment_xml.find_all('p',attrs={'class':''})
                movie_comments = []
                for i in range(1,6):
                    comment = comments[i].span.get_text()
                    movie_comments.append(comment)
                print(movie_comments)

                movie_dict = {}
                movie_dict['title'] = movie_title
                movie_dict['score'] = movie_rate
                movie_dict['rate_num'] = movie_rate_num
                movie_dict['comment'] = movie_comments
                movies.append(movie_dict)
        sleep(5)
    print(movies)
    write_data(movies)


def write_data(movies):
    with open(r"C:\Users\Snail\Desktop\movie.csv",'w',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['title','score','rate_num','comment'])
        writer.writeheader()
        for movie in movies:
            print('正在写入{}'.format(movie['title']))
            writer.writerow(movie)



if __name__ == '__main__':
    get_movie_list()
