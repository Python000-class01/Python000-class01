# -*- coding: utf-8 -*-
from lxml import etree
from ipproxy import IPProxy
from proxy_util import strip, request_page, logger
 
 
class ProxyBaseCrawler(object):
 
    def __init__(self, queue=None, website=None, urls=[]):
        self.queue = queue
        self.website = website
        self.urls = urls
 
    def _start_crawl(self):
        raise NotImplementedError
 
 
class KuaiDailiCrawler(ProxyBaseCrawler):  # 快代理
    def _start_crawl(self):
        for url_dict in self.urls:
            logger.info("开始爬取 [ " + self.website + " ] :::> [ " + url_dict['type'] + " ]")
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                tr_list = html.xpath("//table[@class='table table-bordered table-striped']/tbody/tr")
                for tr in tr_list:
                    ip = tr.xpath("./td[@data-title='IP']/text()")[0] if len(
                        tr.xpath("./td[@data-title='IP']/text()")) else None
                    port = tr.xpath("./td[@data-title='PORT']/text()")[0] if len(
                        tr.xpath("./td[@data-title='PORT']/text()")) else None
                    schema = tr.xpath("./td[@data-title='类型']/text()")[0] if len(
                        tr.xpath("./td[@data-title='类型']/text()")) else None
                    proxy = IPProxy(schema=strip(schema), ip=strip(ip), port=strip(port))
                    if proxy._check_format():
                        self.queue.push(proxy)
                if tr_list is None:
                    has_more = False
 
 
class FeiyiDailiCrawler(ProxyBaseCrawler):  # 飞蚁代理
    def _start_crawl(self):
        for url_dict in self.urls:
            logger.info("开始爬取 [ " + self.website + " ] :::> [ " + url_dict['type'] + " ]")
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                tr_list = html.xpath("//div[@id='main-content']//table/tr[position()>1]")
                for tr in tr_list:
                    ip = tr.xpath("./td[1]/text()")[0] if len(tr.xpath("./td[1]/text()")) else None
                    port = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    schema = tr.xpath("./td[4]/text()")[0] if len(tr.xpath("./td[4]/text()")) else None
                    proxy = IPProxy(schema=strip(schema), ip=strip(ip), port=strip(port))
                    if proxy._check_format():
                        self.queue.push(proxy)
                if tr_list is None:
                    has_more = False
 
 
class WuyouDailiCrawler(ProxyBaseCrawler):  # 无忧代理
    def _start_crawl(self):
        for url_dict in self.urls:
            logger.info("开始爬取 [ " + self.website + " ] :::> [ " + url_dict['type'] + " ]")
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                ul_list = html.xpath("//div[@class='wlist'][2]//ul[@class='l2']")
                for ul in ul_list:
                    ip = ul.xpath("./span[1]/li/text()")[0] if len(ul.xpath("./span[1]/li/text()")) else None
                    port = ul.xpath("./span[2]/li/text()")[0] if len(ul.xpath("./span[2]/li/text()")) else None
                    schema = ul.xpath("./span[4]/li/text()")[0] if len(ul.xpath("./span[4]/li/text()")) else None
                    proxy = IPProxy(schema=strip(schema), ip=strip(ip), port=strip(port))
                    if proxy._check_format():
                        self.queue.push(proxy)
                if ul_list is None:
                    has_more = False
 
 
class IPhaiDailiCrawler(ProxyBaseCrawler):  # IP海代理
    def _start_crawl(self):
        for url_dict in self.urls:
            logger.info("开始爬取 [ " + self.website + " ] :::> [ " + url_dict['type'] + " ]")
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                tr_list = html.xpath("//table//tr[position()>1]")
                for tr in tr_list:
                    ip = tr.xpath("./td[1]/text()")[0] if len(tr.xpath("./td[1]/text()")) else None
                    port = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    schema = tr.xpath("./td[4]/text()")[0] if len(tr.xpath("./td[4]/text()")) else None
                    proxy = IPProxy(schema=strip(schema), ip=strip(ip), port=strip(port))
                    if proxy._check_format():
                        self.queue.push(proxy)
                if tr_list is None:
                    has_more = False
 
 
class YunDailiCrawler(ProxyBaseCrawler):  # 云代理
    def _start_crawl(self):
        for url_dict in self.urls:
            logger.info("开始爬取 [ " + self.website + " ] :::> [ " + url_dict['type'] + " ]")
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url, encoding='gbk'))
                tr_list = html.xpath("//table/tbody/tr")
                for tr in tr_list:
                    ip = tr.xpath("./td[1]/text()")[0] if len(tr.xpath("./td[1]/text()")) else None
                    port = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    schema = tr.xpath("./td[4]/text()")[0] if len(tr.xpath("./td[4]/text()")) else None
                    proxy = IPProxy(schema=strip(schema), ip=strip(ip), port=strip(port))
                    if proxy._check_format():
                        self.queue.push(proxy)
                if tr_list is None:
                    has_more = False
 
 
class XiCiDailiCrawler(ProxyBaseCrawler):  # 西刺代理
    def _start_crawl(self):
        for url_dict in self.urls:
            logger.info("开始爬取 [ " + self.website + " ] :::> [ " + url_dict['type'] + " ]")
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                tr_list = html.xpath("//table[@id='ip_list']//tr[@class!='subtitle']")
                for tr in tr_list:
                    ip = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    port = tr.xpath("./td[3]/text()")[0] if len(tr.xpath("./td[3]/text()")) else None
                    schema = tr.xpath("./td[6]/text()")[0] if len(tr.xpath("./td[6]/text()")) else None
                    if schema.lower() == "http" or schema.lower() == "https":
                        proxy = IPProxy(schema=strip(schema), ip=strip(ip), port=strip(port))
                        if proxy._check_format():
                            self.queue.push(proxy)
                if tr_list is None:
                    has_more = False