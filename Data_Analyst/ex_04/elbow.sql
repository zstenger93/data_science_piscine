SELECT user_id, COUNT(*) AS purchases
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
HAVING COUNT(*) < 30
ORDER BY purchases DESC;