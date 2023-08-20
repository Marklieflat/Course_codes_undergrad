proc sql;
	create table table1 as
	select distinct a.companyname, a.gvkey, a.permno, fyear, datadate, at, seq
	from HomeWork as a inner join comp.funda as b
	on a.gvkey=b.gvkey and indfmt='INDL' and datafmt='STD' 
	and popsrc='D' and consol='C' and fyear=2020;
quit;

proc sql;
	create table table2 as
	select distinct a.*, b.datadate as predatadate
	from table1 as a inner join comp.funda as b
	on a.gvkey=b.gvkey and indfmt='INDL' and datafmt='STD' 
	and popsrc='D' and consol='C' and b.fyear=2019;
quit;

proc sql;
	create table table3 as
	select distinct a.*, PERMCO, COMNAM, TICKER
	from table2 as a inner join crsp.msenames as b
	on a.permno=b.permno and NAMEDT<=datadate<=NAMEENDT;
quit;

proc sql;
	create table table4 as
	select distinct a.*, shrout*abs(prc)/1000 as mvalue
	from table3 as a inner join crsp.msf as b
	on a.permno=b.permno and datadate=intnx('month', date, 0, 'e');
quit;
	
proc sql;
	create table table5 as
	select distinct a.*, date, ret
	from table4 as a inner join crsp.msf as b
	on a.permno=b.permno and date>predatadate and date<=datadate; 
quit;

proc sql;
	create table table6 as
	select distinct a.*, sprtrn
	from table5 as a inner join crsp.msi as b
	on a.date=b.date; 
quit;

proc sql;
create table table7 as
select distinct companyname, COMNAM, TICKER, PERMNO, PERMCO, GVKEY, at, seq as bvalue, mvalue,  
exp(sum(log(1+ret)))-1 as cret, exp(sum(log(1+sprtrn)))-1 as sprtrn, count(date) as mcnt
from table6
group by companyname;
quit;