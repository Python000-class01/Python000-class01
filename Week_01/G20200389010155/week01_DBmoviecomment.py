import requests
import re
import csv
import sys
import pandas as pd
from bs4 import BeautifulSoup as bs

# Python 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    result=[]   #定义接纳所有信息的汇总列表
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):

            # 获取所有链接
        movielink = tags.find('a').get('href')
            # 获取电影名字
        moviename= tags.find('span', class_='title').get_text()
        moviecomment = tags.find('span',class_='rating_num').get_text()
        commentcounts = tags.find(text=re.compile('人评价$'))
        mvresponse=requests.get(movielink,headers=header)
        mvbs_info=bs(mvresponse.text,'html.parser')
        mvview=mvbs_info.find_all('span',class_='short')
        topcom1=str(mvview[0].get_text())
        topcom2=str(mvview[1].get_text())
        topcom3=str(mvview[2].get_text())
        topcom4=str(mvview[3].get_text())
        topcom5=str(mvview[4].get_text())
        print(moviename + "        " + moviecomment + "           " + commentcounts + "    " + movielink+" "+topcom1)
        result.append([moviename,moviecomment,commentcounts,movielink,topcom1,topcom2,topcom3,topcom4,topcom5])
    return result  #返回所有采集信息的嵌套列表汇总。


            # 生成包含所有页面的元组
urls = tuple(f'https://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))


from time import sleep


if __name__ == '__main__':   #定义整个py的入口
    print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
    csv_file = open('DBCS.csv', 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(csv_file)
    writer.writerow(['电影名称', '评分', '短评数量', '电影链接', '热评1', '热评2', '热评3', '热评4', '热评5'])
    offset=0
    csvlist=[]
    for page in urls:
        csvlist.append(get_url_name(page))
        sleep(5)
    print(csvlist)    #测试是否生成了对应列表，注意这里输出为[[[]]]三层嵌套列表，所以需要进行双for循环拆解成单层列表。
    for each in csvlist:
        for i in each:
            writer.writerow(i)
csv_file.close()
