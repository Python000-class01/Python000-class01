# -*- coding: utf-8 -*-
import scrapy
import sys 
import io
from filmifo.items import FilmifoItem
from scrapy.selector import Selector

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer ,encoding = 'gb18030')

class FilmdownloadsSpider(scrapy.Spider):
    name = 'filmdownloads'
    allowed_domains = ['www.rrys2019.com']
    start_urls = ['http://www.rrys2019.com/']  #此处是一个列别

    def start_requests(self):
        # for i in range(0,10):
        url = 'http://www.rrys2019.com'   # url 要带:http://
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # soup = BeautifulSoup(response.text,'html.parser')
        filminfos = Selector(response=response).xpath("//div[@class='box clearfix']/descendant::span/..")


        for filminfo in filminfos:
            item = FilmifoItem()
            # print(filminfo)
            filmname = filminfo.xpath('./a/text()')
            # print(filmname)
            filmlink = filminfo.xpath('./a/@href')
            # print(filmlink)

            film_name_res = filmname.extract_first()
            film_link_res = 'http://www.rrys2019.com' +  filmlink.extract_first()   # //url 地址要写全：http://www.rrys2019.com ，不能学成 www.rrys2019.com


            item['film_name'] = film_name_res
            item['film_link'] = film_link_res
            yield scrapy.Request(url=film_link_res, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        # print(item)
        # soup = BeautifulSoup(response.text, 'html.parser')
        filmtop = Selector(response = response).xpath("//div[@id='score_star']/../p/text()").re('\d+')
        print(filmtop)
        film_top = filmtop[0]
        # print(film_top)
        item['film_top'] = film_top
        filmlevel = Selector(response = response).xpath("//div[@class='level-item']/img/@src")
        film_level = filmlevel.extract_first()
        # print(film_level)
        if film_level == 'http://js.jstucdn.com/images/level-icon/a-big-1.png':
            item['film_level'] = 'A级'
        elif film_level == 'http://js.jstucdn.com/images/level-icon/b-big-1.png':
            item['film_level'] = 'B级'
        elif film_level == 'http://js.jstucdn.com/images/level-icon/c-big-1.png':
            item['film_level'] = 'C级'
        elif film_level == 'http://js.jstucdn.com/images/level-icon/d-big-1.png':
            item['film_level'] = 'D级'
        elif film_level == 'http://js.jstucdn.com/images/level-icon/e-big-1.png':
            item['film_level'] = 'E级'

        film_views = Selector(response = response).xpath("//li[@id='score_list']/div[1]").re('\d+')

        item['film_views'] = film_views[1]
        film_covertinfo = Selector(response=response).xpath('//div[@class="imglink"]/a/img/@src')
        film_covertinfo = film_covertinfo.extract_first()
        print(film_covertinfo)
        item['film_covertinfo'] = film_covertinfo

        print(item)
        yield item
        


        




    #     # content = soup.find('div', attrs={'class': 'intro'}).get_text().strip()
    #     item['film_top'] = film_top
    #     yield item
    #     # pass



        # for i in range(len(title_list)):
        #     item = FilmifoItem()
        #     title = tit le_list[i].find('a').get('title')
        #     link = title_list[i].find('a').get('href')
        #     print('*'*20)
        #     print(title)
        #     print(link)
        #     print(item['film_name'])
        # print(response.url)
        # print(response.text)
        # new_response = str(response.boby,encoding='utf-8')
        # print(new_response)
