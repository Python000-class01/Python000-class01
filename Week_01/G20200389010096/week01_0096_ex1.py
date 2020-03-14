import requests
from bs4 import BeautifulSoup as bs
import re
import time
import csv

output_file = '/Users/ysun/pythonProjects/advanced_camp/Python000-class01/Week_01/G20200389010096/movies.csv'

def retrieve_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))
    movies = []

    for url in urls:
        response = requests.get(url, headers=headers, timeout=15)
        page_content = bs(response.text, 'html.parser')

        for movie_info in page_content.find_all('div', attrs={'class':'info'}):
            movie_header = movie_info.find_all('div', attrs={'class':'hd'})
            movie_profile = movie_info.find_all('div', attrs={'class':'bd'})

            for i in range(len(movie_header)):
                movie_atag = movie_header[i].a
                movie_link = movie_atag.get('href')
                movie_title = movie_atag.span.get_text()
                movie_rating = movie_profile[i].find('div').find_all('span')
                movie_rating_score = movie_rating[1].get_text()
                movie_comments_link = movie_link + 'comments?status=P'
                comments_response = requests.get(movie_comments_link, headers=headers, timeout=10)
                comments_content = bs(comments_response.text, 'html.parser')
                comments_header = comments_content.find('div', attrs={'class':'clearfix Comments-hd'})
                comments_count = int(re.search(r'\d+', comments_header.find_all('span')[0].get_text()).group())
                comments = comments_content.find_all('p',attrs={'class':''})
                comments_top5 = []
                for i in range(5):
                    comment = comments[i].span.get_text()
                    comments_top5.append(comment)

                movie_dict = {}
                movie_dict['title'] = movie_title
                movie_dict['score'] = movie_rating_score
                movie_dict['comments_count'] = comments_count
                movie_dict['comments'] = (' | ').join(comments_top5)
                movies.append(movie_dict)

        time.sleep(5)
    
    write_data(movies)


def write_data(movies):
    with open(output_file, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['TITLE', 'SCORE', 'COMMENTS_COUNT', 'COMMENTS'])
        writer.writeheader()
        for movie in movies:
            print('Writing {} ...'.format(movie['title']))
            writer.writerow(movie)
    

if __name__ == '__main__':
    retrieve_movies()