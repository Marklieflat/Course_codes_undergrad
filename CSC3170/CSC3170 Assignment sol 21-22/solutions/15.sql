-- -----------------------------------------------------
-- --------------- Solution for Q15 --------------------
-- -----------------------------------------------------
select DEPARTMENT_ID as 'Department Name', count(EMPLOYEE_ID) as 'Number of Employees' from employees
where DEPARTMENT_ID > 0
group by DEPARTMENT_ID