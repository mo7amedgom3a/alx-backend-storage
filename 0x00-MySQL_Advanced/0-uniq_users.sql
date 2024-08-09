-- Active: 1723165464730@@127.0.0.1@3306@holberton
-- A SQL script that creates a table (called users) with following fields
-- id, email, name
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
)
