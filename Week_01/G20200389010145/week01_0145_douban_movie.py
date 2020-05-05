import requests
from bs4 import BeautifulSoup as bs
import csv
from time import sleep

#base_url = 'https://movie.douban.com/top250'
user_agent = 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
#https://movie.douban.com/top250?start=0&filter=
url_list = [f'https://movie.douban.com/top250?start={counter * 25}&filter='for counter in range(10)]
header = {}
header['user-agent'] = user_agent



# test_url = 'https://movie.douban.com/subject/1292052/'
def get_movie_info(myurl,movie_name):
    response = requests.get(myurl, headers=header)
    base_data = bs(response.text, 'html.parser')
    movie_info = [movie_name]
    #评分
    rating_num = base_data.find('strong', attrs={'class': 'll rating_num'}).text
    # print(rating_num)
    movie_info.append(rating_num)
    #短评数量
    comment_num = base_data.find('div', attrs={
                                 'id': 'comments-section'}).find('span', attrs={'class': 'pl'}).find('a').text
    # print(comment_num)
    movie_info.append(comment_num[3:-2])
    #评论
    for comments in base_data.find_all('div', attrs={'id': 'hot-comments'}):
        for comment in comments.find_all('p'):
            movie_info.append(comment.text)
    return movie_info

def get_url_info(myurl):
    response = requests.get(myurl,headers=header)
    base_data = bs(response.text,'html.parser')
    movie_infos = []
    for tag in base_data.find_all('div',attrs={'class':'hd'}):
        # print(tag)
        for tag_1 in tag.find_all('a') :
            sleep(3)
            # print(tag_1.find_all('span',attrs={'class':'title'})[0].text)
            # print(tag_1.get('href'))
            # f.write(tag_1.find_all('span', attrs={'class': 'title'})[0].text)
            movie_name = (tag_1.find_all('span', attrs={'class': 'title'})[0].text)
            movie_infos.append(get_movie_info(tag_1.get('href'), movie_name))

    return movie_infos


if __name__ == '__main__': 
    csv_head = ['name', 'rating_num', 'comment_num',
                'comment1', 'comment2', 'comment3', 'comment4', 'comment5', ]
    csv_lines = []
    with open('douban_movie.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f, delimiter=',', lineterminator=';\n')
        f_csv.writerow(csv_head)
        for url in url_list:
            csv_lines = get_url_info(url)
            f_csv.writerows(csv_lines)


