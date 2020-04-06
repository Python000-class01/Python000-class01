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
#mysql
1、Python 3.7连接到MySQL数据库的模块推荐使用PyMySQL模块
2、/usr/local/mysql/support-files/mysql.server start
 3、一般流程：
 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束
    
 


