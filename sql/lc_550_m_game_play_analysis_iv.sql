SELECT ROUND(SUM(
    CASE WHEN days_between_login = 1
    THEN 1.0
    ELSE 0.0
    END
)  / COUNT(DISTINCT player_id), 2) AS fraction
FROM(
SELECT DISTINCT player_id
,DATEDIFF(event_date,
          FIRST_VALUE(event_date)
          OVER(PARTITION BY player_id ORDER BY event_date)) AS days_between_login
FROM ACTIVITY
    ) A

