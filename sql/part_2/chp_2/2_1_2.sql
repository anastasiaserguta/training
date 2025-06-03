SELECT doctor_name AS fio, 'Врач' AS doc_pat FROM doctors
UNION
SELECT full_name, 'Пациент' AS doc_pat FROM patients ORDER BY 1 ASC;

SELECT doctor_name AS fio, '0' AS oms_num FROM doctors
UNION
SELECT full_name, oms_num FROM patients ORDER BY 2 DESC;

