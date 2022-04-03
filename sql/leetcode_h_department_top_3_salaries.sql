-- https://leetcode.com/submissions/detail/670235905/
-- Write your MySQL query statement below
SELECT T3S.Department
    ,T3S.Employee
    ,T3S.Salary
    FROM (
        SELECT D.NAME AS 'Department'
            ,E.NAME AS 'Employee'
            ,E.salary AS 'Salary'
            ,DENSE_RANK() OVER (
                PARTITION BY D.NAME
                ORDER BY E.salary DESC
            ) SAL_RANK
        FROM EMPLOYEE E
        LEFT JOIN DEPARTMENT D
        ON E.DEPARTMENTID = D.ID
    ) T3S
    WHERE SAL_RANK < 4

