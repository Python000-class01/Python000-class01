import jieba
jieba.enable_paddle()
from os import path
import pprint
from snownlp import SnowNLP
import pymysql

dir = path.dirname(__file__)
text = open(path.join(dir, 'jieba.txt'), encoding='utf-8').read()
top10 = jieba.analyse.extract_tags(text, topK=10, withWeight=False)
pprint(top10)
s = SnowNLP(top10)
s.sentiments

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'rootroot',
                       database = 'test',
                       charset = 'utf8mb4'
                        )
TABLE_NAME="snow_nlp"
con1 = conn.cursor()
values = [(1, s.sentiments)]
con1.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)