## 学习笔记
### 实现功能描述
实现从 movie.douban.com/top250 抓取数据
程序分为三个部分：
1. 使用一个线程产生URL
2. 使用一个线程组抓取网页
3. 使用一个线程将数据保存到MySQL
### 数据库设计
数据库名称为:python_train  
用户名为:python_train  
密码为: python_train
当然可以修改连接字符串，设定成自己需要的用户名密码或者数据库名称
设计的两个表，表详情如下
```
mysql> create table douban_movie  (id int auto_increment primary key,movie_name varchar(20), movie_link varchar(100), movie_rating_level varchar(20),movie_rating_num decimal,movie_rating_persons int);
mysql> create table movie_comments(id int auto_increment primary key, movie_id int, movie_comment varchar(400));
mysql> desc douban_movie
    -> ;
+----------------------+---------------+------+-----+---------+----------------+
| Field                | Type          | Null | Key | Default | Extra          |
+----------------------+---------------+------+-----+---------+----------------+
| id                   | int(11)       | NO   | PRI | NULL    | auto_increment |
| movie_name           | varchar(20)   | YES  |     | NULL    |                |
| movie_link           | varchar(100)  | YES  |     | NULL    |                |
| movie_rating_level   | varchar(20)   | YES  |     | NULL    |                |
| movie_rating_num     | decimal(10,0) | YES  |     | NULL    |                |
| movie_rating_persons | int(11)       | YES  |     | NULL    |                |
+----------------------+---------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)

mysql> desc movie_comments;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int(11)      | NO   | PRI | NULL    | auto_increment |
| movie_id      | int(11)      | YES  |     | NULL    |                |
| movie_comment | varchar(400) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```
### 程序设计
1. DBOperation 封装底层数据库操作
2. MovieDBO 封装与douban_movie表相关操作
3. Movie 为douban_movie表的entity
4. MovieCommentsDBO  封装movie_comments表相关操作
5. MovieComments   movie_comments表对应的entity
6. DoubanClawler  爬虫类主要是使用三中不同线程分别处理程序的三个功能块 

### DoubanClawler类描述
1. 爬取网页的线程，调用方法为: douban_crawler
```
self.threads = [ threading.Thread(target=self.douban_crawler) for _ in range(size)]
```
2. 存数据库线程调用方法为save_to_mysql
```
self.db_thread = threading.Thread(target=self.save_to_mysql)
```
3. 产生url线程调用方法为generate_urls
```
self.url_thread = threading.Thread(target=self.generate_urls)
```
