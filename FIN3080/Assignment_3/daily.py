# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:50:26 2022

@author: Mark
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

raw1 = pd.read_csv(r'D:\Code Library\FIN3080\Assignment_3\daily data\daily_1.csv')

raw2 = pd.read_csv(r'D:\Code Library\FIN3080\Assignment_3\daily data\daily_2.csv')

df = raw1.append(raw2).reset_index(drop = True)

df = df.rename(columns = {'ChangeRatio':'ret'})

df1 = df[df.Symbol == 300]

df2 = df[df.Symbol == 399006]

df1.ret.plot.density(color = 'r', label = 'CSI 300')
df2.ret.plot.density(color = 'b', label = 'GEI')
plt.title('Density distribution')
plt.legend()
plt.grid(axis = 'y')
plt.show()

t_stats1, p1 = stats.normaltest(df1.ret)
print(p1)

t_stats2, p2 = stats.normaltest(df2.ret)
print(p2)
