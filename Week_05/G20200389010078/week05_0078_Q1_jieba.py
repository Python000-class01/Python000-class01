import jieba.analyse
import pprint

file = open('doubanbook.txt',encoding="utf-8-sig")
text = file.read()
# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(text,
topK=100,                   # 权重最大的topK个关键词
withWeight=False)         # 返回每个关键字的权重值
# # 基于TextRank算法进行关键词抽取
# textrank = jieba.analyse.textrank(text,
# topK=5,                   # 权重最大的topK个关键词
# withWeight=False)         # 返回每个关键字的权重值

            # pprint 模块提供了打印出任何Python数据结构的类和方法
pprint.pprint(tfidf)




