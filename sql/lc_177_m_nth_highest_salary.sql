CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN(
      SELECT IFNULL(
          (
              SELECT DISTINCT SALARY
              FROM EMPLOYEE
              ORDER BY SALARY DESC
              LIMIT M, 1
          ),
          NULL
      )
      AS 'SecondHighestSalary'
  );
END

