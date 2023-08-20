-- -----------------------------------------------------
-- --------------- Solution for Q11 --------------------
-- -----------------------------------------------------
select FIRST_NAME, LAST_NAME from employees
where MANAGER_ID in (select MANAGER_ID from employees
                    where DEPARTMENT_ID in (select DEPARTMENT_ID from departments
                                            where LOCATION_ID in (select LOCATION_ID from locations where COUNTRY_ID = 'US')))