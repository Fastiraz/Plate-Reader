CREATE DATABASE `plate`;

USE plate;

CREATE TABLE `data`
(
    `id` INT PRIMARY KEY NOT NULL,
    `plate` VARCHAR(10),
    `date` DATE,
    `fiability` VARCHAR(10)
);

INSERT INTO `data` VALUES (1, 'XX-000-XX', '000-00-00', '100%');