-- NOT SUPPORTED IN MYSQL!

SELECT id, name  FROM product
INTERSECT
SELECT id, descr FROM description;