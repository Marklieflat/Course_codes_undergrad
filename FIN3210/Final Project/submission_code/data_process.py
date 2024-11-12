import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('top_10_v5_selected.csv')
columns_to_normalize = ['total_MV','open','high','low','close','volume']

def normalize_group(group):
    scaler = StandardScaler()
    for column in columns_to_normalize:
        group[column] = scaler.fit_transform(group[column].values.reshape(-1, 1))
    return group

# Applying the function to each group
grouped_normalized_df = df.groupby('code').apply(normalize_group)
print(grouped_normalized_df)
grouped_normalized_df.to_csv('top_10_v5_selected_normalized.csv', index=False)