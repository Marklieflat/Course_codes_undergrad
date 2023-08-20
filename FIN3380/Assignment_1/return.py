# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:48:18 2022

@author: Mark
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\Code Library\FIN3380_summer\Assignment_1\ret.csv')

df = df[['PERMNO','TICKER','date','RET','sprtrn']]

df['date'] = pd.to_datetime(df.date).dt.strftime('%Y-%m')

df['grossret'] = df.RET + 1

df['grossidxret'] = df.sprtrn + 1


#调试
# df.loc[df.date == '2010-01','RET'] = 0

# df.loc[df.date == '2010-01','sprtrn'] = 0





df['accret'] = df.groupby(['PERMNO']).grossret.cumprod().reset_index(drop = True)

df['accidxret'] = df.groupby(['PERMNO']).grossidxret.cumprod().reset_index(drop = True)

df['sftret'] = df.groupby('PERMNO').accret.shift(12)

df['sftidxret'] = df.groupby('PERMNO').accidxret.shift(12)

df = df.dropna()

df['perret'] = df.accret / df.sftret - 1

df['peridxret'] = df.accidxret / df.sftidxret - 1

df1 = df[['PERMNO','TICKER','date','perret','peridxret']]