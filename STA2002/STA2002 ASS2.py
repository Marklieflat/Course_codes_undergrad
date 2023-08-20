import numpy as np
import pandas as pd

df = pd.read_csv(r'D:\Download\traffic.csv')

# mean
df1 = df.groupby(['weather_main']).aggregate('mean').reset_index()
df1 = df1[['weather_main','traffic_volume']]
df1 = df1.loc[(df1.weather_main =='Clear')|(df1.weather_main == 'Rain')]
print(df1.head())

# Part(b)
df2 = df.groupby(['weather_main']).aggregate('var').reset_index()
df2 = df2[['weather_main','traffic_volume']]
df2 = df2.loc[(df2.weather_main =='Clear')|(df2.weather_main == 'Rain')]

df3 = df.groupby(['weather_main']).aggregate('count').reset_index()
df3 = df3[['weather_main','traffic_volume']]
df3 = df3.loc[(df3.weather_main =='Clear')|(df3.weather_main == 'Rain')]


var_x = df2.loc[0,'traffic_volume']
var_y = df2.loc[6,'traffic_volume']

n = df3.loc[0,'traffic_volume']
m = df3.loc[6,'traffic_volume']

Sp_square = (n*var_x+m*var_y)/(n+m-2)
Sp = Sp_square**(0.5)
print(Sp)

# Part(c)
Multiplier = (var_x/(n-1) + var_y/(m-1))**(0.5)
print(Multiplier)

Sample_Var_x = n/(n-1) * var_x
Sample_Var_y = m/(m-1) * var_y
ratio = Sample_Var_x/Sample_Var_y