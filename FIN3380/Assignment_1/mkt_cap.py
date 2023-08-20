# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:27:46 2022

@author: Mark
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\Code Library\FIN3380_summer\Assignment_1\第三四张表.csv')

df = df[['gvkey','datadate','fyear','tic','at','bkvlps','csho','prcc_f']]

# df = df.loc[(df.fyear == 2011)|(df.fyear == 2020)]

df = df.rename(columns = {'at':'total_asset','bkvlps':'bookvalpers','csho':'shrout','prcc_f':'price'})

df['bvoe'] = df.bookvalpers * df.shrout

df['mktcap'] = df.price * df.shrout