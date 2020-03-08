from time import sleep
from bs4 import BeautifulSoup as bs
import requests


def get_url_name(myurl, csv_writer):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    header['Host']='movie.douban.com'

    response = requests.get(myurl, headers=header)

    # print(response.text)

    bs_info = bs(response.text, 'html.parser')
    # print(dir(bs_info))

    # print(bs_info.find_all('div',attrs={'class':'pl2'})[0])

    for tags in bs_info.find_all('li'):
        if(len(tags.find_all('span', attrs={'class': 'title'})) > 0):
          content = []
          title = tags.find_all('span', attrs={'class': 'title'})[0].get_text()
          score = tags.find('span', attrs={'class': 'rating_num'}).get_text()
          evaluate_num = tags.find('div', attrs={'class': 'star'}).find_all('span')[
                                   3].get_text()
          detail_url = tags.find('a').get('href')
          detail_response = requests.get(detail_url,headers=header)
          sleep(1)
          bs_detail_info = bs(detail_response.text, 'html.parser')
          content.append(title)
          content.append(score)
          content.append(evaluate_num)
          for detail in bs_detail_info.find_all('span', attrs={'class': 'short'}):
              content.append(detail.get_text())
          print(content)
          csv_writer.writerow(content)
          
       


urls = tuple(
    f'https://movie.douban.com/top250?start={page * 25}' for page in range(2))

# 导入CSV安装包
import csv

# 1. 创建文件对象
f = open('result.csv','w',encoding='utf-8')

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

# 3. 构建列表头
csv_writer.writerow(["标题","得分","评价人数",'评价1','评价2','评价3','评价4','评价5'])

if __name__ == '__main__':
    for page in urls:
        get_url_name(page,csv_writer)
        sleep(5)
