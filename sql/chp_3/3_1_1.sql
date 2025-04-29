INSERT INTO doctors (doctor_name, spec, cabinet_num) 
VALUES('Вахтин Петр Семенович', 'терапевт', 11);

INSERT INTO doctors (doctor_name, cabinet_num) 
VALUES('Мурзина Наталья Сергеевна', 16);

INSERT INTO doctors (doctor_name, spec, cabinet_num) 
VALUES('Жуков Василий Петрович', 'кардиолог', 21);

INSERT INTO med_area (area_address)
VALUES
('ул. Ленина'),
('ул. Рижская'),
('ул. Вавилова');

INSERT INTO med_area (area_num, area_address)
VALUES
(4, 'ул. Зеленая'),
(5, 'ул. Керамическая');

INSERT INTO patients (full_name, sex, birth_date, oms_num, card_num, area_num)
VALUES
('Быкова Светлана Ивановна', 'ж', '2001-12-16', 48324544531, 5623, 2),
('Иванов Сергей Эдуардович', 'м', '1965-08-15', 3224584531, 2345, 1),
('Скрябин Евгений Дмитриевич', 'м', '1985-11-25	', 45320544731, 2678, 3);

INSERT INTO talons (doctor_num, oms_num, visit_time)
VALUES
(1, 3224584531, '2025-11-30 15:16:00'),
(1, 78327844534, '2025-12-01 15:00:00'),
(3, 3224584531, '2025-12-01 13:00:00'),
(2, 78327844534, '2025-10-01 09:15:25'),
(1, 3224584531, '2025-11-05 15:00:00');