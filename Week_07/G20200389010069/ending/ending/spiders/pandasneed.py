import pymysql
import pandas as pd
from snownlp import SnowNLP
from sqlalchemy import create_engine
import mysql.connector


conn = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = '123456',db = 'fang',charset = 'utf8')
df = pd.read_sql('select * from info3',con = conn)
#print(df)

#print(df)
#print(pd.isnull(df))
df = df.dropna()  #空值去除
#print(df)
df = df.drop_duplicates()
#print(df.shape)


sum = []
for  i in df['name']:
    s = SnowNLP(i)
    s1 = s.sentiments
    sum.append(s1)

df['result'] = sum
#print(df)

print(df)

# tfidf = jieba.analyse.extract_tags(text,
# topK=10,                   # 权重最大的topK个关键词
# withWeight=False)
# #print(tfidf)
# font = 'C:\\Users\\NICAI\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\wordcloud\\msyhl.ttc'
# text_string = ','.join(tfidf)
#
# # 生成词云
# wc = WordCloud(
#   width = 600,      #默认宽度
#   height = 200,     #默认高度
#   margin = 2,       #边缘
#   ranks_only = None,
#   prefer_horizontal = 0.9,
#   mask = None,      #背景图形,如果想根据图片绘制，则需要设置
#   color_func = None,
#   max_words = 200,  #显示最多的词汇量
#   stopwords = None, #停止词设置，修正词云图时需要设置
#   random_state = None,
#   background_color = '#ffffff',#背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
#   font_step = 1,
#   mode = 'RGB',
#   regexp = None,
#   collocations = True,
#   normalize_plurals = True,
#   contour_width = 0,
#   colormap = 'viridis',#matplotlib色图，可以更改名称进而更改整体风格
#   contour_color = 'Blues',
#   repeat = False,
#   scale = 2,
#   min_font_size = 10,
#   max_font_size = 200,
#   font_path=font)
#
# wc.generate_from_text(text_string)
#
#
# # 显示图像
# plt.imshow(wc, interpolation = 'bilinear')
# plt.axis('off')
# plt.tight_layout()
# # 存储图像
# wc.to_file('book.png')
#
# plt.show()
#
# s = SnowNLP(text)
# s1 = s.sentiments
# print(s1)

#
#
#
engine = create_engine("mysql+mysqlconnector://{}:{}@{}/{}?charset={}".format('root', '123456', '127.0.0.1:3306', 'fang','utf8'))
con = engine.connect()#创建连接
df.to_sql(name='info4', con=con, if_exists='replace', index=False)
#存入新表 info