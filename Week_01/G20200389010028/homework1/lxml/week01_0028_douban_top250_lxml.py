"""
method2: 使用lxml解析，整理成dataframe格式，调用pandas的to_csv方法将dataframe写入csv文件
顺便练习一下collections模块的defaultdict
"""

import requests
from lxml import etree
import pandas as pd
import numpy as np
from collections import defaultdict
import time

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
url = 'https://movie.douban.com/top250'

df_dict = defaultdict(list) # 创建一个字典值类型为列表的默认字典

delays = [3, 5, 8, 9, 1, 12, 17]

for i in range (10):    
    delay = np.random.choice(delays)
    time.sleep(delay) # 设置延时

    params = {'start':f'{i*25}', 'filter':''} # 传递url参数
    res = requests.get(url, params=params, headers=headers) # 发出请求，返回response对象
    doc = etree.HTML(res.text) # 解析网页源代码

    all_lines = doc.xpath('//div[@class="info"]') # 选取div元素，该div元素拥有值为info的属性
    for line in all_lines:
        name = line.xpath("./div[1]/a/span[1]/text()")[0] # 从当前路径出发，查找含有电影名称的节点，用text方法取出字符串
        grade = line.xpath("./div[2]/div/span[2]/text()")[0]
        num = line.xpath("./div[2]/div/span[4]/text()")[0]
        df_dict['电影名称'].append(name)
        df_dict['评分'].append(grade)
        df_dict['短评数量'].append(num)

        movie_url = line.xpath("./div[1]/a/@href")[0]
        real_url = movie_url+f'{"comments?status=P"}'
        res_movie = requests.get(real_url, headers=headers)
        doc_movie = etree.HTML(res_movie.text)
        comments = doc_movie.xpath('//div[@class="comment"]')
        comment_list = []
        for index, comment in enumerate(comments):
                hot = comment.xpath("./p/span/text()")[0].strip()
                comment_list.append(hot)
                if index == 4:
                    break

        for index, item in enumerate(comment_list):
            df_dict[f'热评{index+1}'].append(item)
            
df = pd.DataFrame(df_dict)
df.to_csv(r"G:\python_advanced\homework\week1\homework1\week01_0028_douban_top250_lxml.csv", encoding='utf-8', index=None)
