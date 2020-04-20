# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import scrapy
import time


class DoubanBookSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DoubanBookDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        content = self.selenium_request(request.url)
        if content.strip() != '':
            return scrapy.http.HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        # return None
        return scrapy.http.HtmlResponse(request.url, encoding='utf-8', body=content, request=request)

    def selenium_request(self, url):
        # js控制浏览器滚动到底部js
        js = """
        function scrollToBottom() {
            var Height = document.body.clientHeight,  //文本高度
                screenHeight = window.innerHeight,  //屏幕高度
                INTERVAL = 100,  // 滚动动作之间的间隔时间
                delta = 500,  //每次滚动距离
                curScrollTop = 0;    //当前window.scrollTop 值
            console.info(Height)
            var scroll = function () {
                //curScrollTop = document.body.scrollTop;
                curScrollTop = curScrollTop + delta;
                window.scrollTo(0,curScrollTop);
                console.info("偏移量:"+delta)
                console.info("当前位置:"+curScrollTop)
            };
            var timer = setInterval(function () {
                var curHeight = curScrollTop + screenHeight;
                if (curHeight >= Height){   //滚动到页面底部时，结束滚动
                    clearInterval(timer);
                }
                scroll();
            }, INTERVAL)
        };
        scrollToBottom()
        """
        chrome_options = webdriver.ChromeOptions()
        # headless无界面模式
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        time.sleep(2)
        # driver.maximize_window();# 窗口最大化
        # 执行js滚动浏览器窗口到底部
        driver.execute_script(js)
        # time.sleep(5)  # 不加载图片的话，这个时间可以不要，等待JS执行
        # driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\test.png")
        #content = driver.execute_script("return document.body.innerHTML;")
        content = driver.page_source.encode('utf-8')
        # driver.quit()
        driver.close()
        # return None
        return content

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)