import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    titlelist = starlist = peoplecountlist = reviewlist = []
    header['user-agent'] = user_agent
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser') 
    for tags in bs_info.find_all('div', attrs={'class': 'item'}):
        title = tags.find('span', class_='title').get_text()
        titlelist += title
        # print(title)
        star = tags.find('span',class_='rating_num').get_text()
        starlist += star
        # print(star)
        people = tags.find('div',class_='star')
        # print(people)
        peoplecount = people.find_all('span')[3].contents[0]
        peoplecountlist += peoplecount
        # print(peoplecount)
        review = tags.find('p',class_='quote').find_all('span')[0].contents[0]
        reviewlist += review
        # print(review)
    totallist = [titlelist,starlist ,peoplecountlist ,reviewlist]
    test=pd.DataFrame(data=totallist)
    test.to_csv('temp.csv',encoding='utf-8')




urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))

if __name__ == '__main__':

    for page in urls:
        get_url_name(page)
        sleep(10)
