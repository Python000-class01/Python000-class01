from snownlp import SnowNLP

with open("L:\\bookshort.txt", "r", encoding='utf-8') as shortcomm:
    shortcommtext = shortcomm.read()

s = SnowNLP(shortcommtext)

# 1 中文分词
print(s.words)

# 2 词性标注
print(list(s.tags))

# 3 情感分析
print(s.sentiments)
text2 = '这本书烂透了'
s2 = SnowNLP(text2)
print(s2.sentiments)

# 4 拼音
print(s.pinyin)

# 5 繁体转简体
text3 = '後面這些是繁體字'
s3 = SnowNLP(text3)
print(s3.han)

# 6 提取关键字
s.keywords(limit=5)

# 7 信息衡量
print(s.tf) # 词频越大越重要
print(s.idf) # 包含此条的文档越少，n越小，idf越大，说明词条t越重要

# 8 训练
#from snownlp import seg
#seg.train('data.txt')
#seg.save('seg.marshal')
# 修改snownlp/seg/__init__.py的 data_path 指向新的模型即可