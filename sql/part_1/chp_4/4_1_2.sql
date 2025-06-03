SELECT * FROM patients WHERE birth_date >= '1980-01-01';

SELECT * FROM doctors WHERE cabinet_num BETWEEN 10 AND 20;

SELECT doctor_name FROM doctors WHERE spec IN ('терапевт', 'кардиолог', 'окулист');

SELECT * FROM doctors WHERE doctor_name LIKE 'A%' OR doctor_name LIKE 'В%' OR doctor_name LIKE 'М%';

SELECT * FROM doctors WHERE spec IS NULL;