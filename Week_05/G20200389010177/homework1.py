# 使用 jieba 对豆瓣中任意一本书评或影评提前 top10 关键词，并绘制词云
import requests
from lxml import etree
import csv
import jieba.analyse
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
# from matplotlib.pyplot import imread

# 基本参数设置
user_agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
comment_url = 'https://book.douban.com/subject/26829016/comments/hot'

# 爬虫下载影评
def get_comments(url):
    res = requests.get(url, headers=user_agent).text
    hot_comments = etree.HTML(res).xpath('//*[@id="comments"]/ul[1]/li')
    comments_top10 = []
    for hot_comment in hot_comments[0:10]:
        comment = hot_comment.xpath('./div//span[@class="short"]/text()')[0]
        # writer.writerow(comment)
        comments_top10.append(comment)
    return comments_top10

# 将下载的影评，使用tf-idf算法提取关键词

comments = get_comments(comment_url)
text = ''.join(comments)
tfidf = jieba.analyse.tfidf(text,topK=15,withWeight=False)

# 制作词云
wc = WordCloud(
  width = 600,      #默认宽度
  height = 400,     #默认高度
  margin = 10,       #边缘
  ranks_only = None,
  prefer_horizontal = 0.9,
  mask = None,      #背景图形,如果想根据图片绘制，则需要设置
  color_func = None,
  max_words = 200,  #显示最多的词汇量
  stopwords = None, #停止词设置，修正词云图时需要设置
  random_state = None,
  background_color = '#ffffff',#背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
  font_step = 1,
  font_path=r'SlideTownsoul-Regular.ttf',
  mode = 'RGB',
  regexp = None,
  collocations = True,
  normalize_plurals = True,
  contour_width = 0,
  colormap = 'viridis',#matplotlib色图，可以更改名称进而更改整体风格
  contour_color = 'Blues',
  repeat = False,
  scale = 2,
  min_font_size = 10,
  max_font_size = 200)

text_string = ','.join(tfidf)
wc.generate_from_text(text_string)
wc.to_file('book1.png')

# 显示词云预览
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()