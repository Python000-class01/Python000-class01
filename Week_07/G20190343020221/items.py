import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content_id = scrapy.Field()
    ndesc = scrapy.Field()
    event_time = scrapy.Field()
    event_date = scrapy.Field()
