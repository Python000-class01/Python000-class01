import requests
from bs4 import BeautifulSoup as bs

url = "https://movie.douban.com/top250"
movie_list = [[], [], [], []]
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
header = {}
header['user_agent'] = user_agent

def get_url_name():
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for a_tags in tags.find_all('a', ):
            get_movie_info(a_tags.get('href'))

def get_movie_info(url):
    movie_list[0].append(
        bs_info.find('div', {'class': 'mod-hd'}).find('span', {'class': 'pl'}).find('a', ).get_text()[3:-2])

    movie_short_com = ''
    for span_tags in bs_info.find_all('div', {'class': 'comment'}):
        for tags in span_tags.find_all('span', {'class': 'short'}):
            movie_short_com = movie_short_com + '\n' + tags.get_text()

    movie_list[1].append(movie_short_com)
    movie_list[2].append(bs_info.find('span', {'property': 'v:itemreviewed'}).get_text())
    movie_list[3].append(bs_info.find('strong', {'class': 'll rating_num'}).get_text())

def save_as_csv():
    dateframe = panda.DataFrame({ movie_list[0], movie_list[1],  movie_list[2], movie_list[3]})
    dateframe.to_csv('homework1.csv', index=False, sep=',')

if __name__ == '__main__':
    get_url_name()
    save_as_csv()