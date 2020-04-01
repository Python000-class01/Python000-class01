# -*- coding: utf-8 -*-
import redis
from proxy_queue import FifoQueue
from proxy_settings import REDIS_HOST, REDIS_PORT
from proxy_crawlers import WuyouDailiCrawler, FeiyiDailiCrawler, KuaiDailiCrawler, IPhaiDailiCrawler, YunDailiCrawler, \
    XiCiDailiCrawler
 
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
fifo_queue = FifoQueue(r)
 
 
def run_kuai():
    kuaidailiCrawler = KuaiDailiCrawler(queue=fifo_queue, website='快代理[国内高匿]',
                                        urls=[{'url': 'https://www.kuaidaili.com/free/inha/{}/', 'type': '国内高匿',
                                               'page': 1},
                                              {'url': 'https://www.kuaidaili.com/free/intr/{}/', 'type': '国内普通',
                                               'page': 1}])
    kuaidailiCrawler._start_crawl()
 
 
def run_feiyi():
    feiyidailiCrawler = FeiyiDailiCrawler(queue=fifo_queue, website='飞蚁代理',
                                          urls=[{'url': 'http://www.feiyiproxy.com/?page_id=1457', 'type': '首页推荐'}])
    feiyidailiCrawler._start_crawl()
 
 
def run_wuyou():
    wuyoudailiCrawler = WuyouDailiCrawler(queue=fifo_queue, website='无忧代理',
                                          urls=[{'url': 'http://www.data5u.com/free/index.html', 'type': '首页推荐'},
                                                {'url': 'http://www.data5u.com/free/gngn/index.shtml', 'type': '国内高匿'},
                                                {'url': 'http://www.data5u.com/free/gnpt/index.shtml', 'type': '国内普通'}])
    wuyoudailiCrawler._start_crawl()
 
 
def run_iphai():
    crawler = IPhaiDailiCrawler(queue=fifo_queue, website='IP海代理',
                                urls=[{'url': 'http://www.iphai.com/free/ng', 'type': '国内高匿'},
                                      {'url': 'http://www.iphai.com/free/np', 'type': '国内普通'},
                                      {'url': 'http://www.iphai.com/free/wg', 'type': '国外高匿'},
                                      {'url': 'http://www.iphai.com/free/wp', 'type': '国外普通'}])
    crawler._start_crawl()
 
 
def run_yun():
    crawler = YunDailiCrawler(queue=fifo_queue, website='云代理',
                              urls=[{'url': 'http://www.ip3366.net/free/?stype=1&page={}', 'type': '国内高匿', 'page': 1},
                                    {'url': 'http://www.ip3366.net/free/?stype=2&page={}', 'type': '国内普通', 'page': 1},
                                    {'url': 'http://www.ip3366.net/free/?stype=3&page={}', 'type': '国外高匿', 'page': 1},
                                    {'url': 'http://www.ip3366.net/free/?stype=4&page={}', 'type': '国外普通', 'page': 1}])
    crawler._start_crawl()
 
 
def run_xici():
    crawler = XiCiDailiCrawler(queue=fifo_queue, website='西刺代理',
                               urls=[{'url': 'https://www.xicidaili.com/', 'type': '首页推荐'},
                                     {'url': 'https://www.xicidaili.com/nn/{}', 'type': '国内高匿', 'page': 1},
                                     {'url': 'https://www.xicidaili.com/nt/{}', 'type': '国内普通', 'page': 1},
                                     {'url': 'https://www.xicidaili.com/wn/{}', 'type': '国外高匿', 'page': 1},
                                     {'url': 'https://www.xicidaili.com/wt/{}', 'type': '国外普通', 'page': 1}])
    crawler._start_crawl()
 
 
if __name__ == '__main__':
    run_xici()
    run_iphai()
    run_kuai()
    run_feiyi()
    run_yun()
    run_wuyou()