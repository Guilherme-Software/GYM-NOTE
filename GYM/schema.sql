DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS notes;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE workout (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    workout_monday VARCHAR(255),
    workout_tuesday VARCHAR(255),
    workout_wednesday VARCHAR(255),
    workout_thursday VARCHAR(255),
    workout_friday VARCHAR(255),
    workout_saturday VARCHAR(255),
    workout_sunday VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE notes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    day VARCHAR(255),
    position INT,
    user_id INT,
    exercise VARCHAR(255),
    sets INT,
    kg INT,
    notes VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user(id)
)
