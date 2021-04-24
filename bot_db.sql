--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Сб апр 24 22:13:55 2021
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: class
CREATE TABLE class (id INT PRIMARY KEY UNIQUE NOT NULL, class_name STRING UNIQUE);

-- Таблица: problems
CREATE TABLE problems (id INT PRIMARY KEY UNIQUE NOT NULL, name STRING UNIQUE NOT NULL, user_id INT REFERENCES users (id) NOT NULL, class_id INT REFERENCES class (id) NOT NULL, describtion STRING, deadline DATETIME);

-- Таблица: used_id
CREATE TABLE used_id (id INT PRIMARY KEY UNIQUE NOT NULL, is_used BOOLEAN);

-- Таблица: users
CREATE TABLE users (id INT PRIMARY KEY UNIQUE NOT NULL, ctx UNIQUE);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
