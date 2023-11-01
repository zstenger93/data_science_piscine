SELECT DISTINCT
    CASE
        WHEN purchase_months = 5 THEN 'loyal platinum'
        WHEN purchase_months = 4 THEN 'loyal gold'
        WHEN purchase_months = 3 THEN 'loyal silver'
        WHEN purchase_months = 2 THEN 'new customer'
        WHEN purchase_months = 1 AND NOT (purchase_month = 1 OR purchase_month = 2) THEN 'inactive'
        WHEN purchase_months = 1 THEN 'new customer'
    END AS purchase_months_category,
    COUNT(DISTINCT user_id) AS customer_count,
    AVG(purchase_months) AS avg_purchase_months,
    AVG(purchase_frequency) AS avg_purchase_frequency
FROM (
    SELECT 
        user_id,
        COUNT(*) AS purchase_months,
        EXTRACT(MONTH FROM MIN(event_time)) AS purchase_month,
        COUNT(*) * 1.0 / COUNT(DISTINCT user_id) AS purchase_frequency
    FROM 
        customers
    WHERE 
        event_type = 'purchase'
    GROUP BY 
        user_id
) AS purchase_counts
GROUP BY 
    purchase_months_category
HAVING 
    AVG(purchase_months) BETWEEN 0 AND 6
ORDER BY 
    customer_count;
