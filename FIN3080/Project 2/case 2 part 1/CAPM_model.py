# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:14:27 2022

@author: Mark
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\Code Library\FIN3080\Project 2\case 2 part 1\市场收益率\IDX_Idxtrdmth.csv')

df = df[['Month','Idxrtn']]

df['Month'] = pd.to_datetime(df.Month).dt.to_period('M')

df = df.rename(columns = {'Idxrtn':'rm'})

# print(df1.info())

df_rf = pd.read_csv(r'D:\Code Library\FIN3080\Project 2\case 2 part 1\shibor\MBK_SHIBORM.csv')

df_rf = df_rf[df_rf.Term == '1天']

df_rf['Shibor'] = df_rf.Shibor/(100*12)

df_rf['SgnDate'] = pd.to_datetime(df_rf.SgnDate).dt.to_period('M')

df_rf = df_rf.groupby('SgnDate').agg({'Shibor':'mean'}).reset_index()

df_rf = df_rf.rename(columns = {'SgnDate':'Month', 'Shibor':'rf'})

result = pd.merge(df, df_rf, how = 'outer', on = 'Month')

result.to_csv('D:\Code Library\FIN3080\Project 2\case 2 part 1\capm_reg.csv',index = False)