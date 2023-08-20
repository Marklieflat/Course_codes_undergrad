# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:29:05 2021

@author: Mark
"""

import numpy as np
import pandas as pd

df = pd.read_excel('D:/Download/Mid-Month Forecast template upto Nov8.xlsx')

columns = [i for i in range(0,21)]
new = []
for i in columns:
    new.append(str(i))
    
print(new)

df.columns = columns