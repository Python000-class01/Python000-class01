import requests
from time import sleep
import random
from bs4 import BeautifulSoup as bs
import re

urls_tuple = tuple(['https://movie.douban.com/top250?start='+str(25*i) for i in range(10)])

r_headers = {}
r_headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36'

for url in urls_tuple:
    sleep(random.randint(0, 5))
    response = requests.get(url, headers=r_headers)
    bs_info = bs(response.text, 'html.parser')

    for div_tag in bs_info.find_all('div', attrs={'class': 'info'}):
        movie_info = ''
        for hd_tag in div_tag.find_all('div', attrs={'class': 'hd'}):
            for span_tag in hd_tag.find_all('span', attrs={'class': 'title'}):
                movie_info += ('名称：' + span_tag.get_text())
                break
        
        for bd_tag in div_tag.find_all('div', attrs={'class': 'bd'}):
            for span_tag in bd_tag.find_all('span', attrs={'class': 'rating_num'}):
                movie_info += ('; 评分：' + span_tag.get_text())
                # break

        movie_info += ('; ' + div_tag.find(string=re.compile('人评价')))

        print(movie_info)