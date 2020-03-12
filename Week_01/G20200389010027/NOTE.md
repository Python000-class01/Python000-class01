# 学习笔记

### 作业1：爬虫作业
0.环境
操作系统：winddows10
Python: 3.8.2
编辑器：vscode
源文件：day0305.py

1.实现
1.1 使用webdriver的firefox浏览器打开页面，获取cookie
1.2 使用request带cookie访问top250页面并获取相关信息
1.3 根据1.2得到的影片链接，访问影片详情页面，获取评论信息
1.4 使用pandas的dataframe功能保存csv文件

2重点
2.1 豆瓣有一定的防爬虫机制，为了防止ip被限制，使用webdriver方式打开电影首页并获取cookie，并在之后的访问中带上这个cookie。另外在每次请求后都要等待若干秒，防止因为访问过于频繁，被网站屏蔽IP
2.2 lxml在加载html时需要一个流，我们已经从response中获取了页面源文件，这里要用StringIO来包装成流
2.3 各类信息都可以使用XPATH来获取
2.3 评论内容里有逗号，回车等，会影响csv文件的格式，在保存之前，需要把这些特殊字符进行删除或者替换

3.测试
在一般网络环境下，250条电影信息执行完，大概需要30分钟

4.问题
一开始想做一个配置文件来保存参数，但是使用configparser获取参数后，调用request.get(url)失败，原因应该是编码问题？

作业2：Json作业
0.环境
源文件：day0307.py
与作业1相同
1.实现
1.1 request.get request.post带数据参数调用
1.2 Json encoder和decoder使用

2.重点
2.1 get方法的querystring参数用param
2.2 post方法的表单参数用data，json参数用json，但是json参数和表单参数是冲突的，两个都传的情况下，返回值里只有json参数
