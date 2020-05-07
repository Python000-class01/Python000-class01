# CREATE TABLE `comment` (
#   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
#   `user` varchar(20) DEFAULT NULL COMMENT '用户名',
#   `short` varchar(200) DEFAULT NULL COMMENT '短评',
#   `timestamp` varchar(20) DEFAULT NULL COMMENT '评论时间',
#   `sentiment` float DEFAULT NULL COMMENT '情感分析',
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8mb4