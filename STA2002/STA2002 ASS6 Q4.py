# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:41:07 2021

@author: Mark
"""

import pandas as pd
import numpy as np

df1 = pd.read_csv('D:/Download/Temp_data.csv')
df2 = pd.read_csv('D:/Download/CO2_data.csv')
df = pd.merge(df1,df2,how = 'outer')
df = df.set_index(df.Year)
df = df.drop(['Year'],axis = 1)
corr_coef = df.corr()

r = corr_coef.iloc[1,0]
t_abs = abs((r*np.sqrt(133))/np.sqrt(1-r**2))

