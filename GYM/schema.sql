DROP TABLE IF EXISTS user;

CREATE TABLE user (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);