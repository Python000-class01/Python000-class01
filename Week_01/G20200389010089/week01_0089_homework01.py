
# *************************************************
# 要求：安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，
#      并以 UTF-8 字符集保存到 csv 格式的文件中。
# 时间：2020.02.29-2020.03.11
# 作者：Carolina
# *************************************************

#!/usr/bin/python
import re
import requests
from bs4 import BeautifulSoup as bs 
import csv

def get_url_name(myurl,file_write):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)

    # 另一种导入包的方法
    from bs4 import BeautifulSoup as bs

    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('td', attrs={'valign':'top'}):
        for atags in tags.find_all('div',attrs={'class':'pl2'}):
            for atagsRate in tags.find_all('div',attrs={'class':'star clearfix'}):
                for atag in atags.find_all('a',):
                    #获取所有链接
                    urlItem = str(atag.get('href'))
                    print(atag.get('href'))
                    file_write.writerow(urlItem)
                    #获取图书名字
                    print(atag.get('title'))
                    file_write.writerow(atag.get('title'))
                #获取评分
                atagRate = atagsRate.find_all('span',attrs={'class':'rating_nums'})
                array1 = str(atagRate).split(">", 1)
                array2 = str(array1[1]).split('<')
                print(array2[0])
                file_write.writerow(array2[0])
                #评论数
                atagComentsNums = atagsRate.find_all('span',attrs={'class':'pl'})
                array1 = str(atagComentsNums).split("(", 1)
                array2 = str(array1[1]).split(")")
                print(array2[0])
                file_write.writerow(array2[0])
                #-------------------    
                headerItem = {}
                headerItem['user-agent'] = user_agent
                responseItem = requests.get(urlItem,headers=headerItem)
                bs_info_item = bs(responseItem.text, 'html.parser')
                index = 0
                for atagComments in bs_info_item.find_all('li',attrs={'class':'comment-item'}):
                    argComment = atagComments.find('span',attrs={'class':'short'})
                    #获取评论5条
                    print(argComment.text)
                    file_write.writerow(argComment.text)
                    index =index + 1
                    if index >5:
                        break
                #防止被封IP
                sleep(5)

#强制转化成元祖的形式
urls = tuple(f'https://book.douban.com/top250?start={ page * 25}' for page in range(10))

from time import sleep
import os
if __name__ =='__main__':
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR,'douban_homework.csv')
    file = open(file_path,'a',encoding='utf-8')
    file_write = csv.writer(file)
    for page in urls:
        get_url_name(page,file_write)
        #防止被封IP
        sleep(10)

    file.close()


