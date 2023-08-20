# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 01:17:39 2022

@author: Mark
"""

import numpy as np
import pandas as pd
import datetime as dt
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from pyfinance import ols
from statsmodels.regression.rolling import RollingOLS

df1 = pd.read_csv('D:\Code Library\FIN3080\Assignment_2\wanke.csv')

df1['date'] = pd.to_datetime(df1.Trdmnt).dt.strftime('%Y-%m')
df1 = df1[['date','Mretwd']]

df2 = pd.read_csv('D:\Code Library\FIN3080\Assignment_2\CSI_800.csv')

df2['date'] = pd.to_datetime(df2.Month).dt.strftime('%Y-%m')
df2 = df2[['date','Idxrtn']]

df3 = pd.read_csv('D:\Code Library\FIN3080\Assignment_2\shibor.csv')

df3 = df3.loc[df3.Term_EN == "1 day", ['SgnDate','Shibor']].reset_index(drop = True)

df3['SgnDate'] = pd.to_datetime(df3.SgnDate).dt.strftime('%Y-%m')

df3['mean_shibor'] = df3.groupby(['SgnDate']).Shibor.transform('mean')

df3 = df3.drop(['Shibor'],1)
df3 = df3.drop_duplicates(subset = ['mean_shibor'], keep = 'first').reset_index(drop = True)
df3 = df3.rename(columns = {'SgnDate':'date'})

df_inter = pd.merge(df1, df2, on = 'date', how = 'outer')

df = pd.merge(df_inter, df3, on = 'date', how = 'outer')
df = df.sort_values(['date']).reset_index(drop = True)

df['mean_shibor'] = df.mean_shibor/(100*12)

df['risk_pre'] = df['Idxrtn'] - df['mean_shibor']

df['Mretwd'] = df['Mretwd'] - df['mean_shibor']

df = df[['date','Mretwd','risk_pre']]

win = 24

# y = ['Mretwd']
# X = ['risk_pre']
# roll = ols.PandasRollingOLS(df[y], df[X], window = win)
# al = roll.alpha
# be = roll.beta

exog = sm.add_constant(df.risk_pre)
roll = RollingOLS(df.Mretwd, exog, window = win, missing = "drop")
roll_res = roll.fit().params

roll_res = roll_res.rename(columns = {'risk_pre':'beta'})

pic_data = pd.merge(df, roll_res,left_index= True, right_index= True)

pic_data = pic_data[['date','beta']]

pic_data = pic_data.loc[df.date >= '2010-01', ['date','beta']].reset_index(drop = True)

plt.figure(1,figsize=[10,5])
plt.plot(pic_data.date, pic_data.beta, color = 'b')
plt.title('The beta of the stock Wanke from 2010-01 to 2022-03')
plt.xlabel('Year-Month')
plt.ylabel('Estimated Beta')
plt.xticks(rotation = 45)
x_major_locator=MultipleLocator(6)
y_major_locator=MultipleLocator(0.5)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.grid(axis = 'y')
plt.show()
