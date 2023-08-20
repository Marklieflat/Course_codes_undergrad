# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:29:12 2022

@author: Mark
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.pyplot import MultipleLocator  

df = pd.read_csv('D:\Code Library\FIN3080\Project 1\case 1\数据压缩包\PEPB.csv')

df['Symbol'] = df['Symbol'].astype(str)

df['judge'] = df['Symbol'].str.startswith('30') & (df['Symbol'].str.len() == 6)

df1 = df[df.judge == True].reset_index(drop = True)

df1 = df1.groupby(['ym']).agg({'PE':'median','PB':'median'}).reset_index()

df1 = df1.rename(columns = {'PE':'PE_GEM','PB':'PB_GEM'})

plt.figure(1,figsize=[20,5])
plt.plot(df1.ym, df1.PE_GEM, 'r', label = 'PE Ratio')
plt.plot(df1.ym, df1.PB_GEM, 'b', label = 'PB Ratio')
plt.title('PE/PB Ratio of GEM board')
plt.xlabel('Year & Month')
plt.ylabel('Ratios')
plt.xticks(rotation = 60)
x_major_locator = MultipleLocator(6)
y_major_locator = MultipleLocator(5)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.legend()
plt.grid(axis = 'y')
plt.show()

df2 = df[df.judge == False].reset_index(drop = True)

df2 = df2.groupby(['ym']).agg({'PE':'median','PB':'median'}).reset_index()

df2 = df2.rename(columns = {'PE':'PE_Main&SME','PB':'PB_Main&SME'})

plt.figure(2,figsize=[20,5])
plt.plot(df2.ym, df2['PE_Main&SME'], 'r', label = 'PE Ratio')
plt.plot(df2.ym, df2['PB_Main&SME'], 'b', label = 'PB Ratio')
plt.title('PE/PB Ratio of main board & SME board')
plt.xlabel('Year & Month')
plt.ylabel('Ratios')
plt.xticks(rotation = 60)
x_major_locator = MultipleLocator(6)
y_major_locator = MultipleLocator(5)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
ax.xaxis.set_major_locator(x_major_locator)
plt.legend()
plt.grid(axis = 'y')
plt.show()

df3 = pd.merge(df1, df2, on = 'ym', how = 'outer')

df3 = df3.sort_values('ym')

plt.figure(3,figsize=[20,5])
plt.plot(df3.ym, df3['PE_Main&SME'], 'r', label = 'Main & SME PE Ratio')
plt.plot(df3.ym, df3['PB_Main&SME'], 'b', label = 'Main & SME PB Ratio')
plt.plot(df3.ym,df3.PE_GEM, 'k', label = 'GEM PE Ratio')
plt.plot(df3.ym,df3.PB_GEM, 'm', label = 'GEM PB Ratio')
plt.title('PE/PB Ratio of main board & SME & GEM board')
plt.xlabel('Year & Month')
plt.ylabel('Ratios')
plt.xticks(rotation = 60)
x_major_locator = MultipleLocator(6)
y_major_locator = MultipleLocator(5)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
ax.xaxis.set_major_locator(x_major_locator)
plt.legend()
plt.grid(axis = 'y')
plt.show()