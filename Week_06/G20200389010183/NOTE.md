# python大作业说明
## 数据模型
这里遇到一个问题就是中文的新闻评论里会有很多imoj，这样用一般的utf8保存就会出错，这里要
将DEFAULT CHARSET=utf8mb4并且collation设为utf8mb4_general_ci，
这里id为每个评论的id，sentiments 为使用 sentiment 进行情感 分析之后的得分 0-1 的数，
rank 为正负情感，rank 大于1为正，0为负。
```
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for jezt_comment_short
-- ----------------------------
DROP TABLE IF EXISTS `jezt_comment_short`;
CREATE TABLE `jezt_comment_short` (
  `id` bigint(20) NOT NULL,
  `rank` tinyint(1) NOT NULL DEFAULT '0',
  `comment` longtext,
  `sentiments` float(20,10) DEFAULT '0.0000000000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
## 数据库
数据库连接信息在`app/backend/hello.py`文件第82行
`engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8", echo=True)`
## flask后台应用


应用使用了一个def query():方法，通过获取请求中携带的pageSize参数，对数据进行检索
默认使用的分页大小为10，进行查询

```
session.query(CommentDO).order_by(CommentDO.sentiments.desc()).limit(page_size)
```

# scrapy爬虫框架
这里爬取的新闻评论的连接为`https://www.thepaper.cn/newDetail_commt.jsp?contid=7082812`
爬虫框架爬取数据后对数据进行情感计算`score=sentiments*10，atti= score > 5 ? 1 : 0`这里并没有对数据进行清理

# 启动应用
进入app/backend/hello.py，
```angular2html
启动 if __name__ == '__main__':就可以运行了
```
访问首页地址`http://127.0.0.1:8080/`，首页显示如下：
![](pic.png)