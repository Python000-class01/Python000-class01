import scrapy


class CommentsItem(scrapy.Item):
    news_id =scrapy.Field()
    comment_id = scrapy.Field()
    comment = scrapy.Field()
    comment_time = scrapy.Field()
