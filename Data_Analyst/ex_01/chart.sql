SELECT event_type, COUNT(*) as event_count
FROM customers
GROUP BY event_type
ORDER BY event_count DESC;