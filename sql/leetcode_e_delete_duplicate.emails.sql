-- https://leetcode.com/submissions/detail/670494400/
-- Please write a DELETE statement and DO NOT write a SELECT statement.
-- Write your MySQL query statement below
DELETE dup_row
FROM Person dup_row
     , Person p
WHERE dup_row.Email = p.email
AND dup_row.id > p.id;


/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your T-SQL query statement below
 */
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(Id)
    FROM Person
    GROUP BY Email
);

/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 */
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(Id)
    FROM Person
    GROUP BY Email
);
