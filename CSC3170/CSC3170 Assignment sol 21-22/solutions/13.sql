-- -----------------------------------------------------
-- --------------- Solution for Q13 --------------------
-- -----------------------------------------------------
select EMPLOYEE_ID, SALARY from employees
where SALARY = (select SALARY from employees
                group by SALARY
                order by SALARY LIMIT 3,1)