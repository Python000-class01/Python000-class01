import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from time import sleep
import csv

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
csv_array = [['电影名称', '评分', '短评数量', '短评前5条内容']]


def get_movie250_to_csv(myurl):
    movies = get_250(myurl)
    for movie in movies:
        csv_array.append(movie)
    with open('week01_0648_movie_250_content.csv', 'w', encoding='utf-8') as f:
        writer_csv = csv.writer(f)
        for line in csv_array:
            writer_csv.writerow(line)


def get_250(myurl):
    response = get_url_response(myurl)
    bs_info = bs(response.text, 'html.parser')
    li_array = bs_info.find_all('ol',attrs={'class': 'grid_view'})
    movies = []
    for tags in li_array:
        for li in tags.find_all('li',):
            movie = []
            a_tag = li.find('a')
            title_tag = li.find('span', attrs={'class', 'title'}).text
            a_href = a_tag.get('href')
            rating_num = li.find('span', attrs={'class', 'rating_num'}).text
            div_star_num = li.find('div', attrs={'class', 'star'}).find_all('span',)[3].text
            # print(f'title_tag:{title_tag},a_href:{a_href},rating_num:{rating_num},div_star_num:{div_star_num}')
            short_list = get_top5_short_list(a_href)
            movie.append(title_tag)
            movie.append(rating_num)
            movie.append(div_star_num)
            movie.append( ','.join(short_list))
            movies.append(movie)
    return movies


def get_top5_short_list(short_url):
    response = get_url_response(short_url)
    bs_info = bs(response.text, 'html.parser')
    short_div_array = bs_info.find_all('div', attrs={'class': 'comment-item'})
    short_list = []
    for short_item in short_div_array:
        comment_author = ''
        comment_info = ''
        comment_info_obj = short_item.find('span', attrs={'class': 'comment-info'})
        if not comment_info_obj is None:
            comment_author_a = comment_info_obj.find('a')
            if comment_author_a:
                comment_author = comment_author_a.text
        comment_short_span = short_item.find('span', attrs={'class': 'short'})
        if comment_short_span:
            comment_info = comment_short_span.text
        if comment_info != '':
            short_list.append(f'短评人:{comment_author},短评内容:{comment_info}')
    return short_list


def get_url_response(url):
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(url, headers=header)
    return response


if __name__ == '__main__':
    url_tuple = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))
    for url in url_tuple:
        get_movie250_to_csv(url)
        sleep(3)

