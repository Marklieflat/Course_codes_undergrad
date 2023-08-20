select d.DEPARTMENT_ID, d.DEPARTMENT_NAME, e.FIRST_NAME
from departments d
join employees e
on (d.MANAGER_ID = e.EMPLOYEE_ID)