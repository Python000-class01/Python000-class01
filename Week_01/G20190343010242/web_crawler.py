import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
from logger import getLogger


class WebCrawler():
    
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    DEFAULT_HEADERS = {'user-agent': USER_AGENT}

    def __init__(self):
        super().__init__()
        self.logger = getLogger(self.__class__.__name__)
    
    def get_response(self, url, method='get', params={}, headers=DEFAULT_HEADERS):
        http_request = getattr(requests, method)
        self.logger.debug(f"Request url: {url}; Method: {method}; Params: {params}; Headers: {headers}")
        response = http_request(url, params=params, headers=headers)
        return response

    def get_response_text(self, url, method='get', params={}, headers=DEFAULT_HEADERS):
        return self.get_response(url, method, params, headers).text

    def get_response_json(self, url, method='get', params={}, headers=DEFAULT_HEADERS):
        return self.get_response(url, method, params, headers).json()
    
    def get_parser_response(self, url, method='get', params={}, headers=DEFAULT_HEADERS, parser='html'):
        if parser == 'html':
            return bs(self.get_response_text(url, method, params, headers), 'html.parser')
        elif parser == 'lxml':
            return lxml.etree.HTML(self.get_response_text(url, method, params, headers))
        else:
            self.logger.error(f"Unsupported parser: {parser}")
            raise Exception(f"Unsupported parser: {parser}")

    