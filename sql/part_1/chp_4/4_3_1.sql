SELECT spec FROM doctors ORDER BY spec;

SELECT * FROM patients ORDER BY birth_date;

SELECT * FROM patients ORDER BY area_num, birth_date DESC;

SELECT * FROM doctors ORDER BY doctor_num LIMIT 2;

SELECT * FROM patients ORDER BY birth_date DESC LIMIT 3;