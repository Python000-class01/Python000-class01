# -*- coding: utf-8 -*-
import scrapy

import json, re, time

from tencent.items import TencentItem


class TencentspiderSpider(scrapy.Spider):
    name = 'tencentSpider'
    allowed_domains = ['qq.com']
    start_urls = [
        'https://coral.qq.com/article/5095279756/comment/v2?oriorder=o&cursor=0'
    ]

    def parse(self, response):
        result = json.loads(response.text)

        last = result['data']['last']
        comments_list = result['data']['oriCommList']
        for comment_info in comments_list:
            # 评论内容
            comment = comment_info['content']
            # 发布时间
            time_ = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(comment_info['time'])))
            # 点赞数
            up = comment_info['up']
            # 用户ID
            userid = comment_info['userid']

            data = {'comment': comment, 'time': time_, 'up': up}

            # 获取用户名
            url = 'https://coral.qq.com/user/{}/comment/v2?callback={}'.format(userid, userid)
            yield scrapy.Request(url=url, callback=self.get_nick, meta=data)

        # 翻页
        url = 'https://coral.qq.com/article/5095279756/comment/v2?oriorder=o&cursor={}'
        yield scrapy.Request(url=url.format(last), callback=self.parse)

    def get_nick(self, response):
        data = response.meta
        # 获取用户名
        nick = re.findall('"usermeta":(.*?),"users"', response.text)[0]
        nick = json.loads(nick)['nick']

        items = TencentItem(comment=data['comment'], time=data['time'], up=data['up'], nick=nick)
        yield items