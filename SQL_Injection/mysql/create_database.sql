CREATE DATABASE website;

USE website;

CREATE TABLE Users (
    email VARCHAR(100) PRIMARY KEY UNIQUE NOT NULL,
    user_name VARCHAR(100) UNIQUE NOT NULL
)
ENGINE = InnoDB;

CREATE TABLE Auth (
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(20) NOT NULL,
    FOREIGN KEY (email) references Users (email)
)
ENGINE = InnoDB;


CREATE TABLE Languages (
    email VARCHAR(100) UNIQUE NOT NULL,
    language VARCHAR(30) NOT NULL,
    FOREIGN KEY (email) references Users (email)
)
ENGINE = InnoDB;

INSERT INTO Users (email, user_name)
VALUES ("amigo@gmail.com", "amigo");

INSERT INTO Auth (email, password)
VALUES ("amigo@gmail.com", "amigo123");

INSERT INTO Languages (email, language)
VALUES ("amigo@gmail.com", "python");

INSERT INTO Users (email, user_name)
VALUES ("andrii@gmail.com", "andrii");

INSERT INTO Auth (email, password)
VALUES ("andrii@gmail.com", "andadgr2345ii123");

INSERT INTO Languages (email, language)
VALUES ("andrii@gmail.com", "c++");

INSERT INTO Users (email, user_name)
VALUES ("akerke@gmail.com", "akerke");

INSERT INTO Auth (email, password)
VALUES ("akerke@gmail.com", "ksfaa2345");

INSERT INTO Languages (email, language)
VALUES ("akerke@gmail.com", "c++");

INSERT INTO Users (email, user_name)
VALUES ("vlad@gmail.com", "vlad");

INSERT INTO Auth (email, password)
VALUES ("vlad@gmail.com", "vvadfvvv");

INSERT INTO Languages (email, language)
VALUES ("vlad@gmail.com", "python");