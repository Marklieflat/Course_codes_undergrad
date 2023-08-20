# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:05:49 2022

@author: Mark
"""

import numpy as np
import pandas as pd
import datetime as dt
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression


df1 = pd.read_csv(r'D:\Code Library\FIN3080\Assignment_2\A_share_stocks.csv')
df1['date'] = pd.to_datetime(df1.Trdmnt).dt.strftime('%Y-%m')
df1 = df1[['Stkcd','date','Mretwd']]

df2 = pd.read_csv(r'D:\Code Library\FIN3080\Assignment_2\regressor.csv')
df2['date'] = pd.to_datetime(df2.date).dt.strftime('%Y-%m')
df2 = df2.rename(columns = {'mean_shibor':'rf'})
df2 = df2.loc[(df2.date >= '2019-07') & (df2.date <= '2021-06'),['date','risk_pre','rf']].reset_index(drop = True)

df = pd.merge(df1, df2, how = 'outer', on = 'date')

df['Mretwd-rf'] = df['Mretwd'] - df['rf']

df = df.dropna()

# Y = df['Mretwd-rf']
# X = df['risk_pre']
# X = sm.add_constant(X)
# result = sm.OLS(Y, X, missing = 'drop').fit()
# beta = result.params
# print(beta)


# def reg_beta(data):
#     global reg
#     Y = data['Mretwd-rf']
#     X = data['risk_pre']
#     X = sm.add_constant(X)
#     result = sm.OLS(Y, X).fit()
#     beta = result.params[1]
#     reg = pd.DataFrame(beta, columns=('beta'))
#     return

def model(df):
    y = df[['Mretwd-rf']]
    X = df[['risk_pre']]
    return np.squeeze(LinearRegression().fit(X,y).coef_)

df_r = df.groupby(['Stkcd']).apply(model)

df_r = df_r.reset_index()

df_r = df_r.rename(columns = {0:'Beta'})

df_r['Beta'] = df_r['Beta'].astype(float)

df_r.Beta.plot.density(color = 'g')
plt.title('The probability distribution of betas')
plt.xlim(-5,5)
plt.xticks(np.arange(-5,5,1))
plt.show()

perc = [0.1,0.25,0.75,0.9]
print(df_r.Beta.describe(percentiles = perc))

# print(df.Stkcd.nunique())


