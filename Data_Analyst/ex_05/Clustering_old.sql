WITH time_groups AS (
    SELECT
        user_id,
		event_type,
        CASE
            WHEN EXTRACT(MONTH FROM MAX(event_time)) - EXTRACT(MONTH FROM MIN(event_time)) < 1 THEN 1
            WHEN EXTRACT(MONTH FROM MAX(event_time)) - EXTRACT(MONTH FROM MIN(event_time)) < 2 THEN 2
            WHEN EXTRACT(MONTH FROM MAX(event_time)) - EXTRACT(MONTH FROM MIN(event_time)) < 3 THEN 3
            ELSE 4
        END AS time_group
    FROM
        customers
    GROUP BY
        user_id, event_type
),
event_groups AS (
    SELECT
        user_id,
        event_type,
        CASE
            WHEN COUNT(DISTINCT event_type) = 1 AND MIN(event_type) = 'view' THEN 4
            ELSE time_group
        END AS event_group
    FROM
        time_groups
    GROUP BY
        user_id, event_type, time_group
)
SELECT
    event_group AS time_group,
    COUNT(user_id) AS user_count
FROM
    event_groups
GROUP BY
    event_group
ORDER BY
    user_count DESC, event_group;