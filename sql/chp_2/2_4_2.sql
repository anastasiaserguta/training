CREATE TABLE patients (
    FULL_NAME VARCHAR(100),
    SEX CHAR(1),
    BIRTH_DATE DATE,
    OMS_NUM BIGINT PRIMARY KEY
);

ALTER TABLE
    patients CHANGE full_name full_name VARCHAR(100) NOT NULL;

ALTER TABLE
    patients CHANGE oms_num oms_num BIGINT UNIQUE;

ALTER TABLE
    patients ADD COLUMN area_num TINYINT;

ALTER TABLE patiens ADD FOREIGN KEY (area_num) REFERENCES med_area(area_num);

