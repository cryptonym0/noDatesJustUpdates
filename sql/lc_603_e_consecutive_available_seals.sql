# Write your MySQL query statement below
SELECT DISTINCT C2.seat_id
FROM Cinema C1
LEFT JOIN Cinema C2
ON ABS(C1.seat_id - C2.seat_id) = 1
WHERE C1.free = true
AND C2.free = true
ORDER BY C2.seat_id ASC
;
