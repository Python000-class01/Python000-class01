create database scrapy;

CREATE TABLE `movie_comment` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `comment` text DEFAULT NULL COMMENT '评论',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8mb4;