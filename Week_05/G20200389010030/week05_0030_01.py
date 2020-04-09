import jieba.analyse
import requests
from lxml import etree
import numpy as np
from wordcloud import WordCloud
from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot as plt


class Douban(object):

    def __init__(self, id, **kwargs):
        self.id = id
        self.comments = []
        self.top = kwargs['top']
        self.bg = kwargs['bg']

    def getComments(self, page=1):
        url = f'https://book.douban.com/subject/{self.id}/comments/hot?p={page}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        res = requests.get(url, headers=headers).text
        html = etree.HTML(res)
        if page == 1:
            count = html.xpath('/html/body/div[3]/div[1]/div/div[1]/div/div[1]/span/text()')
            if len(count) > 0:
                count = int(count[0].split(' ')[1])
            pages = count / 20 if count % 20 == 0 else int(count / 20) + 1
            for i in range(2, pages+1):
                self.getComments(i)
        comments = html.xpath('/html/body/div[3]/div[1]/div/div[1]/div/div[2]/div/ul/li/div[2]/p/span/text()')
        self.comments += list(map(lambda comment: comment.replace('\n', ''), comments))

    def getKeywords(self):
        keywords = []
        results = jieba.analyse.extract_tags('\n'.join(self.comments), topK=self.top, withWeight=True)
        for result in results:
            keywords.append(result)
        def takeSecond(elem):
            return elem[1]
        keywords.sort(key=takeSecond, reverse=True)
        keywords = list(map(lambda word: word[0], keywords))
        return keywords

    def genBackground(self, str):
        img = 'background.jpg'
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        font_type = '/System/Library/Fonts/SFCompactRounded-Heavy.otf'
        font = ImageFont.truetype(font_type, int(400 / (len(str) / 2)))
        color = "#000000"
        draw.text((0, 0), str, color, font)
        return image

    def genWordCloud(self):
        self.getComments()
        keywords = self.getKeywords()
        text_string = ','.join(keywords)
        background_Image = np.array(self.genBackground(self.bg)) if self.bg else None
        wc = WordCloud(
            width=600,
            height=200,
            margin=2,
            ranks_only=None,
            prefer_horizontal=0.9,
            mask=background_Image,
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
            max_font_size=200)
        wc.generate_from_text(text_string)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        wc.to_file('top10.png')
        plt.show()


if __name__ == '__main__':
    # douban = Douban('27028517', 10, bg="PY")
    douban = Douban('27028517', top=100, bg="PY")
    douban.genWordCloud()


