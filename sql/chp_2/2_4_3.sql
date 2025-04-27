CREATE TABLE med_area (
    AREA_NUM TINYINT,
    AREA_ADDRESS VARCHAR(1000)
);

ALTER TABLE med_area CHANGE area_num area_num TINYINT NOT NULL;

ALTER TABLE med_area ADD PRIMARY KEY (area_num, area_address);
