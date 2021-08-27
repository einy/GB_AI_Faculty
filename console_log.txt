MacBookPro:~ admin$ mysqldump example > example.dump
MacBookPro:~ admin$ mysql
...
mysql> CREATE DATABASE sample;
Query OK, 1 row affected (0,00 sec)
mysql> USE sample;
Database changed
mysql> SOURCE example.dump
...
Query OK, 2 rows affected (0,00 sec)
mysql> USE mysql;
...
Database changed
mysql> exit;
Bye 
MacBookPro:~ admin$ mysqldump --where="true limit 100" mysql help_keyword > help_keyword.dump
MacBookPro:~ admin$ 
