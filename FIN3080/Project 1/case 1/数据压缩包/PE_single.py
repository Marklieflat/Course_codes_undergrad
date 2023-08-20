# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:17:04 2022

@author: Mark
"""

import pandas as pd
import numpy as np
from glob import glob
import os

os.chdir(r'D:\Code Library\FIN3080\Project 1\case 1\数据压缩包\stocks_stats')

df_final = pd.DataFrame(columns=['Symbol','year','month','PE'], index = [0])

for csv_file in glob('*.csv'):

    df = pd.read_csv(csv_file)
    
    # print(df.info())
    
    df['PE'] = df['StockPrice']/ df['EPS']
    
    df['year'] = pd.to_datetime(df.TradingDate).dt.year
    
    df['month'] = pd.to_datetime(df.TradingDate).dt.month
    
    df = df[['Symbol','PE','year','month']]
    
    df1 = df.groupby(['Symbol','year','month']).PE.median().reset_index()

    df_final = df_final.append(df1, ignore_index = True)

    df_final = df_final.dropna().reset_index(drop = True)

df_final.to_csv('D:\Code Library\FIN3080\Project 1\case 1\数据压缩包\PE.csv', index = False)



