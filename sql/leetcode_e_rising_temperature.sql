-- https://leetcode.com/submissions/detail/670503950/
--  Write your MySQL query statement below
SELECT W.id
FROM Weather W
    ,Weather P
WHERE DATEDIFF(W.recordDate, P.recordDate) = 1
AND W.temperature > P.temperature;

/* Write your T-SQL query statement below */
SELECT W.id
FROM Weather W
    ,Weather P
WHERE DATEDIFF(d, W.recordDate, P.recordDate) = -1
AND W.temperature > P.temperature;

/* Write your PL/SQL query statement below */
SELECT W.id
FROM Weather W
JOIN Weather P
ON P.recordDate = W.recordDate - 1
AND W.temperature > P.temperature;
