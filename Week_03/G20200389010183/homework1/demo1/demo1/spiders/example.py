import scrapy
from bs4 import BeautifulSoup
from demo1.items import Demo1Item
import json


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['rrys2019.com']
    start_urls = ['http://www.rrys2019.com']

    def parse(self, response):
        # fl box top24
        soup = BeautifulSoup(response.text, 'html.parser')
        top24_div = soup.find('div', attrs={'class': 'fl box top24'})
        top24 = top24_div.find_all('li',)
        print('*****')
        print(top24)
        for i in range(1):
            # 在items.py定义
            item = Demo1Item()
            title = top24[i].find('a').get('title')
            link = self.start_urls[0] + top24[i].find('a').get('href')
            item['title'] = title
            item['link'] = link
            item['rank'] = i
            item['name'] = title
            if top24[i].find('em').get_text() =='电影':
                item['type'] = 'movie'
            else:
                item['type'] = 'tv'

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)


    # 获取content数据 从http://www.rrys2019.com/resource/{id}中
    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find_all('div', attrs={'class': 'con'})[0].get_text().strip()
        item['content'] = content
        type = item['type']
        id = item['link'].split('/')[4]
        item['id'] = id
        data_url = f'http://www.rrys2019.com/resource/index_json/rid/{id}/channel/{type}'
        item['data_url'] = data_url

        yield scrapy.Request(url=data_url, meta={'item': item}, callback=self.parse3)

    '''    {
            "cate_ranks": [
                {
                    "tpl_count": "16052",
                    "id": "33701",
                    "cnname": "\u897f\u90e8\u4e16\u754c",
                    "enname": "Westworld",
                    "channel": "tv",
                    "area": "\u7f8e\u56fd",
                    "poster": "http:\/\/tu.jstucdn.com\/ftp\/2020\/0213\/s_26697f9051288b01d15cadd23c69b0c4.jpg",
                    "category": "\u79d1\u5e7b\/\u60ca\u609a\/\u60ac\u7591\/\u897f\u90e8",
                    "play_status": "\u7b2c3\u5b63\u8fde\u8f7d\u4e2d",
                    "school": "",
                    "publish_year": "2016",
                    "views": "7030762",
                    "score": "8.9",
                    "favorites": "171384",
                    "rank": "9",
                    "poster_b": "http:\/\/tu.jstucdn.com\/ftp\/2020\/0213\/b_26697f9051288b01d15cadd23c69b0c4.jpg",
                    "type": "\u7f8e\u5267"
                }'''
    #    http://www.rrys2019.com/resource/index_json/rid/33701/channel/tv
    #    http://www.rrys2019.com/resource/index_json/rid/33701/channel/movie
    # 获取上面url中的一个获取data数据

    def parse3(self, response):
        item = response.meta['item']
        if response.status != 200:
            # Error happened, return item.
            return item
        print('********************')
        print(response.text[15:])
        print(item['data_url'])
        json_text = json.loads(response.text[15:])
        data = json_text['cate_ranks'][0]
        views = data['views']
        poster = data['poster']
        item['score'] = data['score']
        item['views'] = views
        item['poster'] = poster
        item['rank'] = data['rank']
        yield item
