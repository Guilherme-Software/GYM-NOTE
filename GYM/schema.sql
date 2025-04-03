DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS workout;

CREATE TABLE user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);


CREATE TABLE workout (
id INTEGER,
workout_monday TEXT,
workout_tuesday TEXT,
workout_wednesday TEXT,
workout_thursday TEXT,
workout_friday TEXT,
workout_saturday TEXT,
workout_sunday TEXT,
FOREIGN KEY (id) REFERENCES user(id)
);