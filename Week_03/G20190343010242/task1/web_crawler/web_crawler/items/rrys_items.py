import scrapy


class RrysItem(scrapy.Item):
    seq = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    ranking = scrapy.Field()
    classification = scrapy.Field()
    favorites = scrapy.Field()
    cover = scrapy.Field()