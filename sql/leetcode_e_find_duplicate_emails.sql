-- https://leetcode.com/submissions/detail/670489687/
-- Write your MySQL query statement below
SELECT email as "Email"
FROM PERSON
GROUP BY email
HAVING COUNT(1)>1;

/* Write your T-SQL query statement below */
SELECT email as "Email"
FROM PERSON
GROUP BY email
HAVING COUNT(1)>1;

/* Write your PL/SQL query statement below */
SELECT email as "Email"
FROM PERSON
GROUP BY email
HAVING COUNT(1)>1;