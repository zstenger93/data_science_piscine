SELECT user_id, AVG(price) AS avg_cart_price
FROM customers
WHERE event_type = 'cart'
GROUP BY user_id
HAVING AVG(price) BETWEEN 26 AND 43;
