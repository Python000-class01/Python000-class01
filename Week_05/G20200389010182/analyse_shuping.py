import pandas as pd
import numpy as np
import matplotlib as plt
import jieba.analyse

df = pd.read_csv('book.csv')

# content = df['内容'].to_list().replace('\n','').replace('\r','')
content = df['内容'].to_list()

content_str = "".join(content).replace('\n','')

stop_words = r'stop_words.txt'
jieba.analyse.set_stop_words(stop_words)
tfidf = jieba.analyse.extract_tags(content_str,
topK=10,
withWeight=False)

print(tfidf)

# snowNLP
from snownlp import SnowNLP
first_line = df[df['评分']==3.0].iloc[0]
text = first_line['内容']
s = SnowNLP(text)
print(f'情感倾向： {s.sentiments} , 文本内容： {text}')

def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

df['sentiment'] = df['内容'].apply(_sentiment)

# 查看结果
df.head()
# 分析平均值
df.sentiment.mean()

