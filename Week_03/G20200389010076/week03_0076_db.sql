/*
SQLyog Ultimate v8.32 
MySQL - 5.7.20-log : Database - rrysdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`rrysdb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `rrysdb`;

/*Table structure for table `moviesinfo` */

DROP TABLE IF EXISTS `moviesinfo`;

CREATE TABLE `moviesinfo` (
  `movies` int(11) NOT NULL AUTO_INCREMENT,
  `movies_name` char(50) DEFAULT NULL,
  `movies_from` char(20) DEFAULT NULL,
  `movies_language` char(20) DEFAULT NULL,
  `movies_fist` char(30) DEFAULT NULL,
  `movies_classify` char(50) DEFAULT NULL,
  `movies_rank` char(20) DEFAULT NULL,
  `movies_ABCD` char(10) DEFAULT NULL,
  `movies_browse_time` char(50) DEFAULT NULL,
  `image_url` char(100) DEFAULT NULL,
  PRIMARY KEY (`movies`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;

/*Data for the table `moviesinfo` */

insert  into `moviesinfo`(`movies`,`movies_name`,`movies_from`,`movies_language`,`movies_fist`,`movies_classify`,`movies_rank`,`movies_ABCD`,`movies_browse_time`,`image_url`) values (61,'Altered Carbon: Resleeved','美国','英语/日语','2020-03-19 周四','科幻/动画','本站排名:999999','23565','c','http://tu.jstucdn.com/ftp/2020/0324/b_1cd131086804f75a756ad90f15f77a93.png'),(62,'Impossible Monsters','美国','英语','2019-03-09','惊悚','本站排名:9709','56728','c','http://tu.jstucdn.com/ftp/2020/0316/b_1c7697f89ffe780234013b4e533456be.jpg'),(63,'The Invisible Man','美国','英语','2020-02-28','恐怖/惊悚/悬疑','本站排名:7571','41596','c','http://tu.jstucdn.com/ftp/2020/0323/b_e18cc5da4986f5748037fcf573481805.png'),(64,'Bloodshot','美国','英语','2020-02-21','动作/剧情','本站排名:4384','15970','c','http://tu.jstucdn.com/ftp/2019/1021/b_9fd3ed9de32a0e9d574d5d9db0dbeaee.jpg'),(65,'Just Mercy','美国','英语','2020-01-10 周五','剧情','本站排名:106','6955','a','http://tu.jstucdn.com/ftp/2019/1203/b_73b6374741d82e5de3dea384c3ed5354.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
