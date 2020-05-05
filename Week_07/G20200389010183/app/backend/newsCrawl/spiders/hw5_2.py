import scrapy
from lxml import etree
import json
from newsCrawl.items import CommentItem, Comments
from newsCrawl.util.comment_time_util import to_date_time


class ExampleSpider(scrapy.Spider):
    name = 'hw5_2'
    allowed_domains = ['douban.com']

    def start_requests(self):
        start_url = 'https://www.thepaper.cn/newDetail_commt.jsp?contid=7082812'
        # start_urls = []
        # for i in range(0, 10):
        #     url = start_url + '?start=' + str(i * 20) + '&limit=20&sort=new_score&status=P'
        #     start_urls.append(url)
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        html = etree.HTML(response.text)
        print('**************************************************')
        # //*[@id="comments"]/div[1]
        # print(response.text)
        # comment_ids = html.xpath('//*[@class="comment_que"]')
        items = Comments()
        times = html.xpath(f'//*[@class="comment_que"]/div/div[2]/h3/span/text()')
        user_names = html.xpath(f'//*[@class="comment_que"]/div/div[2]/h3/a/text()')
        ids = html.xpath(f'//*[@class="comment_que"]/div/div[2]//div[@class="ansright_time"]/a[1]/@id')
        comments = html.xpath(f'//*[@class="comment_que"]/div/div[2]//div[@class="ansright_cont"]/a[1]/text()')
        print(len(times))
        print(len(user_names))
        print(len(ids))
        print(len(comments))
        for i in range(0, len(comments)):
            try:
                item = CommentItem()
                item['time'] = to_date_time(times[i])
                item['user_name'] = user_names[i]
                item['id'] = int(ids[i])
                item['comment'] = comments[i]
                yield item
            except Exception as e:
                print(f'获取第{i}个评论时出错{e}')
        print('**************************************************')


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
