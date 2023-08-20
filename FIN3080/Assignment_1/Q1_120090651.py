# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:12:15 2022

@author: Mark
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator  

df = pd.read_csv('D:\Code Library\FIN3080\Assignment_1\年公司\TRD_Yearm.csv')

df = df[(df.Markettype == 1)|(df.Markettype == 4)|(df.Markettype == 16)]

df1 = df.groupby(['Trdynt']).Ynstkcal.sum().reset_index()

plt.figure(1,figsize=[16,7])

plt.plot(df1.Trdynt, df1.Ynstkcal, 'r', marker = 'o',markersize = 3)

plt.xlabel('Year')

plt.ylabel('number of listed company')

plt.xticks(rotation = 45)

x_major_locator=MultipleLocator(1)

y_major_locator=MultipleLocator(500)

ax=plt.gca()

ax.xaxis.set_major_locator(x_major_locator)

ax.yaxis.set_major_locator(y_major_locator)

for a,b in zip(df1.Trdynt, df1.Ynstkcal):
    plt.text(float(a), float(b), str(b), ha='right', va= 'bottom')

plt.grid()

plt.show()