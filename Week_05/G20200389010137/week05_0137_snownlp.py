#!/usr/bin/env python

import pandas as pd
from snownlp import SnowNLP


df = pd.read_csv('week05_0137_douban1/douban.csv')

# 封装一个情感分析的函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

df["sentiment"] = df.short_content.apply(_sentiment)
# 查看结果
print(df.head())
# 分析平均值
print(df.sentiment.mean())