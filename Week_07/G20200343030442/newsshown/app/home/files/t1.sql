CREATE TABLE `t1` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(11) NOT NULL DEFAULT '0',
  `comment` varchar(400) NOT NULL DEFAULT '',
  `score` varchar(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;