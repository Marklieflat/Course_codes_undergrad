/**Direct to your local or remote library**/

libname sav "<your folder with project files>"; 

%let sig=Oprof;

/*Keep the stocks with non-empty signals at each month*/
proc sql;
create table sign as
select distinct permno, intnx('month',date,0,'e') as date format=date9., mcap, ret, &sig
from sav.project_1
where &sig>. /*and year(date)>=1986*/
order by date, &sig;
quit;

/*Calculate monthly ranking for portfolio rebalance every month*/
proc univariate data=sign noprint;
	by date;
	var &sig;
	output out=sign_breaks 
			pctlpre=&sig pctlpts=20 40 60 80;
run;

/*Report the distribution in Table 1*/
proc means data=sign mean p25 median p75 std;
var &sig;
run;

/*Categorize stocks into 5 groups */
proc sql;
create table sign_pct as
select distinct a.*, case when &sig.<&sig.20 then 'P1'
when &sig.20<=&sig.<&sig.40 then 'P2'
when &sig.40<=&sig.<&sig.60 then 'P3'
when &sig.60<=&sig.<&sig.80 then 'P4'
else 'P5' end as port
from sign as a inner join sign_breaks as b
on a.date=b.date;
quit;

/*Calculate monthly value weighted return of each portfolio by provided market cap of each stock from previous month end*/
proc sql;
create table port_ret as
select distinct port, date, sum(mcap*ret)/sum(mcap) as ret, count(distinct permno) as cnt
from sign_pct
group by port, date;
quit;

/*Prepare cumulative returns for Figure I -1*/
data port_cret; set port_ret; by port;
	cret+cret*ret;
	if first.port then cret=1+ret;
run;

proc sort data=port_cret; by date; run;

/*Prepare cumulative returns for Figure I -2*/
proc transpose data=port_cret out=port_cret; 
by date;
var cret;
id port;
run;

data port_cret; set port_cret;
	p1=p1-1; p2=p2-1; p3=p3-1; p4=p4-1; p5=p5-1;
run;

/*Output cumulative returns for Figure I*/
PROC EXPORT DATA= rWORK.Port_cret 
            OUTFILE= "<your folder>...cret.xlsx" 
            DBMS=EXCEL REPLACE;
     SHEET="cret"; 
RUN;

proc sort data=port_ret; by date; run;

/*Output cumulative returns for Table 2*/
proc transpose data=port_ret out=port_cnt(where=(month(date)=12)); 
by date;
var cnt;
id port;
run;

PROC EXPORT DATA= WORK.Port_cnt 
            OUTFILE= "<your folder>...cnt.xlsx" 
            DBMS=EXCEL REPLACE;
     SHEET="cnt"; 
RUN;


/*Prepair Regression Data for Table 3*/
proc sql;
create table port_ret_reg as 
select distinct a.*, mktrf, hml, smb, ret-rf as retrf, umd
from port_ret as a inner join ff.Factors_monthly as b
on intnx('month',a.date,0,'e')=intnx('month',b.date,0,'e');
quit;

proc reg data=port_ret_reg outest=est1 noprint ; 
by port;
model retrf=mktrf;
run;

/*Output CAPM Results*/
PROC EXPORT DATA= WORK.est1
            OUTFILE= "<your folder>...est1.xlsx" 
            DBMS=EXCEL REPLACE;
     SHEET="reg"; 
RUN;

proc reg data=port_ret_reg outest=est2 ; 
by port;
model retrf=mktrf hml smb;
run;

/*Output FF3 Results*/
PROC EXPORT DATA= WORK.est2
            OUTFILE= "<your folder>...est2.xlsx" 
            DBMS=EXCEL REPLACE;
     SHEET="reg"; 
RUN;

/*Generate Max Return Factors*/
proc sql;
create table factor as
select distinct a.date, b.ret-a.ret as factor
from Port_ret(where=(port='P1')) as a inner join Port_ret(where=(port='P5')) as b
on a.date=b.date;
quit;

/*Construct data for Figure II*/
data cfactor; set factor; 
	cfactor+cfactor*factor;
	if _N_=1 then cfactor=1+factor;
run;

/*Output data for Figure II*/
PROC EXPORT DATA= WORK.cfactor
            OUTFILE= "<your folder>...cfactor.xlsx" 
            DBMS=EXCEL REPLACE;
     SHEET="cnt"; 
RUN;


proc sql;
create table port_ret_reg_factor as 
select distinct a.*, factor
from port_ret_reg as a inner join factor as b
on intnx('month',a.date,0,'e')=intnx('month',b.date,0,'e');
quit;


proc reg data=port_ret_reg_factor outest=est3 noprint ; 
by port;
model retrf=mktrf hml smb factor;
run;
