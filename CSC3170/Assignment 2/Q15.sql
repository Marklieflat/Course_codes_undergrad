select d.DEPARTMENT_ID as 'DEPARTMENT NAME', count(e.EMPLOYEE_ID) as 'Number of Employees'
from employees as e
join departments as d
on (e.DEPARTMENT_ID = d.DEPARTMENT_ID)
group by d.DEPARTMENT_ID;