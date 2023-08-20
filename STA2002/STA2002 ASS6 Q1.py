# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:58:28 2021

@author: Mark
"""

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df1 = pd.read_csv('D:/Download/traffic.csv')

df = df1[['weather_main','traffic_volume']]
df = df.loc[(df.weather_main == 'Clouds')|(df.weather_main == 'Clear')|(df.weather_main == 'Snow')]
anova_res = anova_lm(ols('traffic_volume~C(weather_main)', df).fit())

anova_res = anova_res.reset_index(drop = True)
anova_res = anova_res.append({'df':anova_res['df'].sum(),'sum_sq':anova_res['sum_sq'].sum()},ignore_index = True)
anova_res.index = ['Treatment','Error','Total']
print(anova_res)