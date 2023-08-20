-- -----------------------------------------------------
-- --------------- Solution for Q10 --------------------
-- -----------------------------------------------------
select DEPARTMENT_ID, AVG(SALARY), COUNT(*) from employees
group by DEPARTMENT_ID having count(DEPARTMENT_ID) >= 10