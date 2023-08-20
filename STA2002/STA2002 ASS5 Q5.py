# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 16:25:02 2021

@author: Mark
"""

import pandas as pd
import numpy as np
from pandas import DataFrame



inputs = [320,326,325,318,322,320,329,317,316,331,320,320,317,329,316,308,321,319,322,335
,318,313,327,314,329,323,327,323,324,314
,308,305,328,330,322,310,324,314,312,318
,313,320,324,311,317,325,328,319,310,324]

df = DataFrame(inputs, columns = ['obs'])

miu = df['obs'].mean()

sigma = df['obs'].std()

df.obs = df.obs.sort_values().reset_index(drop = True)

print(df[df['obs']<].count())
