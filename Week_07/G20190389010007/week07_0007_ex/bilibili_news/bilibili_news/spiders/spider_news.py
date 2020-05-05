import scrapy
from scrapy.selector import Selector
from bilibili_news.items import BilibiliNewsItem
import re
import json
import datetime
import math

class BilibiliNewsSpide(scrapy.Spider):
    name = "bilibili_news"
    allowed_domains = ["bilibili.com","api.bilibili.com"]
    headers = {
        'User-Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    start_urls = (
        'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=12&oid=5690449&sort=2&_=1'
        )
    item_list=[]
    def get_api_url(self,page_num):
        return (f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={i+1}&type=12&oid=5690449&sort=0' for i in range(page_num))
    
    def get_item(self,item_dict):
        the_date = datetime.datetime.now() 
        pre_date = the_date - datetime.timedelta(hours=24)
        pre_stamp = int(pre_date.timestamp()) #将时间转化为时间戳形式
        if(pre_stamp>item_dict['ctime']):                
            newsItem = BilibiliNewsItem()
            newsItem['member_name']=item_dict['member']['uname']
            newsItem['member_id']=item_dict['member']['mid']
            newsItem['comment_text']=item_dict['content']['message']
            newsItem['comment_id']=item_dict['rpid']
            newsItem['comment_date']=item_dict['ctime']
            return newsItem
        else:
            return None
        # 第一次获取全部数据
        # newsItem = BilibiliNewsItem()
        # newsItem['member_name']=item_dict['member']['uname']
        # newsItem['member_id']=item_dict['member']['mid']
        # newsItem['comment_text']=item_dict['content']['message']
        # newsItem['comment_id']=item_dict['rpid']
        # newsItem['comment_date']=item_dict['ctime']
        # return newsItem
    def dict_to_item(self,item_dict):
            # new_item_list= []
            if item_dict['replies'] == None:
                pass
            else:
                for i in item_dict['replies']:
                    pp = self.get_item(i)
                    if pp is not None:
                        self.item_list.append(pp)
                    self.dict_to_item(i)
            # return new_item_list


            
    # 第一步先获得评论一共有多少页，用于组成api url
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse,headers=self.headers)
    def parse(self,response):
        #获取评论数量
        pageinfo = json.loads(response.text)['data']['page']
        # print(json.dumps(pageinfo))
        page_num =math.ceil(int(pageinfo['count'])/int(pageinfo['size']))
        # print(page_num)       
        self.api_url = self.get_api_url(page_num)        
        for url in self.api_url:
            yield scrapy.Request(url=url, callback=self.parse_comment_detail,headers=self.headers)
    def parse_comment_detail(self,response):
        comment_dict = json.loads(response.text)['data']
        # print(comment_dict['replies'])
        self.item_list=[]  # 清空list
        self.dict_to_item(comment_dict)
        print(len(self.item_list))
        for item in self.item_list:
            yield item
         
            
        




