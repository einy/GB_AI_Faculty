CREATE DATABASE example;
USE example;
CREATE TABLE users (id SERIAL PRIMARY KEY, name varchar(32));
insert into users values (DEFAULT,'Иванов'),(DEFAULT,'Петров');