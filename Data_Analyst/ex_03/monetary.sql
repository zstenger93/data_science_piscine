SELECT user_id, SUM(price) AS purchases
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
HAVING SUM(price) < 200
ORDER BY purchases;
