<<<<<<< HEAD
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS notes;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE workout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    workout_monday TEXT,
    workout_tuesday TEXT,
    workout_wednesday TEXT,
    workout_thursday TEXT,
    workout_friday TEXT,
    workout_saturday TEXT,
    workout_sunday TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    exercise TEXT,
    sets INTEGER,
    kg INTEGER,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (workout_id) REFERENCES workout(id)
)
=======
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
>>>>>>> 43d1475e80626c81c539e548dce0b0f7a9df358c
