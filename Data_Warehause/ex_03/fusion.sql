ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code VARCHAR(255),
ADD COLUMN brand VARCHAR(255);

-- select * from customers as c
-- INNER JOIN 
-- (select 
-- product_id, COALESCE(MIN(category_id), NULL) as category_id,
-- COALESCE(MIN(category_code), NULL) as category_code,
-- COALESCE(MIN(brand), NULL) as brand
-- from items
-- GROUP by product_id )
-- as i
-- ON c.product_id=i.product_id


UPDATE customers c
SET
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM items_nodup i
WHERE c.product_id = i.product_id;