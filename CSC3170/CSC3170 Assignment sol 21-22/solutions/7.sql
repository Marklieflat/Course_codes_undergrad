-- -----------------------------------------------------
-- ---------------- Solution for Q7 --------------------
-- -----------------------------------------------------
select EMPLOYEE_ID, PHONE_NUMBER
from employees
where DEPARTMENT_ID = '20' or DEPARTMENT_ID = '100'
order by DEPARTMENT_ID desc