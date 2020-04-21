# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class SinaPipeline(object):
    def process_item(self, item, spider):
        print(item["mid"])
        with codecs.open(f'comment_last.txt','a','utf-8') as csv:
            mid = "".join(item["mid"]).strip("['")
            content = "".join(item["content"]).strip("['")
            uid = "".join(item["uid"]).strip("['")
            area = "".join(item["area"]).strip("['")
            nick = "".join(item["nick"]).strip("['")
            ip = "".join(item["ip"]).strip("['")
            newsid = "".join(item["newsid"]).strip("['")
            time = "".join(item["time"]).strip("['")
            line = f'"{mid}","{content}","{uid}","{area}","{nick}","{ip}","{newsid}","{time}"\r\n'
            #print(line)
            csv.write(line)
