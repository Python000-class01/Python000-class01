# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import  MatplotlibExampleItem

class GetExampleSpider(scrapy.Spider):
    name = 'get_example'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html',]

    def parse(self, response):
        link_extractor = LinkExtractor(restrict_css='div.toctree-wrapper.compound', deny='/index.html$')

        for link in link_extractor.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_data)


    def parse_data(self, response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        my_item = MatplotlibExampleItem()
        my_item['file_urls'] = [url]
        return my_item
