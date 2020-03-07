## 学习笔记

- 安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中。

![](http://ipic.liangchao.site/2020-03-04-%E6%88%AA%E5%B1%8F2020-03-0419.32.22.png)
![](http://ipic.liangchao.site/2020-03-04-%E6%88%AA%E5%B1%8F2020-03-0419.34.24.png)

1. 获得主页面的电影翻页获得全部链接
2. 打开每个链接, 获得具体的电影名称, 评分, 短评数量与前五条热评
3. 把全部结果写入 csv


- 使用 requests 库对 http://httpbin.org/get 页面进行 GET 方式请求，对 http://httpbin.org/post 进行 POST 方式请求，并将请求结果转换为 JSON 格式（转换 JSON 的库和方式不限）。

1. 向 httpbin.org 发 get, 打印 header, 并保存返回结果到文件
2. 向 httpbin.org 发 post, 打印 post 的参数, 并保存返回结果到文件