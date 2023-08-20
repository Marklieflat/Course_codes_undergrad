# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:07:04 2022

@author: Mark
"""

import pandas as pd
import numpy as np
from glob import glob
import os

os.chdir(r'D:\Code Library\FIN3080\Project 1\case 2\CSMAR_data\stock_data')

df_final = pd.DataFrame(columns=['Symbol','ym','PB','ROE','DPR'], index = [0])

for csv_file in glob('*.csv'):  #读取每年的股票数据

    df = pd.read_csv(csv_file)
    
    df = df.dropna()    # 去掉数据缺失的行数
    
    df['PE'] = df['StockPrice']/ df['EPS']
    
    df['PB'] = df['StockPrice']/ df['NAV']
    
    df['ROE'] = df['EPS']/ df['NAV']
    
    df['ym'] = pd.to_datetime(df.TradingDate).dt.to_period('M') # 转化时间戳格式，便于groupby
    
    df['DPR'] = 1 - (df['EPS']-df['DividentPerShare']) / df['EPS']
    
    df1 = df[['Symbol','ym','PB','ROE','DPR']]  # 选取有效的列
    
    df1 = df1.groupby(['Symbol','ym']).agg({'PB':'median','ROE':'median','DPR':'median'}).reset_index()
    #求每只股票每个月的三个指标中位数
    
    df_final = df_final.append(df1, ignore_index = True) # 将表与表之间连接
    
    df_final = df_final.dropna().reset_index(drop = True)

df_final.to_csv('D:\Code Library\FIN3080\Project 1\case 2\CSMAR_data\Reg_data.csv', index = False)
# 输出处理过一次的csv文件