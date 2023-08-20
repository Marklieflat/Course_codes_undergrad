# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:52:15 2022

@author: Mark
"""

import pandas as pd
import datetime as dt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt  

df = pd.read_csv('D:\Code Library\FIN3080\Assignment_1\股票公司\TRD_Co.csv')

# print(df.info())

df = df[(df.Markettype == 1)|(df.Markettype == 4)|(df.Markettype == 16)]

df = df[df.Listdt != '0000-00-00']

df['Listdt'] = pd.to_datetime(df.Listdt)

df['year'] = df.Listdt.dt.year

df = df.sort_values('year')

df1 = pd.DataFrame(df.year.value_counts()).reset_index()

df1.columns = ['year','listed_company']

df1 = df1.sort_values('year').reset_index(drop = True)

df1['cum_list'] = df1.listed_company.cumsum()

plt.figure(1,figsize=[10,5])
plt.plot(df1.year, df1.cum_list, marker = 'o',markersize = 3)
plt.xlabel('Year')
plt.ylabel('number of listed company')
plt.grid()
plt.show()



