# -*- coding: utf-8 -*-
import scrapy
from configure import getConfig
from task1.web_crawler.web_crawler.items.rrys_items import RrysItem
import re


class RrysSpider(scrapy.Spider):

    name = "rrys"
    allowed_domains = getConfig()[name]["allowed_domains"]
    start_urls = getConfig()[name]["start_urls"]

    def parse(self, response):
        for sel in response.xpath("//body/div[@class=\"middle-box\"]/div[@class=\"w\"]/div[1]/div/ul/li"):
            item = RrysItem()
            item['seq'] = int(sel.xpath("span/text()").extract_first().strip())
            item['title'] = sel.xpath("a/text()").extract_first().strip()
            item['link'] = "http://www.rrys2019.com" + sel.xpath("a/@href").extract_first().strip()
            yield scrapy.Request(item['link'], meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']
        item['ranking'] = int(re.sub(r"[^0-9]", "", response.xpath("//body/div[@class=\"middle-box\"]/div[@class=\"w\"]/div[1]/div[2]/div[1]/ul/li[1]/p/text()").extract_first().strip()))
        item['classification'] = response.xpath("//body/div[@class=\"middle-box\"]/div[@class=\"w\"]/div[1]/div[1]/div[2]/div[2]/div[@class=\"level-item\"]/img/@src").extract_first().strip().replace("http://js.jstucdn.com/images/level-icon/", "").replace("-big-1.png", "").upper()
        item['favorites'] = int(re.sub(r"[^0-9]", "", response.xpath("//li[@id=\"score_list\"]//div[1]/div[2]").extract_first().strip()))
        item['cover'] = response.xpath("//body/div[@class=\"middle-box\"]/div[@class=\"w\"]/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src").extract_first().strip()
        yield item
