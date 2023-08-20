select EMPLOYEE_ID, SALARY
from employees
where SALARY > all(select avg(SALARY) 
				from employees
                group by DEPARTMENT_ID);