CREATE SCHEMA IF NOT EXISTS `newscomments` DEFAULT CHAR SET = 'utf8mb4' DEFAULT COLLATE = 'utf8mb4_general_ci';
USE newscomments;
CREATE TABLE IF NOT EXISTS `news` (
    `news_id` VARCHAR(32) NOT NULL,
    `news_name` VARCHAR(500) NOT NULL,
    `source` VARCHAR(500) NOT NULL
    PRIMARY KEY (`news_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `comments` (
    `comment_id` BIGINT(20) NOT NULL AUTO_INCREMENT,
    `news_id` VARCHAR(32) NOT NULL,
    `comment` TEXT NOT NULL,
    `comment_time` DATETIME NOT NULL,
    `sentiment` FLOAT NOT NULL,
    PRIMARY KEY (`comment_id`),
    INDEX(`news_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;