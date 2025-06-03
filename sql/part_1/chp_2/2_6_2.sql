CREATE TABLE talons (
    doctor_num INT,
    oms_num BIGINT,
    talon_date DATETIME,
    FOREIGN KEY (doctor_num) REFERENCES doctors(doctor_num),
    FOREIGN KEY (oms_num) REFERENCES patients(oms_num)
);

