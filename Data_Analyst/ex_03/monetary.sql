SELECT user_id, SUM(price)
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
HAVING SUM(price) < 225;
