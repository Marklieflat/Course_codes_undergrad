-- -----------------------------------------------------
-- --------------- Solution for Q16 --------------------
-- -----------------------------------------------------
select departments.DEPARTMENT_ID, DEPARTMENT_NAME, FIRST_NAME
from departments inner join employees on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID
where departments.MANAGER_ID = employees.EMPLOYEE_ID
order by DEPARTMENT_ID