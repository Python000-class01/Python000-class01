import os
from apscheduler.schedulers.twisted import TwistedScheduler
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from newscomments.newscomments import settings as news_comments_settings
from newscomments.newscomments.spiders.news_comments_spider import NewsCommentsSpider
from utils.logger import get_logger


logger = get_logger('data_pipeline')
try:
   interval = int(os.getenv("PROCESS_INTERVAL", "3600"))

   settings = Settings()
   settings.setmodule(news_comments_settings)
   process = CrawlerProcess(settings)
   scheduler = TwistedScheduler()
   scheduler.add_job(process.crawl, 'interval', args=[NewsCommentsSpider.name], seconds=interval, id="regular_job")
   logger.info("===== Start data pipeline =====")
   # The scheduler doesn't run immediately, so need to explicitly run it for the first time, then start the scheduler
   process.crawl(NewsCommentsSpider.name)
   scheduler.start()
   process.start(False)
except Exception as ex:
   logger.error("Exception occurred on data pipeline. ", ex)

