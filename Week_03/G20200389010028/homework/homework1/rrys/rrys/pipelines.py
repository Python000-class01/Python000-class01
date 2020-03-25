# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl 

class RrysPipeline(object):
    def __init__(self):
        # 初始化函数，当类实例化时这个方法会自动启动
        self.wb = openpyxl.Workbook() # 加注释，不然报错 NameError: name 'openpyxl' is not defined，神奇。。。
        # 创建工作簿
        self.ws = self.wb.active
        # 定位活动工作表
        self.ws.append(['电影名称', '电影分级', '本站排名', '封面详情'])
        # 往表格添加表头
        # 
    def process_item(self, item, spider):
        line = [item['name'], item['level'], item['rank'], item['image']]
        # 把电影名称、分级、排名、封面详情写成列表的形式，赋值给line
        self.ws.append(line)
        # 把上述信息添加进表格
    
        return item
        # 把item丢回给引擎，这样如果后续有itempipeline需要处理这个item时，引擎就能够自己调度

    def close_spider(self, apider):
        # 当爬虫结束运行时，这个方法就会执行
        self.wb.save('./rrys_hotmv.xlsx')
        # 保存文件
        self.wb.close()
        # 关闭文件
