import requests
import pandas as pd
from time import sleep
import lxml.etree
import csv

#获取电影数据
def get_movie_data(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    movie_name = selector.xpath(
        '//li//div[@class="hd"]/a[1]/span[1]/text()')
    movie_score = selector.xpath(
        '//li//div[@class="star"]/span[2]/text()')
    movie_comment_num = selector.xpath(
        '//li//div[@class="star"]/span[4]/text()')
    movie_url = selector.xpath(
        '//li//div[@class="hd"]/a/@href')
    for i in range(25):
        movie_response = requests.get(movie_url[i], headers=header)
        movie_selector = lxml.etree.HTML(movie_response.text)
        movie_comment_top5 = movie_selector.xpath(
            '//div[@class="comment"]/p/span[@class="short"]/text()')
        movie_data.append([movie_name[i], movie_score[i],
                           movie_comment_num[i]] + movie_comment_top5)

#将数据转换为csv格式
def trans_csv(data):
    column_name = ['电影名', '评分', '评论数', '热评1',
                   '热评2', '热评3', '热评4', '热评5']
    text = pd.DataFrame(columns=column_name, data=data)
    text.to_csv('./movie_data.csv',
                encoding='utf-8', index=0)

def write_csv(data):
    column_name = ['name', 'rating_num','comment_num','comment1', 'comment2', 'comment3','comment4', 'comment5']
    with open('movie.csv','w', encoding='utf-8') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(column_name)
        csv_f.writerows(data)


urls = [f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))]
# urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))
movie_data = []

if __name__ == '__main__':
    for page in urls:
        get_movie_data(page)
        sleep(5)
        print(page)
    print("grab data finished! begin to write data to csv")
    trans_csv(movie_data)
    # write_csv(movie_data)