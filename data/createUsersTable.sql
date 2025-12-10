CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    accountnumber VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    emailaccount VARCHAR(50),
    phonenumber INTEGER,
    address VARCHAR(255),
    password VARCHAR(128)
);
