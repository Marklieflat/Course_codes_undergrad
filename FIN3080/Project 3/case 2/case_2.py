# -*- coding: utf-8 -*-
"""
Created on Sat May  7 00:27:23 2022

@author: Mark
"""

import modin.pandas as pd
import numpy as np
from glob import glob
import os
import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.pyplot import MultipleLocator
from matplotlib import ticker
import ray

# ray.init()

os.chdir('D:\Code Library\FIN3080\Project 3\case 2\daily stock return data')

df_final = pd.DataFrame(columns=['Stkcd','date','stk_ret'], index = [0])

for csv_file in glob('*.csv'):
    
    df = pd.read_csv(csv_file)
    
    df = df.rename(columns = {'Trddt':'date', 'Dretwd':'stk_ret'})
    
    df_final = df_final.append(df, ignore_index = True)
    
df_final = df_final.dropna()

df = df_final

df = df.sort_values(['Stkcd','date'])

df1 = pd.read_csv(r'D:\Code Library\FIN3080\Project 3\case 2\EPS data\eps_data.csv')

df1 = df1.drop('Stknme', axis = 1)

df1 = df1.rename(columns = {'Reptyp':'quarter','Accper':'acc_dl','Eranb':'eps'})

df1 = df1[(df1.quarter == 2) | (df1.quarter == 4)]

df2 = pd.read_csv(r'D:\Code Library\FIN3080\Project 3\case 2\market return data\mkt_ret.csv')

df2 = df2[df2.Markettype == 5].reset_index(drop = True)

df2 = df2.drop('Markettype', axis = 1)

df2 = df2.rename(columns = {'Cdretwdeq':'mkt_ret'})

# Step 2 3 4

df1['year'] = pd.to_datetime(df1.acc_dl).dt.year

df1['sft_eps'] = df1.groupby('Stkcd').eps.shift(2)

df1 = df1.dropna().reset_index(drop = True)

df1['UE'] = df1['eps'] - df1['sft_eps']

df1['sigma'] = df1.groupby('Stkcd')['UE'].transform(lambda s: s.rolling(4).std())

df1 = df1.dropna()

df1['SUE'] = df1['UE'] / df1['sigma']

perc = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

df1['allo'] = 1

def allocation(df):
    quan = df['SUE'].describe(percentiles = perc)
    quan = quan.iloc[4:13]
    df.loc[df['SUE'] <= quan[0],'allo'] = 0
    df.loc[(df['SUE'] > quan[0])&(df['SUE'] <= quan[1]),'allo'] = 1
    df.loc[(df['SUE'] > quan[1])&(df['SUE'] <= quan[2]),'allo'] = 2
    df.loc[(df['SUE'] > quan[2])&(df['SUE'] <= quan[3]),'allo'] = 3
    df.loc[(df['SUE'] > quan[3])&(df['SUE'] <= quan[4]),'allo'] = 4
    df.loc[(df['SUE'] > quan[4])&(df['SUE'] <= quan[5]),'allo'] = 5
    df.loc[(df['SUE'] > quan[5])&(df['SUE'] <= quan[6]),'allo'] = 6
    df.loc[(df['SUE'] > quan[6])&(df['SUE'] <= quan[7]),'allo'] = 7
    df.loc[(df['SUE'] > quan[7])&(df['SUE'] <= quan[8]),'allo'] = 8
    df.loc[df['SUE'] > quan[8],'allo'] = 9
    return df

df1 = df1.groupby(['Stkcd']).apply(allocation)

df1 = df1.reset_index(drop = True)

# Step 5

df3 = df1[['Stkcd','quarter','acc_dl','Annodt','allo']]

df_qt2 = df3[df3.quarter == 2]

df_qt2['acc_dl'] = pd.to_datetime(df_qt2.acc_dl).dt.year

df_qt4 = df3[df3.quarter == 4]

df_qt4['acc_dl'] = pd.to_datetime(df_qt4.acc_dl).dt.year

# Needs to be repeated

# df_qt2_fn = pd.merge(df, df_qt2, how = 'left', left_on = ['Stkcd','date'], right_on = ['Stkcd','Annodt'])

# idx_lst = df_qt2_fn.index[df_qt2_fn.allo.isnull() == False].tolist()

# dret_qt2 = pd.DataFrame(columns=['Stkcd','acc_dl','quarter','t_index','cum_ab_ret'], index = [0])

# for i in idx_lst:
    
#     inter = df_qt2_fn.iloc[i - 120 : i + 121]
    
#     inter = pd.merge(inter, df2, how = 'left', left_on = 'date', right_on = 'Trddt')
    
#     inter['ab_ret'] = inter.stk_ret - inter.mkt_ret
    
#     inter['t_index'] = range(-120,121)
    
#     inter['cum_ab_ret'] = inter.ab_ret.cumsum()
    
#     inter['acc_dl'] = int(inter.loc[inter.t_index == 0, 'acc_dl'].iloc[0])
        
#     inter = inter[['Stkcd','acc_dl','quarter','t_index','cum_ab_ret']]
    
#     inter = inter.fillna(method = 'bfill').fillna(method = 'ffill')
    
#     dret_qt2 = dret_qt2.append(inter, ignore_index = True)
    

# dret_qt2 = dret_qt2.dropna()

# result_qt2 = pd.merge(dret_qt2, df_qt2, how = 'left', on = ['Stkcd','acc_dl','quarter'])

# result_qt2 = result_qt2.groupby(['allo','t_index']).cum_ab_ret.mean().reset_index()

# # For qt4

# df_qt4_fn = pd.merge(df, df_qt4, how = 'left', left_on = ['Stkcd','date'], right_on = ['Stkcd','Annodt'])

# idx_lst = df_qt4_fn.index[df_qt4_fn.allo.isnull() == False].tolist()

# dret_qt4 = pd.DataFrame(columns=['Stkcd','acc_dl','quarter','t_index','cum_ab_ret'], index = [0])

# for i in idx_lst:
    
#     inter = df_qt4_fn.iloc[i - 120 : i + 121]
    
#     inter = pd.merge(inter, df2, how = 'left', left_on = 'date', right_on = 'Trddt')
    
#     inter['ab_ret'] = inter.stk_ret - inter.mkt_ret
    
#     inter['t_index'] = range(-120,121)
    
#     inter['cum_ab_ret'] = inter.ab_ret.cumsum()
    
#     inter['acc_dl'] = int(inter.loc[inter.t_index == 0, 'acc_dl'].iloc[0])
        
#     inter = inter[['Stkcd','acc_dl','quarter','t_index','cum_ab_ret']]
    
#     inter = inter.fillna(method = 'bfill').fillna(method = 'ffill')
    
#     dret_qt4 = dret_qt4.append(inter, ignore_index = True)
    

# dret_qt4 = dret_qt4.dropna()

# result_qt4 = pd.merge(dret_qt4, df_qt4, how = 'left', on = ['Stkcd','acc_dl','quarter'])

# result_qt4 = result_qt4.groupby(['allo','t_index']).cum_ab_ret.mean().reset_index()

# result = result_qt2.append(result_qt4, ignore_index = True)

# result = result.groupby(['allo','t_index']).cum_ab_ret.mean().reset_index()

# result.loc[result.t_index == -120,'cum_ab_ret'] = 0

# x_cor = result.t_index.unique()

# plt.figure(figsize = [15,5])
# plt.plot(x_cor, result.loc[result.allo == 0,'cum_ab_ret'], label = 'Most negative')
# plt.plot(x_cor, result.loc[result.allo == 1,'cum_ab_ret'], label = 'SUE2')
# plt.plot(x_cor, result.loc[result.allo == 2,'cum_ab_ret'], label = 'SUE3')
# plt.plot(x_cor, result.loc[result.allo == 3,'cum_ab_ret'], label = 'SUE4')
# plt.plot(x_cor, result.loc[result.allo == 4,'cum_ab_ret'], label = 'SUE5')
# plt.plot(x_cor, result.loc[result.allo == 5,'cum_ab_ret'], label = 'SUE6')
# plt.plot(x_cor, result.loc[result.allo == 6,'cum_ab_ret'], label = 'SUE7')
# plt.plot(x_cor, result.loc[result.allo == 7,'cum_ab_ret'], label = 'SUE8')
# plt.plot(x_cor, result.loc[result.allo == 8,'cum_ab_ret'], label = 'SUE9')
# plt.plot(x_cor, result.loc[result.allo == 9,'cum_ab_ret'], label = 'Most positive')
# plt.xlabel('Days around Earnings Announcement (Day 0: Announcement date)')
# plt.ylabel('Cumulative Abnormal Return')
# plt.title('Market reactions to Unexpected Quartly Earnings Surprises: China Companies from 2015-2020')
# x_major_locator=MultipleLocator(10)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax = 1, decimals = 2))
# ax.spines['right'].set_visible(False)
# ax.vlines([0], -1, 1, linestyles='dashed', colors='darkred')
# plt.xlim((-122,122))
# plt.ylim((-0.11,0.05))
# plt.legend(loc = 2, bbox_to_anchor = (1.02, 0.8), frameon = False)
# plt.grid(axis = 'y')
# plt.show()






