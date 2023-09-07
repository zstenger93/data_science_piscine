-- ALTER TABLE customers
-- ADD COLUMN category_id BIGINT,
-- ADD COLUMN category_code VARCHAR(255),
-- ADD COLUMN brand VARCHAR(255);

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


-- Create a temporary table to hold merged data
CREATE TEMP TABLE merged_items AS
SELECT 
    product_id,
    COALESCE(MAX(category_id), NULL) AS category_id,
    COALESCE(MAX(category_code), NULL) AS category_code,
    COALESCE(MAX(brand), NULL) AS brand
FROM items
GROUP BY product_id;

-- Truncate the original items table
TRUNCATE TABLE items;

-- Insert the merged data back into the items table
INSERT INTO items (product_id, category_id, category_code, brand)
SELECT * FROM merged_items;

UPDATE customers AS c
SET
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM (
    SELECT 
        product_id,
        COALESCE(MAX(category_id), NULL) AS category_id,
        COALESCE(MAX(category_code), NULL) AS category_code,
        COALESCE(MAX(brand), NULL) AS brand
    FROM items
    GROUP BY product_id
) AS i
WHERE c.product_id = i.product_id;
