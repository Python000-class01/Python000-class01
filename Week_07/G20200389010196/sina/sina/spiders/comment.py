import scrapy
import scrapy.http
import time
from sina.items import SinaItem
import codecs
import json
import jsonpath
import os

#scrapy crawl comment -a newsid=comos-ircuyvh8608153
#用linux crontab 实行定时爬去
#每半小时执行一次
#0/30 * * * * cd /home/sina && python -m scrapy crawl comment -a newsid=comos-ircuyvh8608153

class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['comment.sina.com.cn']
    urltmpl = 'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=%s&page='
    offset = 1

    def __init__(self, newsid, **kwargs):
        self.urltmpl = self.urltmpl % newsid
        self.start_urls = [ self.urltmpl + str(self.offset), ]
        self.cnt = 0
        super().__init__(**kwargs) 

    def start_requests(self):
        #文件存在后就不用再写头部
        if (os.path.exists('comment_last.txt') == False) :
            with codecs.open(f'comment_last.txt','w','utf-8') as csv:
                line = f'"mid","content","uid","area","nick","ip","newsid","time"\r\n'
                csv.write(line)
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        cmntlist = jsonpath.jsonpath(result,"$..cmntlist")[0] # jsonpath返回一个列表
        
        for comment in cmntlist:
            # type(fan) --> dict
            item = SinaItem()
            item['mid'] = jsonpath.jsonpath(comment, "$..mid")
            item['content'] = jsonpath.jsonpath(comment, "$..content")
            item['uid'] = jsonpath.jsonpath(comment, "$..uid")
            item['area'] = jsonpath.jsonpath(comment, "$..area")
            item['nick'] = jsonpath.jsonpath(comment, "$..nick")
            item['ip'] = jsonpath.jsonpath(comment, "$..ip")
            item['newsid'] = jsonpath.jsonpath(comment, "$..newsid")
            item['time'] = jsonpath.jsonpath(comment, "$..time")
            #print(item)
            yield item
        self.offset += 1
        yield scrapy.Request(self.urltmpl + str(self.offset), callback=self.parse, dont_filter=True)
        