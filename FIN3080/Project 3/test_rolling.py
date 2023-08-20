# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:29:59 2022

@author: Mark
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, 5], [2, 3], [3, 7],[1,9],[2,8],[3,0],[1,2],[2,6],[3,3],[1,10],[2,5],[3,7]]), columns=['stockid', 'price'])



df1 = df.groupby('stockid')['price'].rolling(window = 3).mean()

