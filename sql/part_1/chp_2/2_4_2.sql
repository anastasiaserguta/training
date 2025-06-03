CREATE TABLE patients (
    full_name VARCHAR(100),
    sex CHAR(1),
    birth_date DATE,
    oms_num BIGINT PRIMARY KEY
);

ALTER TABLE
    patients CHANGE full_name full_name VARCHAR(100) NOT NULL;

ALTER TABLE
    patients CHANGE oms_num oms_num BIGINT UNIQUE;

ALTER TABLE
    patients ADD COLUMN area_num TINYINT;

ALTER TABLE patiens ADD FOREIGN KEY (area_num) REFERENCES med_area(area_num);

