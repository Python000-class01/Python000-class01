## 学习笔记

#### 1.第一题主要是python requests库的运用，对豆瓣数据进行爬取，同时借助作业熟悉python语言。其中有一个坑，不知道大家遇到没，我在这里记录一下。

在将写入csv文件的时候，大家一般都是通过utf-8编码写入，用Excel打开会出现乱码问题。在查阅相关资料得知，要使用```UTF-8 with BOM```编码写入，在python中即```utf-8-sig```

```python3
with open('douban.csv', 'w', encoding='utf-8-sig') as f:
    pass
```



#### 2. 第二题主要是对requests库进一步熟悉，requests的返回值有个json的方法，调用其就可以将结果转换为JSON



#### 3. some tips

1. 作为一名pythoner写的python要pythonic
2. 编写python程序要贴合python官方的设计风格
3. 使用```pip3 freeze > requirements.txt```命令即可导出项目所依赖的库

