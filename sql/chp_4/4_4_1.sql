SELECT MAX(cabinet_num) AS max_cabinet FROM doctors; 

SELECT COUNT(*) AS count_docs FROM doctors;

SELECT SUM(visit_amount) AS sum_amount_2023 FROM talons WHERE YEAR(visit_time) = 2023;