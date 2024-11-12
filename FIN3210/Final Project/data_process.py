import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

"""
Part 1
"""
# df = pd.read_csv('top_10_v5_selected_normalized.csv')
# idx = df.code.value_counts().index[:10].tolist()
# df = df[df.code.isin(idx)]
# print(df.code.value_counts())
# res = df.groupby('date').mean().reset_index()
# res.drop(['code'], axis=1, inplace=True)
# print(res)
# res.to_csv('top_10.csv', index=False)


"""
Part 2
"""

# df = pd.read_csv('top_10_v5_selected_normalized.csv')
# df1 = pd.read_csv('denoised_data_port.csv').iloc[:, 1:]

# df = df.iloc[:, :6]
# print(df)
# print(df1)
# res = pd.concat([df, df1], axis=1)
# res.dropna(inplace=True)
# res.to_csv('portfolio_wt.csv', index=False)

"""
Part 3
"""
# df = pd.read_csv('top_10_v5_selected.csv')
# columns_to_normalize = ['total_MV','open','high','low','close','volume']

# def normalize_group(group):
#     scaler = StandardScaler()
#     for column in columns_to_normalize:
#         group[column] = scaler.fit_transform(group[column].values.reshape(-1, 1))
#     return group

# # Applying the function to each group
# grouped_normalized_df = df.groupby('code').apply(normalize_group)
# print(grouped_normalized_df)
# grouped_normalized_df.to_csv('top_10_v5_selected_normalized.csv', index=False)

"""
Part 4
"""
# df = pd.read_csv('top_10_v5_selected_normalized.csv')
# df = df.groupby('date').mean().reset_index()
# df.drop(['code'], axis=1, inplace=True)
# df.to_csv('normalized_portfolio.csv', index=False)

"""
Part 5
"""

df = pd.read_csv('top_10_v5_selected_normalized.csv')
print(df.columns)