ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code VARCHAR(255),
ADD COLUMN brand VARCHAR(255);

UPDATE customers AS c
SET
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM items AS i
WHERE c.product_id = i.product_id;
