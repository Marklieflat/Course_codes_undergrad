# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:40:49 2022

@author: Mark
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_1\project_1.sas7bdat')

print(df.PERMNO.nunique())

ff3 = pd.read_sas(r'D:\Code Library\FIN3380_summer\Project_1\factors_monthly.sas7bdat')

mr = df[['PERMNO','DATE','RET','mcap','maxret']]

# mr['ym'] = pd.to_datetime(mr.DATE).dt.to_period('M')

# # print(mr.PERMNO.value_counts())

# # print(mr.PERMCO.value_counts())

# # print(mr.PERMNO.nunique())

# # print(mr.PERMCO.nunique())

# # print(mr.mcap.notnull().sum())

mr = mr.sort_values(['PERMNO','ym']).reset_index(drop = True)

mr = mr[['PERMNO','ym','RET','mcap','maxret']]

mr = mr.loc[mr.maxret.isnull() == False] # Drop the columns with no maximum return value
mr['RET'] = mr.RET.fillna(0) # Fill the empty return value with 0




perc = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

mr['allo'] = 1



def allocation(df):
    quan = df['maxret'].describe(percentiles = perc)
    quan = quan.iloc[4:13]
    df.loc[df.maxret <= quan[0],'allo'] = 0
    df.loc[(df.maxret > quan[0])&(df.maxret <= quan[1]),'allo'] = 1
    df.loc[(df.maxret > quan[1])&(df.maxret <= quan[2]),'allo'] = 2
    df.loc[(df.maxret > quan[2])&(df.maxret <= quan[3]),'allo'] = 3
    df.loc[(df.maxret > quan[3])&(df.maxret <= quan[4]),'allo'] = 4
    df.loc[(df.maxret > quan[4])&(df.maxret <= quan[5]),'allo'] = 5
    df.loc[(df.maxret > quan[5])&(df.maxret <= quan[6]),'allo'] = 6
    df.loc[(df.maxret > quan[6])&(df.maxret <= quan[7]),'allo'] = 7
    df.loc[(df.maxret > quan[7])&(df.maxret <= quan[8]),'allo'] = 8
    df.loc[df.maxret > quan[8],'allo'] = 9
    return df

mr = mr.groupby(['ym']).apply(allocation)

# print(mr.allo.value_counts())

mr['totalmcap'] = mr.groupby(['allo','ym']).mcap.transform('sum')

mr['weight'] = mr.mcap / mr.totalmcap

mr['vw_ret'] = mr.weight * mr.RET

num_pf = mr.groupby(['allo','ym']).agg({'PERMNO':'count'}).reset_index()

num_pf['year'] = pd.to_datetime(num_pf.ym).dt.year


# vw_pf = mr.groupby(['allo','ym']).agg({'vw_ret':'sum'}).reset_index()

# vw_pf = vw_pf.sort_values(['ym','allo']).reset_index(drop = True)

# ff3['ym'] = pd.to_datetime(ff3.date).dt.to_period('M')

# ff3 = ff3[['ym','mktrf','smb','hml','rf']]

# ff3 = ff3[ff3.ym >= '1980-01'].reset_index(drop = True)

# vw_pf = pd.merge(vw_pf, ff3, how = 'left', on = 'ym')

# vw_pf['ri-rf'] = vw_pf['vw_ret'] - vw_pf['rf']

# vw_pf = vw_pf.dropna()

# def capm_alpha(df):
#     y = df[['ri-rf']]
#     X = df[['mktrf']]
#     return np.squeeze(LinearRegression().fit(X,y).intercept_)

# def ff3_alpha(df):
#     y = df[['ri-rf']]
#     X = df[['mktrf','smb','hml']]
#     return np.squeeze(LinearRegression().fit(X,y).intercept_)

# capm_a = vw_pf.groupby('allo').apply(capm_alpha)

# ff3_a = vw_pf.groupby('allo').apply(ff3_alpha)


# # Statsmodel CAPM(Get p_value)
# Y = vw_pf.loc[vw_pf.allo == 0,'ri-rf']
# X = vw_pf.loc[vw_pf.allo == 0,'mktrf']
# X = sm.add_constant(X)
# model1 = sm.OLS(Y,X)
# capm_res = model1.fit()
# print(capm_res.summary())

# # Statsmodel FF3(Get p_value)
# Y = vw_pf.loc[vw_pf.allo == 0,'ri-rf']
# X = vw_pf.loc[vw_pf.allo == 0,['mktrf','smb','hml']]
# X = sm.add_constant(X)
# model2 = sm.OLS(Y,X)
# ff3_res = model2.fit()
# print(ff3_res.summary())

# test = mr[mr.allo == 0]
# test1 = mr[mr.allo == 9]

# ls_pf = vw_pf[(vw_pf.allo == 0)|(vw_pf.allo == 9)].reset_index(drop = True)

# ls_pf['sft_ret'] = ls_pf.vw_ret.shift(1) # Shift the return and get the long-short portfolio return in each month
# ls_pf['ls_ret'] = ls_pf.vw_ret - ls_pf.sft_ret

# ls_pf = ls_pf[ls_pf.allo == 9]
# ls_pf = ls_pf[['ym','ls_ret','mktrf','rf']].reset_index(drop = True)

# vis = ls_pf # Get the gross return of each component
# vis['grs_ls_ret'] = vis.ls_ret + 1
# vis['grs_mkt'] = vis.mktrf + vis.rf + 1
# vis['grs_rf'] = vis.rf + 1

# vis['cum_ls_ret'] = vis['grs_ls_ret'].cumprod()-1 # Get the cumulative return of each component
# vis['cum_mkt'] = vis['grs_mkt'].cumprod()-1
# vis['cum_rf'] = vis['grs_rf'].cumprod()-1

# vis = vis[['ym','cum_ls_ret','cum_mkt','cum_rf']] # Reorganize the data
# vis.loc[vis.ym == '1980-01',['cum_ls_ret','cum_mkt','cum_rf']] = 0
# vis['ym'] = vis.ym.astype('str')








