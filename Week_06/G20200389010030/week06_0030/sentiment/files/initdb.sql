CREATE SCHEMA IF NOT EXISTS `sentiment` DEFAULT CHAR SET = 'utf8mb4' DEFAULT COLLATE = 'utf8mb4_general_ci';
USE sentiment;
CREATE TABLE IF NOT EXISTS `sentiment` (
    `item_id` BIGINT(20) NOT NULL AUTO_INCREMENT,
    `item_name` VARCHAR(255) NOT NULL,
    `score` INT(11) NOT NULL,
    `trend` VARCHAR(255) NOT NULL,
    `comment` TEXT NOT NULL,
    `sentiment` FLOAT NOT NULL,
    PRIMARY KEY (`item_id`),
    INDEX(`item_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;