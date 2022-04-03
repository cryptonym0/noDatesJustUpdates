-- https://leetcode.com/submissions/detail/670243329/
-- Write your MySQL query statement below
SELECT request_at as "Day"
 ,ROUND(SUM(IF(status != "completed", 1, 0))/
     COUNT(status), 2) as "Cancellation Rate"
FROM TRIPS T
WHERE  request_at BETWEEN "2013-10-01" AND "2013-10-03"
AND CLIENT_ID NOT IN (SELECT USERS_ID FROM USERS WHERE BANNED = "Yes")
AND DRIVER_ID NOT IN (SELECT USERS_ID FROM USERS WHERE BANNED = "Yes")
GROUP BY REQUEST_AT
