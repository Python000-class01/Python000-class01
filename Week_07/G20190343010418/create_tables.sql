DROP TABLE IF EXISTS `news_info`;
CREATE TABLE `news_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `title` varchar(100) COLLATE utf8_unicode_ci NOT NULL COMMENT '新闻标题',
  `content` varchar(2000) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '新闻内容',
  `updatetime` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='新闻基本信息';

DROP TABLE IF EXISTS `news_comments`;
CREATE TABLE `news_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `news_id` int(11) NOT NULL COMMENT '新闻编号',
  `comments` varchar(1000) COLLATE utf8_unicode_ci NOT NULL COMMENT '评论内容',
  `sentiment` float DEFAULT NULL COMMENT '情感分析得分',
  `updatetime` datetime DEFAULT NULL COMMENT '评论时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
