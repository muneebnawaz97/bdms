CREATE DATABASE IF NOT EXISTS BDMS;

USE BDMS;

CREATE TABLE IF NOT EXISTS BDMS.LOGIN_CREDENTIALS(
login_id int NOT NULL,
login_username varchar(255) NOT NULL,
login_password varchar(255) NOT NULL,
user_role varchar(255) NOT NULL,
PRIMARY KEY (login_id)
);

INSERT INTO LOGIN_CREDENTIALS(login_id,login_username,login_password,user_role) VALUES ( 0,
    "admin",
    "admin",
    "admin");

CREATE TABLE IF NOT EXISTS BDMS.EMPLOYEES(
employee_id int NOT NULL,
mobile numeric,
email varchar(255),
age numeric,
gender varchar (255),
cnic varchar(255) NOT NULL,
roles varchar(255),
login_id int NOT NULL,
PRIMARY KEY (employee_id, cnic),
FOREIGN KEY (login_id) references LOGIN_CREDENTIALS (login_id)
);