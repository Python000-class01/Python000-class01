from pandas import pandas as pd

df = pd.read_csv('./book_douban/comment_4913064.txt')
df["rating_num"]= df["star"].map({'力荐':5, '推荐':4,'还行':3})
s = ""
for d in df["content"]:
    s += d

import jieba
import jieba.analyse

jieba.analyse.set_stop_words('./stopwords.txt')
tfidf = jieba.analyse.extract_tags(s, topK=10, withWeight=True)
text_string = ','.join([ t[0] for t in tfidf])

from wordcloud import WordCloud

wc = WordCloud(
    width = 600,
    height=200,
    margin=2,
    ranks_only=None,
    prefer_horizontal=0.9,
    mask=None,
    color_func=None,
    max_words=10,
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
    min_font_size=20,
    max_font_size=200
)

wc.generate_from_text(text_string)

from matplotlib import pyplot as plt
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
wc.to_file('book.png')