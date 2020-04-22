import scrapy
import requests
from bs4 import BeautifulSoup as bs
import re
import json
from datetime import datetime
from news.items import NewsItem
import pandas
from snownlp import SnowNLP

# http://comment.sina.com.cn/page/info?version=1&format=json&channel=jc&newsid=comos-irczymi7491452&group=0&compress=0&ie=utf-8&oe=utf-8&page={pageNum}&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user
class SinaNewsSpider(scrapy.Spider):
    name = 'sina_news'
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }

    start_urls = ["http://comment5.news.sina.com.cn/comment/skin/default.html?channel=jc&newsid=comos-irczymi7491452&group=0"]
    
    def parse(self, response):
        totalNum = 127
        pageNum = totalNum // 10 + 1
        index = 1
        while index <= pageNum:
            url = f"http://comment.sina.com.cn/page/info?version=1&format=json&channel=jc&newsid=comos-irczymi7491452&group=0&compress=0&ie=utf-8&oe=utf-8&page={index}&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user"
            yield scrapy.Request(url, callback=self.parse_details)
            index += 1
            
    def parse_details(self, response):
        uidLst = []
        nickLst = []
        areaLst = []
        contentLst = []
        timeLst = []

        try:
            jd = json.loads(response.text)
            # print("Load Successfully.")
            cmntlist = jd['result']['cmntlist']
            if len(cmntlist) != 0:
                for user in cmntlist:
                    uid = user.get('uid', None) 
                    nick = user.get('nick', 'Anonymous') 
                    area = user.get('area', 'China') 
                    content = user.get('content', None)
                    time = user.get('time', None)
                    uidLst.append(uid)
                    nickLst.append(nick)
                    areaLst.append(area)
                    contentLst.append(content)
                    timeLst.append(time)

            # 用pandas导出csv
            data = pandas.DataFrame({"uid":uidLst, 'nick':nickLst, "area":areaLst, "time":time, "content":contentLst})
            data["sentiment"] = data.content.apply(self._sentiment)
            data.to_csv("../commentsData.csv", mode='a', index=False, header=False, sep=',', encoding = 'utf-8')
        except Exception as e:
            print(f"Error:{e}")

    # ???????????
    def _sentiment(self, text):
        s = SnowNLP(text)
        return s.sentiments


            
    



