-- -----------------------------------------------------
-- --------------- Solution for Q12 --------------------
-- -----------------------------------------------------
select EMPLOYEE_ID, SALARY from employees
where SALARY > (select AVG(SALARY) from employees
                group by DEPARTMENT_ID
                order by AVG(SALARY) DESC LIMIT 1)