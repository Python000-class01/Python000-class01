CREATE TABLE `t1` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `n_star` int(11) NOT NULL DEFAULT '0',
  `short` varchar(400) NOT NULL DEFAULT '',
  `sentiment` float(12,10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;