# Write your MySQL query statement below
SELECT
    install_dt
    ,COUNT(DISTINCT player_id) AS installs
    ,ROUND(SUM(
    CASE WHEN days_between_login = 1
    THEN 1.0
    ELSE 0.0
    END
) / COUNT(DISTINCT player_id),2) AS Day1_retention
FROM(
SELECT DISTINCT player_id
    ,FIRST_VALUE(event_date)
          OVER(PARTITION BY player_id ORDER BY event_date) AS install_dt
    ,DATEDIFF(event_date,
          FIRST_VALUE(event_date)
          OVER(PARTITION BY player_id ORDER BY event_date)) AS days_between_login
FROM ACTIVITY
    ) A
    GROUP BY install_dt

