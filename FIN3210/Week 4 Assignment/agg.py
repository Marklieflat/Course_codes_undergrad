import pandas as pd

df1 = pd.read_csv('IDX_Idxtrd_1.csv')
df2 = pd.read_csv('IDX_Idxtrd_2.csv')

df = pd.concat([df1, df2], axis=0)
df.to_csv('return.csv', index=False)