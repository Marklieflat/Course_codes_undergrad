-- -----------------------------------------------------
-- ---------------- Solution for Q9 --------------------
-- -----------------------------------------------------
select distinct JOB_ID, COUNT(*) from employees
group by JOB_ID
order by JOB_ID