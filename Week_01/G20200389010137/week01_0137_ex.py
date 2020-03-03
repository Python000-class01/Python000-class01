#!/usr/bin/env python
"""
采集豆瓣电影 top250 相关信息
先采集概要信息：包括电影名称、详情 url、评分、评论人数，进行保存
再采集详情页面：包括热门 top5 评论，标记采集成功失败，以便对失败的进行核查或再进行复采
"""

import requests
from lxml import etree
import os, sys
import time, random, datetime
import csv
import pandas as pd

debug=False

class DoubanMovieSpider():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
            }
        self.timeout = (3.05, 10)
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def get_req(self, url, params=None):
        try:
            with self.session.get(url=url, params=params ,headers=self.headers, timeout=self.timeout) as response:
                if debug:
                    print('General:', '-' * 30)
                    print('Request URL:', response.request.url)
                    print('Request Method:', response.request.method)
                    print('Status Code:', response.status_code, response.reason)

                    print('Request Headers:', '-' * 30)
                    for k, v in response.request.headers.items(): print(f'{k}: {v}')

                    print('Query String Parameters:', '-' * 30)
                    if params is not None: print(response.request._encode_params(params))

                    print('Response Headers:', '-' * 30)
                    for k, v in response.headers.items(): print(f'{k}: {v}')

                    #soup = BeautifulSoup(response.text, 'lxml')
                    #print('Response:', '-' * 30, '\n', soup.prettify())
                    #return soup
                if response.status_code == 200:
                    # return response.content
                    print(f'页面访问成功：{response.request.url} Status Code: {response.status_code} {response.reason}')
                    return response.text
                else:
                    print(f'页面访问失败：{response.request.url} Status Code: {response.status_code} {response.reason}')
                    return
        except :
            print('url失败')
            return
    def get_summary(self, page, output):
        """
        获取概要信息：电影名称、评分、短评数量
        """
        print(f'采集第 {page + 1} 页 {"-" * 50}')

        url = 'https://movie.douban.com/top250'
        params = {
            "start" : int(page) * 25,
            "filter" : ''
            }

        text = self.get_req(url, params)
        if debug: print(type(text), text)

        lxmHtml = etree.HTML(text)
        movieTitles = lxmHtml.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a/span[1]/text()')
        movieUrls = lxmHtml.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a/@href')
        movieAverage = lxmHtml.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/div/span[2]/text()')
        movieQuoteCount = lxmHtml.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/div/span[4]/text()')
        movieQuoteCount = [ str(i).replace('人评价', '') for i in movieQuoteCount]
        if debug:
            print(movieTitles)
            print(movieUrls)
            print(movieAverage)
            print(movieQuoteCount)

        results = []
        for j in range(0, 25):
            # l = {
            #     '排名':int( page * 25 + j + 1),
            #     '电影名称':movieTitles[j],
            #     '电影详情url':movieUrls[j],
            #     '评分':movieAverage[j],
            #     '评论人数':movieQuoteCount[j]}
            r = (int( page * 25 + j + 1), movieTitles[j], movieUrls[j], movieAverage[j], movieQuoteCount[j])
            results.append(r)
        for i in results: print(i)
        self.save_data(results, output)

    def get_details(self, url):
        """
        获取详情的评论
        """
        text = self.get_req(url)
        try:
            lxmHtml = etree.HTML(text)
        except Exception as e:
            print(f'页面解析失败: {e}')
            result = ['NaN', 'NaN', 'NaN', 'NaN', 'NaN', '0']
        else:
            quotes = lxmHtml.xpath('//*[@id="hot-comments"]/div[*]/div/p/span[@class="short"]/text()')
            # result = [i.replace("'",'"') for i in quotes].append('1')
            result = [i.replace("'",'"').replace(',', '，') for i in quotes]
            result.append('1')                            # 添加成功标记 1
            if (result is None) or (len(result) != 6):
                print(f'解析结果不正确: result={result}')
                result = ['', '', '', '', '', '0']        # 0 标记错误

        # if quote:
        #     # results = '\n'.join(quote)
        # else:
        #     results = ''
        # # print(quote)

        return result

    def save_data(self, data, output):
        """
        保存数据
        """
        with open(output, 'a', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerows(data)

    def save_quote(self, file):
        """
        保存详情信息
        """
        df = pd.read_csv(file)
        df['评论top1'] = ''
        df['评论top2'] = ''
        df['评论top3'] = ''
        df['评论top4'] = ''
        df['评论top5'] = ''
        df['采集成功'] = ''
        df.to_csv(file, index=False)
        urls = df['电影详情url']
        print(f'开始采集 共 {len(urls)} 条: {"-" * 50}')
        for i, url in enumerate(urls):
            print(f'采集第 {i+1} 条 ...')
            quoteTop5 = self.get_details(url)
            # print(f'quoteTop5= {quoteTop5}')
            df.at[i, '评论top1'] = quoteTop5[0]
            df.at[i, '评论top2'] = quoteTop5[1]
            df.at[i, '评论top3'] = quoteTop5[2]
            df.at[i, '评论top4'] = quoteTop5[3]
            df.at[i, '评论top5'] = quoteTop5[4]
            df.at[i, '采集成功']  = quoteTop5[5]
            df.to_csv(file, index=False)
            time.sleep(random.randint(3, 10))

def main():
    f1 = './douban1.csv'
    s = DoubanMovieSpider()

    # tabheader = ['排名', '电影名称', '电影详情url', '评分', '评价人数']
    # with open(f1, 'w', encoding='utf-8', newline='') as f:
    #     w = csv.writer(f)
    #     w.writerow(tabheader)
    # for page in range(0, 10):
    #     s.get_summary(page, f1)
    #     time.sleep(random.randint(5, 10))

    s.save_quote(f1)


if __name__ == "__main__":
    print(datetime.datetime.now())
    main()