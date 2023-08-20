select EMPLOYEE_ID, PHONE_NUMBER
from employees
where DEPARTMENT_ID in (20,100)
order by DEPARTMENT_ID desc;