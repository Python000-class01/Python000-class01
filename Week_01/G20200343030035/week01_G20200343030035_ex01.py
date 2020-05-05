'''
安装并使用 requests、bs4 库，
爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
并以 UTF-8 字符集保存到 csv 格式的文件中。
豆瓣电影top250地址：'https://movie.douban.com/top250'
'''

import requests
from bs4 import BeautifulSoup as bs
import csv
from time import sleep

# movieInfo : name/grade/commentNum
def get_movieInfo(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')

 
    for tags in bs_info.find_all('div',attrs={'class':'info'}): 
        # get name
        name = tags.select('.title')[0].getText()
        # get rating
        rating = tags.select('.rating_num')[0].getText()
        # get commentNum
        commentNum = tags.select('.star span')[3].getText()[:-3]
        # get address
        address = tags.select('a')[0].get('href')
        
        sleep(5)
        # get hotcomments
        hotcom = []
        res = requests.get(address,headers=header)
        bs_inner = bs(res.text,'html.parser')
        for item in bs_inner.select('.comment .short'):
            hotcom.append(item.getText())
        movieInfo = [name,rating,commentNum,hotcom]
        writeCSV(movieInfo)

# 写入csv
def writeCSV(content):
    with open(filename,'a', newline='', encoding='utf-8') as fi:
        cw = csv.writer(fi, delimiter='\t')
        cw.writerow(content)
    



if __name__ == '__main__':
    urls = tuple(f'https://movie.douban.com/top250?start={ page * 25}' for page in range(10))
    filename = 'top250movie_info.csv'
    writeCSV(['电影名称','评分','短评数量','5条热评'])
    for page in urls:
        get_movieInfo(page)
        sleep(5)

