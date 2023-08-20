# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 20:58:41 2022

@author: Mark
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.pyplot import MultipleLocator
import statsmodels.formula.api as sm

df = pd.read_csv(r'D:\Code Library\FIN3080\Project 2\case 2 part 1\个股月度回报率\TRD_Mnth.csv')

df['Trdmnt'] = pd.to_datetime(df['Trdmnt']).dt.to_period('M')

# print(df.info())

stock_id = df.loc[df.Trdmnt == '2007-01','Stkcd']

# df = df[(df.Trdmnt >= '2008-10') & (df.Trdmnt <= '2009-01')]

df1 = df.loc[df.Stkcd.isin(stock_id)]

df1['Msmvttl'] = df1.groupby('Stkcd').Msmvttl.shift(1)

df1 = df1[df1.Trdmnt >= '2007-01']

df1 = df1.sort_values(['Stkcd','Trdmnt'])

df1 = df1.dropna()

df1['gross_ret'] = 1 + df1.Mretwd

# print(df1[df1.Mretwd.isnull() == True])

df1['cum_ret'] = df1.groupby(['Stkcd']).gross_ret.cumprod()

perc = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

quan = df['Msmvttl'].describe(percentiles = perc)

df1['allo'] = 1

def allocation(df):
    quan = df['Msmvttl'].describe(percentiles = perc)
    quan = quan.iloc[4:13]
    df.loc[df.Msmvttl <= quan[0],'allo'] = 0
    df.loc[(df.Msmvttl > quan[0])&(df.Msmvttl <= quan[1]),'allo'] = 1
    df.loc[(df.Msmvttl > quan[1])&(df.Msmvttl <= quan[2]),'allo'] = 2
    df.loc[(df.Msmvttl > quan[2])&(df.Msmvttl <= quan[3]),'allo'] = 3
    df.loc[(df.Msmvttl > quan[3])&(df.Msmvttl <= quan[4]),'allo'] = 4
    df.loc[(df.Msmvttl > quan[4])&(df.Msmvttl <= quan[5]),'allo'] = 5
    df.loc[(df.Msmvttl > quan[5])&(df.Msmvttl <= quan[6]),'allo'] = 6
    df.loc[(df.Msmvttl > quan[6])&(df.Msmvttl <= quan[7]),'allo'] = 7
    df.loc[(df.Msmvttl > quan[7])&(df.Msmvttl <= quan[8]),'allo'] = 8
    df.loc[df.Msmvttl > quan[8],'allo'] = 9
    return df

df1 = df1.groupby(['Trdmnt']).apply(allocation)

# print(df1.allo.value_counts())
    
ew_portfolio = df1.groupby(['allo','Trdmnt']).agg({'cum_ret':'mean'})
    
ew_portfolio = ew_portfolio.reset_index()
    
# print(ew_portfolio.info())

ew_portfolio = ew_portfolio.rename(columns = {'Trdmnt':'ym'})

# plt.figure(figsize = [10,5])
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 0,'cum_ret'], label = '0')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 1,'cum_ret'], label = '1')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 2,'cum_ret'], label = '2')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 3,'cum_ret'], label = '3')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 4,'cum_ret'], label = '4')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 5,'cum_ret'], label = '5')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 6,'cum_ret'], label = '6')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 7,'cum_ret'], label = '7')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 8,'cum_ret'], label = '8')
# plt.plot(ew_portfolio.loc[ew_portfolio.allo == 0,'ym'], ew_portfolio.loc[ew_portfolio.allo == 9,'cum_ret'], label = '9')
# plt.legend()
# plt.grid(axis = 'y')
# plt.show()

ew_portfolio['ret'] = ew_portfolio.groupby('allo').cum_ret.pct_change()

ew_portfolio.loc[ew_portfolio.ret.isnull() == True, 'ret'] = ew_portfolio.cum_ret - 1

result = ew_portfolio.groupby(['allo']).agg({'ret':'mean'}).reset_index()

plt.figure(1, figsize = [10,5])
plt.plot(result.allo, result.ret*100,'b')
plt.xlabel('portfolio ID (smaller number means smaller market capitalization)')
plt.ylabel('Average return of the portfolio(%)')
plt.title('Long-Short Portfolio average return by market capitalization over 2007-2022')
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.grid(axis = 'y')
plt.show()

# Correlation of different groups
# corr = ew_portfolio.drop('cum_ret', axis = 1)

# corr = corr.set_index(['ym','allo'])

# corr = corr.unstack()

# result_corr = corr.corr()

# CAPM alpha

# reg = pd.read_csv(r'D:\Code Library\FIN3080\Project 2\case 2 part 1\capm_reg.csv')

# reg = reg.rename(columns = {'Month':'ym'})

# reg['ym'] = pd.to_datetime(reg.ym).dt.to_period('M')

# capm = pd.merge(reg, ew_portfolio, how = 'outer', on = 'ym')

# capm = capm.drop(['cum_ret'],axis = 1)

# capm = capm.sort_values(['ym','allo'])

# capm = capm[(capm.allo == 0) | (capm.allo == 9)]

# capm['sft_ret'] = capm.ret.shift(1)

# capm['ls_ret'] = capm['ret'] - capm['sft_ret']

# capm = capm.groupby('ym').agg({'ls_ret':'last','rm':'last','rf':'last'}).reset_index()

# capm['y'] = capm.ls_ret - capm.rf

# capm['x'] = capm.rm - capm.rf

# capm = capm[['ym','y','x']]

# ls_pf = sm.ols(formula = 'y~x', data = capm).fit()

# print(ls_pf.summary())

# plt.figure(2, figsize = [10,5])
# plt.plot(capm_res.allo, capm_res.alpha, 'r')
# plt.xlabel('portfolio ID (smaller number means smaller market capitalization)')
# plt.ylabel('CAPM alpha')
# plt.title('Long-Short portfolio CAPM alpha over 2006-2022')
# x_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.grid(axis = 'y')
# plt.show()