import jieba.analyse

with open("L:\\bookshortcomment.txt", "r", encoding='utf-8') as shortcomm:
    shortcommtext = shortcomm.read()

# 动态添加词典
jieba.add_word('数学之美')

stop_words=r'stop_words.txt'
# stop_words 的文件格式是文本文件，每行一个词语
jieba.analyse.set_stop_words(stop_words)

# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(shortcommtext,
topK=10,                   # 权重最大的topK个关键词
withWeight=True)         # 返回每个关键字的权重值
# 基于TextRank算法进行关键词抽取
textrank = jieba.analyse.textrank(shortcommtext,
topK=10,                   # 权重最大的topK个关键词
withWeight=True)         # 返回每个关键字的权重值

import pprint             # pprint 模块提供了打印出任何Python数据结构的类和方法
pprint.pprint(tfidf)
pprint.pprint(textrank)