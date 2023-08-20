%wrds(s=1);
 
libname sav "~/fin3380/";

***********************;
* ADD FUTURE EARNINGS *;
***********************;

proc sql;
create table addfutureyear as
select a.*, b.ib as ib_p1, b.at as at_p1
from sav.Compustat1980to2021 a
inner join sav.Compustat1980to2021 b
on a.gvkey=b.gvkey and b.fyear=a.fyear+1;
quit;

************;
* ADD IBES *;
************;

proc sql;
create table addibes as
select a.*, b.actual, b.consensus, b.ibesshrout
from addfutureyear a
inner join sav.ibes1993to2021 b
on a.permno=b.permno 
and a.datadate=b.datadate;
quit;

proc sql;
create table addibesfut as
select a.*, b.actual as actual_p1, b.consensus as consensus_p1, b.ibesshrout as ibesshrout_p1
from addibes a
inner join sav.ibes1993to2021 b
on a.permno=b.permno 
and year(a.datadate)+1=year(b.datadate);
quit;

/*You can use SQL and its coalesce function for the same purpose*/
data varlist; set addibesfut; where at>0;

earn_p1=ib_p1/at_p1;
earn=ib/at;
AFE_p1=((actual_p1-consensus_p1)*ibesshrout_p1)/at_p1;
AFE=((actual-consensus)*ibesshrout)/at;

if XRD=. then XRD=0;
if CHE=. then CHE=0;
if IVAO=. then IVAO=0;
if DLTT=. then DLTT=0;
if DLC=. then DLC=0;
if CEQ=. then CEQ=0;
if PSTK=. then PSTK=0;
if MIB=. then MIB=0;
if SPI=. then SPI=0;

Research=XRD/AT;
SpecialItems=SPI/AT;
NOA = (AT - CHE - IVAO) - (AT - (DLTT+DLC) - (CEQ+PSTK) - MIB); 
ATO = SALE / NOA;
run;

proc means data=varlist mean std p1 p25 p50 p75 p99;
var earn afe research ato specialitems;
quit;

*****************;
* Winsorization *;
*****************;

data varlist; set varlist;
if ATO>21.3838515 then ATO=21.3838515; if .<ATO<-17.9972798 then ATO=-17.9972798;
run;

data sav.groupassign3; 
set varlist;
if nmiss(earn_p1, earn, afe_p1, afe, research, specialitems, ato)=0;
if fyear>1991; *only 4 firms made sample in 1991;
run;

***********;
* TABLE 1 *;
***********;

proc freq data=sav.groupassign3;
tables fyear;
quit;

***********;
* TABLE 2 *;
***********;

proc means data=sav.groupassign3 mean std p1 p25 p50 p75 p99;
var earn afe research ato specialitems;
quit;

***********;
* TABLE 3 *;
***********;

proc reg data=sav.groupassign3;
model earn_p1 = earn ;
quit;

proc reg data=sav.groupassign3;
model earn_p1 = earn research ato specialitems;
quit;

proc reg data=sav.groupassign3;
model afe_p1 = afe;
quit;

proc reg data=sav.groupassign3;
model afe_p1 = afe research ato specialitems;
quit;

****************************;
* OUT OF SAMPLE PREDICTION *;
****************************;
data groupassign3; set sav.groupassign3;
keep earn_p1 earn AFE_p1 AFE research ato specialitems noa fyear permno gvkey actual consensus
eps:;
run;

proc corr data=groupassign3 spearman;
var actual consensus;
with eps:;
run;

proc reg data=groupassign3 outest=params noprint;
model earn_p1 = earn research ato specialitems;
where fyear<=2017; 
quit;

proc sql;
create table outofsample as 
select distinct a.permno, a.gvkey, a.fyear, a.earn_p1, afe_p1,
a.earn*b.earn+a.research*b.research+a.ato*b.ato+
a.specialitems*b.specialitems+Intercept as predicted_earn
from groupassign3 as a inner join params as b
on a.fyear=2018;
quit;

data outofsample; set outofsample; 
predicted_earn2019=predicted_earn;
modelABFE=abs(earn_p1-predicted_earn2019);
modelMSFE=(earn_p1-predicted_earn2019)**2;
analystABFE=abs(afe_p1);
analystMSFE=afe_p1**2;
run;

proc means data=outofsample mean;
var analystABFE analystMSFE modelABFE modelMSFE;
quit; 

