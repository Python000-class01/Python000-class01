from web_crawler import WebCrawler
from logger import getLogger
import sys


class HttpBin():

    def __init__(self, base_url):
        super().__init__()
        self.logger = getLogger(self.__class__.__name__)
        self.crawler = WebCrawler()
        self.base_url = base_url
    
    def request_json(self, method="get", params={}):
        return self.crawler.get_response_json(f"{self.base_url}/{method.lower()}", method=method, params=params,headers={})

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        base_url = "http://httpbin.org"
        http_bin = HttpBin(base_url)
        try:
            http_bin.logger.info(http_bin.request_json(method=args[1]))
        except Exception as e:
            http_bin.logger.error("Exception: ", e)
    else:
        raise Exception("Invalid argument(s).")