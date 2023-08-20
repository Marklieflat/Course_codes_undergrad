# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:16:39 2022

@author: Mark
"""

import pandas as pd

df = pd.read_csv('D:\Code Library\FIN3080\Assignment_2\shibor.csv')


df = df.loc[df.Term_EN == "1 day", ['SgnDate','Shibor']].reset_index(drop = True)