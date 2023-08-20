import numpy as np
import pandas as pd

df = pd.read_csv('D:/Download/AB_2021.csv')

df1 = df[df.landing_page == 'A']
df2 = df[df.landing_page == 'B']

y1 = df1.converted.value_counts()[1]
y2 = df2.converted.value_counts()[1]

df3 = df.groupby(['landing_page']).converted.count().reset_index()

n1 = df3.loc[0,'converted']
n2 = df3.loc[1,'converted']

PA_hat = y1/n1
PB_hat = y2/n2

p = (y1 + y2)/(n1 + n2)

t = (PA_hat - PB_hat)/ np.sqrt(p*(1-p)*(1/n1 + 1/n2))