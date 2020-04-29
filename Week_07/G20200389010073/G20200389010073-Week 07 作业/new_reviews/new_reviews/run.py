# -*- coding: utf-8 -*-
# from sys import path
# path.append(r'D:\Python Class\G20200389010073-Week 07 作业\new_reviews\new_reviews')

from scrapy import cmdline
name = 'reviews'
cmdline.execute(f'scrapy crawl {name} --nolog'.split())
