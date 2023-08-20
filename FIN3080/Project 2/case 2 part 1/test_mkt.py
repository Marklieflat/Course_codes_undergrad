# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:07:33 2022

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

# df1['Msmvttl'] = df1.groupby('Stkcd').Msmvttl.shift(1)

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