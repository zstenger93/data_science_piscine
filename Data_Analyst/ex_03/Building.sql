SELECT user_id, COUNT(*)
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
