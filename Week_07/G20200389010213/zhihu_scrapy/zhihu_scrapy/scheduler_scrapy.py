from scrapy.crawler import CrawlerProcess
from spiders.zhihu import ZhihuSpider
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

process = CrawlerProcess(get_project_settings())
sched = TwistedScheduler()
sched.add_job(process.crawl, 'interval', args=[ZhihuSpider], seconds=300)
sched.start()
process.start(False)    # Do not stop reactor after spider closes