# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:01:46 2022

@author: Mark
"""

import numpy as np
import pandas as pd
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

df1 = df1[df1.Trdmnt >= '2007-01']

df1 = df1.sort_values(['Stkcd','Trdmnt'])

df1 = df1.dropna()

# print(df1.info())

df1['prev_ret'] = df1.groupby('Stkcd').Mretwd.shift(1)

df1 = df1.dropna()

perc = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

df1['allo'] = 1

def allocate_ret(df):
    quan = df['prev_ret'].describe(percentiles = perc)
    quan = quan.iloc[4:13]
    df.loc[df.prev_ret <= quan[0],'allo'] = 0
    df.loc[(df.prev_ret > quan[0])&(df.prev_ret <= quan[1]),'allo'] = 1
    df.loc[(df.prev_ret > quan[1])&(df.prev_ret <= quan[2]),'allo'] = 2
    df.loc[(df.prev_ret > quan[2])&(df.prev_ret <= quan[3]),'allo'] = 3
    df.loc[(df.prev_ret > quan[3])&(df.prev_ret <= quan[4]),'allo'] = 4
    df.loc[(df.prev_ret > quan[4])&(df.prev_ret <= quan[5]),'allo'] = 5
    df.loc[(df.prev_ret > quan[5])&(df.prev_ret <= quan[6]),'allo'] = 6
    df.loc[(df.prev_ret > quan[6])&(df.prev_ret <= quan[7]),'allo'] = 7
    df.loc[(df.prev_ret > quan[7])&(df.prev_ret <= quan[8]),'allo'] = 8
    df.loc[df.prev_ret > quan[8],'allo'] = 9
    return df

df1 = df1.groupby('Trdmnt').apply(allocate_ret)
    
# print(df1.allo.value_counts())
    
ew_pf = df1.groupby(['allo','Trdmnt']).agg({'Mretwd':'mean'}).reset_index()

# # print(ew_pf.info())

ew_pf = ew_pf.rename(columns = {'Trdmnt':'ym'})

# ew_pf['ret'] = ew_pf.groupby('allo').cum_ret.pct_change()

# ew_pf.loc[ew_pf.ret.isnull() == True, 'ret'] = ew_pf.cum_ret - 1

result = ew_pf.groupby('allo').agg({'Mretwd':'mean'}).reset_index()

plt.figure(1, figsize = [10,5])
plt.plot(result.allo, result.Mretwd*100,'b')
plt.xlabel('portfolio ID (smaller number means smaller previous monthly return)')
plt.ylabel('Average return of the portfolio(%)')
plt.title('Long-Short Portfolio average return by chasing ups and downs over 2007-2022')
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.grid(axis = 'y')
plt.show()