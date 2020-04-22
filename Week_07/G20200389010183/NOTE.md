# python大作业说明
## 数据模型
这里遇到一个问题就是中文的新闻评论里会有很多imoj，这样用一般的utf8保存就会出错，这里要
将DEFAULT CHARSET=utf8mb4并且collation设为utf8mb4_general_ci，
这里id为每个评论的id，score为使用sentiment进行情感 分析之后的得分*10的取整，
atti为正负情感，score大于5为正，否则为负，time用来对comment进行排序以及统计。首页的柱状图就是通过
时间的日为单位进行统计的。
```
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for news_comment
-- ----------------------------
DROP TABLE IF EXISTS `news_comment`;
CREATE TABLE `news_comment` (
  `id` bigint(20) NOT NULL,
  `atti` tinyint(1) NOT NULL DEFAULT '0',
  `time` datetime DEFAULT NULL,
  `comment` varchar(2000) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `score` tinyint(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
## 数据库
数据库连接信息在`app/backend/hello.py`文件第82行
`engine = create_engine("mysql+pymysql://root:123456@localhost:3306/test?charset=utf8", echo=True)`
## flask后台应用


应用使用了一个def query():方法，通过获取请求中携带的pageSize和keyword参数，对数据进行检索
默认使用的分页大小为10，当keyword不为空时，进行查询

```
res = session.query(CommentDO).filter(CommentDO.comment.like(f'%{keyword}%')).order_by(
    CommentDO.time.desc()).limit(page_size)
```
查询到结果后将统计数据通过柱状图和饼状图进行展示，柱状图为根据条件过滤后每日爬取数据的数量，饼状图为正负情感的数量
# scrapy爬虫框架
这里爬取的新闻评论的连接为`https://www.thepaper.cn/newDetail_commt.jsp?contid=7082812`
爬虫框架爬取数据后对数据进行情感计算`score=sentiments*10，atti= score > 5 ? 1 : 0`这里并没有对数据进行清理，只不过对时间进行了特殊梳理，使得页面上的'5分钟前'，'3小时前'转变为
爬取数据时间减去响应时间的实时的时间。
# 定时任务
```
spider = Process(target=crawl_sched, args=(60,))#传入爬虫执行的时间，这里测试设置为1分钟，一般设置为 3600*24 一天
    spider.start()
    flask_app = Process(target=flask_task)
    flask_app.start()

    spider.join()
    flask_app.join()
```
这里启用了两个进程，一个运行flask后台项目，一个定时运行爬取新闻评论的任务；
这里使用了shed库
```
s = sched.scheduler(time.time, time.sleep)
def spider_task():
    proc = CrawlerProcess(get_project_settings())
    proc.crawl(ExampleSpider)
    proc.start()


def crawl_sched(time_loop_seconds):
    print('开始定时任务爬取数据')
    s.enter(time_loop_seconds, 2, spider_task)
    s.enter(time_loop_seconds, 1, crawl_sched, argument=(time_loop_seconds,))  # time_loop_seconds每隔秒执行一次perform1
    s.run()
    print('定时任务结束')
```
sched模块实现了一个时间调度程序，该程序可以通过单线程执行来处理按照时间尺度进行调度的时间。
通过调用scheduler.enter(delay,priority,func,args)函数，可以将一个任务添加到任务队列里面，当指定的时间到了，就会执行任务(func函数)。

delay：任务的间隔时间。
priority：如果几个任务被调度到相同的时间执行，将按照priority的增序执行这几个任务。
func：要执行的任务函数
args：func的参数

s.run()会阻塞当前线程的执行
可以用

```
t=threading.Thread(target=s.run)
t.start()
```
也可以用`s.cancal(action)`来取消sched中的某个action

# 启动应用
进入app/backend/hello.py，
```angular2html
启动 if __name__ == '__main__':就可以运行了
```
访问首页地址`http://127.0.0.1:8080/`，首页显示如下：
![](pic.png)