DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS recipes;


-- __________CREATE____________
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE recipes(
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    image TEXT
);


-- __________INSERT____________
INSERT INTO users (id, username, password, email)
VALUES (1, 'Audrey', '123456', 'a.gaudilliere@gmail.com');

INSERT INTO recipes (id, name, description, image)
VALUES (1, 'Tiramisu', 'Dessert italien', 'tiramisu.jpg');
        








