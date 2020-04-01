# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Week030082ScrapyPipeline(object):
    def process_item(self, item, spider):
        article = open('./renren2019.txt', 'a+', encoding='utf-8')
        title = item['title']  # 影片名称
        rank = item['rank']  # 影片排名
        link = item['link']  # 影片链接
        m_level = item['m_level']  # 影片评级
        m_image_link = item['m_image_link']  # 影片封面下载地址
        browse_total = item['browse_total']  # 影片浏览数
        output = f'{rank}\t{title}\t{m_level}\t{browse_total}\t{link}\t{m_image_link}\n\n'
        article.write(output)
        article.close()
        return item
