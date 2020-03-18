"""
安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的
电影名称、评分、短评数量和前 5 条热门短评，
并以 UTF-8 字符集保存到 csv 格式的文件中。
"""


"""
method1: 使用Beautifulsoup解析，存储为csv文件
"""
import requests, bs4
import csv
import numpy as np
import time


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
url = 'https://movie.douban.com/top250'

csv_file = open(r'G:\python_advanced\homework\week1\homework1\\week01_0028_douban_top250.csv', 'w', newline='', encoding='utf-8')
# 用open()函数创建csv文件对象
writer = csv.writer(csv_file)
# 用csv.writer()函数创建一个writer对象
writer.writerow(['电影名称', '评分', '短评数量', '热评1', '热评2', '热评3', '热评4', '热评5'])
# 写入表头

delays = [3, 5, 8, 9, 1, 12, 17]
for i in range (10):
    params = {'start':str(i * 25), 'filter':''} # 传递url参数
    
    delay = np.random.choice(delays)
    time.sleep(delay) # 设置延时

    res = requests.get(url, params=params, headers=headers) # 发出请求，返回response对象
    # print(res.status_code)
    bs = bs4.BeautifulSoup(res.text, 'html.parser') # 解析网页源代码
    info_list = bs.find_all('div', class_='info') # 找到所有的<div class="info">元素，该元素下有需要的信息
    for movie in info_list:
        title = movie.find('span', class_='title').text # 获得电影名
        star = movie.find('div', class_='star') # <div, class="star">下有评分、短评数量信息
        rates = star.find_all('span')[1].text # 评分在第2个span标签内
        num = star.find_all('span')[3].text # 短评数量在第4个span标签内
        
        movie_url = movie.find('a')['href'] # 获得电影详情链接
        res_comment = requests.get(movie_url, headers=headers) 
        bs_comment = bs4.BeautifulSoup(res_comment.text, 'html.parser')
        comments = bs_comment.find_all('span', class_='short')
        results = []
        results[:3] = [title, rates, num]
        for comment in comments:
            short = comment.text # 获得短评
            results.append(short) 

        writer.writerow(results) # 将电影名称、评分、短评数量、热门短评等信息写进csv文件

csv_file.close()
