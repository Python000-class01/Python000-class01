import scrapy
from lxml import etree
import json
from homework5_2.items import CommentItem, Comments


class ExampleSpider(scrapy.Spider):
    name = 'hw5_2'
    allowed_domains = ['douban.com']

    def start_requests(self):
        start_url = 'https://movie.douban.com/subject/34805219/comments'
        start_urls = []
        for i in range(0, 10):
            url = start_url + '?start=' + str(i * 20) + '&limit=20&sort=new_score&status=P'
            start_urls.append(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        html = etree.HTML(response.text)
        print('**************************************************')
        # //*[@id="comments"]/div[1]
        comment_ids = html.xpath('//*[@class="comment-item"]/@data-cid')
        items = Comments()
        comments = []
        for comment_id in comment_ids:
            item = CommentItem()
            item['id'] = comment_id
            # url = 'https://movie.douban.com/j/review/' + comment_id + '/full'
            # /html/body/div[3]/div[1]/div/div[1]/div[4]/div[1]/div[2]/h3/span[2]/span[2]
            # //*[@id="comments"]/div[1]/div[2]/h3/span[2]/span[2]
            rank = html.xpath(f'// *[ @ data-cid = {comment_id}] / div[2] /h3/span[2]/ span[2]/@class')
            # print(rank)
            try:
                if rank:
                    item['rank'] = int(rank[0][7:8])
                else:
                    item['rank'] = 0
            except ValueError:
                item['rank'] = 0
            # //*[@id="comments"]/div[1]/div[2]/p/span
            item['comment'] = html.xpath(f'// *[ @data-cid = {comment_id}] / div[2] /p/span/text()')[0]
            # yield from self.parse2(item)
            print(item['comment'])
            comments.append(item)
        items['comments'] = comments
        print('**************************************************')
        return items

        # item = Homework52Item()
        # item['id'] = comment_data[0]
        # url = 'https://movie.douban.com/j/review/' + comment_data[0] + '/full'
        # rank = html.xpath(f'// *[ @ id = {comment_data[0]}] / header / span[1]/@class')
        # if rank:
        #     item['rank'] = int(rank[0][7:8])
        # else:
        #     item['rank'] = 0
        # yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)

    async def parse2(self, item):
        return item
