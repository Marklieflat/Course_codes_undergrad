# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:38:51 2021

@author: Mark
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'D:/Download/STA test sample.csv')


sum1 = df['1'].sum()
sum2 = df['2'].sum()
sum3 = df['3'].sum()
sum4 = df['4'].sum()


sumup = sum1+sum2+sum3+sum4
grand_mean = sumup/26

df['1_minus_sq'] = (df['1'] - grand_mean)**2
df['2_minus_sq'] = (df['2'] - grand_mean)**2
df['3_minus_sq'] = (df['3'] - grand_mean)**2
df['4_minus_sq'] = (df['4'] - grand_mean)**2

ssto = df['1_minus_sq'].sum() + df['2_minus_sq'].sum() + df['3_minus_sq'].sum() + df['4_minus_sq'].sum()

