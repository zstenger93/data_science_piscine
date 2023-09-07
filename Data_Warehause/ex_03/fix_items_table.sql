CREATE TABLE items_nodup AS
SELECT
    product_id,
    COALESCE(MAX(category_id), NULL) AS category_id,
    COALESCE(MAX(category_code), NULL) AS category_code,
    COALESCE(MAX(brand), NULL) AS brand
FROM
    items
GROUP BY
    product_id;