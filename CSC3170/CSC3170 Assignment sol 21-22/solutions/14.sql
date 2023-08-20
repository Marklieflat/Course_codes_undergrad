-- -----------------------------------------------------
-- --------------- Solution for Q14 --------------------
-- -----------------------------------------------------
select EMPLOYEE_ID, JOB_ID, employees.DEPARTMENT_ID, DEPARTMENT_NAME 
from employees inner JOIN departments on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID
where departments.DEPARTMENT_ID in (select departments.DEPARTMENT_ID from departments
                                    where LOCATION_ID in (select LOCATION_ID from locations where city = 'Seattle'))
order by DEPARTMENT_ID