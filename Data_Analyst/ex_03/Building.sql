SELECT event_time, user_id, event_type, price
FROM customers
WHERE event_type = 'purchase';