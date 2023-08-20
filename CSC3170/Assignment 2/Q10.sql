select DEPARTMENT_ID, avg(SALARY), count(EMPLOYEE_ID)
from employees
group by DEPARTMENT_ID
having count(EMPLOYEE_ID) > 10;