/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : 65001

 Date: 23/04/2020 01:20:11
*/

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

-- ----------------------------
-- Records of news_comment
-- ----------------------------
BEGIN;
INSERT INTO `news_comment` VALUES (28063726, 1, '2020-04-21 11:21:42', '\n                                        我觉得酒驾，醉驾，无证驾驶，闯红灯，违规使用远光灯，也应该适用此法。', 'shihcheng', 8);
INSERT INTO `news_comment` VALUES (28063772, 0, '2020-04-22 11:21:42', '\n                                        任何人闯红灯列为碰瓷处理，交通会井井有条', '默默守候你的那个人', 0);
INSERT INTO `news_comment` VALUES (28063800, 0, '2020-04-22 11:21:42', '\n                                        早就该这么弄了', '卢浩', 2);
INSERT INTO `news_comment` VALUES (28063932, 1, '2020-04-22 11:21:42', '\n                                        还有开车玩手机的。', 'hefei133', 6);
INSERT INTO `news_comment` VALUES (28064026, 0, '2020-04-22 12:21:42', '\n                                        城市管理部门也应该定时加强巡视，发现缺丢失的及时安装。', '有态度的……', 0);
INSERT INTO `news_comment` VALUES (28065865, 0, '2020-04-22 14:21:42', '\n                                                违法排放污染物的企业，是不是也应该以此类推，按投毒罪追责呢', '人人都有露水珠', 0);
INSERT INTO `news_comment` VALUES (28066307, 0, '2020-04-22 15:21:42', '\n                                                盗窃是不光彩的行为，偷窨井盖更是罪上加罪。窨井盖是人心共设施，盗走了就是给路人和车辆设陷阱一样，特别是在夜晚，车少人稀，如果有人不慎跌入，就有生命危险！应加大对此盗窃行为的打击力度，对他们破坏公共设施的犯罪应严判重判', '东风顺', 5);
INSERT INTO `news_comment` VALUES (28066510, 1, '2020-04-22 15:21:42', '\n                                                古人云“勿以恶小而为之；勿以善小而不为之。”“善小为之”且不说；“恶小而为之”造成的后果是不能用小来衡量的⋯⋯。', '澎湃网友3EJ7Vz', 9);
INSERT INTO `news_comment` VALUES (28066531, 1, '2020-04-22 15:21:42', '\n                                                支持', 'top域名', 6);
INSERT INTO `news_comment` VALUES (28067299, 0, '2020-04-22 16:21:42', '\n                                                重责收购者同样重要　甚至更重要', '简单', 1);
INSERT INTO `news_comment` VALUES (28067755, 0, '2020-04-22 17:21:42', '\n                                                赞同，坚决拥护', '老陶陶', 5);
INSERT INTO `news_comment` VALUES (28067943, 1, '2020-04-22 17:21:42', '\n                                                可以参照“光缆无铜，盗之无用”标语，把窨井盖刻上标语“非金属制造，废品站不要”😉', 'Ch Lu', 9);
INSERT INTO `news_comment` VALUES (28068011, 1, '2020-04-22 17:21:42', '\n                                                好！好！好！', 'jlhc', 8);
INSERT INTO `news_comment` VALUES (28068222, 1, '2020-04-22 17:21:42', '\n                                                闯红灯和远光灯不适用吧，也可能是无意的。但酒驾一定是明知故犯。', '更新鱼', 9);
INSERT INTO `news_comment` VALUES (28068242, 1, '2020-04-22 17:21:42', '\n                                                这个很难，要看地方政府有没有断腕的决心。毕竟影响税收和就业还可能有权钱交易。', '更新鱼', 7);
INSERT INTO `news_comment` VALUES (28070188, 0, '2020-04-22 20:12:41', '事人已老，子孙承祸。', '南方小佳人', 3);
INSERT INTO `news_comment` VALUES (28070354, 1, '2020-04-22 20:12:41', '\n                                                排水管道上的检查井（窨井），是给水排水专业工程设计的重要内容之一。恳请全社会尊重并支持给水排水专业的科学设计。可能社会公众不知道设计是建设之先锋，当你站在城市的任何一个位置环顾周边设施的时候，眼前的一切都是设计的成果通过施工单位转化成了现实。目前很多排水设施的损毁，与多年前的设计过程密不可分。给水排水设计是一门科学技术，但在很多领导眼中不完全是这样，很多情况下，他们用自己的非专业权威指导了专业设计，使专业设计师没有完全从科技角度实施设计，这其中包括了所谓的任期内工程必须完工，那叫萝卜快了不洗泥，等等。这些，形成了短期效益之后的长久隐患。当然这里还有投资限制和时代局限性等原因，但事实续存。', '平视世界之人', 9);
INSERT INTO `news_comment` VALUES (28070421, 1, '2020-04-22 20:12:41', '\n                                                汽车转弯时司机不打转向灯，是否也是一种谋杀犯罪呢？不要以为前车没打后车也跟着不打，要知道行人要注视着所有的车辆，谁知道哪个司机是杀手呢？', '平视世界之人', 9);
INSERT INTO `news_comment` VALUES (28070453, 1, '2020-04-22 20:12:41', '\n                                                司机违反交通规则，是比破坏窨井盖更常见的事情。不要因为从汽车上得到了巨大的收入而失去了公平之心。汽车应被视为杀人凶器。', '平视世界之人', 9);
INSERT INTO `news_comment` VALUES (28071287, 1, '2020-04-22 21:12:41', '\n                                                二、盗窃、破坏人员密集往来的非机动车道、人行道以及车站、码头、公园、广场、学校、商业中心、厂区、社区、院落等生产生活、人员聚集场所的窖井盖，足以危害公共安全，尚未造成严重后果的，依照刑法第一百一十四条的规定，以以危险方法危害公共安全罪定罪处罚；致人重伤、死亡或者便公私财产遭受重大损失的，依照刑法第一百一十五条第一款的规定处罚。', '陈滂CP', 9);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
