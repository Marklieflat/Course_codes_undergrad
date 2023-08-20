/*This code is a short sample code to regenerate the 

Price and Volume Effects Associated with Changes in the S&P 500 List: New
Evidence for the Existence of Price Pressures

Lawrence Harris; Eitan Gurel

The Journal of Finance, Vol. 41, No. 4. (Sep., 1986), pp. 815-829.
*/
libname sav '/home/u61728407/sasuser.v94/Mark/Proj2';

/* estper:	Length of the estimation period in trading days over which    
                 the risk model is estimated                                   */
/* start:		Beginning of the event window (wtr to the event date,e.g. -2)  */
/* end:			End of the event window (relative to the event date, e.g., +1) */
/* gap:    		Length of pre-event window,i.e., number of trading days b/w    
                the end of estimation period and the start of the event window */ 


%macro date_creator(estper=200, start=-30, end=60, gap=0);
	%let evtwin=%eval(&end-&start+1); /*length of event window in trading days */
	data caldates;
	merge sav.dsi(keep=date rename=(date=estper_beg))
	sav.dsi(keep=date firstobs=&estper rename=(date=estper_end))
	sav.dsi(keep=date firstobs=%eval(&estper+&gap+1) rename=(date=evtwin_beg))
	sav.dsi(keep=date firstobs=%eval(&estper+&gap-&start+1) rename=(date=evtdate))
	sav.dsi(keep=date firstobs=%eval(&estper+&gap+&evtwin) rename=(date=evtwin_end));
	  format estper_beg estper_end evtwin_beg evtdate evtwin_end date9.;
	  label estper_beg='Start of the Estimation Window'
	      estper_end='End of the Estimation Window'
	      evtwin_beg='Start of the Event Window'
	      evtwin_end='End of the Event Window'
	      evtdate='Event Date';
	  index+1;
	  if nmiss(estper_beg,estper_end,evtwin_beg,evtwin_end,evtdate)=0;
	run;
%mend date_creator; 

%date_creator;

%let minest=120; /*Minimum of non-missing returns required for estimation      */

/* proc sql; */
/*   create table evt_input as  */
/*   select distinct permno, start as edate format date9. */
/*   from crsp.dsp500list  */
/*   where '01jan1978'd<= start <'01jan1984'd;  */
/* quit; */

proc sql;
  create table evt_input as 
  select distinct permno,  announcedate as edate format date9.
  from sav.wrds_keydev_students
  where keydeveventtypeid=46; 
quit;

proc sql; 
	create table evt_head as 
	select distinct a.permno, b.*, a.edate as org_date
	from evt_input as a left join caldates as b
	on b.evtdate-a.edate>=0 and b.evtdate-a.edate<=4
	group by a.edate
	having (b.evtdate-a.edate)=min(b.evtdate-a.edate);
quit;

 /*Returns for sample securities around the event dates */
proc sql; 
	create table _evtrets_ as 
	select a.permno, a.date format date9., a.ret,
           b.evtdate, b.estper_beg, b.estper_end,
           b.evtwin_beg, b.evtwin_end
	from sav.dsf as a, evt_head as b
	where a.permno=b.permno and b.estper_beg<=a.date<=b.evtwin_end;
quit;

proc sql; 
	 /* Merge in the risk factors                                           */
	 /* User can create her own risk factors and use it instead of FF+M ones*/
	create table evtrets as 
	select a.*, (b.mktrf+b.rf) as mkt, (a.ret-b.rf) as retrf, b.mktrf, b.rf, b.smb, b.hml, b.umd
	   from _evtrets_ as a left join
	        sav.factors_daily (keep=date mktrf smb hml umd rf) as b
	on a.date=b.date 
	order by a.permno,a.evtdate,a.date;
quit;

/* STEP 4. Estimating Factor Exposures over the estimation period*/ 
proc reg data=evtrets edf outest=params  noprint;
   where estper_beg<=date<=estper_end;
   by permno evtdate; 
   eq1: model ret = mkt;
   eq2: model ret = mkt;
   eq3: model retrf = mktrf smb hml;
   eq4: model retrf = mktrf smb hml umd;
run; 

proc sql;
	create table abrets as
	select distinct a.*,  b._p_+b._edf_ as nobs, a.ret-b.mkt*a.mkt as ar0,
	a.ret-alpha1-beta1*a.mkt as ar1, a.retrf-alpha2-beta2*a.mktrf-sminb2*a.smb-hminl2*a.hml as ar2,
	a.retrf-alpha3-beta3*a.mktrf-sminb3*a.smb-hminl3*a.hml-umind3*a.umd as ar3
	from evtrets(where=(evtwin_beg<=date<=evtwin_end)) as a
	inner join params (where=(_model_='eq1')) as b
 	on a.permno=b.permno and a.evtdate=b.evtdate
  	inner join params (where=(_model_='eq2') 
 	rename=(intercept=alpha1 mkt=beta1)) as c
 	on a.permno=c.permno and a.evtdate=c.evtdate
  	inner join params (where=(_model_='eq3') 
  	rename=(intercept=alpha2 mktrf=beta2 smb=sminb2 hml=hminl2)) as d 
 	on a.permno=d.permno and a.evtdate=d.evtdate
  	inner join params (where=(_model_='eq4') 
  	rename=(intercept=alpha3 mktrf=beta3 smb=sminb3 hml=hminl3 umd=umind3)) as e
 	on a.permno=e.permno and a.evtdate=e.evtdate
 	where calculated nobs>=&minest;
quit;

/*Align with Index*/
proc sql;
	create table abrets_days as
	select distinct a.*, c.index-b.index as day
	from abrets as a inner join caldates as b
	on a.evtdate=b.evtdate
	inner join caldates as c
	on a.date=c.evtdate;
quit;

/* Graph Generating Block Star */
/* proc sql; */
/* 	create table car_days as */
/* 	select distinct day, mean(ar0) as aar0, mean(ar1) as aar1, mean(ar2) as aar2, mean(ar3) as aar3 */
/* 	from  abrets_days */
/* 	group by day; */
/* quit; */
/*  */
/* data car_days; set car_days; retain caar;  */
/* caar0+aar0; */
/* if _N_=1 then caar0=aar0; */
/* run; */
/* Graph Generating Block End */
 

/*Statistic report beginning*/
proc sql;
	create table car_table as
	select distinct permno, evtdate, sum(ar1) as car1 'CAR(-5,5)'
	from abrets_days 
	where -5<=day<=5
	group by permno, evtdate;
quit;

proc sql;
	create table car_rpt as
	select distinct mean(car1) as mean_car format=percentn8.3,
	sum(car1>.) as cnt "Total numbers of events", 
	sum(car1>=0) as poscnt "Events with positive(>=0) return", 
	sum(car1<0) as negcnt "Events with negative(<0) return",
	t(car1) as t_value format=comma9.3 "Standard t-value (different from zero)", 
	prt(car1) as p_value format=percentn8.3 "Standard p-value (different from zero)"
	from car_table;
quit;
/*Statistic report ending*/
