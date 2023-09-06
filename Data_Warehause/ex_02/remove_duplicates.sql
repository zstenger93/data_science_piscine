CREATE TEMPORARY TABLE temp_customers AS SELECT DISTINCT * FROM customers;
TRUNCATE customers;
INSERT INTO customers SELECT * FROM temp_customers;
