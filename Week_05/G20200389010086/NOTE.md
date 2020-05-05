学习笔记
# jieba
1、jieba 分精确模式 、全模式、paddle模式、 搜索引擎模式
example:
strings = ['我来未来', 'Python新世界真好玩']

6. 基于TF-IDF算法的关键词抽取
import jieba.analyse

jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
sentence为待提取的文本
topK为返回几个TF/IDF权重的最大关键词，默认值为20
withWeight为是否一并返回关键词权重值
allowPOS仅包括指定词性的词，默认值为空，即不筛选
jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件
关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径
用法： jieba.analyse.set_idf_path(file_name) # file_name为自定义语料库的路径。
#使用停止词
jieba.analyse.set_stop_words("../stop_words.txt")
#自定义词典路径
jieba.analyse.set_idf_path("../idf.txt.big.txt")
tags = jieba.analyse.extract_tags(content, topK=topK)
7. 基于TextRank算法的关键词抽取
jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) 直接使用，接口相同，注意默认过滤词性。
jieba.analyse.TextRank() 新建自定义 TextRank 实例
基本思想
将待抽取关键词的文本进行分词
以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
计算图中节点的PageRank，注意是无向带权图
#textrank
for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))
#词性标注
jieba.posseg.cut("我爱北京天安门")
#Tokenize: 返回词语在原文的起止位置,默认模式，输入参数仅支持unicode
result = jieba.tokenize(u'永和服装饰品有限公司')
#搜索模式
result = jieba.tokenize('永和服装饰品有限公司', mode='search')
8. 词性标注
jieba.posseg.POSTokenizer(tokenizer=None) 新建自定义分词器，tokenizer 参数可指定内部使用的 jieba.Tokenizer 分词器。
jieba.posseg.dt 为默认词性标注分词器。
标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。
除了jieba默认分词模式，提供paddle模式下的词性标注功能。paddle模式采用延迟加载方式，通过enable_paddle()安装paddlepaddle-tiny，并且import相关代码；
>>> import jieba
>>> import jieba.posseg as pseg
>>> words = pseg.cut("我爱北京天安门") #jieba默认模式
>>> jieba.enable_paddle() #启动paddle模式。 0.40版之后开始支持，早期版本不支持
>>> words = pseg.cut("我爱北京天安门",use_paddle=True) #paddle模式
>>> for word, flag in words:
...    print('%s %s' % (word, flag))
...
我 r
爱 v
北京 ns
天安门 ns
paddle模式词性和专名类别标签集合如下表，其中词性标签 24 个（小写字母），专名类别标签 4 个（大写字母）:
标签	含义	标签	含义	标签	含义	标签	含义
n	普通名词	f	方位名词	s	处所名词	t	时间
nr	人名	ns	地名	nt	机构名	nw	作品名
nz	其他专名	v	普通动词	vd	动副词	vn	名动词
a	形容词	ad	副形词	an	名形词	d	副词
m	数量词	q	量词	r	代词	p	介词
c	连词	u	助词	xc	其他虚词	w	标点符号
PER	人名	LOC	地名	ORG	机构名	TIME	时间
9. 并行分词
原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升。
基于 python 自带的 multiprocessing 模块，目前暂不支持 Windows。
用法：
jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
jieba.disable_parallel() # 关闭并行分词模式
注意：并行分词仅支持默认分词器 jieba.dt 和 jieba.posseg.dt

# 搜索引擎模式
1、
result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造') 

print('Search Mode: ' + '/'.join(list(result)))

2、停止词，过略掉不想要的关键词；如下示例：
`stop_words = r'stop_words.txt'
    jieba.analyse.set_stop_words(stop_words)`
#mysql
1、Python 3.7连接到MySQL数据库的模块推荐使用PyMySQL模块
2、/usr/local/mysql/support-files/mysql.server start
 3、一般流程：
 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束
    
 


