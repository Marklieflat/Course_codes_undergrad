# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:27:54 2021

@author: Mark
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

df1 = pd.read_csv('D:/Download/D.csv')
sp_mean_xD = df1.x.mean()
sp_var_xD = df1.x.var()
sp_mean_yD = df1.y.mean()
sp_var_yD = df1.y.var()

df2 = pd.read_csv('D:/Download/S.csv')
sp_mean_xS = df2.x.mean()
sp_var_xS = df2.x.var()
sp_mean_yS = df2.y.mean()
sp_var_yS = df2.y.var()

df1['Xi_minus_Xbar'] = df1['x']-sp_mean_xD
df1['Yi(Xi_minus_Xbar)'] = df1['Xi_minus_Xbar']*df1['y']
df1['(Xi_minus_Xbar_sq)'] = df1['Xi_minus_Xbar']**2
beta = df1['Yi(Xi_minus_Xbar)'].sum()/df1['(Xi_minus_Xbar_sq)'].sum()


result1 = sm.ols(formula = 'y~Xi_minus_Xbar',data = df1).fit()
print(result1.summary())

SSTx_sqrt = np.sqrt(df1['(Xi_minus_Xbar_sq)'].sum())

df1['predict'] = 47.83-0.1035825*df1['Xi_minus_Xbar']
df1['residual'] = df1['y']-df1['predict']
df1['residual_sq'] = df1['residual']**2
Sr = np.sqrt(df1['residual_sq'].sum()*(1/140))

beta_bar = (1/SSTx_sqrt)*Sr*1.96

df2['Xi_min_Xbar'] = df2['x']-sp_mean_xS
result2 = sm.ols(formula = 'y~Xi_min_Xbar',data = df2).fit()
print(result2.summary())
df2['predict'] = 47.8395-0.101113*df2['Xi_min_Xbar']
df2['residual'] = df2['y']-df2.predict
df2['residual_sq'] = df2['residual']**2
SRs = np.sqrt(df2.residual_sq.sum()*(1/140))
df2['SSTx'] = df2['Xi_min_Xbar']**2
SSTxs_sqrt = np.sqrt(df2.SSTx.sum())
interval = (1/SSTxs_sqrt)*SRs*1.96

x1 = df1['x']
y1 = df1['y']
plt.scatter(x1,y1,marker = 'o', c = 'r')

# x2 = df2['x']
# y2  =df2['y']
# plt.scatter(x2,y2,marker = 'o', c = 'b')