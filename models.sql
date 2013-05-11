create table if not exists `feed`(
    `id` int(11) AUTO_INCREMENT,
    `create_time` int(11),
    `typ` int(1), 
    `content` text,
    `owner` int(1),
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET=utf8;
