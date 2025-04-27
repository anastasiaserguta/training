CREATE TABLE doctors (
    doctor_num INT AUTO_INCREMENT,
    doctor_name VARCHAR(250) NOT NULL,
    spec VARCHAR(100),
    cabinet_num TINYINT,
    PRIMARY KEY(doctor_num)
);