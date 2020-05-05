BOT_NAME = 'book'

SPIDER_MODULES = ['book.spiders']
NEWSPIDER_MODULE = 'book.spiders'


USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
    'book.pipelines.BookPipeline': 300,
}