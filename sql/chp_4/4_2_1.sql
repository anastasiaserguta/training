SELECT full_name, oms_num, YEAR(CURDATE()) - YEAR(birth_date) AS age FROM patients;

SELECT doctor_num, doctor_name, IF(spec IS NULL, 'Не заполнена', spec) AS spec FROM doctors;

SELECT UPPER(doctor_name) AS up_full_name FROM doctors;

UPDATE talons SET visit_amount = visit_amount * 0.9 WHERE doctor_num = 3;