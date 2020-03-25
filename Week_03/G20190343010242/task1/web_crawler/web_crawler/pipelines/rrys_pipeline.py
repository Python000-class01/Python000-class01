import pandas
import os


class RrysPipeline(object):

    def open_spider(self, spider):
        self.data = []

    def close_spider(self, spider):
        columns = ['seq', 'title', 'link', 'ranking', 'classification', 'favorites', 'cover']
        sorted_data = sorted(self.data, key=lambda item: item['seq'])
        df = pandas.DataFrame(sorted_data, columns=columns)
        ROOT_DIR = os.getcwd()
        path = os.path.join(ROOT_DIR, "output")
        if not os.path.exists(path):
            os.makedirs("output")
        df.to_csv(f"{path}/rrys.csv", columns=columns, index=False,encoding="utf-8")

    def process_item(self, item, spider):
        if spider.name == 'rrys':
            self.data.append(dict(item))
            return item
        return None