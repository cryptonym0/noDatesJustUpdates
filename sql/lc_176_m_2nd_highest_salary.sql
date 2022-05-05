# Write your MySQL query statement below
SELECT
    IFNULL(
        (
            SELECT DISTINCT SALARY
            FROM EMPLOYEE
            ORDER BY SALARY DESC
            LIMIT 1,1
        ),
        NULL
    )
    AS 'SecondHighestSalary'

