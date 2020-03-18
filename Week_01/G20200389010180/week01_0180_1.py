#-*- coding:utf-8 -*-
#===========================================================
#FileName:     Douban movie Top250
#Description:  抓取Douban Top 250电影数据
#Author:       Tom ke
#Version:      V0.1
#Date:         2020-3-6
#Log:          
#===========================================================

import requests,re,timeit,logging,lxml.etree
import pandas as pd
from time import sleep


def Main():
    start_time = timeit.default_timer() 
    #配置日志功能
    logging.basicConfig(level=logging.INFO,
                        format='[%(levelname)s] %(message)s',
                        datefmt='%Y %b %d %H:%M:%S',
                        filename='.\Logs.log')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)-8s] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger('').addHandler(console)

    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))
    douban_mv_top250 = []
    
    for page in urls:
        page_data = crawl_page(page)
        if page_data:
            douban_mv_top250 += page_data
            sleep(5)

    columns = ['URL','排名','电影名1','电影名2','电影名3','评分','短评数','短评1','短评2','短评3','短评4','短评5']
    df = pd.DataFrame(columns=columns,data=douban_mv_top250)
    #print(df)
    df.to_csv('./douban.csv',encoding='utf_8_sig') 

    stop_time = timeit.default_timer()
    logging.info('Run time:{}'.format(start_time-stop_time))

#抓取页面并获取数据
def crawl_page(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    header = {}
    header['user-agent'] = user_agent
    try:
        response = requests.get(url, headers=header, timeout=5)
        logging.info(f'抓取一级页面：{url}    Status Code: {response.status_code}')
        response.raise_for_status()
    except Exception as e:
        logging.warning(f'抓取出错：{url}  原因：{e}')
        return

    selector = lxml.etree.HTML(response.text)
    divs = selector.xpath('//div[@class="item"]')
    mv_info_list = []
    
    #匹配页面电影信息
    for div in divs:
        sub_url = div.xpath('.//a/@href')[0]
        rank = div.xpath('./div[1]/em/text()')[0]
        title_1 = ''.join(div.xpath('.//*[@class="title"][1]/text()')).strip()
        title_2 = ''.join(div.xpath('.//*[@class="title"][2]/text()')).strip()
        title_3 = ''.join(div.xpath('.//*[@class="other"]/text()')).strip()
        rating_num = div.xpath('.//*[@class="rating_num"]/text()')[0]
        comment_num = re.findall(r'\d+', div.xpath('.//*[@class="star"]/span[4]/text()')[0])[0]
        mv_info_list.append([sub_url,rank,title_1,title_2,title_3,rating_num,comment_num])
    
    if not mv_info_list:
        logging.warning(f'抓取出错：{url}  原因：页面无匹配数据')
        return
    #二级页面抓取
    for item in mv_info_list:
        try:
            response = requests.get(item[0], headers=header, timeout=5)
            logging.info(f'抓取二级页面：{item[0]}    Status Code: {response.status_code}')
            response.raise_for_status()
        except Exception as e:
            logging.warning(f'抓取出错：{item[0]}  原因：{e}')
            continue
        selector = lxml.etree.HTML(response.text)
        for i in range(1,6):
            item.append(''.join(selector.xpath('//*[@id="hot-comments"]/div[{}]//p/span/text()'.format(i))))
        sleep(3)
    return mv_info_list


if __name__=="__main__":
    Main()
