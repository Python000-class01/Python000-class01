from configure import getConfig
from logger import getLogger
from web_crawler import WebCrawler
import jieba.analyse as analyse
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import os


class DoubanBookReviews:

    def __init__(self):
        super().__init__()
        self.logger = getLogger(self.__class__.__name__)
        self.reviewUrl = getConfig()['task1']['review_url']
        self.web_crawler = WebCrawler()

    def get_reviews(self):
        selector = self.web_crawler.get_parser_response(self.reviewUrl, parser='lxml')
        reviewEles = selector.xpath('//div[@class=\"short-content\"]')
        reviews = []
        for ele in reviewEles:
            review = ele.text.strip().replace('&nbsp', '').replace('\n', '').replace('\r', '').replace('(', '').replace('...', '')
            if review and review != '':
                reviews.append(review)
        return ''.join(reviews)

    def get_keywords(self):
        keys = [key for key in analyse.extract_tags(self.get_reviews(), topK=getConfig()['task1'].get('topK', 10), withWeight=False)]
        return keys

    def generate_word_cloud(self, fileName=None):
        text_string = ','.join(self.get_keywords())
        wc = WordCloud(
            width=600,
            height=200,
            margin=2,
            ranks_only=None,
            prefer_horizontal=0.9,
            mask=None,
            color_func=None,
            max_words=200,
            stopwords=None,
            random_state=None,
            background_color='#ffffff',
            font_step=1,
            mode='RGB',
            regexp=None,
            collocations=True,
            normalize_plurals=True,
            contour_width=0,
            colormap='viridis',
            contour_color='Blues',
            repeat=False,
            scale=2,
            min_font_size=10,
            max_font_size=200,
            font_path=os.environ.get('FONT_PATH', os.path.join(os.path.dirname(__file__), 'PingFang.ttc')))

        wc.generate_from_text(text_string)
        if fileName:
            ROOT_DIR = os.getcwd()
            path = os.path.join(ROOT_DIR, "output")
            if not os.path.exists(path):
                os.makedirs("output")
            wc.to_file(os.path.join(path, fileName))
        else:
            plt.imshow(wc, interpolation='bilinear')
            plt.axis('off')
            plt.tight_layout()
            plt.show()

