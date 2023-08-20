select JOB_ID , count(EMPLOYEE_ID)
from employees
group by JOB_ID;