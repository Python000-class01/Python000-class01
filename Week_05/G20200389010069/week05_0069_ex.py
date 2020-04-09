import requests
from bs4 import BeautifulSoup as bs
import  pandas as pd
import jieba.analyse
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import os
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib.pyplot import imread
import random



url = 'https://book.douban.com/subject/34822422/reviews'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.3974.400'}
respons = requests.get(url,headers=headers)
bs_info = bs(respons.text,'html.parser')
print(bs_info)
shortcontent = bs_info.find_all('div',attrs={'class':"short-content"})

with open('ciyu.txt','w',encoding='utf-8') as f :
    for i in shortcontent:
        i = i.get_text()
        f.write(i)


text = pd.read_csv('ciyu.txt')
text = ' '.join(text)
stop_words='stop_words.txt'
jieba.analyse.set_stop_words(stop_words)
tfidf = jieba.analyse.extract_tags(text,
topK=10,                   # 权重最大的topK个关键词
withWeight=False)
#print(tfidf)
font = 'C:\\Users\\NICAI\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\wordcloud\\msyhl.ttc'
text_string = ','.join(tfidf)

# 生成词云
wc = WordCloud(
  width = 600,      #默认宽度
  height = 200,     #默认高度
  margin = 2,       #边缘
  ranks_only = None,
  prefer_horizontal = 0.9,
  mask = None,      #背景图形,如果想根据图片绘制，则需要设置
  color_func = None,
  max_words = 200,  #显示最多的词汇量
  stopwords = None, #停止词设置，修正词云图时需要设置
  random_state = None,
  background_color = '#ffffff',#背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
  font_step = 1,
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
  max_font_size = 200,
  font_path=font)

wc.generate_from_text(text_string)


# 显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
# 存储图像
wc.to_file('book.png')

plt.show()










import pandas as pd
from snownlp import SnowNLP
import pymysql


text = ['好东西，经典值得慢慢品尝 我有一本83年板古老的商务印书局的《新华词典》',
        '经典哦','读新华字典，好熟悉的感觉啊，虽然很久没看了。 那时还在上中学，我和坐在身后的同学都喜欢看新华字典，尤其是周二开校务会时，老师不容许桌上放任何书，书桌里的字典就成了我们打发时光的最好伙伴。',
        '布基纳法索吧。呵呵。',
        '记忆中，小学一年级时买的字典使用时间最长。还有一本不知是第几版的，老的都掉了皮皮。字典在学生时代可谓功不可没，现在读的次数极了。但是却读的兴趣很大了。旧象楼主说的一样。',
        '新华字典里每页都有不认识的字，真是学无止境呀',
        '哈哈，有趣',
        '喜欢有趣或擅于发现趣味的人～',
        '成语字典里面故事更多，更精彩呢 ',
        '我小时候好像最喜欢一本彩图百科字典……漂亮~'
        ]
text =str(text)

s = SnowNLP(text)
s1 = s.sentiments
print(s1)


dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'rootroot',
    'db' : 'test'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

        self.run()

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

if __name__ == "__main__":
    db = ConnDB(dbInfo, sqls)
    print(result)

