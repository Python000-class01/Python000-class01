'''
@Author: Zst0hg
@Date: 2020-03-19 15:51:22
@LastEditTime: 2020-03-20 17:17:44
@LastEditors: Please set LastEditors
@Description: Win10, VSCode, python3.8
@FilePath: \Code\Python\Python-GeekTime-000\week03\rrys\rrys\spiders\rrys.py
'''
import scrapy
from scrapy_splash import SplashRequest
import json
import requests

class movieSpider(scrapy.Spider):
    name = "rrys"
    allowed_domains = ["www.rrys2019.com"]
    start_urls = ["http://www.rrys2019.com/"]
    def parse(self, response):
        next_urls = []
        for movie in response.css("div.clearfix")[0].css("ul li"):
            name = movie.css("a::text").get()
            href = response.url + movie.css("a::attr(href)").get()
            res = {
                'name' : name,
                'href' : href
            }
            print(res)
            next_urls.append(href)

        splash_args = {
            'wait' : 0.5,
            'html' : 1,
            'iframes' : 1
        }
        for next_url in next_urls:
            yield SplashRequest(next_url, callback=self.parse_detail, endpoint = "render.json", args=splash_args)

    def parse_detail(self, response):
        name = response.css("div.resource-tit h2::text").get().strip()
        rank = response.css("p.f4::text").get().strip()
        if "\xa0\xa0" in rank:
            rank = rank.split("\xa0\xa0")[-1]
        else:
            rank = rank.split(":")[-1]
        level = response.css("div.level-item img::attr(src)").get()
        if level != None:
            level = level.split("/")[-1].split("-")[0]
        # 单独Request一个JS文件获取 View
        codeNum = response.url.strip().split("/")[-1]
        view_res = requests.get(f"http://www.rrys2019.com/resource/index_json/rid/{codeNum}/channel/movie")
        jd = json.loads(view_res.text.strip('var index_info = '))
        if 'views' in jd:
            view = jd['views']
        else:
            view = None
        imglink = response.css("div.imglink a img::attr(src)").get()
        print(f"name-{name}, rank-{rank}, level-{level}, view-{view}")
