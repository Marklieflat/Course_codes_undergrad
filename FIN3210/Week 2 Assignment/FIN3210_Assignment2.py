import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm
from lifelines import CoxPHFitter
import matplotlib.pyplot as plt


"""
Transform the data from xlsx to csv
"""
# rrd = pd.read_excel('FIN3210 Week 2 Renrendai loans.xlsx', sheet_name='Data Borrower')
# rrd.to_csv('FIN3210 Week 2 Renrendai loans.csv', index=False)
# plat = pd.read_excel('FIN3210  Week 2 p2p lending platforms.xlsx', sheet_name='Platform Data')
# plat.to_csv('FIN3210  Week 2 p2p lending platforms.csv', index=False)

"""
Read the data from the disk
"""
rrd_tot = pd.read_csv('FIN3210 Week 2 Renrendai loans.csv')
plat_tot = pd.read_csv('FIN3210  Week 2 p2p lending platforms.csv')
# rrd_tot['AMOUNT'].plot(kind = 'kde')
# plt.xlim(1000,100000)
# plt.show()

"""
1)	Present two tables for the summary statistics of the key variables in Renrendai loans.xlsx and p2p lending platforms.xlsx
Procedures: Data cleaning, preserve the relevant data.
"""
rrd = rrd_tot[['BIDS','DEFAULT','AMOUNT','INTEREST','MONTHS','CREDIT',
               'HOUSE','CAR','HOUSE_L','CAR_L','EDUCATION','WORKTIME',
               'INCOME','MARRY','AGE']]
rrd = pd.get_dummies(rrd, columns=['MARRY'])
# print(rrd.describe().T)

plat = plat_tot[['OnlineTime_YMD','Bankrupt_WDZJ','Collapse','Benign',
                 'Fraud','RegCapital','Background','Capitaldeposit',
                 'Obtaininvest','Joinasso','Autobid','Transright','Riskdeposit','Thirdguarantee']]
plat = pd.get_dummies(plat, columns=['Background'])
# print(plat.describe().T)

"""
2)	Perform a logit regression and examine the relation between the default likelihood 
and borrower characteristics such as credit, house, car, education, work time, etc. 
"""
X = rrd[['CREDIT','HOUSE','CAR','EDUCATION','WORKTIME']]
y = rrd[['DEFAULT']]
X = sm.add_constant(X)
logit_model = sm.Logit(y, X, missing = 'drop').fit()
# print(logit_model.summary())

"""
3)	Perform an ols regression and examine the relation between the number of bids 
and borrower characteristics such as credit, house, car, education, work time, etc.
"""
X = rrd[['CREDIT','HOUSE','CAR','EDUCATION','WORKTIME']]
y = rrd[['BIDS']]
X = sm.add_constant(X)
ols_model = sm.OLS(y, X, missing = 'drop').fit()
# print(ols_model.summary())

"""
4)	Perform the Cox model (Proportional hazards model) and examine the relation 
between the platform default (survival) likelihood and platform characteristics 
such as RegCapital, Joinasso, etc.
"""
cox_dt = plat[['OnlineTime_YMD','Bankrupt_WDZJ','Collapse','Benign','Fraud','RegCapital','Joinasso']]
cox_dt.dropna(inplace=True)
cox_dt['OnlineTime_YMD'] = pd.to_datetime(cox_dt['OnlineTime_YMD'], format='%Y%m%d')
cox_dt['Bankrupt_WDZJ'] = pd.to_datetime(cox_dt['Bankrupt_WDZJ'], format='%Y%m%d')
cox_dt['deltatime'] = (cox_dt['Bankrupt_WDZJ'] - cox_dt['OnlineTime_YMD']).apply(pd.Timedelta).dt.days
cox_dt.drop(['OnlineTime_YMD','Bankrupt_WDZJ'], axis=1, inplace=True)
cph = CoxPHFitter()
cph.fit(cox_dt, duration_col = 'deltatime', event_col = 'Collapse')
cph.print_summary()

