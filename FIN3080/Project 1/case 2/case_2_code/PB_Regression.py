# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:27:18 2022

@author: Mark
"""

import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.formula.api as sm


df = pd.read_csv('D:\Code Library\FIN3080\Project 1\case 2\CSMAR_data\Reg_data.csv')

df_r = pd.read_csv('D:\Code Library\FIN3080\Project 1\case 2\CSMAR_data\TRD_Mont.csv')

df_r = df_r[(df_r.Markettype == 1) | (df_r.Markettype == 4) | (df_r.Markettype == 16)] # 选取主板中小板创业板数据

df_r = df_r.groupby(['Trdmnt']).Mretwdos.mean().reset_index() # 将三个板股票每月的回报率求平均值

df_r = df_r.rename(columns = {'Trdmnt':'ym','Mretwdos':'ret'})

df1 = df.groupby(['ym']).agg({'PB':'median','ROE':'median','DPR':'median'}).reset_index()   
#从当月所有股票中取中位数代表该月的三个指标

df1 = pd.merge(df1, df_r, on = 'ym', how = 'outer') # 将CSMAR市场数据与自己处理的数据横向拼接

df1 = df1.dropna()

df2 = df1[['ROE','DPR','ret']]

vif_data = [variance_inflation_factor(df2.values, df2.columns.get_loc(i)) for i in df2.columns] #做VIF检验

print(vif_data)

print(df1.corr())  # 得到每列数据之间的相关系数

result1 = sm.ols(formula = 'PB~DPR',data = df1,).fit() # 做回归分析

print(result1.summary())

result2 = sm.ols(formula = 'PB~ROE',data = df1).fit() # 做回归分析

print(result2.summary())

result3 = sm.ols(formula = 'PB~ret',data = df1).fit() # 做回归分析

print(result3.summary())
