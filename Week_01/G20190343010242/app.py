from web_crawler import WebCrawler
from time import sleep
from configure import getConfig
from logger import getLogger
import pandas
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed


class App():

    OUTPUT_FOLDER = "outputs"

    def __init__(self, target):
        super().__init__()
        self.crawler = WebCrawler()
        target_config = getConfig().get("targets", {}).get(target)
        self.logger = getLogger(self.__class__.__name__)
        if not target_config:
            self.logger.error("target is not found in config.")
            raise Exception("target is not found in config.")
        self.logger.info(f"Application is processing target {target}")
        self.target_config = target_config
        self.max_threads = int(getConfig()["configs"]["max_threads"])
        self.sleep_time = int(self.target_config["sleep"])
        self.detail_urls = []
        self.items = []
    
    def _get_urls(self):
        url = self.target_config['url']
        page_size = self.target_config['page_size']
        total_items = self.target_config['total_items']
        pages = int(total_items / page_size) if total_items % page_size == 0 else int(total_items / page_size) + 1
        page_param = self.target_config['page_param']
        urls = tuple(f'{url}?{page_param}={ page * page_size }' for page in range(pages))
        return urls
    
    def _get_detail_url(self, pageUrl):
        urls = []
        try:
            self.logger.info(f"Processing url: {pageUrl}")
            sleep(self.sleep_time)
            item_type = self.target_config['item_type']
            item_attr = self.target_config['item_attr']
            info_attr = self.target_config['info_attr']
            bs_info = self.crawler.get_parser_response(pageUrl)
            item_blocks = bs_info.findAll(item_type, attrs={'class': item_attr})
            print(bs_info)
            for item_block in item_blocks:
                info = item_block.find('div', attrs={'class': info_attr})
                detail_url = info.find('a').get('href')
                if detail_url:
                    urls.append(detail_url)
                else:
                    self.logger.warning("No detail url is found, item will be skipped.")
        except Exception as e:
            self.logger.error(f"Exception occurred on url: {pageUrl}.", e)
        return urls
    
    def _get_all_detail_urls(self):
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            tasks = [executor.submit(self._get_detail_url, url) for url in self._get_urls()]
            for future in as_completed(tasks):
                self.detail_urls.extend(future.result())

    def _handle_item(self, url):
        items = []
        try:
            self.logger.info(f"Processing detail url: {url}")
            sleep(self.sleep_time)
            selector = self.crawler.get_parser_response(url, parser='lxml')
            item = {}
            for property in self.target_config['item_properties']:
                item[property['name']] = self._handle_property(selector, property)
            items.append(item)
        except Exception as e:
            self.logger.error(f"Exception occurred on url: {url}.", e)
        return items
    
    def _handle_property(self, selector, property):
        name = property['name']
        xpath_values = selector.xpath('//*' + property['xpath'])
        if name in ['Directors', 'ScriptWriters', 'Actors', 'Authors', 'HotComments']:
            return ' | '.join(xpath_values)
        elif name == 'Year':
            return xpath_values[0].strip().replace('(', '').replace(')', '')
        else:
            return xpath_values[0].strip()

    def get_items(self):        
        self._get_all_detail_urls()
        with ThreadPoolExecutor(max_workers=self.max_threads) as t:
            jobs = [t.submit(self._handle_item, detail_url) for detail_url in self.detail_urls]
            for future in as_completed(jobs):
                self.items.extend(future.result())

    def to_output_file(self):
        columns = list(map(lambda property : property["name"], self.target_config['item_properties']))
        df = pandas.DataFrame(self.items, columns=columns)
        path = f"{os.getcwd()}/{self.OUTPUT_FOLDER}"
        if not os.path.exists(path):
            logger.debug(f"Create output folder: {self.OUTPUT_FOLDER}")
            os.makedirs(self.OUTPUT_FOLDER)
        df.to_csv(f"{path}/{self.target_config['output_file_name']}.csv", columns=columns, index=False, encoding=self.target_config['output_encoding'])
        
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        app = App(args[1])
        app.get_items()
        if app.target_config['enable_output']:
            app.logger.info(f"Output target to file {app.target_config['output_file_name']}.csv")
            app.to_output_file()
    else:
        raise Exception("Invalid argument(s).")