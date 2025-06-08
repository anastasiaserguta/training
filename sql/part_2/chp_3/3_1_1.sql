SELECT doctors.doctor_name, doctors.spec, talons.visit_time, talons.oms_num
FROM doctors 
JOIN talons
ON (doctors.doctor_num = talons.doctor_num);


SELECT patients.full_name, patients.oms_num, patients.area_num, med_area.area_address
FROM patients
JOIN doctors
ON (patients.area_num = med_area.area_num);


SELECT doc.doctor_name, doc.spec, talons.visit_time, pat.full_name, pat.birth_date
FROM doctors doc
JOIN talons
ON (doc.doctor_num = talons.doctor_num)
JOIN patients pat
ON (talons.oms_num = pat.oms_num);