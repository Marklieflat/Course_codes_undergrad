# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:13:43 2022

@author: Lenovo
"""

import pandas as pd
import math
from datetime import datetime  
import statsmodels.api as sm 
from statsmodels.tools.eval_measures import rmse
import matplotlib.pyplot as plt
import wrds, sqlite3, seaborn

local_sql = sqlite3.connect(':memory:')
local_sql.create_function('sqrt',1,math.sqrt)

dsf = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_2\dsf.sas7bdat')

dsi = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_2\dsi.sas7bdat')

factor = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_2\factors_daily.sas7bdat')

event = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_2\wrds_keydev_students.sas7bdat')

#Test
# print(event.PERMNO.nunique())

event = event[event.keydeveventtypeid == 46.0]
event = event[['PERMNO','announcedate']].reset_index(drop = True)
event = event.rename(columns = {'announcedate':'adate','PERMNO':'permno'})

dsf.to_sql('dsf', local_sql, index = False, if_exists = 'replace')
dsi.to_sql('dsi', local_sql, index = False, if_exists = 'replace')
factor.to_sql('factor', local_sql, index = False, if_exists = 'replace')
event.to_sql('event', local_sql, index = False, if_exists = 'replace')

sqlcode = """
        select distinct date
        from dsi
        order by date;
"""

crsp_day = pd.read_sql_query(sqlcode, local_sql)
crsp_day = crsp_day.reset_index()
crsp_day.columns = ['crspday','date']
crsp_day['date'] = pd.to_datetime(crsp_day.date).dt.strftime('%Y-%m-%d')

crsp_day.to_sql('crsp_day', local_sql, index=False, if_exists='replace') 

sqlcode = """
    select distinct a.*, crspday
    from event as a left join crsp_day as b
    on adate<=date and date<=date(adate, "4 day")
    group by a.permno, adate
    having date = min(date)
"""
event = pd.read_sql_query(sqlcode, local_sql)
event['adate'] = pd.to_datetime(event.adate).dt.strftime('%Y-%m-%d')

estper=200;                       #Length of the estimation window in trading days                       
pos=60;                           #End of the event window (greater than CAR_to)                         
pre=-30;                          #Beginning of Abnormal Return Window(less than CAR_from for a est.GAP) 
minest=120;                       #Minimum of non-missing returns required for estimation                
CAR_from=-5;                      #Beginning of event window of interest                                 
CAR_to=5;                         #End of event window of interest                                       
evtwin=CAR_to-CAR_from + 1;       #length of event window in trading days 

event.to_sql('event', local_sql, index=False, if_exists='replace')  

sqlcode="""
    select distinct a.*, 
    d.date as estper_beg, /*Start of the Estimation Window*/
    e.date as estper_end, /*End of the Estimation Window*/
    b.date as evtwin_beg, /*Start of the Abnormal Return Window*/
    a.adate as evtdate, /*Event Date*/
    c.date as evtwin_end /*End of the Abnormal Return Window*/
    from event as a inner join crsp_day as b
    on b.crspday-a.crspday= {} /*pre*/
    inner join crsp_day as c
    on c.crspday-a.crspday= {} /*pos*/
    inner join crsp_day as d
    on b.crspday-d.crspday= {} /*estper*/
    inner join crsp_day as e
    on b.crspday-e.crspday=1
""".format(pre-1, pos-1, estper)
tradedates=pd.read_sql_query(sqlcode, local_sql)

permno_tuple = tuple(tradedates['permno'])

sqlcode = """
    select distinct permno, a.date, a.ret, ret-rf as retrf, mktrf, smb, hml, umd,
    mktrf+rf as mkt, ret-mktrf-rf as exret
    from dsf as a inner join factor as b
    on a.date = b.date and permno in {}
    order by a.permno, a.date;
""".format(permno_tuple)

daily_rets = pd.read_sql_query(sqlcode, local_sql)
daily_rets = daily_rets.rename(columns = {'PERMNO':'permno','DATE':'date','RET':'ret'})
daily_rets['date'] = pd.to_datetime(daily_rets.date).dt.strftime('%Y-%m-%d')

tradedates.to_sql('tradedates', local_sql, index=False, if_exists='replace') 
daily_rets.to_sql('daily_rets', local_sql, index=False, if_exists='replace') 

sqlcode="""    
    select distinct a.*, c.crspday-a.crspday+1 as day, b.date, mktrf, mkt, smb, hml, umd, ret, retrf, exret
    from tradedates as a inner join daily_rets as b
    on a.permno=b.permno and b.date>=estper_beg and b.date<=evtwin_end
    left join crsp_day as c
    on b.date=c.date
    order by permno, adate, day; 
"""
reg_panel=pd.read_sql_query(sqlcode, local_sql)

# Define an OLS function with statsmodels module
def regOLS(data, yvar, xvars=None):
    data['const']=1
    y = data[yvar]
    
    if xvars==None:
        X = data['const']
    else: 
        X = pd.concat([data['const'], data[xvars]], axis=1)
    
    result = sm.OLS(y, X).fit() 
    yhat = result.predict(X)
    
    param2 = {'nobs': result.nobs, 'rmse':rmse(y, yhat)} # calc rmse
    param2 = pd.Series(data=param2, index=['nobs', 'rmse'])
    
    res=result.params.append(param2)
    return res

#We only keep the daily records over the estimation window prior to S&P inclusion events
est_panel=reg_panel[(reg_panel['estper_beg']<=reg_panel['date'])&(reg_panel['date']<=reg_panel['estper_end'])]
est_panel=est_panel.dropna() #Drop the missing values

#Calcuate total return variance and count Nobs
params_mar=est_panel.groupby(['permno', 'adate']).apply(regOLS, 'exret') #MAR 

#We conduct calculate OLS estimates of various models for each event. 
params_mm=est_panel.groupby(['permno', 'adate']).apply(regOLS, 'ret', 'mkt') #MM
params_ff3=est_panel.groupby(['permno', 'adate']).apply(regOLS, 'retrf', ['mktrf', 'smb', 'hml']) #FF3
params_ff4=est_panel.groupby(['permno', 'adate']).apply(regOLS, 'retrf', ['mktrf', 'smb', 'hml', 'umd']) #FF3+UMD

car_panel=reg_panel[(reg_panel['day']>=pre) & (reg_panel['day']<=pos)]

car_panel.to_sql('car_panel', local_sql, if_exists='replace') 
params_mar.to_sql('params_mar', local_sql, if_exists='replace') 
params_mm.to_sql('params_mm', local_sql, if_exists='replace') 
params_ff3.to_sql('params_ff3', local_sql, if_exists='replace') 
params_ff4.to_sql('params_ff4', local_sql, if_exists='replace')

sqlcode="""      
    select distinct a.permno, a.adate, a.day, a.ret, b.nobs as nobs, 

    /*Market Adjusted Model's AR*/
    a.exret as abret0, b.rmse*b.rmse as var0, 

    /*Market Model's AR*/
    a.ret-c.const-c.mkt*a.mkt as abret1, c.rmse*c.rmse as var1, 

    /*Fama French 3 Factor's AR*/
    a.retrf-d.const-d.mktrf*a.mktrf-d.smb*a.smb-d.hml*a.hml as abret2, d.rmse*d.rmse as var2, 

    /*Fama French 3 Factor +UMD 's AR*/
    a.retrf-e.const-e.mktrf*a.mktrf-e.smb*a.smb-e.hml*a.hml-e.umd*a.umd as abret3, e.rmse*e.rmse as var3

    from car_panel as a inner join params_mar as b
    on a.permno=b.permno and a.adate=b.adate
    inner join params_mm as c
    on a.permno=c.permno and a.adate=c.adate
    inner join params_ff3 as d
    on a.permno=d.permno and a.adate=d.adate
    inner join params_ff4 as e
    on a.permno=e.permno and a.adate=e.adate

    /*minest (Minimum of non-missing returns required for estimation)*/
    where b.nobs > {} ; 
""".format(minest)

abrets_panel=pd.read_sql_query(sqlcode, local_sql)

car_graph=abrets_panel[(abrets_panel['day']<=60) & (abrets_panel['day']>=-20)].copy()

car_graph[['RAW', 'CAR_MAR', 'CAR_MM', 'CAR_FF3', 'CAR_FF4']]=car_graph.groupby(['permno','adate'])['ret','abret0','abret1','abret2','abret3'].transform(pd.Series.cumsum)
car_graph.groupby('day')['RAW', 'CAR_MAR', 'CAR_MM', 'CAR_FF3', 'CAR_FF4'].mean().plot(title='Cumulative Abnormal Returns', xlabel='Day', figsize=(20,10))

# Let's take a look of CAR distribution through days
fig, ax = plt.subplots(figsize=(20,10))
seaborn.boxplot(x = car_graph['day'], y = car_graph['CAR_MAR'], ax = ax)

# OPTIONAL: You can reset Event Windows Here:
CAR_from=-5;                       #Beginning of event window of interest                                 
CAR_to=5;                         #End of event window of interest                                       
evtwin=CAR_to-CAR_from + 1;       #length of event window in trading days 

abrets_panel.to_sql('abrets_panel', local_sql, if_exists='replace') 

sqlcode=""" 
    select distinct permno, adate, nobs, 
    sum(abret0) as car0, sum(abret0)/sqrt( {} *var0) as scar0, /*evtwin*/
    sum(abret1) as car1, sum(abret1)/sqrt( {} *var1) as scar1, /*evtwin*/
    sum(abret2) as car2, sum(abret2)/sqrt( {} *var2) as scar2, /*evtwin*/
    sum(abret3) as car3, sum(abret3)/sqrt( {} *var3) as scar3  /*evtwin*/
    from abrets_panel
    where {} <=day /*CAR_from*/ and day<= {} /*CAR_to*/
    group by permno, adate;
""".format(evtwin,evtwin,evtwin,evtwin,CAR_from,CAR_to)

cars_panel=pd.read_sql_query(sqlcode, local_sql)

cars_panel.dropna().to_sql('cars_panel', local_sql, if_exists='replace') 

sqlcode=""" 
    select "MAR" as Model, avg(car0) as car, sum(car0>0) as pos, sum(car0<=0) as neg,
    avg(scar0)*sqrt(count(scar0)) as tpatel
    from cars_panel
    UNION
    select "MM" as Model, avg(car1) as car, sum(car1>0) as pos, sum(car1<=0) as neg,
    avg(scar1)*sqrt(count(scar1)) as tpatel
    from cars_panel
    UNION
    select "FF" as Model, avg(car2) as car, sum(car2>0) as pos, sum(car2<=0) as neg,
    avg(scar2)*sqrt(count(scar2)) as tpatel
    from cars_panel
    UNION
    select "FFM" as Model, avg(car3) as car, sum(car3>0) as pos, sum(car3<=0) as neg,
    avg(scar3)*sqrt(count(scar3)) as tpatel
    from cars_panel;
"""
cars_stats=pd.read_sql_query(sqlcode, local_sql)

#Relabeling the variables
cars_stats = cars_stats.rename(columns={'car': 'CAR('+str(CAR_from)+','+str(CAR_to)+')', 'tpatel': 'Patell t'})

outlier = abrets_panel.sort_values(['abret0','abret1','abret2','abret3'], ascending = False).head(10)

high_abret = abrets_panel[(abrets_panel.day == 0)|(abrets_panel.day == 1)].sort_values(['abret0','abret1','abret2','abret3'], ascending = False).head(10)

test = pd.merge(event, cars_panel, how = 'outer', on = ['permno','adate'])

nulldata = test[test.nobs.isnull() == True].reset_index(drop = True)
