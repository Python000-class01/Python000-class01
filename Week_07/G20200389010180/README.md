项目脚本分为三部分：

#### 1. p1_crawl 抓取
使用Scrapy抓取SMZDM商品新闻评论并存储至Mysql数据库
#### 2. p2_data_process 数据处理
使用Pandas处理数据，去空格去重，使用SnowNLP添加情感分析值，处理后的数据存储至Mysql
#### 3. p3_display 展示
使用Flask展示数据，包括评论内容（部分）、评论搜索、分日评论量柱状图、舆情正负向饼图，图表部分使用了Chart.js



