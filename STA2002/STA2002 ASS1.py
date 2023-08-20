import numpy as np
import pandas as pd

df = pd.read_csv(r'D:\Download\GMM_20.csv', sep = ',')

df1 = df.groupby(['K']).aggregate('mean').reset_index()
df2 = df.groupby(['K']).aggregate('count').reset_index()

df1 = df1.rename(columns = {'X':'mean'})
df2 = df2.rename(columns = {'X':'counts'})

result = pd.merge(df1, df2, on = 'K', how = 'outer')

n0 = result.loc[0, 'counts']
n1 = result.loc[1, 'counts']
mean0 = result.loc[0,'mean']
mean1 = result.loc[1,'mean']

df['mean'] = df['K'].apply(lambda x : mean0 if x == 0 else mean1)
df['xi-mean'] = df['X'] - df['mean']
df['(xi-mean)**2'] = df['xi-mean']**2

df3 = df.groupby(['K']).aggregate({'(xi-mean)**2':'mean'}).reset_index()
sigma0 = df3.loc[0, '(xi-mean)**2']
sigma1 = df3.loc[1, '(xi-mean)**2']
pi0 = n0/100000
print('The estimation of pi0 is',pi0)
print('The estimation of sigma0 square is',sigma0)
print('The estimation of sigma1 square is',sigma1)
print('The estimation of miu0 is',mean0)
print('The estimation of miu1 is',mean1)
