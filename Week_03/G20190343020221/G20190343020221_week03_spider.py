import scrapy
from xiachufang.items import XiachufangItem
from bs4 import BeautifulSoup

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'gb18030') #字符转换

class ExampleSpider(scrapy.Spider):
    name = 'example' # 代表爬虫的入口
    allowed_domains = ['example.com'] #允许的域名
    start_urls = ['http://example.com/'] # 没做任何配置则为第一个请求的页面

    def start_requests(self):
        for i in range(0, 10):
            url = f'http://www.xiachufang.com/explore/?page={i}'
            yield scrapy.Request(url = url, callback = self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的页面（response对象）发给该方法
            # 这里可以用callback指定新的函数，不是用parse作为默认的回调函数

    # 解析函数
    def parse(self,response):
        # new_response = str(response.body, encoding = 'utf-8') # 解决爬取出现乱码问题
        # print(new_response) #爬取整个页面内容
        # debug
        # items[]
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('p', attrs = {'class': 'name'})
        for i in range(len(title_list)):
            # 在items.py定义
            item = XiachufangItem()
            title = title_list[i].find('a').get('title')
            link = title_list[i].find('a').get('href')
            item['title'] = title
            item['link'] = link

            # 通过scrapy.request再次发起请求
            yield scrapy.Request(url = 'http://www.xiachufang.com' + link, meta = {'item': item}, callback = self.parse2)
            
    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('p',attrs = {'class':'text'}).get_text().strip()
        item['content'] = content
        yield item
