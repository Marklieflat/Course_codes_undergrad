# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 16:55:18 2022

@author: Mark
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_1\project_1.sas7bdat')

ff3 = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_1\factors_monthly.sas7bdat')

roa = df[['PERMNO','DATE','RET','mcap','ROA']]

roa['ym'] = pd.to_datetime(roa.DATE).dt.to_period('M')

roa = roa.sort_values(['PERMNO','ym']).reset_index(drop = True)

roa = roa[['PERMNO','ym','RET','mcap','ROA']]

roa = roa.dropna()

perc = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

roa['allo'] = 1

def allocation(df):
    quan = df['ROA'].describe(percentiles = perc)
    quan = quan.iloc[4:13]
    df.loc[df.ROA <= quan[0],'allo'] = 0
    df.loc[(df.ROA > quan[0])&(df.ROA <= quan[1]),'allo'] = 1
    df.loc[(df.ROA > quan[1])&(df.ROA <= quan[2]),'allo'] = 2
    df.loc[(df.ROA > quan[2])&(df.ROA <= quan[3]),'allo'] = 3
    df.loc[(df.ROA > quan[3])&(df.ROA <= quan[4]),'allo'] = 4
    df.loc[(df.ROA > quan[4])&(df.ROA <= quan[5]),'allo'] = 5
    df.loc[(df.ROA > quan[5])&(df.ROA <= quan[6]),'allo'] = 6
    df.loc[(df.ROA > quan[6])&(df.ROA <= quan[7]),'allo'] = 7
    df.loc[(df.ROA > quan[7])&(df.ROA <= quan[8]),'allo'] = 8
    df.loc[df.ROA > quan[8],'allo'] = 9
    return df

roa = roa.groupby(['ym']).apply(allocation)

# print(roa.allo.value_counts())

roa['totalmcap'] = roa.groupby(['allo','ym']).mcap.transform('sum')

roa['weight'] = roa.mcap / roa.totalmcap

roa['vw_ret'] = roa.weight * roa.RET

vw_pf = roa.groupby(['allo','ym']).agg({'vw_ret':'sum'}).reset_index()

vw_pf = vw_pf.sort_values(['ym','allo']).reset_index(drop = True)

ff3['ym'] = pd.to_datetime(ff3.date).dt.to_period('M')

ff3 = ff3[['ym','mktrf','smb','hml','rf']]

ff3 = ff3[ff3.ym >= '1980-01'].reset_index(drop = True)

vw_pf = pd.merge(vw_pf, ff3, how = 'left', on = 'ym')

vw_pf['ri-rf'] = vw_pf['vw_ret'] - vw_pf['rf']

vw_pf = vw_pf.dropna()

def capm_alpha(df):
    y = df[['ri-rf']]
    X = df[['mktrf']]
    return np.squeeze(LinearRegression().fit(X,y).intercept_)

def ff3_alpha(df):
    y = df[['ri-rf']]
    X = df[['mktrf','smb','hml']]
    return np.squeeze(LinearRegression().fit(X,y).intercept_)

capm_a = vw_pf.groupby('allo').apply(capm_alpha)

ff3_a = vw_pf.groupby('allo').apply(ff3_alpha)

# Statsmodel CAPM(Get p_value)
Y = vw_pf.loc[vw_pf.allo == 0,'ri-rf']
X = vw_pf.loc[vw_pf.allo == 0,'mktrf']
X = sm.add_constant(X)
model1 = sm.OLS(Y,X)
capm_res = model1.fit()
print(capm_res.summary())

# Statsmodel FF3(Get p_value)
Y = vw_pf.loc[vw_pf.allo == 0,'ri-rf']
X = vw_pf.loc[vw_pf.allo == 0,['mktrf','smb','hml']]
X = sm.add_constant(X)
model2 = sm.OLS(Y,X)
ff3_res = model2.fit()
print(ff3_res.summary())
