# 吃瓜群众情感分析
---
## Introduction
+ 使用Scrapy抓取Sina新闻的吃瓜群众评论存入MySQL数据库
+ 使用SnowNLP对评论进行简单的情感分析
+ 使用Flask + pyecharts对情感分析的结果进行简单的展示
+ 使用Flask-APScheduler在后台定时调用spider抓取评论(目前使用os.system()调用，需要改进)

## Usage
0. 运行环境: Python3. 需要的package可以参考本目录下的requirements.txt, 但因为没有特意的设置虚拟环境所以有很多无用的。本项目中主要用到了Scrapy, Flask及其相关插件，SnowNLP, pyecharts等.可以先按照这几个package之后按照运行错误进行相应安装。(后续大概会完善...) 
1. 在setting/setting.py 中做global的设置，主要是MySQL相关，之后spider会按照这里的设置建立db和table.
2.  `cd flask_app`
3.  `python manage.py dev`  (注意： 启动后会先运行一次爬虫，视网络情况页面打开可能有数秒钟的延时，目前还不知道怎么fix...)



## Demo
+ 当前目录下的demo.html是一个简单的demo
  