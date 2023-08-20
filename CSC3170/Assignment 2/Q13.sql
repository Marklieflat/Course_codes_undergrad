select EMPLOYEE_ID, SALARY
from employees E1
where 4 = (select count(distinct SALARY)
			from employees E2
            where E2.SALARY <= E1.SALARY)
