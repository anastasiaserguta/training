SELECT * FROM doctors;

SELECT doctor_num, doctor_name FROM doctors;

SELECT full_name, birth_date FROM patients;

SELECT DISTINCT visit_time FROM talons;

SELECT DISTINCT doctor_num, visit_time FROM talons;

SELECT * FROM doctors WHERE (doctor_num = 1 OR doctor_num = 2) AND NOT spec = 'терапевт';

