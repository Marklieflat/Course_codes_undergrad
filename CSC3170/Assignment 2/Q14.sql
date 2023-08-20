select e.EMPLOYEE_ID, e.JOB_ID, d.DEPARTMENT_ID, d.DEPARTMENT_NAME
from employees e join departments d
on (e.DEPARTMENT_ID = d.DEPARTMENT_ID)
join locations l on (d.LOCATION_ID = l.LOCATION_ID)
where l.CITY = 'Seattle';