SELECT DISTINCT
    CASE
        WHEN purchase_months = 5 THEN 'loyal platinum'
        WHEN purchase_months = 4 THEN 'loyal gold'
        WHEN purchase_months = 3 THEN 'loyal silver'
        WHEN purchase_months = 2 THEN 'new customer'
        WHEN purchase_months = 1 AND NOT (purchase_month = 1 OR purchase_month = 2) THEN 'inactive'
        WHEN purchase_months = 1 THEN 'new customer'
    END AS purchase_months_category,
    COUNT(DISTINCT user_id) AS customer_count
FROM (
    SELECT
        user_id,
        COUNT(DISTINCT EXTRACT(MONTH FROM event_time)) AS purchase_months,
        EXTRACT(MONTH FROM MIN(event_time)) AS purchase_month
    FROM
        customers
    WHERE
        event_type = 'purchase'
    GROUP BY
        user_id
) AS purchase_counts
GROUP BY
    purchase_months_category
ORDER BY
	customer_count;