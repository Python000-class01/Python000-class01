# 安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
# 并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import time

def get_url(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # header = {}
    # header['user-agent'] = user_agent
    header = {'user-agent':user_agent}
    response = requests.get(url,headers=header)
    soup = bs(response.text, 'html.parser')
    for tags in soup.find_all('div', attrs={'class': 'info'}):
        url_list = []
        for atag in tags.find_all('a',):
            # 获取链接
            url1 = atag.get('href')
            # print(url1)
            url_list.append(url1)    
            # # 获取电影名称
            # title = atag.find('span', attrs={'class': 'title'}).text
            # print(title)
            
        # for star in tags.find_all('div', attrs={'class': 'star'}):
        #     # 获取电影评分
        #     goal = star.find('span', attrs={'class':'rating_num'}).text
        #     print(goal)  
            
            # # 获取电影短评数量   
            # pj = star.find(text=re.compile('人评价'))
            # nums = re.findall(r'\d+',pj)[0]
            # # nums = star.find_all('span')[3].text
            # print(nums)
            
        for url2 in url_list:
            response1 = requests.get(url2, headers=header)
            soup1 = bs(response1.text, 'html.parser')
            title = soup1.find('span',attrs={'property':'v:itemreviewed'}).text
            # print(title)
            goal = soup1.find('strong', attrs={'class':'ll rating_num'}).text
            # print(goal)
            nums = soup1.find('span', attrs={'property':'v:votes'}).text
            # print(nums)
            comments = soup1.find_all('div', attrs={'class':'comment'} )
            #获取5条热门短评
            rmdp = ''
            for comment in comments:
                rmdp += comment.find('span', attrs={'class':'short'}).text + ' \n'
            # print(rmdp)
            list_all.append([title, goal, nums, rmdp])
            time.sleep(5)
        

list_all = []
urls = tuple(f'https://movie.douban.com/top250?start={page*25}' for page in range(10))


#单独执行python文件的一般入口
if __name__ == '__main__':
    for page in urls:
        get_url(page)
        time.sleep(5)
    
    save = pd.DataFrame(columns=['电影名称', '评分', '短评数量', '5条热门短评'], data=list_all,index='序号')
    save.to_csv('zuoye1.csv', encoding='utf-8',)