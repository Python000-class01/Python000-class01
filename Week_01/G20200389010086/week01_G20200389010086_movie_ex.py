import requests
from bs4 import BeautifulSoup
from time import sleep
import lxml.etree
import csv

HEADER = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36 '
}


def get_db_url(url):
    response = requests.get(url, headers=HEADER)
    bs_info = BeautifulSoup(response.text, 'lxml')
    for tags in bs_info.find_all('div', attrs={'class', 'hd'}):
        for tag in tags.find_all('a', ):
            get_movie_info(tag.get('href'))


def get_movie_info(movie_url):
    response = requests.get(movie_url, headers=HEADER)
    # 处理 电影名、评分、短频数量、热评等
    selector = lxml.etree.HTML(response.text)
    movie_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]

    movie_star = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
    movie_comment_number = selector.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()')[0]
    movie_hot_top5_comments = selector.xpath(' //*[@id="hot-comments"]/div/div/p/span/text()')

    movie_info = [movie_name, movie_star, movie_comment_number, movie_hot_top5_comments[0], movie_hot_top5_comments[1],
                  movie_hot_top5_comments[2], movie_hot_top5_comments[3], movie_hot_top5_comments[4]]

    writeCsv(csv_file, movie_info, 'a')


def writeCsv(file, line, write_type):
    out = open(file, write_type, encoding='utf-8')
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(line)


csv_file = '豆瓣电影top250.csv'
csv_header = ['影名', '评分', '热评数', '热评1', '热评2', '热评3', '热评4', '热评5']
writeCsv(csv_file, csv_header, 'w')

# python 文件的执行入口
if __name__ == '__main__':
    #  f-string是格式化字符串的新语法。f-string用大括号 {} 表示被替换字段，其中直接填入替换内容
    URLS = tuple(f'https://movie.douban.com/top250?start={page * 25}filter=' for page in range(1))
    for url in URLS:
        get_db_url(url)
        sleep(5)