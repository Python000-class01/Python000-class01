#安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
#并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
import re
import csv
from bs4 import BeautifulSoup as bs
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
header={}
header['user-agent'] = user_agent

def get_url_name(myurl):
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text,'html.parser')
    ol = bs_info.find('ol',class_ = 'grid_view')
    for detail in ol.find_all('div',class_ = 'item'):
        name = detail.find('div',class_ = 'hd').find('span',class_ = 'title').text
        NumberTag = detail.find('em').text
        Stars = detail.find('div', class_='star').find('span', class_='rating_num').text
        comnum = str(detail.find(text=re.compile('\d+人评价')))
        href = detail.find('a').get('href')
        comfive = []
        comfive.append(five_comment(href))
        print(comfive)
        writer.writerow((NumberTag,name,Stars,comnum,comfive))

    print('finish')

def five_comment(urls):
    res = requests.get(urls, headers=header)
    bs_com = bs(res.text, 'html.parser')
    comfive = []
    for comment in bs_com.find_all('div', class_='comment'):
        com = comment.find('span', class_='short').text
        comfive.append(com)
    #print(comfive)
    return '--//---'.join(comfive)

url=tuple(f'https://movie.douban.com/top250?start={page * 25}&filter='for page in range(10))
from time import sleep
if __name__ == '__main__':
    fp = open('./douban250movie.csv', 'w', newline='', encoding='utf_8_sig')
    writer = csv.writer(fp)
    writer.writerow(('序号', '电影名', '评分', '评价','短评'))
    for page in url:
        get_url_name(page)
        sleep(3)
    fp.close()