-- -----------------------------------------------------
-- ---------------- Solution for Q6 --------------------
-- -----------------------------------------------------
select EMPLOYEE_ID
from employees
where EMPLOYEE_ID in (select MANAGER_ID from departments) and
      EMPLOYEE_ID not in (select MANAGER_ID from employees)