# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:57:50 2022

@author: Mark
"""

import pandas as pd

df = pd.read_csv(r'D:\Code Library\FIN3380_summer\Assignment_3\prc_data.csv')

df = df[df.TICKER == 'NFLX']

df['date'] = pd.to_datetime(df.date).dt.strftime('%Y-%m-%d')

df = df[(df.date >= '2020-10-21') & (df.date <= '2021-01-15')].reset_index(drop = True)

df.loc[df.index == 0,['RET','sprtrn']] = 0

df['grs_ret'] = df.RET + 1

df['grs_idxret'] = df.sprtrn + 1

df['cum_ret'] = df.grs_ret.cumprod()-1

df['cum_idxret'] = df.grs_idxret.cumprod()-1