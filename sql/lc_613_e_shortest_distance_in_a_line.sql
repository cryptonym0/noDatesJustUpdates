# Write your MySQL query statement below
SELECT MIN(ABS(P1.X - P2.X)) AS shortest
FROM POINT P1
JOIN POINT P2
ON P1.X != P2.X