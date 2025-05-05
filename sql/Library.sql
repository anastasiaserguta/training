CREATE DATABASE library;

CREATE TABLE readers ( 
	reader_num INT AUTO_INCREMENT PRIMARY KEY,
    reader_name VARCHAR(100),
    reader_adress VARCHAR(1000),
    reader_phone VARCHAR(15) NOT NULL
);

CREATE TABLE books (
	book_num INT AUTO_INCREMENT PRIMARY KEY,
    book_author VARCHAR(100),
    book_name VARCHAR(1000),
    book_count INT NOT NULL DEFAULT(0)
);

CREATE TABLE books_in_use (
	reader_num INT,
    book_num INT,
    issue_date DATE,
    return_date DATE,
    return_period TINYINT NOT NULL DEFAULT(14),
    fine_amount DECIMAL(10,2) NOT NULL DEFAULT 0,
    PRIMARY KEY (reader_num, book_num, issue_date),
    FOREIGN KEY (book_num) REFERENCES books(book_num),
    FOREIGN KEY (reader_num) REFERENCES readers(reader_num)
);

INSERT INTO readers (reader_name, reader_adress, reader_phone)
VALUES
	('Сидоров', 'ул. Ленина, 5а', '4424556'),
	('Ванюшкин', 'ул. Космонавтов, д. 31, кв. 143', '4545222'),
	('Дроздов', 'ул. Ленина, д. 3, кв. 13', '8955454'),
	('Голубева', 'ул. Тимирязева, д. 35, кв. 18', '5454555'),
	('Шишкин', 'ул. Революции, д. 16/7, кв. 45', '454564564'),
	('Книголюбова', 'ул. Пушкина, д. 38', '54664545'),readers
	('Петров', 'ул. Пушкина, д. 31, кв. 16', '6115646'),
	('Паринова', null, '46488484'),
	('Птичкина', 'ул. Зеленая, д. 3/7', '65545445'),
	('Дроздов', 'ул. Конструкторов, д. 89, кв. 14', '546544');

INSERT INTO books (book_author, book_name, book_count)
VALUES
	('Толстой', 'Война и мир', 15),
	('Достоевский', 'Идиот', 13),
	('Пушкин', 'Евгений Онегин', 18),
	('Пушкин', 'Руслан и Людмила', 5),
	('Пушкин', 'Медный всадник', 11),
	('Барто', 'Стихи детям', 1),
	('Чехов', 'Вишневый сад', 8),
	('Чехов', 'Дядя Ваня', 7),
	('Тургенев', 'Отцы и дети', 13),
	('Тургенев', 'Муму', 4);
    
INSERT INTO books_in_use (reader_num, book_num, issue_date, return_date)
VALUES
	(1, 1, '2023-09-15', '2023-10-17'),
	(1, 8, '2023-10-17', null),
	(2, 1, '2023-10-04', '2023-10-16'),
	(3, 2, '2023-09-11', '2023-09-30'),
	(3, 4, '2023-09-11', '2023-09-30'),
	(3, 5, '2023-09-11', '2023-09-30'),
	(4, 1, '2023-09-28', '2023-10-05'),
	(4, 3, '2023-09-28', '2023-10-05'),
	(4, 8, '2023-10-05', '2023-10-31'),
	(5, 6, '2023-09-14', '2023-10-14'),
	(6, 1, '2023-09-09', '2023-09-20'),
	(6, 1, '2023-09-20', '2023-10-01'),
	(7, 1, '2023-09-13', '2023-09-21'),
	(7, 7, '2023-09-21', '2023-10-20'),
	(8, 7, '2023-09-11', null);
    
UPDATE books_in_use 
SET fine_amount = (DATEDIFF(return_date, issue_date) - return_period) * 8.45
WHERE return_date IS NOT NULL AND DATEDIFF(return_date, issue_date)>return_period;

SELECT * FROM readers;

SELECT reader_name, reader_adress FROM readers;

SELECT * FROM books GROUP BY book_num LIMIT 3;

SELECT book_author, CONCAT(book_name, ' (', book_count, ')') AS book_name FROM books;

SELECT ROUND(AVG(fine_amount), 2) AS avg_fine_amount FROM books_in_use;

SELECT MIN(fine_amount) AS min_fine_amount FROM books_in_use WHERE fine_amount > 0;

SELECT MAX(fine_amount) AS max_fine_amount FROM books_in_use;

SELECT COUNT(book_name) AS books_count FROM books;

SELECT * FROM books WHERE book_count > 10;

SELECT * FROM books WHERE book_count BETWEEN 10 AND 20;

SELECT * FROM readers WHERE reader_name LIKE('Паринова%') OR reader_name LIKE('Шишкин%') OR reader_name LIKE('Птичкина%');
SELECT * FROM readers WHERE reader_name IN ('Паринова', 'Шишкин', 'Птичкина');

SELECT * FROM books WHERE book_name LIKE('С%') OR book_name LIKE('О%') OR book_name LIKE('В%');

SELECT * FROM readers WHERE reader_adress IS NULL;

SELECT * FROM readers WHERE reader_adress IS NOT NULL;

SELECT book_author, COUNT(book_name) AS books_count FROM books GROUP BY book_author;

SELECT book_author, COUNT(book_name) AS books_count FROM books WHERE book_author IN ('Тургенев', 'Чехов') GROUP BY book_author;

SELECT book_author FROM books GROUP BY book_author HAVING COUNT(book_name) = 1;

SELECT reader_name FROM readers ORDER BY reader_name;

SELECT * FROM books ORDER BY book_count DESC;

SELECT * FROM books ORDER BY book_count DESC LIMIT 3;




