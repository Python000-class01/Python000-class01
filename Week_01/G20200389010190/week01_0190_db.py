import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


def get_url(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
   
    response = requests.get(url,headers=header)
    soup = bs(response.text, 'html.parser')
    for tags in soup.find_all('div', attrs={'class': 'info'}):
        url_list = []
        for atag in tags.find_all('a',):
           
            url1 = atag.get('href')
         
            url_list.append(url1)    
            

        for url2 in url_list:
            response1 = requests.get(url2, headers=header)
            soup1 = bs(response1.text, 'html.parser')
            title = soup1.find('span', attrs={'property':'v:itemreviewed'}).text
           
            goal = soup1.find('strong', attrs={'class':'ll rating_num'}).text
      
            nums = soup1.find('span', attrs={'property':'v:votes'}).text
     
            comments = soup1.find_all('div', attrs={'class':'comment'} )
          
            rmdp = ''
            n = 0
            for comment in comments:
                rmdp += comment.find('span', attrs={'class':'short'}).text + ' \n'
                n += 1
                if n >= 5:
                    break
            )
            list_all.append([title, goal, nums, rmdp])
         


list_all = []
urls = tuple(f'https://movie.douban.com/top250?start={page*25}' for page in range(10))

from time import sleep

if __name__ == '__main__':
    for page in urls:
        get_url(page)
        sleep(5)

    save = pd.DataFrame(columns=['电影名称', '评分', '短评数量', '5条热门短评'], data=list_all,index='序号')
    save.to_csv('db.csv', encoding='utf-8',) 