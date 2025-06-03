CREATE TABLE product
(
    id INT,
    name VARCHAR(25)
);

INSERT INTO product
(id, name)
values
(1, 'Карандаш'),
(3, 'Ручка'),
(4, 'Пластилин'),
(5, 'Клей');

CREATE TABLE description
(
    id INT,
    descr VARCHAR(50)
);

INSERT INTO description
(id, descr)
values
(1, 'Черный карандаш'),
(3, 'Гелевая ручка'),
(5, 'ПВА'),
(7, 'Кисть средняя');

