SELECT
    EXTRACT(MONTH FROM event_time) AS month,
    EXTRACT(DAY FROM event_time) AS day,
    user_id
FROM
    customers
WHERE
    event_type = 'purchase';
