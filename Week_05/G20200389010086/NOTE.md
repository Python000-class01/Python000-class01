学习笔记
# jieba
1、jieba 分精确模式 、全模式、paddle模式、 搜索引擎模式
example:
strings = ['我来未来', 'Python新世界真好玩']
# 搜索引擎模式
1、
result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造') 

print('Search Mode: ' + '/'.join(list(result)))

2、停止词，过略掉不想要的关键词；如下示例：
`stop_words = r'stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)`
 


