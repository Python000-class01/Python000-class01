import requests
from bs4 import BeautifulSoup as bs


def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')
    total_list=[]
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        movie_list=[]
        for tag in tags.find_all('div', attrs={'class': 'hd'}):
            for title_tag in tag.find_all('span', class_='title'):
                # print(title_tag.get_text())
                movie_list.append(title_tag.get_text())
        for tag in tags.find_all('div', attrs={'class': 'bd'}):
            for star_tag in tag.find_all('span', class_='rating_num'):
                # print(star_tag.get_text())
                movie_list.append(star_tag.get_text())
            for comment_tag in tag.find_all('span',class_=''):
                # print(comment_tag.get_text())
                movie_list.append(comment_tag.get_text())
        total_list.append(movie_list)
    # with open('movie.csv','a') as f:
    #     for list1 in total_list:
    #         for list2 in list1:
    #             f.write(list2)

    print(total_list)

urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(3))

from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)

######################
