import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd
from time import sleep

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(myurl, headers = header)
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        url = tags.find('a',).get('href')
        title = ''
        ready_to_write = []
        for atags in tags.find_all('span', attrs={'class': 'title'}):
            title += atags.text
        star = tags.find('span', attrs={'class': 'rating_num'}).text
        comment = tags.find('div', attrs={'class': 'star'}).contents[7].text

        ready_to_write = [title, star, comment]
        res = requests.get(url, headers = header)
        bs_info2 = bs(res.text, 'html.parser')
        i = 0
        for short in bs_info2.find_all('span', attrs={'class': 'short'}):
            i += 1
            if i < 6:
                ready_to_write.append(str(short.text).replace("\n", ""))
            else:
                break
        data_list.append(ready_to_write)
        

if __name__ == '__main__':
    data_list = []
    urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))
    for page in urls:
        get_url_name(page)
        sleep(5)
    film = pd.DataFrame(columns=['title', 'star', 'comment', 'short1', 'short2', 'short3', 'short4', 'short5'], data = data_list)
    film.to_csv('./film.csv', encoding = 'utf8')