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