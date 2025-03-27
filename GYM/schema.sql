DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS workout;

CREATE TABLE user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);


CREATE TABLE workout (
id INTEGER PRIMARY KEY AUTOINCREMENT,
workout_monday TEXT NOT NULL,
workout_tuesday TEXT NOT NULL,
workout_wednesday TEXT NOT NULL,
workout_thursday TEXT NOT NULL,
workout_friday TEXT NOT NULL,
workout_saturday TEXT NOT NULL,
workout_sunday TEXT NOT NULL
);