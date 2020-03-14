import requests
from bs4 import BeautifulSoup as bs
from os.path import exists

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
    header = {}

    header['user-agent'] = user_agent

    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text,'html.parser')

    return bs_info

def get_movie_info(movie_url):
    bs_info = get_url_name(movie_url)
    with open("L:\\movie.csv", "a", encoding='utf-8') as movie_file:
        for tags in bs_info.find_all('div',attrs={'class':'info'}):
            for atag in tags.find_all('a',):
                movie_href = atag.get('href')
                for title in tags.find('span',attrs={'class':'title'}):
                    movie_name = title.string
                for rating in tags.find_all('span',attrs={'class':'rating_num'}):
                    movie_rating = rating.get_text()
                movie_comment = get_url_name(movie_href)
                movie_shortComment = ','
                for comment_section in movie_comment.find_all('div',attrs={'id':'comments-section'}):
                    for comment_href in comment_section.find_all('span',attrs={'class':'pl'}):
                        for comment_count in comment_href.find_all('a',):
                            comment_counts = comment_count.get_text()
                    for hot_comment in comment_section.find_all('div',attrs={'class':'tab'}):
                        for short_comment in hot_comment.find_all('span',attrs={'class':'short'}):
                            movie_shortComment = movie_shortComment + short_comment.get_text()
            
            movie_string = movie_name + ',' + movie_rating + ',' + comment_counts + movie_shortComment
            movie_file.write(movie_string + '\n')


urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))

from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_movie_info(page)
        sleep(5)