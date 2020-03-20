## flask-sqlacodegen 'mysql+pymysql://python_train:python_train@localhost:3307/python_train' --outfile blog_models.py --flask

create table blog_user(id int auto_increment primary key, username varchar(20),password varchar(20) );
create table blog_post(id int auto_increment primary key,author_id int, created date,title varchar(20), body varchar(400));