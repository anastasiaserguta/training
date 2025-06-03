SELECT spec, COUNT(*) AS count_docs FROM doctors GROUP BY spec;

SELECT oms_num, SUM(visit_amount) AS sum_visit FROM talons GROUP BY oms_num;

SELECT sex, count(sex) AS count_pacient FROM patients GROUP BY sex;

SELECT sex, COUNT(birth_date) AS count_pacient FROM patients WHERE YEAR(birth_date) > '1970' GROUP BY(sex);

SELECT doctor_num FROM talons GROUP BY doctor_num HAVING COUNT(visit_time) > 1;