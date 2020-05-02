from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from newscomments.newscomments.spiders.newscomments_spider import NewsCommentsSpider
from datetime import datetime


settings = get_project_settings()
settings['USER_AGENT'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
settings['ITEM_PIPELINES'] = {
   'newscomments.newscomments.pipelines.comments_pipeline.CommentsPipeline': 300,
}
process = CrawlerProcess(settings)
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'interval', args=[NewsCommentsSpider], seconds=3600, next_run_time=datetime.now())
scheduler.start()
process.start(False)


