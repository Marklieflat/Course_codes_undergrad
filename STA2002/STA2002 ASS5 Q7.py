# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 21:38:55 2021

@author: Mark
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
from pandas import DataFrame

df = pd.read_excel('D:/Download/MSFT_stock_2020.xlsx')

#Check the data 
df.info()

df['Date'] = pd.to_datetime(df.Date)

perc=[0.01,0.05,0.25,0.5,0.75,0.9,0.95,0.99]
df = df.sort_values('Date')
print(df.describe(percentiles = perc))

print(df.Close.max())

#Part A
df['Close+1'] = df.Close.shift(1)

df['ret'] = df['Close']/df['Close+1']
df['lg_ret'] = df['ret'].apply(np.log)

N_plus = df.loc[df.lg_ret>0, ['Close']].count()[0]
p_valueA = stats.binom_test(4391,n = 8717, p = 0.5, alternative = 'greater')

#Part B
df1 = df.dropna()
df1 = df1.sort_values(['lg_ret']).reset_index(drop = True)
df1 = df1[df1.lg_ret != 0].reset_index(drop=True)
df1['rank'] = df1['lg_ret'].rank(method = 'average')

# print(df1.loc[df1.lg_ret == df1.lg_ret.max(),['rank']])

df1['sign'] = df1['lg_ret'].apply(lambda x: 1 if x>0 else -1)

df1['signed_rank'] = df1['sign']*df1['rank']

sum_of_signed_ranks = df1['signed_rank'].sum()

obs = df1['signed_rank'].count()

sigma = np.sqrt(8509*8510*(8509*2+1)/6)

p_valueB = 1-norm.cdf(sum_of_signed_ranks, 0, sigma)

#Part C
df = df.dropna()

ret_mean = df['lg_ret'].mean()

ret_sample_var = df['lg_ret'].var()*(8717/8716)

ret_sample_std = np.sqrt(ret_sample_var)

t_stat = ret_mean/(ret_sample_std/np.sqrt(8717))

#Part D
ob1 = df.loc[df.lg_ret<-0.001,['Close']].count()[0]
ob2 = df.loc[(df.lg_ret>=-0.001) & (df.lg_ret<-0.0004),['Close']].count()[0]
ob3 = df.loc[(df.lg_ret>=-0.0004) & (df.lg_ret<0),['Close']].count()[0]
ob4 = df.loc[(df.lg_ret>=0) & (df.lg_ret<0.0004),['Close']].count()[0]
ob5 = df.loc[(df.lg_ret>=0.0004) & (df.lg_ret<0.001),['Close']].count()[0]
ob6 = df.loc[df.lg_ret>=0.001,['Close']].count()[0]
obs_list = [ob1,ob2,ob3,ob4,ob5,ob6]

E1 = norm.cdf(-0.001,0,0.02)*8717
E2 = (norm.cdf(-0.0004,0,0.02)-norm.cdf(-0.001,0,0.02))*8717
E3 = (norm.cdf(0,0,0.02)-norm.cdf(-0.0004,0,0.02))*8717
E4 = (norm.cdf(0.0004,0,0.02)-norm.cdf(0,0,0.02))*8717
E5 = (norm.cdf(0.001,0,0.02)-norm.cdf(0.0004,0,0.02))*8717
E6 = (1 - norm.cdf(0.001,0,0.02))*8717
expt_list = [E1,E2,E3,E4,E5,E6]

obsfrm = DataFrame(obs_list,columns = ['Observed'])
expfrm = DataFrame(expt_list,columns = ['Expected'])
final_frm1 = pd.merge(obsfrm,expfrm,how = 'outer', left_index = True, right_index = True)

final_frm1['chi'] = (final_frm1['Observed']-final_frm1['Expected'])**2/(final_frm1['Expected'])
q_5 = final_frm1['chi'].sum()

#Part E
EE1 = norm.cdf(-0.001,ret_mean,ret_sample_std)*8717
EE2 = (norm.cdf(-0.0004,ret_mean,ret_sample_std)-norm.cdf(-0.001,ret_mean,ret_sample_std))*8717
EE3 = (norm.cdf(0,ret_mean,ret_sample_std)-norm.cdf(-0.0004,ret_mean,ret_sample_std))*8717
EE4 = (norm.cdf(0.0004,ret_mean,ret_sample_std)-norm.cdf(0,ret_mean,ret_sample_std))*8717
EE5 = (norm.cdf(0.001,ret_mean,ret_sample_std)-norm.cdf(0.0004,ret_mean,ret_sample_std))*8717
EE6 = (1 - norm.cdf(0.001,ret_mean,ret_sample_std))*8717

exp2_list = [EE1,EE2,EE3,EE4,EE5,EE6]
exp2frm = DataFrame(exp2_list,columns = ['Expected'])
final_frm2 = pd.merge(obsfrm,exp2frm,how = 'outer', left_index = True, right_index = True)
final_frm2['chi'] = (final_frm2['Observed']-final_frm2['Expected'])**2/(final_frm2['Expected'])
q_3 = final_frm2['chi'].sum()
